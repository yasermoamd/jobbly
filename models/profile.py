from extentions import db
from uuid import uuid4
from models.job import Job
from typing import List


class Profile(db.Model):
    __tablename__ = 'profile'
    
    id = db.Column(db.String(), primary_key=True, default=str(uuid4()))
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    job_title = db.Column(db.String(), nullable=False)
    user_id = db.Column(db.String(), db.ForeignKey('user.id'), default=str(uuid4()))
    jobs = db.relationship(List[Job], backref='profile', lazy=True, uselist=True)

    def __repr__(self):
        return f"<Profile {self.first_name} {self.last_name} account>"
