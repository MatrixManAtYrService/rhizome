"""Git diff analysis utilities for schema and data sync operations."""

import json
import re
from collections.abc import Sequence
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path
from typing import Protocol

import git
import typer


class ChangeType(StrEnum):
    """Types of changes that can be detected in files."""

    TRIVIAL = "trivial"
    NONTRIVIAL = "nontrivial"
    NONE = "none"


@dataclass
class AutoIncrementCheckResult:
    """Result of checking AUTO_INCREMENT changes."""

    has_auto_increment: bool
    lines_match: bool


@dataclass
class SummaryStats:
    """Summary statistics for changes."""

    trivial_count: int
    nontrivial_count: int
    unchanged_count: int
    total_files: int


@dataclass
class FileSummary:
    """File categorization by change type."""

    trivial: list[str]
    nontrivial: list[str]
    none: list[str]


@dataclass
class DetailedSummary:
    """Detailed summary including stats and file lists."""

    summary: SummaryStats
    files: FileSummary


class ChangeClassifier(Protocol):
    """Protocol for classifying changes in files."""

    def classify_changes(self, diff_item: git.Diff) -> ChangeType:
        """
        Classify changes in a git diff item.

        Args:
            diff_item: GitPython Diff object representing changes to a file

        Returns:
            ChangeType enum value
        """
        ...


class SchemaChangeClassifier:
    """Classifier for schema file changes."""

    def classify_changes(self, diff_item: git.Diff) -> ChangeType:
        """
        Classify schema changes as trivial, nontrivial, or none.

        Trivial changes include:
        - AUTO_INCREMENT value changes only

        Args:
            diff_item: GitPython Diff object

        Returns:
            ChangeType enum value
        """
        if not diff_item.diff:
            return ChangeType.NONE

        diff_text = self._get_diff_text(diff_item)
        if not diff_text:
            return ChangeType.NONE

        added_lines, removed_lines = self._extract_change_lines(diff_text)

        if not added_lines and not removed_lines:
            return ChangeType.NONE

        if len(added_lines) != len(removed_lines):
            return ChangeType.NONTRIVIAL

        return self._classify_line_pairs(added_lines, removed_lines)

    def _get_diff_text(self, diff_item: git.Diff) -> str | None:
        """Extract and validate diff text from diff item."""
        diff_text = diff_item.diff.decode("utf-8") if isinstance(diff_item.diff, bytes) else str(diff_item.diff)
        return diff_text if diff_text and diff_text.strip() else None

    def _extract_change_lines(self, diff_text: str) -> tuple[list[str], list[str]]:
        """Extract added and removed lines from diff text."""
        lines = diff_text.split("\n")
        added_lines: list[str] = []
        removed_lines: list[str] = []

        for line in lines:
            # Skip diff headers and context lines
            if line.startswith("@@") or line.startswith("+++") or line.startswith("---"):
                continue

            # Collect actual content changes
            if line.startswith("+"):
                content = line[1:].strip()
                if content:  # Skip empty lines
                    added_lines.append(content)
            elif line.startswith("-"):
                content = line[1:].strip()
                if content:  # Skip empty lines
                    removed_lines.append(content)

        return added_lines, removed_lines

    def _classify_line_pairs(self, added_lines: list[str], removed_lines: list[str]) -> ChangeType:
        """Classify changes by comparing line pairs for AUTO_INCREMENT differences."""
        auto_increment_pattern = r"AUTO_INCREMENT=\d+"
        all_trivial = True
        has_auto_increment_changes = False

        for added, removed in zip(added_lines, removed_lines, strict=False):
            normalized_result = self._normalize_and_check_auto_increment(added, removed, auto_increment_pattern)

            if normalized_result.has_auto_increment:
                has_auto_increment_changes = True

            if not normalized_result.lines_match:
                all_trivial = False
                break

        # If all changes are the same after normalization but no AUTO_INCREMENT changes were found,
        # then this is just whitespace/identical content - classify as NONE
        if all_trivial and not has_auto_increment_changes:
            return ChangeType.NONE

        return ChangeType.TRIVIAL if all_trivial else ChangeType.NONTRIVIAL

    def _normalize_and_check_auto_increment(self, added: str, removed: str, pattern: str) -> AutoIncrementCheckResult:
        """Normalize lines and check for AUTO_INCREMENT changes."""

        # Normalize AUTO_INCREMENT values
        added_normalized = re.sub(pattern, "AUTO_INCREMENT=XXXX", added)
        removed_normalized = re.sub(pattern, "AUTO_INCREMENT=XXXX", removed)

        # Check if this line pair had AUTO_INCREMENT changes
        has_auto_increment = bool(
            (re.search(pattern, added) or re.search(pattern, removed)) and added_normalized == removed_normalized
        )

        lines_match = added_normalized == removed_normalized

        return AutoIncrementCheckResult(has_auto_increment=has_auto_increment, lines_match=lines_match)


class DataChangeClassifier:
    """Classifier for data file changes."""

    def classify_changes(self, diff_item: git.Diff) -> ChangeType:
        """
        Classify data changes as trivial, nontrivial, or none.

        For data files, we might consider trivial changes to be:
        - Timestamp updates only
        - ID value changes only

        Args:
            diff_item: GitPython Diff object

        Returns:
            ChangeType enum value
        """
        if not diff_item.diff:
            return ChangeType.NONE

        # For now, classify all data changes as nontrivial
        # This can be enhanced later with specific data change logic
        diff_text = diff_item.diff.decode("utf-8") if isinstance(diff_item.diff, bytes) else str(diff_item.diff)

        if not diff_text or not diff_text.strip():
            return ChangeType.NONE

        # Simple check: if there are any +/- lines with content, it's nontrivial
        lines = diff_text.split("\n")
        for line in lines:
            if (line.startswith("+") or line.startswith("-")) and line[1:].strip():
                return ChangeType.NONTRIVIAL

        return ChangeType.NONE


