from database import Database


class SystemUser:
    def __init__(self, id, name, user_type, username, password):
        self.id = id
        self.name = name
        self.user_type = user_type
        self.username = username
        self.password = password
        self.db = Database('json/users.json')

    # add a user
    def save_user(self):
        self.db.create_one_item_in_json({
            "id": self.id,
            "name": self.name,
            "user_type": self.user_type,
            "username": self.username,
            "password": self.password
        })

    # update user
    def update_user(self):
        self.db.update_one_item_in_json(0, {
            "id": self.id,
            "name": self.name,
            "user_type": self.user_type,
            "username": self.username,
            "password": self.password
        })

    # delete user
    def delete_user(self):
        self.db.delete_one_item_from_json("id", self.id)

