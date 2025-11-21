from random import randint

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

if __name__ == "__main__":
    trap = Trap()
    dmg = trap.activate()
    print(trap.description())