def get_file_diffs(file_paths: Sequence[str | Path]) -> list[git.Diff]:
    """
    Get git diffs for specific files using GitPython DiffIndex.

    Args:
        file_paths: List of file paths to get diffs for

    Returns:
        List of GitPython Diff objects
    """
    if not file_paths:
        return []

    try:
        # Find the git repo root
        repo = git.Repo(search_parent_directories=True)

        # Convert file paths to relative paths from repo root
        relative_paths: list[str] = []
        for file_path in file_paths:
            file_path = Path(file_path)
            try:
                relative_path = file_path.relative_to(repo.working_dir)
                relative_paths.append(str(relative_path))
            except ValueError:
                # File is outside repo, skip it
                continue

        if not relative_paths:
            return []

        # Get diffs for these specific files using the working tree vs HEAD
        # Convert to tuple of Path objects for GitPython compatibility
        path_objects = tuple(Path(p) for p in relative_paths)
        diffs = repo.index.diff("HEAD", paths=path_objects, create_patch=True)
        return list(diffs)

    except (git.InvalidGitRepositoryError, git.GitCommandError, OSError):
        return []


class ChangeTracker:
    """Tracks file changes during sync operations."""

    def __init__(self, classifier: ChangeClassifier) -> None:
        self.classifier = classifier
        self.changes: dict[str, ChangeType] = {}
        self.tracked_files: list[str] = []

    def track_file(self, file_path: str | Path) -> None:
        """
        Track a file for later analysis.

        Args:
            file_path: Path to the file to track
        """
        self.tracked_files.append(str(file_path))

    def analyze_tracked_files(self) -> None:
        """Analyze all tracked files for changes."""
        if not self.tracked_files:
            return

        diffs = get_file_diffs(self.tracked_files)

        # Create a mapping of file paths to diffs
        diff_map = {diff.b_path: diff for diff in diffs if diff.b_path}

        # Analyze each tracked file
        for file_path in self.tracked_files:
            relative_path = self._get_relative_path(file_path)
            if relative_path in diff_map:
                change_type = self.classifier.classify_changes(diff_map[relative_path])
            else:
                # No diff found, file was unchanged
                change_type = ChangeType.NONE

            self.changes[file_path] = change_type

    def _get_relative_path(self, file_path: str) -> str:
        """Get relative path from repo root."""
        try:
            repo = git.Repo(search_parent_directories=True)
            return str(Path(file_path).relative_to(repo.working_dir))
        except (git.InvalidGitRepositoryError, ValueError):
            return file_path

    def get_summary(self) -> FileSummary:
        """
        Get a summary of all tracked changes.

        Returns:
            FileSummary with lists of files by change type
        """
        trivial_files: list[str] = []
        nontrivial_files: list[str] = []
        none_files: list[str] = []

        for file_path, change_type in self.changes.items():
            if change_type == ChangeType.TRIVIAL:
                trivial_files.append(file_path)
            elif change_type == ChangeType.NONTRIVIAL:
                nontrivial_files.append(file_path)
            else:
                none_files.append(file_path)

        # Sort nontrivial changes for better visibility
        nontrivial_files.sort()

        return FileSummary(trivial=trivial_files, nontrivial=nontrivial_files, none=none_files)

    def get_detailed_summary(self) -> DetailedSummary:
        """
        Get a detailed summary including file lists and change counts.

        Returns:
            DetailedSummary with stats and file categorization
        """
        file_summary = self.get_summary()

        return DetailedSummary(
            summary=SummaryStats(
                trivial_count=len(file_summary.trivial),
                nontrivial_count=len(file_summary.nontrivial),
                unchanged_count=len(file_summary.none),
                total_files=len(self.changes),
            ),
            files=file_summary,
        )

    def print_summary(self, errors: list[str] | None = None) -> None:
        """Print a formatted summary of changes."""
        detailed_summary = self.get_detailed_summary()
        errors = errors or []

        typer.echo("\nChange Summary:")
        # Convert to dict for JSON serialization
        summary_dict = {
            "summary": {
                "trivial_count": detailed_summary.summary.trivial_count,
                "nontrivial_count": detailed_summary.summary.nontrivial_count,
                "unchanged_count": detailed_summary.summary.unchanged_count,
                "total_files": detailed_summary.summary.total_files,
                "error_count": len(errors),
            },
            "files": {
                "trivial": detailed_summary.files.trivial,
                "nontrivial": detailed_summary.files.nontrivial,
                "none": detailed_summary.files.none,
            },
            "errors": errors,
        }
        typer.echo(json.dumps(summary_dict, indent=2))

        # If there are nontrivial changes, highlight them
        nontrivial_files = detailed_summary.files.nontrivial
        if nontrivial_files:
            typer.echo(f"\n⚠️  {len(nontrivial_files)} files with nontrivial changes:")
            for file_path in nontrivial_files:
                typer.echo(f"  • {file_path}")

        # If there are errors, highlight them
        if errors:
            typer.echo(f"\n❌ {len(errors)} errors occurred:")
            for error in errors:
                typer.echo(f"  • {error}")
