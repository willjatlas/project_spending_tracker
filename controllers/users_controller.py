from flask import Flask, Blueprint, render_template, redirect, request
from models.user import User

import repositories.user_repository as user_repository

users_blueprint = Blueprint("users", __name__)

# Index 
@users_blueprint.route("/users")
def users():
    users = user_repository.select_all()
    return render_template("users/index.html", users = users, title = "Users")

# New
@users_blueprint.route("/users/new")
def new_user():
    return render_template("users/new.html", title = "New User")

# Create
@users_blueprint.route("/users", methods=["POST"])
def create_user():
    first_name = request.form["first_name"]
    last_name  = request.form["last_name"]
    email      = request.form["email"]
    wallet     = float(request.form["wallet"])
    user       = User(first_name, last_name, email, wallet)
    user_repository.save(user)
    return redirect("/users")

# Delete
@users_blueprint.route("/users/<id>/delete")
def delete(id):
    user_repository.delete(id)
    return redirect("/users")

# Edit
@users_blueprint.route("/users/<id>/edit")
def edit(id):
    user = user_repository.select(id)
    return render_template("users/edit.html", user = user, title = "Edit User")

# Update
@users_blueprint.route("/users/<id>", methods=["POST"])
def update_user(id):
    first_name =  request.form["first_name"]
    last_name  =  request.form["last_name"]
    email      =  request.form["email"]
    wallet     =  float(request.form["wallet"])
    user       =  User(first_name, last_name, email, wallet, id)
    user_repository.update(user)
    return redirect("/users")

