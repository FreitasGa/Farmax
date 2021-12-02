from flask import Blueprint, redirect, render_template, request, url_for
from config import mongo

router = Blueprint("main", __name__)


@router.route("/", methods=["GET", "POST"])
def main():
    items = mongo.db.drugs.find()
    items = [item for item in items]

    print(items, len(items))

    if request.method == "POST":
        print('Post')

    return render_template("main.html", items=items, lenght=len(items))