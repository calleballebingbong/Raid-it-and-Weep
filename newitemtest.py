from random import randint
import random
import re

items = ["Flashbang","Knife","Bandage","Crowbar","Medkit","Katana"]
inventory_system = []
hp = 75
damage = 5

class inventory:
    def __init__(self, item, display, index, damage=0, hp_restore=0, hp=100):
        self.item = item
        self.display = display
        self.index = index
        self.damage = damage
        self.hp_restore = hp_restore
        self.hp = hp

    def show_inventory(self):  # add self parameter
        if inventory_system:
            print("Inventory:")
            for i, item in enumerate(inventory_system, 1):
                print(f"{i}) {item}")
        else:
            print("Your inventory is empty.")
    
    def add_to_inventory(self, item, damage=0, hp_restore=0):
        if item in ["Knife", "Crowbar", "Katana"]:
            formatted = f"{item}, adds {damage} str"
        elif item in ["Medkit", "Bandage"]:
            formatted = f"{item}, restores {hp_restore} hp"
        elif item == "Flashbang":
            formatted = f"{item}, causes {damage} damage"
        else:
            formatted = str(item)
        inventory_system.append(formatted)
    
    def discard_from_inventory(self, index):
        if index >= 0 and index < len(inventory_system):
            removed_item = inventory_system.pop(index)
            removed_item = removed_item.split(",")[0]
            print(f"Removed {removed_item} from inventory.")

    def use_item(self, index, Player):  # pass Player object instead
        if index >= 0 and index < len(inventory_system):
            item = inventory_system[index]
            item_name = item.split(",")[0]
            m = re.search(r"(\d+)", item)
            value = int(m.group(1)) if m else 0
            
            if item_name == "Medkit":
                Player.hp = min(100, Player.hp + value)
                print(f"Used {item_name}. {value} HP restored. Current HP: {Player.hp}")
            elif item_name == "Bandage":
                Player.hp = min(100, Player.hp + value)
                print(f"Used {item_name}. {value} HP restored. Current HP: {Player.hp}")
            elif item_name in ["Knife", "Crowbar", "Katana"]:
                multiplier_increase = value * 0.1
                Player.damage_multiplier += multiplier_increase
                print(f"Used {item_name}. Damage multiplier increased by {multiplier_increase}. New multiplier: {Player.damage_multiplier}x")
            elif item_name == "Flashbang":
                Player.hp = max(0, Player.hp - value)
                print(f"Used {item_name}. You took {value} damage from the blast. Current HP: {Player.hp}")
            else:
                print("Cannot use this item.")
                return
            
            inventory_system.pop(index)
        else:
            print("Invalid inventory index.")

class Player:
    def __init__(self, hp=100, damage_multiplier=1.0):
        self.hp = hp
        self.damage_multiplier = damage_multiplier

    def take_damage(self, dmg):
        self.hp -= dmg
        return self.hp

def lootbox():
    damage = 0
    hp_restore = 0
    if random.randint(1, 10) <= 9:
        item = random.choices(items, weights=[0.25, 0.25, 0.25, 0.1, 0.1, 0.05], k=1)[0]
        if item == "Medkit":
            hp_restore = randint(15,25)
        elif item == "Bandage":
            hp_restore = randint(5,10)
        elif item == "Crowbar":
            damage = randint(6,10)
        elif item == "Knife":
            damage = randint(3,5)
        elif item == "Katana":
            damage = randint(11,15)
        elif item == "Flashbang":
            damage = randint(1,10)
    else:
        item = None
        
    if item in ["Knife", "Crowbar", "Katana"]:
        return item, f"You found a {item}! (+{damage} str)", damage, 0
    elif item in ["Medkit", "Bandage"]:
        return item, f"You found a {item}!(+{hp_restore} hp)", 0, hp_restore
    elif item == "Flashbang":
        return item, f"You found a {item}!(Causes {damage} damage)", damage, 0
    else:
        return item, "You found nothing.", 0, 0

# Example usage:
Player = Player()
inv = inventory("", "", 0)

item, description, damage, hp_restore = lootbox()
print(description)
inv.add_to_inventory(item, damage, hp_restore)

while True:
    view_inv = input("Do you want to view your inventory? (y/n): ")
    if view_inv.lower() == 'y':
        inv.show_inventory()  # pass self automatically
        use_item = input("Do you want to use an item? (y/n): ")
        if use_item.lower() == 'y':
            index = int(input("Enter the index of the item to use (1-4): ")) - 1
            inv.use_item(index, Player)  # pass Player object
            print(f"Current HP: {Player.hp}, Damage Multiplier: {Player.damage_multiplier}x")
    elif view_inv.lower() == 'n':
        break
    else:
        print("Invalid input.")
