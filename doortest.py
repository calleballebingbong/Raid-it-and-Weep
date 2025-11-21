import random
from random import randint
class Door:
    def __init__(self, rooms):
        self.rooms = rooms

    def random_room(self):
        return random.choice(self.rooms)
    
    def enter(self, room):
        if room == "trap":
            return "You have entered a trap room! Watch out!"
        elif room == "fight":
            return "You have entered a fight room! Prepare for battle!"
        elif room == "storage room":
            return "You have entered a storage room! You found some items!"
    
room_list = ["trap", "fight", "storage room"]
door = Door(room_list)

print("Welcome to the door test!")
chosen = door.random_room()

print(door.enter(chosen))
    
    
    
    