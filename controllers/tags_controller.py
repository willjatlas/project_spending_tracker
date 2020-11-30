from flask import Blueprint, Flask, redirect, render_template, request
from modules.tag import Tag

import repositories.tag_repository as tag_repository

tags_blueprint = Blueprint("tags", __name__)

# Index 
@tags_blueprint.route("/tags")
def tags():
    tags = tag_repository.select_all()
    return render_template("tags/index.html", tags = tags)

# New
@tags_blueprint.route("/tags/new")
def new_tag():
    return render_template("tags/new.html")

# Create
@tags_blueprint.route("/tags", methods=["POST"])
def create_tag():
    tag_type = request.form["tag_type"]
    tag = Tag(tag_type)
    tag_repository.save(tag)
    return redirect("/tags")

# Delete
@tags_blueprint.route("/tags/<id>/delete")
def delete(id):
    tag_repository.delete(id)
    return redirect("/tags")

# Edit
@tags_blueprint.route("/tags/<id>/edit")
def edit(id):
    tag = tag_repository.select(id)
    return render_template("tags/edit.html", tag = tag)

# Update
@tags_blueprint.route("/tags/<id>", methods=["POST"])
def update_tag(id):
    tag_type = request.form["tag_type"]
    tag = Tag(tag_type, id)
    tag_repository.update(tag)
    return redirect("/tags")


    