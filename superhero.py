import random


class Ability:
    def __init__(self, name, attack_strength):
        '''Create Instance Variables:
            name:String
            max_damage: Integer
         '''
        # TODO: Instantiate the variables listed in the docstring with then
        # values passed in
        self.name = name
        self.max_damage = attack_strength

    def attack(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''
        # TODO: Use random.randint(a, b) to select a random attack value.
        # Return an attack value between 0 and the full attack.
        # Hint: The constructor initializes the maximum attack value.
        attacks = random.randint(0, self.max_damage)
        return attacks


class Armor:
    def __init__(self, name, max_block):
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        self.name = name
        self.max_block = max_block

        # TODO: Create instance variables for the values passed in.
    def block(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''
        # TODO: Use random.randint(a, b) to select a random attack value.
        # Return an attack value between 0 and the full attack.
        # Hint: The constructor initializes the maximum attack value.
        blocks = random.randint(0, self.max_block)
        return blocks


class Hero:
    def __init__(self, name, health=100):
        '''Instance properties:
            abilities: List
            armors: List
            name: String
            starting_health: Integer
            current_health: Integer
        '''
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = health
        self.current_health = health
        # TODO: Initialize instance variables values as instance variables
        # (Some of these values are passed in above,
        # others will need to be set at a starting value)
        # abilities and armors are lists that will contain objects that we can use

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        # TODO: Add ability object to abilities:List
        self.abilities.append(ability)

    def add_armor(self, armor):
        '''Add armor to self.armors
            Armor: Armor Object
        '''
        # TODO: Add armor object that is passed in to `self.armors`
        self.armors.append(armor)

    def attack(self):
        '''Calculate the total damage from all ability attacks.
            return: total:Int
        '''
        # TODO: This method should run Ability.attack() on every ability
        # in self.abilities and returns the total as an integer.
        total_damage = 0
        for hero in self.abilities:
            total_damage += Ability.attack(hero)
        return total_damage

    def defend(self, damage_amt):
        '''Runs `block` method on each armor.
            Returns sum of all blocks
        '''
        # TODO: This method should run the block method on each armor in self.armors
        total_defense = 0
        for hero in self.armors:
            total_defense += Ability.block(hero)
        return total_defense

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
    # TODO: Create a method that updates self.current_health to the current
    # minus the the amount returned from calling self.defend(damage).
        self.current_health -= damage
    def is_alive(self):  
        '''Return True or False depending on whether the hero is alive or not.
        '''
        # TODO: Check whether the hero is alive and return true or false
        if self.current_health > 0:
            return True
        else:
            return False
    def fight(self, opponent):  
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
    # TODO: Fight each hero until a victor emerges.
    # Print the victor's name to the screen.
        print(f'{self.name} will be fighting {opponent.name}')
        while(self.is_alive() == True and opponent.is_alive() == True):
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())
            if opponent.is_alive() == False:
                print(f'{self.name} won!')
            elif self.is_alive()==False:
                print(f'{opponent.name} wion!')
            elif len(self.abilities)==0 and len(opponent.abilities)==0:
                print(f"It's a tie")

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)