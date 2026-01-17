"""Tests for the CLI commands."""

from typer.testing import CliRunner

from silicon.cli import app

runner = CliRunner()


class TestHelloCommand:
    """Tests for the hello command."""

    def test_hello_default(self):
        """Test hello with default name."""
        result = runner.invoke(app, ["hello"])
        assert result.exit_code == 0
        assert "Hello, World!" in result.stdout

    def test_hello_with_name(self):
        """Test hello with custom name."""
        result = runner.invoke(app, ["hello", "--name", "Developer"])
        assert result.exit_code == 0
        assert "Hello, Developer!" in result.stdout

    def test_hello_with_short_flag(self):
        """Test hello with -n short flag."""
        result = runner.invoke(app, ["hello", "-n", "Tester"])
        assert result.exit_code == 0
        assert "Hello, Tester!" in result.stdout


class TestGoodbyeCommand:
    """Tests for the goodbye command."""

    def test_goodbye_default(self):
        """Test goodbye with default name."""
        result = runner.invoke(app, ["goodbye"])
        assert result.exit_code == 0
        assert "Goodbye, World!" in result.stdout

    def test_goodbye_with_name(self):
        """Test goodbye with custom name."""
        result = runner.invoke(app, ["goodbye", "--name", "Developer"])
        assert result.exit_code == 0
        assert "Goodbye, Developer!" in result.stdout

    def test_goodbye_with_short_flag(self):
        """Test goodbye with -n short flag."""
        result = runner.invoke(app, ["goodbye", "-n", "Tester"])
        assert result.exit_code == 0
        assert "Goodbye, Tester!" in result.stdout


class TestVersionCommand:
    """Tests for the version command."""

    def test_version_command(self):
        """Test version command outputs version."""
        result = runner.invoke(app, ["version"])
        assert result.exit_code == 0
        assert result.stdout.strip().startswith("v")

    def test_version_flag(self):
        """Test --version flag outputs version."""
        result = runner.invoke(app, ["--version"])
        assert result.exit_code == 0
        assert result.stdout.strip().startswith("v")

    def test_version_short_flag(self):
        """Test -v short flag outputs version."""
        result = runner.invoke(app, ["-v"])
        assert result.exit_code == 0
        assert result.stdout.strip().startswith("v")


class TestHelpCommand:
    """Tests for help output."""

    def test_help_flag(self):
        """Test --help shows usage information."""
        result = runner.invoke(app, ["--help"])
        assert result.exit_code == 0
        assert "hello" in result.stdout
        assert "goodbye" in result.stdout
        assert "version" in result.stdout

    def test_help_short_flag(self):
        """Test -h short flag shows usage information."""
        result = runner.invoke(app, ["-h"])
        assert result.exit_code == 0
        assert "hello" in result.stdout

    def test_hello_help(self):
        """Test hello --help shows command help."""
        result = runner.invoke(app, ["hello", "--help"])
        assert result.exit_code == 0
        assert "--name" in result.stdout

    def test_goodbye_help(self):
        """Test goodbye --help shows command help."""
        result = runner.invoke(app, ["goodbye", "--help"])
        assert result.exit_code == 0
        assert "--name" in result.stdout
