from db.run_sql import run_sql
from models.pet import Pet
from models.vet import Vet
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

def save(pet):
    sql = "INSERT INTO pets(name, dob, type, owner, owner_tel, owner_email, notes, vet_id) VALUES (%s, %s,%s,%s,%s,%s,%s,%s) RETURNING *"
    values = [pet.name, pet.dob, pet.type, pet.owner, pet.owner_tel, pet.owner_email, pet.notes, pet.vet.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    pet.id = id
    return pet

def delete_all():
    sql = "DELETE FROM pets"
    run_sql(sql)