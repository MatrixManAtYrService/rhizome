"""Tests for git_diff functionality."""

from unittest.mock import MagicMock

import git

from rhizome.git_diff import ChangeTracker, ChangeType, DataChangeClassifier, FileSummary, SchemaChangeClassifier


class TestChangeType:
    """Test the ChangeType enum."""

    def test_change_type_values(self) -> None:
        """Test that ChangeType has expected string values."""
        assert ChangeType.TRIVIAL == "trivial"
        assert ChangeType.NONTRIVIAL == "nontrivial"
        assert ChangeType.NONE == "none"


class TestSchemaChangeClassifier:
    """Test the SchemaChangeClassifier class."""

    def setUp(self) -> None:
        self.classifier = SchemaChangeClassifier()

    def test_empty_diff(self) -> None:
        """Test that empty diff returns NONE."""
        classifier = SchemaChangeClassifier()

        # Mock diff item with no diff content
        mock_diff = MagicMock(spec=git.Diff)
        mock_diff.diff = None

        assert classifier.classify_changes(mock_diff) == ChangeType.NONE

    def test_auto_increment_only_change(self) -> None:
        """Test that AUTO_INCREMENT only changes are classified as TRIVIAL."""
        classifier = SchemaChangeClassifier()

        diff_content = """-) ENGINE=InnoDB AUTO_INCREMENT=153254 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
+) ENGINE=InnoDB AUTO_INCREMENT=154398 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci"""

        mock_diff = MagicMock(spec=git.Diff)
        mock_diff.diff = diff_content.encode("utf-8")

        assert classifier.classify_changes(mock_diff) == ChangeType.TRIVIAL

    def test_nontrivial_change(self) -> None:
        """Test that actual schema changes are classified as NONTRIVIAL."""
        classifier = SchemaChangeClassifier()

        diff_content = """   `id` int NOT NULL AUTO_INCREMENT,
+  `new_column` varchar(255) DEFAULT NULL,
   PRIMARY KEY (`id`)"""

        mock_diff = MagicMock(spec=git.Diff)
        mock_diff.diff = diff_content.encode("utf-8")

        assert classifier.classify_changes(mock_diff) == ChangeType.NONTRIVIAL

    def test_whitespace_only_change(self) -> None:
        """Test that whitespace-only changes return NONE."""
        classifier = SchemaChangeClassifier()

        diff_content = """-  PRIMARY KEY (`id`)
+  PRIMARY KEY (`id`)"""

        mock_diff = MagicMock(spec=git.Diff)
        mock_diff.diff = diff_content.encode("utf-8")

        assert classifier.classify_changes(mock_diff) == ChangeType.NONE


class TestDataChangeClassifier:
    """Test the DataChangeClassifier class."""

    def test_empty_diff(self) -> None:
        """Test that empty diff returns NONE."""
        classifier = DataChangeClassifier()

        mock_diff = MagicMock(spec=git.Diff)
        mock_diff.diff = None

        assert classifier.classify_changes(mock_diff) == ChangeType.NONE

    def test_data_change(self) -> None:
        """Test that data changes are classified as NONTRIVIAL."""
        classifier = DataChangeClassifier()

        diff_content = """-  "id": 123,
+  "id": 456,"""

        mock_diff = MagicMock(spec=git.Diff)
        mock_diff.diff = diff_content.encode("utf-8")

        assert classifier.classify_changes(mock_diff) == ChangeType.NONTRIVIAL


class TestChangeTracker:
    """Test the ChangeTracker class."""

    def test_initialization(self) -> None:
        """Test ChangeTracker initialization."""
        classifier = SchemaChangeClassifier()
        tracker = ChangeTracker(classifier)

        assert tracker.classifier == classifier
        assert tracker.changes == {}
        assert tracker.tracked_files == []

    def test_track_file(self) -> None:
        """Test file tracking."""
        classifier = SchemaChangeClassifier()
        tracker = ChangeTracker(classifier)

        tracker.track_file("test.sql")

        assert "test.sql" in tracker.tracked_files

    def test_get_summary_empty(self) -> None:
        """Test get_summary with no analyzed files."""
        classifier = SchemaChangeClassifier()
        tracker = ChangeTracker(classifier)

        summary = tracker.get_summary()

        expected = FileSummary(trivial=[], nontrivial=[], none=[], new=[])
        assert summary == expected

    def test_get_detailed_summary_empty(self) -> None:
        """Test get_detailed_summary with no analyzed files."""
        classifier = SchemaChangeClassifier()
        tracker = ChangeTracker(classifier)

        detailed = tracker.get_detailed_summary()

        assert detailed.summary.trivial_count == 0
        assert detailed.summary.nontrivial_count == 0
        assert detailed.summary.unchanged_count == 0
        assert detailed.summary.total_files == 0
        assert detailed.files.trivial == []
        assert detailed.files.nontrivial == []
        assert detailed.files.none == []

    def test_nontrivial_sorting(self) -> None:
        """Test that nontrivial changes are sorted."""
        classifier = SchemaChangeClassifier()
        tracker = ChangeTracker(classifier)

        # Manually set some changes to test sorting
        tracker.changes = {
            "z_file.sql": ChangeType.NONTRIVIAL,
            "a_file.sql": ChangeType.NONTRIVIAL,
            "m_file.sql": ChangeType.NONTRIVIAL,
        }

        summary = tracker.get_summary()
        nontrivial_files = summary.nontrivial

        # Should be sorted alphabetically
        assert nontrivial_files == ["a_file.sql", "m_file.sql", "z_file.sql"]
