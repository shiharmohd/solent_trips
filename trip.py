import json

from database import Database


class Trip:

    def __init__(self, name, start_date, travellers, duration, coordinator, contact):
        self.name = name
        self.start_date = start_date
        self.contact = contact
        self.coordinator = coordinator
        self.travellers = travellers
        self.duration = duration
        self.db = Database('json/trip.json')

    # add a trip
    def save_trip(self):
        self.db.create_one_item_in_json({
            "name": self.name,
            "start_date": self.start_date,
            "travellers": self.travellers,
            "duration": self.duration,
            "coordinator": self.coordinator,
            "contact": self.contact
        })

    # update trip
    def update_trip(self):
        self.db.update_one_item_in_json(0, {
            "name": self.name,
            "start_date": self.start_date,
            "travellers": self.travellers,
            "duration": self.duration,
            "coordinator": self.coordinator,
            "contact": self.contact
        })

    # delete trip
    def delete_trip(self):
        self.db.delete_one_item_from_json("name", self.name)
