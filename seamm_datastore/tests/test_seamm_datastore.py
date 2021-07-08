"""
Unit and regression test for the seamm_datastore package.
"""

# Import package, test suite, and other packages as needed
import seamm_datastore
import pytest
import sys

def test_seamm_datastore_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "seamm_datastore" in sys.modules
