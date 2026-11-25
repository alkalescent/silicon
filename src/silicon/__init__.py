"""Package initialization with dynamic version and public API exports."""

from silicon.tools import Greeter

try:
    # Written by the hatch-vcs build hook, so Nuitka binaries compile it in
    from silicon._version import __version__
except ImportError:  # Source tree that was never built or installed
    __version__ = "0.0.0"

__all__ = ["Greeter", "__version__"]
