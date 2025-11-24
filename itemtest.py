from random import randint
import random
items = ["Knife","Bandage","Crowbar","Medkit", "Katana"]
inventory_system = []
class inventory:
    def __init__(self, item, display, index):
        self.item = item
        self.display = display
        self.index = index

    def display(display):
        if inventory_system:
            print("Inventory:")
            for item in inventory_system:
                print(f"- {item}")
        else:
            print("Your inventory is empty.")
    
    def add_to_inventory(self, item):
        inventory_system.append(item)
    
    def discard_from_inventory(self, index):
        if 0 <= index < len(inventory_system):
            removed_item = inventory_system.pop(index)
            print(f"Removed {removed_item} from inventory.")
        else:
            print("Invalid index. No item removed.")

def lootbox():
    if random.randint(1, 4) <= 3:
        item = random.choices(items, weights=[0.3, 0.3, 0.2, 0.1, 0.1], k=1)[0]
        if item == "Medkit":
            item = f"{item}"
            
        elif item == "Bandage":
            item = f"{item}"
            
        elif item == "Crowbar":
            damage = randint(6,10)
            item = f"{item}, adds {damage} damage"

        elif item == "Knife":
            damage = randint(3,5)
            item = f"{item}, adds {damage} damage"  

        elif item == "Katana":
            damage = randint(11,15)
            item = f"{item}, adds {damage} damage"  

        return item, f"You found a {item}!"
    
    else:
        return None, "You found nothing."

while True:
    choice = input("Do you want to open a lootbox? (yes/no): ").lower()
    if choice == 'yes':
        item, message = lootbox()
        print(message)
        if item and len(inventory_system) < 5:
            inventory.add_to_inventory(inventory, item)
        elif len(inventory_system) >= 5:
            print("Your inventory is full.")
            choice2 = input("Do you want to discard an item to make space? (yes/no): ").lower()
            if choice2 == 'yes':
                choice3 = input("Enter a number between 1 - 5 for the item you want to discard: ")
                for choice3 in ['1','2','3','4','5']:
                    index = int(choice3) - 1
                    inventory.discard_from_inventory(inventory, index)
                    inventory.add_to_inventory(inventory, item)
                    break
            else:
                print("You chose not to discard any items.")    
        choice4 = input("Do you want to view your inventory? (yes/no): ").lower()
        if choice4 == 'yes':
            inventory.display(inventory_system)
    if choice == 'no':
        print("Exiting the lootbox system.")
        break
        

