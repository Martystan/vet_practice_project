from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.pet import Pet
from models.vet import Vet
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

vets_blueprint = Blueprint("vets", __name__)

@vets_blueprint.route("/vets")
def vets():
    vets = vet_repository.select_all()
    return render_template("vets/index.html", all_vets = vets)

@vets_blueprint.route("/vets/<vet_id>", methods = ['GET'])
def show_vets_pets(vet_id):
    
    pets = vet_repository.select_by_vet(vet_id)
    vet = vet_repository.select(vet_id)
    
    return render_template('vets/my_pets.html', vet= vet , all_pets = pets)
