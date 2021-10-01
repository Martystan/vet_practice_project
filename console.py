import pdb
from models.pet import Pet
from models.vet import Vet
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

pet_repository.delete_all()
vet_repository.delete_all()

vet1 = Vet("Eric Knight")
vet_repository.save(vet1)

pet1 = Pet("Lassie", "1/01/2019", "Rough Collie", "Joe Carraclough", "0123456789", "joe@gmail.com", "some notes", vet1)
pet_repository.save(pet1)

pdb.set_trace()

