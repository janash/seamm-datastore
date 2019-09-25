"""
Unit and regression test for the jobstore package.
"""

# Import package, test suite, and other packages as needed
import jobstore
import pytest
import sys
import os

@pytest.fixture(scope="module", params=["sqlite"])
def seamm_datastore(request):
    file_path = os.path.dirname(__file__)
    data_path = os.path.join(file_path, "..","data")
    db_path = os.path.join(data_path, "test.db")
    seamm_datastore = jobstore.DataStore(db_path=db_path, db_type=request.param)

    yield data_path, seamm_datastore

def test_jobstore_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "jobstore" in sys.modules

def test_datastore_creation(seamm_datastore):
    
    data_path, datastore = seamm_datastore
    store_location = os.path.join(data_path, "test.db")

    assert os.path.exists(store_location)


def test_add_flowchart(seamm_datastore):
    data_path, datastore = seamm_datastore
    one_flowchart = os.path.join(data_path, "1", "flowchart.flow")
    datastore.add_flowchart(one_flowchart)

    stored_flowchart = datastore.get_flowchart_file()

    assert stored_flowchart
    assert len(stored_flowchart) == 1

    with open(one_flowchart) as f:
        reference_data = f.read()
    
    assert reference_data == stored_flowchart[0][0]