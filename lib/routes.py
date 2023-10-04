# Author: Sakthi Santhosh
# Created on: 25/08/2023
from flask import redirect, render_template, request

from lib import app_handle, db_handle
from lib.models import URLMap

@app_handle.route('/')
def index_handle():
    url = request.args.get("url")

    if url is None or url == '':
        return render_template("index.html")

    data = URLMap.query.filter_by(actual_url=url).first()

    if data is None:
        data = URLMap(actual_url=url)

        db_handle.session.add(data)
        db_handle.session.commit()
    return render_template("output.html", url=data.shortened_url())

@app_handle.route("/r/<string:token>")
def redirect_handle(token: str):
    data = URLMap.query.filter_by(shortened_url_token=token).first_or_404()
    return redirect(data.actual_url)
