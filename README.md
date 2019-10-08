SEAMM Jobstore
==============================
[//]: # (Badges)
[![Travis Build Status](https://travis-ci.org/REPLACE_WITH_OWNER_ACCOUNT/jobstore.png)](https://travis-ci.org/REPLACE_WITH_OWNER_ACCOUNT/jobstore)
[![AppVeyor Build status](https://ci.appveyor.com/api/projects/status/REPLACE_WITH_APPVEYOR_LINK/branch/master?svg=true)](https://ci.appveyor.com/project/REPLACE_WITH_OWNER_ACCOUNT/jobstore/branch/master)
[![codecov](https://codecov.io/gh/REPLACE_WITH_OWNER_ACCOUNT/jobstore/branch/master/graph/badge.svg)](https://codecov.io/gh/REPLACE_WITH_OWNER_ACCOUNT/jobstore/branch/master)

Tools for storing jobs from MolSSI SEAMM.

This repository contains the model and some functions for a simple job datastore for SEAMM. The current implementation assumes jobs have already been run, and the user wants to add them to a database (just used sqlite for now, but is implemented with sqlalchemy) to keep track of what jobs have been run, their submission time, locations, and procedure (flowchart) used.

Jobs may also be added to projects to allow grouping of jobs.

Current table structure:

`flowcharts` table
------------------
*Description* - This table holds information about the flowcharts used in jobs.

- `id` - The flowchart id - based on a hash of the flowchart text (primary key)
- `description` - A description of the flowchart (optional)
- `flowchart_file` - The text (json) of the flowchart

`jobs` table
------------
*Description* - This table holds information about the jobs which have been run. Jobs are identified by the presence of a `job.out` file and a flowchart being present in a directory.

- `path` - The location (path) of the job (primary key)
- `flowchart_id` - The flowchart ID (foreign key `flowcharts.id`)
- `submission_date` - The date and time the flowchart was run. Currently based on the last modification date of the `flowcharts.flow` file.
- `author` - (optional column) - The person who submitted the job.

`projects` table
----------------
*Description* - This table holds information about projects. In this table, the projects are not associated with any jobs.

- `name` - The name of the project. Limited to 100 characters. (primary key)
- `description` - A description of the project. Limited to 1000 characters

`project_jobs` table
--------------------
*Description* - This table links jobs (from `jobs` table) with projects (from `projects` table).

- `job_path` - The location of a job (foreign key `jobs.path`, primary key)
- `project` - The project name (foreign key `projects.name`, primary key)

`users` table
-------------
*Description* - This table contains user information for accessing the database. Will be used eventually to limit which users can access jobs/projects.

- `username` - The username of the user (primary key)
- `email` - The email address of the user
- `password` - The password of the user (will be hashed)

`user_projects` table
---------------------
*Description* - This table links users with projects.

- `user` - The username of user (primary key, foreign key in users.username)
- `project` - The name of a project (primary key, foreign key in projets.name)


### Copyright

Copyright (c) 2019, Jessica Nash


#### Acknowledgements
 
Project based on the 
[Computational Molecular Science Python Cookiecutter](https://github.com/molssi/cookiecutter-cms) version 1.1.
