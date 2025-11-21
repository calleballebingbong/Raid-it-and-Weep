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
        
class Trap:
    def __init__(self, min_dmg=10, max_dmg=30):
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        self.dmg = 0
    def make_damage(self, adventurer):
        adventurer.health -= self.dmg

    def activate(self):
        self.dmg = randint(self.min_dmg, self.max_dmg)
        return self.dmg

    def description(self):
        if self.dmg <= 15:
            return f"You activated a tripwire and took {self.dmg} damage. It was just a scratch."
        elif self.dmg <= 25:
            return f"You activated a shrapnel trap and took {self.dmg} damage. You're hurt, bandage up!"
        else:
            return f"You activated an explosive mine and took {self.dmg} damage. Critical hit!"

    
room_list = ["trap", "fight", "storage room"]
door = Door(room_list)

print("Welcome to the door test!")
chosen = door.random_room()

print(door.enter(chosen))
if chosen == "trap":
    trap = Trap()
    damage = trap.activate()
    print(trap.description())
    
    
    