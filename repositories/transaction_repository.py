from db.run_sql import run_sql
from modules.transaction import Transaction
import repositories.user_repository as user_repository
import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository 

def save(transaction):
    sql = """INSERT INTO transactions(user_id, date, time, merchant_id,
            amount, tag_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING ID"""
    values = [transaction.user, transaction.date, transaction.time, 
            transaction.merchant, transaction.amount, transaction.tag]
    results = run_sql(sql, values)
    transaction.id = results[0]['id']
    return transaction

def select_all():
    transactions = [] 
    sql = "SELECT * FROM transactions"
    results = run_sql(sql)
    for row in results:
        user = user_repository.select(["user_id"])
        merchant = merchant_repository.select(["merchant_id"])
        tag = tag_repository.select(["tag_id"])
        transaction = Transaction(user, row["date"], row["time"], merchant,
                      row["amount"], tag, row["id"] ) 
        transactions.append(transaction)
    return transactions

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    value = [id]
    run_sql(sql, value)
    