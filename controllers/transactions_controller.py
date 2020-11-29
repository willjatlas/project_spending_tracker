from flask import Flask, Blueprint, render_template, redirect, request

import repositories.transaction_repository as transaction_repository

transactions_blueprint = Blueprint("transactions", __name__)

#Index 
@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    return render_template("transactions/index.html", transactions = transactions)

