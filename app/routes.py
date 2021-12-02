from flask import Blueprint, redirect, render_template, request, url_for
from config import mongo

router = Blueprint("router", __name__)


@router.route("/", methods=["GET", "POST"])
def main():
    medicine_collection = mongo.db.medicine

    items = medicine_collection.find()
    items = [item for item in items]

    print(items, len(items))

    if request.method == "POST":
        name = request.form.get("Nome")
        description = request.form.get("Descricao")
        price = request.form.get("Preco")

        item = {"name": name, "price": price, "description": description}
        medicine_collection.insert_one(item)
        print(item)

    return render_template("main.html", items=items, lenght=len(items))