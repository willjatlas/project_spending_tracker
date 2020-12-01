from db.run_sql import run_sql
from modules.user import User 

def save(user):
    sql = """INSERT INTO users(first_name, last_name, email, wallet)
             VALUES (%s, %s, %s, %s) RETURNING ID"""
    values = [user.first_name, user.last_name, user.email, user.wallet]
    results = run_sql(sql, values)
    user.id = results[0]['id']
    return user

def select_all():
    users = [] 
    sql = "SELECT * FROM users"
    results = run_sql(sql)
    for row in results:
        user = User(row["first_name"], row["last_name"],
                row["email"], row["wallet"], row["id"])
        users.append(user)
    return users

def select(id):
    user = None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        user = User(result["first_name"], result["last_name"], result["email"],
               result["wallet"], result["id"])
    return user

def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)

def delete(id):
    sql ="DELETE FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(user):
    sql = """UPDATE users SET (first_name, last_name, email,
             wallet) = (%s, %s, %s, %s) WHERE id = %s"""
    values = [user.first_name, user.last_name, user.email, user.wallet, user.id]
    run_sql(sql, values)