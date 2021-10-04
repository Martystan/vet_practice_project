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

def select_all():
    pets = []
    sql = "SELECT * FROM pets"
    results = run_sql(sql)
    for row in results:
        vet = vet_repository.select(row['vet_id'])
        pet = Pet(row['name'], row['dob'], row['type'], row['owner'], row['owner_tel'], row['owner_email'], row['notes'], vet, row['id'])
        pets.append(pet)
    return(pets)

def select(id):
    pet = None
    sql = "SELECT * FROM pets WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        vet = vet_repository.select(result['vet_id'])
        pet = Pet(result['name'], result['dob'], result['type'], result['owner'], result['owner_tel'], result['owner_email'], result['notes'], vet, result['id'])
    return pet

def update(pet):
    sql = "UPDATE pets SET(name, dob, type, owner, owner_tel, owner_email, notes, vet_id) = (%s,%s,%s,%s,%s,%s,%s,%s) WHERE id = %s"
    values = [pet.name, pet.dob, pet.type, pet.owner, pet.owner_tel, pet.owner_email, pet.notes, pet.vet.id, pet.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM pets"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM pets WHERE id = %s"
    values = [id]
    run_sql(sql, values)
