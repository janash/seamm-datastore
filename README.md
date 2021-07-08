seamm_datastore
==============================
[//]: # (Badges)
[![GitHub Actions Build Status](https://github.com/molssi-seamm/seamm_datastore/workflows/CI/badge.svg)](https://github.com/molssi-seamm/seamm_datastore/actions?query=workflow%3ACI)
[![codecov](https://codecov.io/gh/molssi-seamm/seamm_datastore/branch/master/graph/badge.svg)](https://codecov.io/gh/molssi-seamm/seamm_datastore/branch/master)


This package contains SQLAlchemy models for the SEAMM datastore. The following gives an example of how to connect to a database in memory. You can switch the database by providing a different database URI.

```python
import seamm_datastore

# Create a database session
db = seamm_datastore.connect("sqlite:///memory:", initialize=True)
```

### Copyright

Copyright (c) 2021, Jessica A. Nash (The Molecular Sciences Software Institute)


#### Acknowledgements
 
Project based on the 
[Computational Molecular Science Python Cookiecutter](https://github.com/molssi/cookiecutter-cms) version 1.5.
