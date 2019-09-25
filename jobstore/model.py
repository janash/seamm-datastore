"""
Table models for SEAMM datastore SQLAlchemy database.
"""

from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

Base = declarative_base()

class Flowchart(Base):
    __tablename__ = 'flowcharts'

    id = Column(String, nullable=False, primary_key=True, unique=True)
    description = Column(String, nullable=True)
    flowchart_file = Column(String, nullable=False)

    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.description = kwargs['description']
        self.flowchart_file = kwargs['flowchart_file']

class Job(Base):
    __tablename__ = 'jobs'

    path = Column(String, nullable=False, primary_key=True)
    flowchart_id = Column(String, ForeignKey("flowcharts.id"))
    submission_date = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, **kwargs):
        self.path = kwargs['path']
        self.flowchart_id  = kwargs['flowchart_id']
        self.submission_date = kwargs['submission_date']

class Project(Base):
    __tablename__ = "projects"

    name = Column(String(100), nullable=False, primary_key=True)
    description = Column(String(1000), nullable=True, unique=False)

class JobProject(Base):
    __tablename__ = "project_jobs"

    id = Column(Integer, primary_key=True)
    job_path = Column(String, ForeignKey('jobs.path'))
    project = Column(String, ForeignKey('projects.name'))
