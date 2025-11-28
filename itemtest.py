from random import randint
import random
import re
items = ["Flashbang","Knife","Bandage","Crowbar","Medkit","Katana"]
inventory_system = []
hp = 75
class inventory:
    def __init__(self, item, display, index, damage=0, hp_restore=0, hp=100):
        self.item = item
        self.display = display
        self.index = index
        self.damage = damage
        self.hp_restore = hp_restore
        self.hp = hp

    def show_inventory(display):
        if inventory_system:
            print("Inventory:")
            for item in inventory_system:
                print(f"- {item}")
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

    def use_item(self, index, hp = 0, damage = 0):
        if index >= 0 and index < len(inventory_system):
            item = inventory_system[index]
            item_name = item.split(",")[0]
            m = re.search(r"(\d+)", item)
            hp_restore = int(m.group(1)) if m else 0
            damage = int(m.group(1)) if m else 0
            if item_name == "Medkit":
                hp = min(100, hp + hp_restore)
                print(f"Used {item_name}. {hp_restore} HP restored. Current HP: {hp}")
            elif item_name == "Bandage":
                hp = min(100, hp + hp_restore)
                print(f"Used {item_name}. {hp_restore} HP restored. Current HP: {hp}")
            elif item_name in ["Flashbang"]:
                hp = min(100, hp - damage)
                print(f"Used {item_name}. You took {damage} damage from the blast. Current HP: {hp}")
            else:
                print("Cannot use this item.")
                return hp
            inventory_system.pop(index)
            return hp
        else:
            print("Invalid inventory index.")
            return hp

def lootbox():
    if random.randint(1, 10) <= 9:
        item = random.choices(items, weights=[0.25, 0.25, 0.25, 0.1, 0.1, 0.05], k=1)[0]
        if item == "Medkit":
            hp_restore = randint(15,25)
            item = f"{item}"
        elif item == "Bandage":
            hp_restore = randint(5,10)
            item = f"{item}"
        elif item == "Crowbar":
            damage = randint(6,10)
            item = f"{item}"
        elif item == "Knife":
            damage = randint(3,5)
            item = f"{item}"  
        elif item == "Katana":
            damage = randint(11,15)
            item = f"{item}"  
        elif item == "Flashbang":
            damage = randint(1,10)
            item = f"{item}"
    else:
        item = "Nothing"
        damage = 0
        hp_restore = 0
    if item in ["Knife", "Crowbar", "Katana"]:
        return item, f"You found a {item}! (+{damage} str)", damage, 0
    elif item in ["Medkit", "Bandage"]:
        return item, f"You found a {item}!(+{hp_restore} hp)", 0, hp_restore
    elif item == "Flashbang":
        return item, f"You found a {item}!(Causes {damage} damage)", damage, 0
    else:
        return item, "You found nothing.", 0, 0

while True:
    choice = input("Do you want to open a lootbox? (yes/no) or see inventory?: ").lower()
    if choice == 'yes':
        item, message, damage, hp_restore = lootbox()
        print(message)
        if item and len(inventory_system) < 5:
            inventory.add_to_inventory(inventory, item, damage, hp_restore)
            while True:
                choice4 = input("Do you want to view your inventory? (yes/no): ").lower()
                if choice4 == 'yes':
                    inventory.show_inventory(inventory_system)
                    for item in inventory_system:
                        use_choice = input("Do you want to use an item? (yes/no): ").lower()
                        if use_choice == 'yes':
                            while True:
                                item_index = input("Enter the number of the item you want to use (1-5): ")
                                try:
                                    index = int(item_index) - 1
                                    if 0 <= index < len(inventory_system):
                                        hp = inventory.use_item(inventory, index, hp = hp, damage = damage)
                                        break
                                except ValueError:
                                    print("Invalid input. Please enter a number between 1 and 5.")
                                break
                        elif use_choice == 'no':
                            break
                        else:
                            print("Invalid input. Please enter 'yes' or 'no'.")
                    break
                elif choice4 == 'no':
                    break
                else: 
                    print("Invalid input. Please enter 'yes' or 'no'.")
        elif len(inventory_system) >= 5:
            print("Your inventory is full.")
            inventory.show_inventory(inventory_system)
            while True:
                choice2 = input("Do you want to discard an item to make space? (yes/no): ").lower()
                if choice2 == 'yes':
                    while True:
                        choice3 = input("Enter a number between 1 - 5 for the item you want to discard: ")
                        try:
                            index = int(choice3) - 1
                            if 0 <= index < len(inventory_system):
                                inventory.discard_from_inventory(inventory, index)
                                inventory.add_to_inventory(inventory, item, damage, hp_restore)
                                break
                        except ValueError:
                            print("Invalid input. Please enter a number between 1 and 5.")
                    break
                elif choice2 == 'no':
                    print("You chose not to discard any items.")   
                    break
                else: 
                    print("Invalid input. Please enter 'yes' or 'no'.") 
    if choice == 'no':
        print("Exiting the lootbox system.")
        break
    if choice == 'inventory':
        inventory.show_inventory(inventory_system)
        for item in inventory_system:
            use_choice = input("Do you want to use an item? (yes/no): ").lower()
            if use_choice == 'yes':
                while True:
                    item_index = input("Enter the number of the item you want to use (1-5): ")
                    try:
                        index = int(item_index) - 1
                        if 0 <= index < len(inventory_system):
                            hp = inventory.use_item(inventory, index, hp = hp, damage = damage)
                            break
                    except ValueError:                           
                        print("Invalid input. Please enter a number between 1 and 5.")
                    break
            elif use_choice == 'no':
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")