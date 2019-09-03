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
        self.strength = attack_strength

    def attack(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''
        # TODO: Use random.randint(a, b) to select a random attack value.
        # Return an attack value between 0 and the full attack.
        # Hint: The constructor initializes the maximum attack value.
        strength = random.randint(0, self.strength)
        return strength


class Armor:
    def __init__(self, name, max_block):
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        self.name = name
        self.block = max_block

        # TODO: Create instance variables for the values passed in.
    def block(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''
        # TODO: Use random.randint(a, b) to select a random attack value.
        # Return an attack value between 0 and the full attack.
        # Hint: The constructor initializes the maximum attack value.
        blocks = random.randint(0, self.block)
        return blocks


class Weapon(Ability):
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        # TODO: Use what you learned to complete this method.
        strength = random.randint(self.strength//2, self.strength)
        return strength


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
        self.deaths = 0
        self.kills = 0
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

    def stats(self):
        '''Print team statistics'''
        # TODO: This method should print the ratio of kills/deaths for each
        # member of the team to the screen.
        # This data must be output to the console.
        # Hint: Use the information stored in each hero.
        pass
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
            print('{} died'.format(self.name))
            return False

    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''

        #TODO: Refactor this method to update the
        # number of kills the hero has when the opponent dies.
        # Also update the number of deaths for whoever dies in the fight
        print(f'{self.name} will be fighting {opponent.name}')
        while(self.is_alive() == True and opponent.is_alive() == True):
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())
            if opponent.is_alive() == False:
                print(f'{self.name} won!')
                self.kills +=1
                opponent.deaths +=1
            elif self.is_alive() == False:
                print(f'{opponent.name} won!')
                opponent.kills +=1
                self.deaths +=1
            elif len(self.abilities) == 0 and len(opponent.abilities) == 0:
                print(f"It's a tie")

    def add_kill(self, num_kills):
        ''' Update kills with num_kills'''
        # TODO: This method should add the number of kills to self.kills
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        ''' Update deaths with num_deaths'''
        # TODO: This method should add the number of deaths to self.deaths
        self.deaths += num_deaths



class Team:
    def __init__(self, name):
        ''' Initialize your team with its team name
        '''
        # TODO: Implement this constructor by assigning the name and heroes, which should be an empty list
        self.name=name
        self.heroes=[]

    def remove_hero(self, name):
        '''Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        # TODO: Implement this method to remove the hero from the list given their name.
        for hero in self.heroes:
            if name == hero.name:
                self.heroes.remove(hero)
                return 1
        return 0

    def view_all_heroes(self):
            '''Prints out all heroes to the console.'''
            # TODO: Loop over the list of heroes and print their names to the terminal.
            for hero in self.heroes:
                print(hero.name)
    def add_hero(self, hero):
            '''Add Hero object to self.heroes.'''
            # TODO: Add the Hero object that is passed in to the list of heroes in
            # self.heroes
            self.heroes.append(hero)

    def attack(self, other_team):
        ''' Battle each team against each other.'''

        # TODO: Randomly select a living hero from each team and have
        # them fight until one or both teams have no surviving heroes.
        # Hint: Use the fight method in the Hero class.

        while len(self.alive_heroes()) > 0 and len(other_team.alive_heroes()) > 0:
            hero_1 = random.choice(self.alive_heroes())
            hero_2 = random.choice(other_team.alive_heroes())
            ##make the randomly selected alive heroes fight
            hero_1.fight(hero_2)

    def alive_heroes(self):
        """Makes a list of alive heroes from team """
        alive_heroes = []
        for hero in self.heroes:
            if hero.is_alive():
                alive_heroes.append(hero)
            return alive_heroes

    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        # TODO: This method should reset all heroes health to their
        # original starting value.
        for hero in self.heroes:
            hero.current_health=100

    def stats(self):
        '''Print team statistics'''
        # TODO: This method should print the ratio of kills/deaths for each
        # member of the team to the screen.
        # This data must be output to the console.
        # Hint: Use the information stored in each hero.
        for hero in self.heroes:
            print(hero.kills // hero.health)
            
# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block is executed.

#     hero1 = Hero("Wonder Woman")
#     hero2 = Hero("Dumbledore")
#     ability1 = Ability("Super Speed", 300)
#     ability2 = Ability("Super Eyes", 130)
#     ability3 = Ability("Wizard Wand", 80)
#     ability4 = Ability("Wizard Beard", 20)
#     hero1.add_ability(ability1)
#     hero1.add_ability(ability2)
#     hero2.add_ability(ability3)
#     hero2.add_ability(ability4)
#     hero1.fight(hero2)
