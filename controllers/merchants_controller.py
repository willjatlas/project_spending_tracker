from flask import Blueprint, Flask, redirect, render_template, request
from modules.merchant import Merchant

import repositories.merchant_repository as merchant_repository

merchants_blueprint = Blueprint("merchants", __name__)

# Index
@merchants_blueprint.route("/merchants")
def merchants():
    merchants = merchant_repository.select_all()
    return render_template("merchants/index.html", merchants = merchants,
                            title = "Merchants")

# New
@merchants_blueprint.route("/merchants/new")
def new_merchant():
    return render_template("merchants/new.html", title = "New Merchant")

# Create
@merchants_blueprint.route("/merchants", methods=["POST"])
def create_merchant():
    name        =  request.form["name"]
    description =  request.form["description"]
    merchant    =  Merchant(name, description)
    merchant_repository.save(merchant)
    return redirect("/merchants")

# Delete
@merchants_blueprint.route("/merchants/<id>/delete")
def delete(id):
    merchant_repository.delete(id)
    return redirect("/merchants")

# Edit 
@merchants_blueprint.route("/merchants/<id>/edit")
def edit(id):
    merchant = merchant_repository.select(id)
    return render_template("merchants/edit.html", merchant = merchant, 
                            title = "Edit Merchant")

# Update
@merchants_blueprint.route("/merchants/<id>", methods=["POST"])
def update_merchant(id):
    name        =  request.form["name"]
    description =  request.form["description"]
    merchant    =  Merchant(name, description, id)
    merchant_repository.update(merchant)
    return redirect("/merchants")

