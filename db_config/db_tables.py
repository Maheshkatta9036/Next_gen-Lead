from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from datetime import datetime
import uuid

db = SQLAlchemy()
Base = declarative_base()

