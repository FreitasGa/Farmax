from flask import Blueprint, redirect, render_template, request, url_for, flash
from config import mongo

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
        
    if name != medicine_collection.find({"name": name}):
        item = {"name": name, "price": price, "description": description}
        medicine_collection.insert_one(item)

    elif name == medicine_collection.find({"name": name}):
        flash('Remédio já cadastrado!')

    return redirect(url_for("router.main"))