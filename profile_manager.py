from linked_adts import LinkedDictionary, LinkedQueue
from graph_adt import Vertex, UndirectedGraph
from user_profile import UserProfile


# ProfileManager class
class ProfileManager:
    # ProfileManager constructor
    def __init__(self):
        self.user_graph = UndirectedGraph()
        self.user_profiles = LinkedDictionary()
        self.currentUser = None

    # Adds a profile to the ProfileManager
    def add_profile(
        self,
        name,
        location,
        relationship_status,
        age,
        occupation,
        astrological_sign,
        status,
    ):
        user = UserProfile(
            name,
            location,
            relationship_status,
            age,
            occupation,
            astrological_sign,
            status,
        )
        self.user_profiles.add(user.get_name, user)
        self.user_graph.add_vertex(user.get_name)
        self.currentUser = user

    # Returns the profile based on it's name
    def get_profile(self, name):
        return self.user_profiles.get_value(name)

    # Removes the profile from the ProfileManager
    def remove_profile(self, name):
        self.user_profiles.remove(name)
        # Add removal of UserProfile with the name from the graph

    # Connecting two profiles as friends with weight
    def connect_profiles(self, name1, name2, weight=0):
        if self.user_graph.contains(name1) & self.user_graph.contains(name2):
            self.user_graph.add_edge(name1, name2, weight)
            self.get_profile(name1).add_friend(self.get_profile(name2))
            self.get_profile(name2).add_friend(self.get_profile(name1))

    # Displays all the profiles in the network
    def display_profiles(self):
        print("Select which type of search below.")
        print("1. Breadth-First Search Order \n2. Depth-First Search Order")
        option = input("Enter a option number: ")
        if option == "1":
            list_all = self.user_graph.bfs(self.user_profiles.get_keys[0])
        elif option == "2":
            list_all = self.user_graph.dfs(self.user_profiles.get_keys[0])
        else:
            print("Invalid option!")
            return

        result = ""
        if not list_all.is_empty():
            while not list_all.is_empty():
                result += list_all.dequeue() + " "
        print(result)

    # Display profile details
    def display_profile_details(self, name):
        print(self.user_profiles.get_value(name).print_details())

    # Get the friends of friends list
    def get_friends_of_friends(self, name):
        pass

    # Reads profiles from a csv and builds out the profile manager
    def read_profiles_from_csv(self, file_path):
        pass

    # Creates a user graph image
    def create_user_graph(self, current_user, depth=1):
        pass

    def menu1(self):
        print("Create a profile")
        name = input("Enter your name: ")
        location = input("Enter your location: ")
        relationship_status = input("Enter your relationship status: ")
        age = input("Enter your age: ")
        occupation = input("Enter your occupation: ")
        astrological_sign = input("Enter your astrological_sign: ")
        status = input("Enter a status: ")
        print("Thank you! Your profile has been created")
        self.add_profile(
            name,
            location,
            relationship_status,
            age,
            occupation,
            astrological_sign,
            status,
        )

    def menu2(self):
        self.currentUser.print_details()
        print("What would you like to change?")
        print(
            "1. Name \n2. Location\n3. Relationship Status\n4. Age\n5. Occupation\n6. Astrological Sign\n7. Status"
        )
        option = input("Enter a menu option: ")
        if option == "1":
            edit = input("Enter a new name: ")
            self.currentUser.set_name(edit)
        elif option == "2":
            edit = input("Enter a new location: ")
            self.currentUser.set_location(edit)
        elif option == "3":
            edit = input("Enter a new relationship status: ")
            self.currentUser.set_relationship_status(edit)
        elif option == "4":
            edit = input("Enter a new age: ")
            self.currentUser.set_age(edit)
        elif option == "5":
            edit = input("Enter a new occupation: ")
            self.currentUser.set_occupation(edit)
        elif option == "6":
            edit = input("Enter a new astrological sign: ")
            self.currentUser.set_astrological_sign(edit)
        elif option == "7":
            edit = input("Enter a new status: ")
            self.currentUser.set_status(edit)
        else:
            print("Invalid option!")
            return self.menu2()

    def menu(self):
        if self.currentUser is None:
            print("Welcome to Social Media *insert name*!")
            print("Please create a profile to access menu.")
            self.menu1()
            return self.menu()
        else:
            print("\nMenu:")
            print(
                "1. Create a profile \n2. Modify profile\n3. View all profiles\n4. Add a friend\n5. View your friend list\n6. View your friend's friend list\n7. Delete a profile\n8. Switch the current user\n9. Read profiles from CSV\n10. Create graph of current user's network\n11. Logout (end program)"
            )
            print("-" * 45)  # Add a horizontal line
            option = input("Enter a menu option: ")
            print()  # Add an extra blank line for spacing
            if option == "1":
                self.menu1()
                return self.menu()
            elif option == "2":
                self.menu2()
                return self.menu()
            elif option == "3":
                self.display_profiles()
                return self.menu()
            elif option == "4":
                friend = input("Enter name of a new friend: ")
                if self.user_graph.contains(friend):
                    self.connect_profiles(self.currentUser.get_name, friend, weight=0)
                else:
                    print("Invalid friend name.")
                return self.menu()
            elif option == "5":
                friends = self.currentUser.get_friends()
                print(f"Friends: \n{[friend.print_details() for friend in 1 ]}")
                return self.menu()
            elif option == "6":
                return self.menu()
            elif option == "7":
                return self.menu()
            elif option == "11":
                print("Goodbye!")
                return
            else:
                print("Invalid option!")
                return self.menu()


pm = ProfileManager()
pm.menu()
