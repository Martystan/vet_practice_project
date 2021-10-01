from db.run_sql import run_sql
from models.pet import Pet
from models.vet import Vet

def save(vet):
    sql = "INSERT INTO vets(name) VALUES (%s) RETURNING *"
    values = [vet.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    vet.id = id
    return vet

def delete_all():
    sql = "DELETE FROM vets"
    run_sql(sql)