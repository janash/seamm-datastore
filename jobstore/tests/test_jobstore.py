"""
Unit and regression test for the jobstore package.
"""

# Import package, test suite, and other packages as needed
import jobstore
import pytest
import sys

def test_jobstore_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "jobstore" in sys.modules
