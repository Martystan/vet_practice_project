from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.pet import Pet
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

pets_blueprint = Blueprint("pets", __name__)

@pets_blueprint.route("/pets")
def pets():
    pets = pet_repository.select_all()
    return render_template("pets/index.html", all_pets = pets)

@pets_blueprint.route("/pets/<id>", methods = ['GET'])
def show_pet_info(id):
    pet = pet_repository.select(id)
    return render_template('pets/show_pet_info.html', pet = pet)

@pets_blueprint.route("/pets/<id>/edit", methods = ['GET'])
def edit_pet(id):
    pet = pet_repository.select(id)
    vets = vet_repository.select_all()
    return render_template('pets/edit.html', pet = pet, all_vets = vets)

@pets_blueprint.route("/pets/<id>", methods = ['POST'])
def update_pet(id):
    print(request.form)
    name = request.form['name']
    dob = request.form['dob']
    type = request.form['type']
    owner = request.form['owner']
    owner_email = request.form['owner_email']
    owner_tel = request.form['owner_tel']
    notes = request.form['notes']
    vet_id = request.form['vet_id']
    vet = vet_repository.select(vet_id)
    pet = Pet(name, dob, type, owner, owner_tel, owner_email, notes, vet, id)
    pet_repository.update(pet)
    return redirect("/pets/" + id)

@pets_blueprint.route("/pets/new", methods = ['GET'])
def add_patient():
    vets = vet_repository.select_all()
    render_template("pets/new.html", all_vets = vets)
