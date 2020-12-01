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
    transactions =  transaction_repository.select_all()
    users        =  user_repository.select_all()
    total_amount =  0.00
    for transaction in transactions:
        total_amount += float(transaction.amount)
    return render_template("transactions/index.html", transactions = transactions, 
                            users = users, total_amount = total_amount)

# Index user transactions. 
@transactions_blueprint.route("/transactions/by_user", methods=["POST"])
def user_transactions():
    user_id      =  request.form["user_id"]
    user         =  user_repository.select(user_id)
    transactions =  transaction_repository.select_by_user(user_id)
    total_amount =  0.00
    for transaction in transactions:
        total_amount += float(transaction.amount)
    return render_template("transactions/user_index.html", transactions = transactions,
                            user = user , total_amount = format(total_amount, '.2f'))

# New - shows the form page for entering a new transaction to hte db. 
@transactions_blueprint.route("/transactions/new")
def new_transaction():
    users     =  user_repository.select_all()
    tags      =  tag_repository.select_all()
    merchants =  merchant_repository.select_all()
    return render_template("transactions/new.html", users = users, tags = tags,
                            merchants = merchants)

# Create - adds the from entry to the db.
@transactions_blueprint.route("/transactions", methods=["POST"])
def create_transaction():
    user_id     =  request.form["user_id"]
    date        =  request.form["date"]
    time        =  request.form["time"]
    merchant_id =  request.form["merchant_id"]
    amount      =  float(request.form["amount"])
    tag_id      =  request.form["tag_id"]
    user        =  user_repository.select(user_id)
    merchant    =  merchant_repository.select(merchant_id)
    tag         =  tag_repository.select(tag_id)
    transaction =  Transaction(user, date, time, merchant, amount, tag)
    transaction_repository.save(transaction)
    return redirect("/transactions")







