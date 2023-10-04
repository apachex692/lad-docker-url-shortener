# Author: Sakthi Santhosh
# Created on: 25/08/2023
from datetime import datetime
from flask import url_for
from secrets import token_hex
from sqlalchemy import event

from lib import db_handle

class URLMap(db_handle.Model):
    __tablename__ = "url_map"

    id = db_handle.Column(
        db_handle.Integer,
        primary_key=True
    )
    actual_url = db_handle.Column(
        db_handle.Text,
        unique=False,
        nullable=False
    )
    shortened_url_token = db_handle.Column(
        db_handle.String(8),
        unique=True,
        nullable=False
    )
    created_on = db_handle.Column(
        db_handle.DateTime(),
        default=datetime.now,
        unique=False,
        nullable=False
    )

    def shortened_url(self):
        return url_for(
            endpoint="redirect_handle",
            _external=True,
            token=self.shortened_url_token
        )

    def __repr__(self):
        return f"<URLMap {self.actual_url}: {self.shortened_url_token}>"

@event.listens_for(target=URLMap, identifier="before_insert")
def create_shortened_url(mapper, connection, target):
    target.shortened_url_token = token_hex(4)
