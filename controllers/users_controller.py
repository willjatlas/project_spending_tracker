from flask import Flask, Blueprint, render_template, redirect, request
from modules.user import User

import repositories.user_repository as user_repository

users_blueprint = Blueprint("users", __name__)

# Index 
@users_blueprint.route("/users")
def users():
    users = user_repository.select_all()
    return render_template("users/index.html", users = users)

# New
@users_blueprint.route("/users/new")
def new_user():
    return render_template("users/new.html")

# Create
@users_blueprint.route("/users", methods=["POST"])
def create_user():
    pass

# Delete
@users_blueprint.route("/users/<id>/delete")
def delete(id):
    user_repository.delete(id)
    return redirect("/users")

# Edit
@users_blueprint.route("/users/<id>/edit")
def edit(id):
    user = user_repository.select(id)
    return render_template("users/edit.html", user = user)

# Update
@users_blueprint.route("/users/<id>", methods=["POST"])
def update_user(id):
    pass

