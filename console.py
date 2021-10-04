import pdb
from models.pet import Pet
from models.vet import Vet
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

pet_repository.delete_all()
vet_repository.delete_all()

vet1 = Vet("Eric Knight")
vet_repository.save(vet1)

vet2 = Vet("John Dolittle")
vet_repository.save(vet2)

pet1 = Pet("Lassie", "01/01/2019", "Rough Collie", "Joe Carraclough", "0123456789", "joe@gmail.com", "some notes", vet1)
pet_repository.save(pet1)

pet2 = Pet("Crookshanks", "01/09/2010", "Persian", "Hermione Granger", "012345667788", "hermione@hogwarts.com", "some notes", vet2 )
pet_repository.save(pet2)

vet1.name = "Dr Dolittle"
vet_repository.update(vet1)

pet1.name = "whatevs"
pet_repository.update(pet1)

# for vet in vet_repository.select_all():
#     print(vet.__dict__)

# for pet in pet_repository.select_all():
#     print(pet.__dict__)

pdb.set_trace()

