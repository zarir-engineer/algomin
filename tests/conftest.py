# tests/conftest.py
import os
import sys

# Insert project root (one level up from tests/) into path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
