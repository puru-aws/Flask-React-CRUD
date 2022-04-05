from app import db, ma
from datetime import datetime


class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return "<Articles %r>" % self.title


class ArticlesShema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "title", "body", "date")
