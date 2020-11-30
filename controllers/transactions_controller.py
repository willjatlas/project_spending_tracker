from flask import Flask, Blueprint, render_template, redirect, request
from modules.transaction import Transaction

import repositories.transaction_repository as transaction_repository
import repositories.user_repository as user_repository
import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository

transactions_blueprint = Blueprint("transactions", __name__)

# Index - shows all transactions from the db.
@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    return render_template("transactions/index.html", transactions = transactions)


# New - shows the form page for entering a new transaction to hte db. 
@transactions_blueprint.route("/transactions/new")
def new_transaction():
    users = user_repository.select_all()
    tags = tag_repository.select_all()
    merchants = merchant_repository.select_all()
    return render_template("transactions/new.html", users = users, tags = tags, merchants = merchants)



