from extentions import db
from uuid import uuid4

class Job(db.Model):
    __tablename__ = 'job'

    id = db.Column(db.String(), primary_key=True, default=str(uuid4()))
    title = db.Column(db.String(), nullable=False)
    description = db.Column(db.Text())
    profile_id = db.Column(db.String(), db.ForeignKey('profile.id'))

    def __repr__(self):
        return f"<Job {self.title}>"
