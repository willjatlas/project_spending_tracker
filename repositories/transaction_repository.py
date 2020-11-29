from db.run_sql import run_sql
from modules.transaction import Transaction
import repositories.user_repository as user_repository
import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository 

def save(transaction):
    sql = """INSERT INTO transactions(user_id, date, time, merchant_id,
            amount, tag_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"""
    values = [transaction.user.id, transaction.date, transaction.time, 
            transaction.merchant.id, transaction.amount, transaction.tag.id]
    results = run_sql(sql, values)
    transaction.id = results[0]['id']
    return transaction

def select_all():
    transactions = [] 
    sql = "SELECT * FROM transactions"
    results = run_sql(sql)
    for result in results:
        user = user_repository.select(result["user_id"])
        merchant = merchant_repository.select(result["merchant_id"])
        tag = tag_repository.select(result["tag_id"])
        transaction = Transaction(user, result["date"], result["time"], merchant,
                      result["amount"], tag, result["id"] ) 
        transactions.append(transaction)
    return transactions

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)

def delete(id): 
    sql = "DELETE FROM transactions WHERE id = %s"
    value = [id]
    run_sql(sql, value)
    