from flask import Blueprint, redirect, render_template, request, url_for
from config import mongo

router = Blueprint("main", __name__)


@router.route("/", methods=["GET", "POST"])
def main():
    db_collection = mongo.db.drugs
    items = db_collection.find()

    print(items)
    
    if request.method == "POST":
        print('Post')

    return render_template("main.html")