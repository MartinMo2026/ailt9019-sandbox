"""Worked Example 4 · Check an environment variable safely.

Run me with: python check_env.py
"""

import os

VAR_NAME = "PATH"  # change me to any env var you want to test


def env_exists(name):
    """Return True if the env var `name` is set, False otherwise.

    Never prints or returns the value itself.
    """
    return name in os.environ


if __name__ == "__main__":
    exists = env_exists(VAR_NAME)
    print(f"Does env var '{VAR_NAME}' exist? -> {exists}")