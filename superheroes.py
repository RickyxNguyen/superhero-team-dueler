import random
import system


class Ability:
    def __init__(self, name, attack_strength):
        '''Create Instance Variables:
            name:String
            max_damage: Integer
         '''
        self.name = name
        self.strength = attack_strength

    def attack(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''
        strength = random.randint(0, self.strength)
        return strength



class Armor:
    def __init__(self, name, defense):
        '''Instantiate instance properties.
            name: String
            block: Integer
        '''
        self.name = name
        self.block = defense

    def defense(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''

        defend = random.randint(0, self.block)
        return defend


class Weapon(Ability):
    def attack(self):
        '''  This method returns a random value
        between one half to the full attack power of the weapon.
        '''
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
        self.status="alive"
        # TODO: Initialize instance variables values as instance variables
        # (Some of these values are passed in above,
        # others will need to be set at a starting value)
        # abilities and armors are lists that will contain objects that we can use

    def add_ability(self, ability):
        ''' Adds ability to abilities list '''
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        ''' Adds weapon to abilities list '''
        self.abilities.append(weapon)

    def add_armor(self, armor):
        '''Add armor to self.armors
            Armor: Armor Object
        '''
        self.armors.append(armor)

    def attack(self):
        '''Calculate the total damage from all ability attacks.
            return: total:Int
        '''
        total_damage = 0
        for i in self.abilities:
            total_damage += i.attack()
        return total_damage

    def hero_stats(self):
        '''Print team statistics'''

        if self.deaths > 0:
            kd_ratio = self.kills/self.deaths
        else:
            kd_ratio = self.kills
        print("{} K/D Ratio: {}".format(self.name, kd_ratio))

    def defend(self):
        '''Runs `block` method on each armor.
            Returns sum of all blocks
        '''
        # TODO: This method should run the block method on each armor in self.armors
        total_defense = 0
        for hero in self.armors:
            total_defense += hero.block()
        return total_defense

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''

        self.current_health -= (damage - self.defend())

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.
        '''
        if self.current_health > 0:
            return True
        else:
            print('{} is dead'.format(self.name))
            return False

    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''

        fighting = True
        while fighting == True:
            if self.abilities == None:
                return "Draw"
                fighting = False
            
            hero_attack = self.attack()
            opponent_attack = opponent.attack()

            hero1_defense = self.defend()
            hero2_defense = opponent.defend()

            self.take_damage(opponent_attack)
            opponent.take_damage(opponent_attack)

            if self.is_alive() == False:
                opponent.add_kill(1)
                self.add_deaths(1)
                self.status = "dead"
                opponent.status = "alive"
                print("{} won!".format(opponent.name))
                fighting = False
            elif opponent.is_alive() == False:
                self.add_kill(1)
                opponent.add_deaths(1)
                opponent.status = "dead"
                self.status = "alive"
                print("{} won!".format(self.name))
                fighting = False
            else:
                continue

    def add_kill(self, num_kills):
        ''' Update kills with num_kills'''
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        ''' Update deaths with num_deaths'''
        self.deaths += num_deaths


class Team:
    def __init__(self, name):
        ''' Initialize your team with its team name
        '''
        # TODO: Implement this constructor by assigning the name and heroes, which should be an empty list
        self.name = name
        self.heroes = []

    def remove_hero(self, name):
        '''Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
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

    def attack(self, opponents):
        ''' Sets up each time to check if they are alive and if they are it will set them up to fight.'''

        alive_heroes = []
        alive_opponents = []

        for i in self.heroes:
                if i.status == "alive":
                    alive_heroes.append(self.heroes.index(i))
        
        for x in opponents.heroes:
                if x.status == "alive":
                    alive_opponents.append(opponents.heroes.index(x))

        while len(alive_heroes) > 0 and len(alive_opponents) > 0:
            random_hero_1 = self.heroes[random.choice(alive_heroes)]
            random_hero_2 = opponents.heroes[random.choice(alive_opponents)]

            random_hero_1.fight(random_hero_2)

            for death1 in self.heroes:
                if death1.status == "dead":
                    alive_heroes.pop(self.heroes.index(death1))
            
            for death2 in opponents.heroes:
                if death2.status == "dead":
                    alive_opponents.pop(opponents.heroes.index(death2))
        
        if len(alive_heroes) > 0:
            return self.name
        elif len(alive_opponents) > 0:
            return opponents.name
        elif len(alive_heroes) == len(alive_opponents):
            return "Draw!"

    def update_kills(self, kills):
        """Updates a heroes kill count for kills made in team battles """
        for hero in self.heroes:
            hero.add_kill(kills)

    def alive_heroes(self):
        '''Makes a list of alive heroes from team '''
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
            hero.current_health = 100
            hero.status = "Alive"

    def find_hero(self, name):
        """Find index of specific hero on a team """
        hero_index = -1
        for x, hero in enumerate(self.heroes):
            if hero.name == name:
                hero_index = x
        return hero_index

    def stats(self):
        '''Print team statistics'''

        for hero in self.heroes:
            print("------------------------------------")
            print("Hero: {} | Kills: {} : | Deaths: {}".format(hero.name, hero.kills, hero.deaths))

class Arena:
    def __init__(self):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''

        self.team_one = None
        self.team_two = None
        self.winning_team = None
        self.team_amt = 0


    """Creates ability"""
    def create_ability(self):
        name = input("Enter Ability Name: ")
        strength = int(input("Enter Ability Attack Strength: "))
        ability = Ability(name, strength)
        return ability
    
    """Creates weapon"""
    def create_weapon(self):
        name = input("Enter Weapon Name: ")
        strength = int(input("Enter Weapon Attack Strength: "))
        weapon = Weapon(name, strength)
        return weapon
    """Creates armor"""
    def create_armor(self):
        name = input("Enter Armor Name: ")
        block_power = int(input("Enter Blocking Strength: "))
        armor = Armor(name, block_power)
        return armor
    
    def create_hero(self):
        name = input("Enter Hero Name: ")
        amt = int(input("Enter Hero HP: "))
        hero = Hero(name,amt)

        ability_creation = True
        while ability_creation:
            ability_option = input("Create ability? (Y/N): ").lower()
            if ability_option.isalpha():
                if ability_option == "y":
                    ability = self.create_ability()
                    hero.add_ability(ability)
                elif ability_option == "n":
                    ability_creation = False
                else:
                    print("Not one of the two choices")
                    continue
            else:
                print('Not a letter')
                continue
        
        weapon_creation = True
        while weapon_creation:
            weapon_option = input("Create weapon? (Y/N): ").lower()
            if weapon_option.isalpha():
                if weapon_option == "y":
                    weapon = self.create_weapon()
                    hero.add_weapon(weapon)
                elif weapon_option == "n":
                    weapon_creation = False
                else:
                    print("Not one of the two choices")
                    continue
            else:
                print('Not a letter')
                continue
        
        armor_creation = True
        while armor_creation:
            armor_option = input("Create armor? (Y/N): ").lower()
            if armor_option.isalpha():
                if armor_option == "y":
                    armor = self.create_armor()
                    hero.add_armor(armor)
                elif armor_option == "n":
                    armor_creation = False
                else:
                    print("Not one of the two choices")
                    continue
            else:
                print('Not a letter')
                continue
        
        return hero

    """Functions will loop until user says no to having more heroes"""
    def build_team_one(self):
        self.team_amt = int(input("How many heroes for both teams?: "))
        name = input("Team 1 Name: ")
        self.team_one = Team(name)

        for i in range(self.team_amt):
            hero = self.create_hero()
            self.team_one.add_hero(hero)
        
        self.team_one.view_all_heroes()

    """Functions will loop until user says no to having more heroes"""
    def build_team_two(self):
        name = input("Team 2 Name: ")
        self.team_two = Team(name)

        for i in range(self.team_amt):
            hero = self.create_hero()
            self.team_two.add_hero(hero)
        
        self.team_two.view_all_heroes()
            
    def team_battle(self):
        self.winning_team = self.team_one.attack(self.team_two)
    
    def show_stats(self):
        print("The winners are: " + self.winning_team)
        
        self.team_one.stats()
        self.team_two.stats()

        if self.winning_team == self.team_one.name:
            for hero in self.team_one.heroes:
                if hero.status == "Alive":
                    print("Surviving Heroes: " + hero.name)
        elif self.winning_team == self.team_two.name:
            for hero in self.team_two.heroes:
                if hero.status == "Alive":
                    print("Surviving Heroes: " + hero.name)


if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    # Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        # Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            # Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
