from database import Database


class TripLeg:

    def __init__(self, id, start_location, destination, transport_provider, transport_mode):
        self.id = id
        self.start_location = start_location
        self.destination = destination
        self.transport_provider = transport_provider
        self.transport_mode = transport_mode
        self.db = Database('json/tripleg.json')

    # add a trip
    def save_tripleg(self):
        self.db.create_one_item_in_json({
            "trip_name": self.trip_name,
            "start_location": self.start_location,
            "destination": self.destination,
            "transport_provider": self.transport_provider,
            "transport_mode": self.transport_mode
        })

    # update trip
    def update_tripleg(self):
        self.db.update_one_item_in_json(0, {
            "trip_name": self.trip_name,
            "start_location": self.start_location,
            "destination": self.destination,
            "transport_provider": self.transport_provider,
            "transport_mode": self.transport_mode
        })

    # delete trip
    def delete_tripleg(self):
        self.db.delete_one_item_from_json(self.trip_name)
