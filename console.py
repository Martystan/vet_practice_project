import pdb
from models.pet import Pet
from models.vet import Vet
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

pet_repository.delete_all()
vet_repository.delete_all()

vet1 = Vet("Dr Noel Fitzpatrick")
vet_repository.save(vet1)

vet2 = Vet(" Dr John Dolittle")
vet_repository.save(vet2)

vet4 = Vet(" Dr Elinor McGrath")
vet_repository.save(vet4)

vet3 = Vet(" Dr James Herriot")
vet_repository.save(vet3)

pet1 = Pet("Lassie", "https://upload.wikimedia.org/wikipedia/commons/4/48/Rough_Collie_600.jpg",  "01/01/2019", "Rough Collie", "Joe Carraclough", "0123456789", "joe@gmail.com", "some notes", vet1)
pet_repository.save(pet1)

pet2 = Pet("Crookshanks","https://s36537.pcdn.co/wp-content/uploads/2018/11/persian-cat-face.jpg.optimal.jpg", "01/09/2010", "Persian", "Hermione Granger", "012345667788", "hermione@hogwarts.com", "some notes", vet2 )
pet_repository.save(pet2)

pet3 = Pet("Marley", "http://media2.s-nbcnews.com/i/msnbc/Components/Photos/060123/060123_marleyandme_vmed_230p.jpg", "1/01/2010", "Labrador Retriever", "John Grogan", "098765432", "john@gmail.com", "Destructive but cute", vet2 )
pet_repository.save(pet3)

pet4 = Pet("Marley", "http://media2.s-nbcnews.com/i/msnbc/Components/Photos/060123/060123_marleyandme_vmed_230p.jpg", "1/01/2010", "Labrador Retriever", "John Grogan", "098765432", "john@gmail.com", "Destructive but cute", vet2 )
pet_repository.save(pet4)

pet5 = Pet("Marley", "http://media2.s-nbcnews.com/i/msnbc/Components/Photos/060123/060123_marleyandme_vmed_230p.jpg", "1/01/2010", "Labrador Retriever", "John Grogan", "098765432", "john@gmail.com", "Destructive but cute", vet2 )
pet_repository.save(pet5)

pet6 = Pet("Marley", "http://media2.s-nbcnews.com/i/msnbc/Components/Photos/060123/060123_marleyandme_vmed_230p.jpg", "1/01/2010", "Labrador Retriever", "John Grogan", "098765432", "john@gmail.com", "Destructive but cute", vet3 )
pet_repository.save(pet6)

pet7 = Pet("Crookshanks","https://s36537.pcdn.co/wp-content/uploads/2018/11/persian-cat-face.jpg.optimal.jpg", "01/09/2010", "Persian", "Hermione Granger", "012345667788", "hermione@hogwarts.com", "some notes", vet1 )
pet_repository.save(pet7)

pet8 = Pet("Crookshanks","https://s36537.pcdn.co/wp-content/uploads/2018/11/persian-cat-face.jpg.optimal.jpg", "01/09/2010", "Persian", "Hermione Granger", "012345667788", "hermione@hogwarts.com", "some notes", vet3 )
pet_repository.save(pet8)

pet9 = Pet("Alex","https://lh3.googleusercontent.com/proxy/1X0XcFctvMFzwWaI7qxhBuoukEa0pQtYrbGTxtPLUuCPcTICmo5JIJb1I1lQL0eNeVgLXzw1u6oneUVDIHmcivCgUvMiqX8JWVGtqatR8EUV", "01/09/2010", "African Grey Parrot", "Irene Pepperberg", "012345667788", "hermione@hogwarts.com", "smarter than most people", vet4 )
pet_repository.save(pet9)

pdb.set_trace()