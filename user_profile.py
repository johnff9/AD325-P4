class UserProfile:
    def __init__(self, name, location, relationship_status, age, occupation, astrological_sign, status=""):
        self.name = name
        self.location = location
        self.relationship_status = relationship_status
        self.age = age
        self.occupation = occupation
        self.astrological_sign = astrological_sign
        self.status = status
        self.friends = []

    def get_name(self):
        return self.name

    def get_location(self):
        return self.location

    def get_relationship_status(self):
        return self.relationship_status

    def get_age(self):
        return self.age

    def get_occupation(self):
        return self.occupation

    def get_astrological_sign(self):
        return self.astrological_sign

    def get_status(self):
        return self.status

    def set_name(self, name):
        self.name = name

    def set_location(self, location):
        self.location = location

    def set_relationship_status(self, relationship_status):
        self.relationship_status = relationship_status

    def set_age(self, age):
        self.age = age

    def set_occupation(self, occupation):
        self.occupation = occupation

    def set_astrological_sign(self, astrological_sign):
        self.astrological_sign = astrological_sign

    def set_status(self, status):
        self.status = status

    def add_friend(self, friend_profile):
        if friend_profile not in self.friends:
            self.friends.append(friend_profile)

    def remove_friend(self, friend_profile):
        if friend_profile in self.friends:
            self.friends.remove(friend_profile)

    def get_friends(self):
        return [friend.get_name() for friend in self.friends]

    def print_details(self):
        print(f"Name: {self.name}\nLocation: {self.location}\nRelationship Status: {self.relationship_status}")
        print(f"Age: {self.age}\nOccupation: {self.occupation}\nAstrological Sign: {self.astrological_sign}\nStatus: {self.status}")
        print("Friends: ", ", ".join(self.get_friends()))
