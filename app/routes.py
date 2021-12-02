import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

router = Blueprint("main", __name__)

@router.route("/", methods=("GET", "POST"))
def main():
    if request.method == "POST":
        print('Post')

    return render_template("main.html")