from db.run_sql import run_sql
from modules.tag import Tag

def save(tag):
    sql = "INSERT INTO tags(tag_type) VALUES (%s) RETURNING ID"
    values = [tag.tag_type]
    results = run_sql(sql, values)
    tag.id = results[0]['id']
    return tag

def select_all():
    tags = [] 
    sql = "SELECT * FROM tags"
    results = run_sql(sql)
    for row in results:
        tag = Tag(row["tag_type"], row["id"])
        tags.append(tag)
    return tags

def select(id):
    tag = None
    sql = "SELECT * FROM tags WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        tag = Tag(result["tag_type"], result["id"])
    return tag

def delete_all():
    sql = "DELETE FROM tags"
    run_sql(sql)