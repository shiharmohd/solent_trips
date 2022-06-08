from database import Database


class Traveller:

    def __init__(self, id, name, address, date_of_birth, emergency_contact, government_id):
        self.id = id
        self.name = name
        self.address = address
        self.date_of_birth = date_of_birth
        self.emergency_contact = emergency_contact
        self.government_id = government_id
        self.db = Database('json/traveller.json')

    # add traveller
    def save_traveller(self):
        self.db.create_one_item_in_json({
            "id" : self.id,
            "name": self.name,
            "address" : self.address,
            "date_of_birth": self.date_of_birth,
            "emergency_contact": self.emergency_contact,
            "government_id": self.government_id
        })

    # update trip
    def update_traveller(self):
        self.db.update_one_item_in_json(0, {
            "id" : self.id,
            "name": self.name,
            "address": self.address,
            "date_of_birth": self.date_of_birth,
            "emergency_contact": self.emergency_contact,
            "government_id": self.government_id
        })

    # delete trip
    def delete_traveller(self):
        self.db.delete_one_item_from_json("id", self.id)