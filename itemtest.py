from random import randint
import random
items = ["Knife","Bandage","Crowbar","Medkit", "Katana"]
inventory = []

def display_inventory():
    if inventory:
        print("Inventory:")
        for item in inventory:
            print(f"- {item}")
    else:
        print("Your inventory is empty.")
    
def add_to_inventory(item):
    inventory.append(item)

def lootbox():
    if random.randint(1, 4) <= 3:
        item = random.choices(items, weights=[0.3, 0.3, 0.2, 0.1, 0.1], k=1)[0]
        if item == "Medkit":
            item = f"Medkit"
            
        elif item == "Bandage":
            item = f"Bandage"
            
        elif item == "Crowbar":
            damage = randint(6,10)
            item = f"Crowbar, adds {damage} damage"

        elif item == "Knife":
            damage = randint(3,5)
            item = f"Knife, adds {damage} damage"  

        elif item == "Katana":
            damage = randint(11,15)
            item = f"Katana, adds {damage} damage"  

        return item, f"You found a {item}! It's added to your inventory."
    
    else:
        return None, "You found nothing."

while True:
    choice = input("Do you want to open a lootbox? (yes/no): ").strip().lower()
    if choice == 'yes':
        item, message = lootbox()
        print(message)
        if item:
            add_to_inventory(item)
            continue
        choice2 = input("Do you want to view your inventory? (yes/no): ").strip().lower()
        if choice2 == 'yes':
            display_inventory()
        else:
            continue
    if choice == 'no':
        print("Exiting the lootbox system.")
        break

