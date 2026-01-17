"""Tests for the Greeter class in tools module."""

from silicon.tools import Greeter


class TestGreeter:
    """Tests for the Greeter class."""

    def test_greet_default(self):
        """Test greeting with default name."""
        greeter = Greeter()
        assert greeter.greet() == "Hello, World!"

    def test_greet_custom_name(self):
        """Test greeting with custom name."""
        greeter = Greeter("Developer")
        assert greeter.greet() == "Hello, Developer!"

    def test_farewell_default(self):
        """Test farewell with default name."""
        greeter = Greeter()
        assert greeter.farewell() == "Goodbye, World!"

    def test_farewell_custom_name(self):
        """Test farewell with custom name."""
        greeter = Greeter("Developer")
        assert greeter.farewell() == "Goodbye, Developer!"

    def test_name_attribute(self):
        """Test that name attribute is stored correctly."""
        greeter = Greeter("Test")
        assert greeter.name == "Test"

    def test_name_attribute_default(self):
        """Test that default name attribute is World."""
        greeter = Greeter()
        assert greeter.name == "World"
