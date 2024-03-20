from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

Base = DeclarativeBase()
db = SQLAlchemy()