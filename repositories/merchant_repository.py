from db.run_sql import run_sql
from modules.merchant import Merchant

def save(merchant):
    sql = "INSERT INTO merchants(name, description) VALUES (%s, %s) RETURNING ID"
    values = [merchant.name, merchant.description]
    results = run_sql(sql, values)
    merchant.id = results[0]['id']
    return merchant

def select_all():
    merchants = [] 
    sql = "SELECT * FROM merchants"
    results = run_sql(sql)
    for row in results:
        merchant = Merchant(row["name"], row["description"], row["id"])
        merchants.append(merchant)
    return merchants

def select(id):
    merchant = None
    sql = "SELECT * FROM merchants WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        merchant = Merchant(result["name"], result["description"], result["id"])
    return merchant 

def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM merchants WHERE id = %s"
    values = [id]
    run_sql(sql,values)

def update(merchant):
    sql = "UPDATE merchants SET (name, description) = (%s,%s) WHERE id = %s"
    values = [merchant.name, merchant.description, merchant.id]
    run_sql(sql, values)
