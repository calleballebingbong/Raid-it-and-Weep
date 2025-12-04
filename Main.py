import random
from random import randint
import re
import time
from rich import print
from pyfiglet import Figlet
f = Figlet(font="larry3d")

def type_text(text, delay): #typewriter effect
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

type_text(f.renderText("RAID IT AND WEEP!"), 0.001)
print("[green]You entered the room[/]")




class Player: #player class
    def __init__(self, hp=1000, strength=1, level=1, xp=0,): #player stats
        self.hp = hp
        self.strength = strength
        self.level = level
        self.xp = xp
        self.damage_multiplier = 1.0   # <-- add this
    
    def player_status(self): #om player lever/print stats
        if self.hp > 0:
            return f"HP: [green] {self.hp} [/green], Strength: [red] {self.strength} [/red], Level: [yellow] {self.level} [/yellow], DMGx: [cyan]{self.damage_multiplier:.2f}[/cyan]"
        else:
            return "You died! Game Over."
        
    def player_check(self): #om player lever
        if self.hp <= 0:
            return True
        else:
            return False
            
            
    
    def take_damage(self, damage): #om player tar skada
        self.hp -= damage
        return f"You take {damage} damage!"
    
    def gain_xp(self, amount): #om player får xp/ level up system
        self.xp += amount
        if self.xp >= self.level * 50:
            self.level += 1
            return f"You have leveled up to level {self.level}!"
        return f"Gained {amount} XP. \n Total XP: {self.xp}"


class Enemy: #enemy class
    def __init__(self, name, hp_multiplier):  #enemy stats
        self.name = name
        self.hp_multiplier = hp_multiplier
        self.hp = hp_multiplier * 20
    
    def take_damage(self, damage): #om enemy tar skada
        self.hp -= damage
        return self.hp <= 0 #return true om enemy är död
    
    def attack(self): #om enemy attackerar
        damage = self.hp_multiplier * randint(1, 5)
        return damage #return skada
    
def turn_system(): #turn system
    turn_system_choice = ""
    print("what do you want to do?")
    print("Attack [1], item [2], Run [3]")
    turn_system_choice = input("Choose an action: ")
    return turn_system_choice


class Door: #dörr class
    def __init__(self, rooms): #dörr rum
        self.rooms = rooms

    def random_room(self): #välj random rum
        return random.choice(self.rooms)
    
    def enter(self, room): #gå in i rum msg
        if room == "trap":
            return "You have entered a [bold yellow] trap [/bold yellow] room! Watch out!"
        elif room == "fight":
            return "You have entered a [bold red]fight[/bold red] room! Prepare for battle!"
        elif room == "storage room":
            return "You have entered a [bold purple] storage [/bold purple] room! You found some items!"
    
    def description(self, description): #dörr beskrivning
        return "You open a door that leads to a " + description + " room."

        
class Trap: #trap class
    def __init__(self, min_dmg=10, max_dmg=30): #trap skada (min max)
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        self.dmg = 0
    def make_damage(self, player): #hp reducering
        player.hp -= self.dmg

    def activate(self): #välj skada
        self.dmg = randint(self.min_dmg, self.max_dmg)
        return self.dmg

    def description(self): #trap beskrivning baserat på skada
        if self.dmg <= 15:
            return f"You activated a tripwire and took [bold red]{self.dmg} damage.[/bold red] It was just a scratch."
        elif self.dmg <= 25:
            return f"You activated a shrapnel trap and took [bold red]{self.dmg} damage.[/bold red] You're hurt, bandage up!"
        else:
            return f"You activated an explosive mine and took [bold red]{self.dmg} damage.[/bold red] [yellow]Critical[/yellow] hit!"
        
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
                if chosen == "fight":
                    enemy.hp = max(0, enemy.hp - value)
                    print(f"Used {item_name}. {enemy.name} took {value} damage from the blast. Current HP: {enemy.hp}")
                else:
                    print("Cannot use this item here.")
            else:
                print("Cannot use this item.")
                return
            
            inventory_system.pop(index)
        else:
            print("Invalid inventory index.") 

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
        item = None
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


# Initialize
player = Player() #create player
enemies_list = {"goblin": 1, "troll": 2, "dragon": 3} #create enemies bibliotek, ("namn": hp_multiplier)
random_enemy_name = list(enemies_list.keys())[randint(0, 2)] #välj random enemy
enemy = Enemy(random_enemy_name, enemies_list[random_enemy_name]) #create enemy object
room_list = {"trap": 1, "fight": 2, "storage room": 3}
description_list = ["dark and gloomy", "bright and shiny", "damp and musty", "cobweb filled", "vine covered", "icy cold", "sweltering hot"]
description = random.choice(description_list)
door_description = Door(description_list)
options = list(room_list.keys())
door = Door(options)
door_chance = randint(1, 4) 
rand_door_desc = 1
items = ["Flashbang","Knife","Bandage","Crowbar","Medkit","Katana"]
inventory_system = []
inv = inventory("", "", 0)

