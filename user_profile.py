# UserProfile is the concrete object class
class UserProfile:

    # Constructor for a UserProfile object containing a variety of different fields that a UserProfile object will use
    def __init__(self, name, location, relationship_status, age, occupation, astrological_sign, status="", friend_list=[]):
        self.set_name(name)
        self.set_location(location)
        self.set_relationship_status(relationship_status)
        self.set_age(age)
        self.set_occupation(occupation)
        self.set_astrological_sign(astrological_sign)
        self.set_status(status)
        self.friend_list = friend_list if friend_list is not None else []

    # Returns the name of the UserProfile
    def get_name(self):
        return self.name
    
    # Sets the name of the UserProfile
    def set_name(self, name):
        self.name = name

    # Return the location of the UserProfile
    def get_location(self):
        return self.location
    
    # Sets the location of the UserProfile
    def set_location(self, location):
        self.location = location

    # Return the relationship status of the UserProfile
    def get_relationship_status(self):
        return self.relationship_status
    
    # Sets the relationship_status of the UserProfile
    def set_relationship_status(self, relationship_status):
        self.relationship_status = relationship_status

    # Returns the age of the UserProfile
    def get_age(self):
        return self.age
    
    # Sets the age of the UserProfile
    def set_age(self, age):
        self.age = age

    # Returns the occupation of the UserProfile
    def get_occupation(self):
        return self.occupation
    
    # Sets the occupation of the UserProfile
    def set_occupation(self, occupation):
        self.occupation = occupation

    # Returns the astrological sign of the UserProfile
    def get_astrological_sign(self):
        return self.astrological_sign
    
    # Sets the astrological_sign of the UserProfile
    def set_astrological_sign(self, astrological_sign):
        self.astrological_sign = astrological_sign

    # Returns the status of the 
    def get_status(self):
        return self.status

    # Sets the status
    def set_status(self, status):
        self.status = status

    # Returns the friends of this UserProfile
    def get_friends(self):
        return self.friend_list

    # Adds friend UserProfiles to this UserProfile's friends list
    def add_friend(self, friend_profile):
        self.friend_list.append(friend_profile)

    # Removes friend from UserProfile friends list
    def remove_friend(self, friend_profile):
        self.friend_list.remove(friend_profile)

    # Prints out the details of the UserProfile
    def print_details(self):
        print(f"Name: {self.get_name()}")
        print(f"Location: {self.get_location()}")
        print(f"Relationship Status: {self.get_relationship_status()}")
        print(f"Age: {self.get_age()}")
        print(f"Occupation: {self.get_occupation()}")
        print(f"Astrological Sign: {self.get_astrological_sign()}")
        print(f"Status: {self.get_status()}")
        print(f"Friends: {[friend.get_name() for friend in self.get_friends()]}")
    