"""Tests for the CLI commands."""

from typer.testing import CliRunner

from silicon.cli import app

runner = CliRunner(env={"NO_COLOR": "1", "TERM": "dumb"})


class TestHelloCommand:
    """Tests for the hello command."""

    def test_hello_default(self) -> None:
        """Test hello with default name."""
        result = runner.invoke(app, ["hello"])
        assert result.exit_code == 0
        assert "Hello, World!" in result.stdout

    def test_hello_with_name(self) -> None:
        """Test hello with custom name."""
        result = runner.invoke(app, ["hello", "--name", "Developer"])
        assert result.exit_code == 0
        assert "Hello, Developer!" in result.stdout

    def test_hello_with_short_flag(self) -> None:
        """Test hello with -n short flag."""
        result = runner.invoke(app, ["hello", "-n", "Tester"])
        assert result.exit_code == 0
        assert "Hello, Tester!" in result.stdout


class TestGoodbyeCommand:
    """Tests for the goodbye command."""

    def test_goodbye_default(self) -> None:
        """Test goodbye with default name."""
        result = runner.invoke(app, ["goodbye"])
        assert result.exit_code == 0
        assert "Goodbye, World!" in result.stdout

    def test_goodbye_with_name(self) -> None:
        """Test goodbye with custom name."""
        result = runner.invoke(app, ["goodbye", "--name", "Developer"])
        assert result.exit_code == 0
        assert "Goodbye, Developer!" in result.stdout

    def test_goodbye_with_short_flag(self) -> None:
        """Test goodbye with -n short flag."""
        result = runner.invoke(app, ["goodbye", "-n", "Tester"])
        assert result.exit_code == 0
        assert "Goodbye, Tester!" in result.stdout


class TestVersionCommand:
    """Tests for the version command."""

    def test_version_command(self) -> None:
        """Test version command outputs version."""
        result = runner.invoke(app, ["version"])
        assert result.exit_code == 0
        assert result.stdout.strip().startswith("v")

    def test_version_flag(self) -> None:
        """Test --version flag outputs version."""
        result = runner.invoke(app, ["--version"])
        assert result.exit_code == 0
        assert result.stdout.strip().startswith("v")

    def test_version_short_flag(self) -> None:
        """Test -v short flag outputs version."""
        result = runner.invoke(app, ["-v"])
        assert result.exit_code == 0
        assert result.stdout.strip().startswith("v")

    def test_version_matches_package(self) -> None:
        """Test version prints the package version from the version file."""
        from silicon import __version__
        from silicon._version import __version__ as built_version

        result = runner.invoke(app, ["version"])
        assert result.exit_code == 0
        assert result.stdout.strip() == f"v{__version__}"
        assert __version__ == built_version

    def test_version_fallback_without_version_file(self) -> None:
        """Test version falls back to 0.0.0 when the version file is missing."""
        import importlib
        import sys
        from unittest.mock import patch

        import silicon

        try:
            with patch.dict(sys.modules, {"silicon._version": None}):
                importlib.reload(silicon)
                assert silicon.__version__ == "0.0.0"
        finally:
            importlib.reload(silicon)


class TestHelpCommand:
    """Tests for help output."""

    def test_help_flag(self) -> None:
        """Test --help shows usage information."""
        result = runner.invoke(app, ["--help"])
        assert result.exit_code == 0
        assert "hello" in result.stdout
        assert "goodbye" in result.stdout
        assert "version" in result.stdout

    def test_help_short_flag(self) -> None:
        """Test -h short flag shows usage information."""
        result = runner.invoke(app, ["-h"])
        assert result.exit_code == 0
        assert "hello" in result.stdout

    def test_hello_help(self) -> None:
        """Test hello --help shows command help."""
        result = runner.invoke(app, ["hello", "--help"])
        assert result.exit_code == 0
        assert "--name" in result.stdout

    def test_goodbye_help(self) -> None:
        """Test goodbye --help shows command help."""
        result = runner.invoke(app, ["goodbye", "--help"])
        assert result.exit_code == 0
        assert "--name" in result.stdout
