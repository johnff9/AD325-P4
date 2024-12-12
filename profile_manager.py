import csv
from linked_adts import LinkedDictionary, LinkedQueue
from graph_adt import Vertex, UndirectedGraph
from user_profile import UserProfile
from graphviz import Graph


# ProfileManager class
class ProfileManager:
    def __init__(self):
        self.profiles = LinkedDictionary()
        self.graph = UndirectedGraph()
        self.current_user = None

    def add_profile(self, name, location, relationship_status, age, occupation, astrological_sign, status=""):
        # Input validation
        if not name or not location or not relationship_status or not age or not occupation or not astrological_sign or not status:
            print("\nAll fields are required to create a profile.\n")
            return

        try:
            age = int(age)  # Validate age input
        except ValueError:
            print("\nInvalid age. Please enter a valid integer.\n")
            return

        if name.isdigit():  # Check if the name is a number
            print("\nInvalid name. The name cannot be a number.\n")
            return

        if name in self.profiles.get_keys():
            print(f"\nProfile with name '{name}' already exists.\n")
            return

        new_profile = UserProfile(
            name,
            location,
            relationship_status,
            age,
            occupation,
            astrological_sign,
            status,
        )
        self.profiles.add(name, new_profile)
        self.graph.add_vertex(name)  # Add the profile to the graph as a vertex
        self.current_user = new_profile  # Set the current user to the newly created profile
        print("\nProfile created successfully!")
        
    def get_profile(self, name):
        return self.profiles.get_value(name)

    def remove_profile(self, name):
        if name in self.profiles.get_keys():
            # Remove the profile from the profiles dictionary
            if not self.profiles.remove(name):
                print(f"Error removing profile '{name}' from dictionary.")
                return

            # Remove the vertex from the graph
            self.graph.remove_vertex(name)
            print(f"Profile '{name}' removed successfully.")
        else:
            print(f"Profile '{name}' does not exist.")

    def connect_profiles(self, name1, name2, weight=0):
        # Input validation
        if name1 not in self.profiles.get_keys() or name2 not in self.profiles.get_keys():
            print(f"One or both profiles ('{name1}', '{name2}') do not exist.")
            return

        self.graph.add_edge(name1, name2, weight)
        self.profiles.get_value(name1).add_friend(self.profiles.get_value(name2))
        self.profiles.get_value(name2).add_friend(self.profiles.get_value(name1))
        print(f"Connected '{name1}' and '{name2}' as friends.")

    def display_profiles(self):
        print("Select which type of search below.")
        print("1. Breadth-First Search Order \n2. Depth-First Search Order")
        option = input("Enter an option number: ")

        if option == "1":
            list_all_bfs = self.graph.bfs(self.current_user.get_name())
            all_profiles = list(self.profiles.get_keys())
            print("Profiles in Breadth-First Search Order:")
            print(", ".join(all_profiles))
        elif option == "2":
            list_all_dfs = self.graph.dfs(self.current_user.get_name())
            all_profiles = list(self.profiles.get_keys())
            print("Profiles in Depth-First Search Order:")
            print(", ".join(all_profiles))
        else:
            print("Invalid option!")

    def display_profile_details(self, name):
        profile = self.get_profile(name)
        if profile:
            profile.print_details()

    def get_friends_of_friends(self, name):
        profile = self.get_profile(name)
        if profile:
            friends = profile.get_friends()
            fof = set()
            for friend in friends:
                fof.update(self.get_profile(friend).get_friends())
            fof -= set(friends)
            fof.discard(name)
            return fof

    def read_profiles_from_csv(self, file_path):
        try:
            with open(file_path, mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.add_profile(
                        row["name"],
                        row["location"],
                        row["relationship_status"],
                        int(row["age"]),
                        row["occupation"],
                        row["astrological_sign"],
                        row["status"],
                    )
                    friends = row["friends"].split(",")
                    for friend in friends:
                        if friend.strip():
                            self.connect_profiles(row["name"], friend.strip())
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
        except Exception as e:
            print(f"Error reading CSV file: {e}")

    def create_user_graph(self, current_user, depth=1):
        g = Graph("User Network")

        def traverse(user, d):
            if d > depth:
                return
            for friend in self.get_profile(user).get_friends():
                g.edge(user, friend)
                traverse(friend, d + 1)

        self.current_user = current_user
        traverse(current_user, 0)
        g.render("user_network", format="png", cleanup=True)

    def menu1(self):
        print("Create a profile")
        name = input("Enter your name: ")
        location = input("Enter your location: ")
        relationship_status = input("Enter your relationship status: ")
        age = input("Enter your age: ")
        occupation = input("Enter your occupation: ")
        astrological_sign = input("Enter your astrological_sign: ")
        status = input("Enter a status: ")
        self.add_profile(
            name,
            location,
            relationship_status,
            age,
            occupation,
            astrological_sign,
            status,
        )
        self.current_user = self.profiles.get_value(name)

    def menu2(self):
        self.current_user.print_details()
        print("What would you like to change?")
        print(
            "1. Name \n2. Location\n3. Relationship Status\n4. Age\n5. Occupation\n6. Astrological Sign\n7. Status"
        )
        option = input("Enter a menu option: ")
        if option == "1":
            edit = input("Enter a new name: ")
            self.current_user.set_name(edit)
        elif option == "2":
            edit = input("Enter a new location: ")
            self.current_user.set_location(edit)
        elif option == "3":
            edit = input("Enter a new relationship status: ")
            self.current_user.set_relationship_status(edit)
        elif option == "4":
            edit = input("Enter a new age: ")
            self.current_user.set_age(edit)
        elif option == "5":
            edit = input("Enter a new occupation: ")
            self.current_user.set_occupation(edit)
        elif option == "6":
            edit = input("Enter a new astrological sign: ")
            self.current_user.set_astrological_sign(edit)
        elif option == "7":
            edit = input("Enter a new status: ")
            self.current_user.set_status(edit)
        else:
            print("Invalid option!")
            return self.menu2()

    def menu(self):
        if self.current_user is None:
            print("Welcome to Social Media *insert name*!")
            print("Please create a profile to access menu.")
            self.menu1()
            return self.menu()
        else:
            print("\nMenu:")
            print(
                "1. Create a profile \n2. Modify profile\n3. View all profiles\n4. Add a friend\n5. View your friend list\n6. View your friend's friend list\n7. Delete a profile\n8. Switch the current user\n9. Read profiles from CSV\n10. Create graph of current user's network\n11. Logout (end program)"
            )
            print("-" * 45)
            print(f"Current username: {[self.current_user.get_name()]}")
            option = input("Enter a menu option: ")
            print()
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
                if self.graph.contains(friend):
                    self.connect_profiles(
                        self.current_user.get_name(), friend, weight=0
                    )
                else:
                    print("Invalid friend name.")
                return self.menu()
            elif option == "5":
                friends = self.current_user.get_friends()
                print(f"Friends: \n{[friend for friend in friends]}")
                return self.menu()
            elif option == "6":
                friends_of_friends = self.get_friends_of_friends(self.current_user.get_name())
                print(f"Friends of Friends: \n{[fof for fof in friends_of_friends]}")
                return self.menu()
            elif option == "7":
                rm = input("Enter name of profile to remove: ")
                self.remove_profile(rm)
                return self.menu()
            elif option == "8":
                nm = input("Enter a name of user you want to switch to: ")
                if self.graph.contains(nm) and nm in self.profiles.get_keys():
                    self.current_user = self.get_profile(nm)
                    print(f"Current user switched to '{nm}'.")
                else:
                    print("Invalid name. Please try again.")
                return self.menu()
            elif option == "9":
                file_path = input("Enter the file path of the CSV: ")
                self.read_profiles_from_csv(file_path)
                return self.menu()
            elif option == "10":
                self.create_user_graph(self.current_user.get_name(), depth=2)
                return self.menu()
            elif option == "11":
                print("Logged out.")
                self.current_user = None
                return self.menu()
            else:
                print("Invalid option!")
                return self.menu()

pm = ProfileManager()
pm.menu()