# Game loop
print(player.player_status()) 
    

while player.hp >= 0:
    door_chance = randint(1, 4) 
    print("You see three doors in front of you:")
    while rand_door_desc <= 3:
        description = random.choice(description_list)
        print(f"[bold] A door leading to a {description} room.[{rand_door_desc}] [/bold]")
        rand_door_desc += 1
    rand_door_desc = 1
    choice = input("Which door do you want to choose? (press enter for random): ")
    if choice in ("1", "2", "3"):
        if door_chance == 4:
            chosen = "storage room"
        elif door_chance == 3:
            chosen = "trap"
        else:
            chosen = "fight"
    else:
        print("Invalid choice — choosing a random door instead.")
        chosen = door.random_room()
    print(door.description(description))

    print(f"[green] {door.enter(chosen)} [/] ") #color test
    if chosen == "trap":
        trap = Trap()
        damage = trap.activate()
        trap.make_damage(player)
        print(trap.description())
        print(player.player_status())
        if player.player_check() == True:
            restart = input("Do you want to restart? (yes/no): ")
            if restart.lower() == "no":
                print("Game Over!")
                exit()
            else:
                print("You chose to restart the game!")
                player.hp = 100
                player.level = 1
                player.xp = 0
                player.strength = 1
                print(player.player_status())

    elif chosen == "fight":
        random_enemy_name = list(enemies_list.keys())[randint(0, 2)]
        enemy = Enemy(random_enemy_name, enemies_list[random_enemy_name])
        print(player.player_status()) 
        print(f"The {enemy.name} appears!")
        while player.hp >= 0:
            turn_choice = turn_system()
            if turn_choice == "3":
                print("You ran away safely!")
                break
            elif turn_choice == "2":
                inv.show_inventory()                 # use the instance
                use_choice = input("Do you want to use an item? (yes/no): ").lower()
                if use_choice == 'yes':
                    item_index = input("Enter the number of the item you want to use: ")
                    try:
                        index = int(item_index) - 1
                        if 0 <= index < len(inventory_system):
                            inv.use_item(index, player)  # pass instance 'inv' and player instance
                        else:
                            print("Index out of range.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
            elif turn_choice == "1":
                base = randint(player.strength, player.strength * 5)
                player_damage = int(base * player.damage_multiplier)  # <-- apply multiplier
                print(player.take_damage(enemy.attack()))
                print(f"You attack for {player_damage} damage!")
                if enemy.take_damage(player_damage):
                    xp_gained = enemies_list[enemy.name] * 15
                    print(f"You defeated the {enemy.name}!")
                    print(player.gain_xp(xp_gained))
                    break
                else:
                    print(f"The {enemy.name} has {enemy.hp} HP left.")
                print(player.player_status())
                if player.player_check() == True:
                    restart = input("Do you want to restart? (yes/no): ")
                    if restart.lower() == "no":
                        print("Game Over!")
                        exit()
                    else:
                        print("You chose to restart the game!")
                        player.hp = 100
                        player.level = 1
                        player.xp = 0
                        player.strength = 1
                        print(player.player_status())
                        break
                else:
                    input("Press Enter to continue...")
            else:
                print("Invalid choice, try again.")
    elif chosen == "storage room":
                item, description, damage, hp_restore = lootbox()
                print(description)
                inv.add_to_inventory(item, damage, hp_restore)

                while True:
                    print("What do you want to do?")
                    while True:
                        view_inv = input("[I]nventory or exit the room?[ENTER]:")
                        if view_inv.lower() == "i":
                            inv.show_inventory()  # pass self automatically
                            use_item = input("Use and [I]tem or go back?[ENTER]:")
                            if use_item.lower() == 'i':
                                try:
                                    index = int(input("Which item do you want to use? [1-4]:")) - 1
                                    if 0 <= index < len(inventory_system):
                                        inv.use_item(index, player)  # pass player instance
                                        print(f"Current HP: {player.hp}, Damage Multiplier: {getattr(player,'damage_multiplier',1.0)}x")
                                    
                                    else:
                                        print("Invalid input.")
                                except ValueError:
                                    print("Invalid input.")
                            else:
                                break
                        elif view_inv.lower() == '':
                            break
                        else:
                            print("Invalid input.")
                    break
