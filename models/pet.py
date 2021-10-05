class Pet:
    def __init__(self, name, photo, dob, type, owner, owner_tel, owner_email, notes, vet, id = None):
        self.name = name
        self.photo = photo
        self.dob = dob
        self.type = type
        self.owner = owner
        self.owner_tel = owner_tel
        self.owner_email = owner_email
        self.notes = notes
        self.vet = vet
        self.id = id