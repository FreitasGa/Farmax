from flask import Blueprint, redirect, render_template, request, url_for, flash
from config import mongo
from calc import calcMax

router = Blueprint("router", __name__)


@router.route("/", methods=["GET"])
def main():
    medicine_collection = mongo.db.medicine

    items = medicine_collection.find()
    items = [item for item in items]

    return render_template("main.html", items=items, lenght=len(items))


@router.route("/add_medicine", methods=["POST"])
def add_medicine():
    medicine_collection = mongo.db.medicine

    name = request.form.get("Nome")
    description = request.form.get("Descricao")
    price = request.form.get("Preco")

    price = int(price)
    count = calcMax(price)
    max = count * price

    if name != medicine_collection.find_one({"name": name})["name"]:
        print("cheguei")
        item = {"name": name, "price": price, "description": description, "count": count, "max": max}
        medicine_collection.insert_one(item)

    else:
        flash('Remédio já cadastrado!')

    return redirect(url_for("router.main"))
