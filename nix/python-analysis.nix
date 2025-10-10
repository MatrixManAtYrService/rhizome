{ pkgs, ... }:

let
  common = import ./common.nix { inherit pkgs; };
  inherit (common) makeCheck createAnalysisPackage;

  # Individual check definitions
  ruffCheckCheck = makeCheck {
    name = "ruff-check";
    description = "Python linting with ruff (auto-fix enabled)";
    dependencies = with pkgs; [ ruff ];
    roots = [ "src" "tests" ];
    command = "ruff check --fix --unsafe-fixes --exit-non-zero-on-fix";
    verboseCommand = "ruff check --fix --unsafe-fixes --exit-non-zero-on-fix --verbose";
  };

  ruffFormatCheck = makeCheck {
    name = "ruff-format";
    description = "Python formatting with ruff (auto-format enabled)";
    dependencies = with pkgs; [ ruff ];
    roots = [ "src" "tests" ];
    command = "ruff format";
    verboseCommand = "ruff format --verbose";
  };

  pyrightCheck = makeCheck {
    name = "pyright";
    description = "Python type checking with pyright";
    dependencies = with pkgs; [ ]; # nix develop provides the environment
    command = "nix develop --command pyright src tests";
    verboseCommand = "nix develop --command pyright src tests --verbose";
  };
in
createAnalysisPackage {
  name = "python-analysis";
  description = "Python code analysis";
  checks = {
    "1-ruff-format" = ruffFormatCheck;
    "2-ruff-check" = ruffCheckCheck;
    "3-pyright" = pyrightCheck;
  };
}
