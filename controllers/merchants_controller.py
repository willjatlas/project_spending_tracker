from flask import Blueprint, Flask, redirect, render_template, request
import repositories.merchant_repository as merchant_repository

merchants_blueprint = Blueprint("merchants", __name__)

# @merchants_blueprint.route("/merchants")
# def merchants():
#     merchants = merchant_repository.select_all()
#     return render_template("")