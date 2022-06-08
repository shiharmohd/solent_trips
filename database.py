import json


class Database:

    def __init__(self, file_name):
        self.file_name = file_name

    def load_data(self):
        with open(self.file_name) as f:
            return json.load(f)

    # Save the file with new data
    def save_data(self, json_data):
        with open(self.file_name, 'w') as f:
            json.dump(json_data, f, indent=4)

    # Read an Item from file
    def get_one_item_from_json(self, id):
        json_data = self.load_data()
        for x in json_data:
            if x['id'] == id:
                return x

    # Read an user from file
    def get_one_user_from_json(self, username):
        json_data = self.load_data()
        for x in json_data:
            if x['username'] == username:
                return x

    # Create New Item and save it into file
    def create_one_item_in_json(self, data):
        json_data = self.load_data()
        json_data.append(data)
        self.save_data(json_data)

    # Delete One Item from Json
    def delete_one_item_from_json(self, id, value):
        json_data = self.load_data()
        for i in range(len(json_data)):
            if json_data[i][id] == value:
                del json_data[i]
                break
        self.save_data(json_data)

    # Update One Item from JSON
    def update_one_item_in_json(self, id, data):
        json_data = self.load_data()
        json_data[id] = data
        self.save_data(json_data)

    # Read an Item from file
    def get_one_item_from_json(self, id):
        json_data = self.load_data()
        for x in json_data:
            if x['id'] == id:
                return x