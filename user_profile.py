# UserProfile is the concrete object class
class UserProfile:

    # Constructor for a UserProfile object containing a variety of different fields that a UserProfile object will use
    def __init__(self, name, location, relationship_status, age, occupation, astrological_sign, status=""):
        self.name = name
        self.location = location
        self.relationship_status = relationship_status
        self.age = age
        self.occuptation = occupation
        self.astrological_sign = astrological_sign
        self.setStatus(status)

    # Returns the name of the UserProfile
    def get_name(self):
        return self.name

    # Return the location of the UserProfile
    def get_location(self):
        return self.location

    # Return the relationship status of the UserProfile
    def get_relationship_status(self):
        return self.relationship_status

    # Returns the age of the UserProfile
    def get_age(self):
        return self.age

    # Returns the occupation of the UserProfile
    def get_occupation(self):
        return self.occuptation

    # Returns the astrological sign of the UserProfile
    def get_astrological_sign(self):
        return self.astrological_sign

    # Returns the status of the 
    def get_status(self):
        return self.status

    # Sets the status
    def set_status(self, status):
        self.status = status

    # Returns the friends of this UserProfile
    def get_friends(self):
        pass

    # Adds friend UserProfiles to this UserProfile's friends list
    def add_friend(self, friend_profile):
        pass

    # Removes friend from UserProfile friends list
    def remove_friend(self, friend_profile):
        pass

    # Prints out the details of the UserProfile
    def print_details(self):
        pass

    