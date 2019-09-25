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

        return random.randint(0, self.strength)

    def update_attack(self, new_dmg):
        '''Allows user to update attack damage of ability '''
        self.strength = new_dmg


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

        return random.randint(0, self.block)


class Weapon(Ability):
    def attack(self):
        '''  This method returns a random value
        between one half to the full attack power of the weapon.
        '''
        return random.randint(self.strength//2, self.strength)


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

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        ''' Add ability to abilities list '''
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
        total_defense = 0
        for hero in self.armors:
            total_defense += hero.block()
        return total_defense

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''

        self.current_health -= damage

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

        print('{} will be fighting {}'.format(self.name, opponent.name))
        while(self.is_alive() == True and opponent.is_alive() == True):
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())
            if opponent.is_alive() == False:
                self.kills += 1

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

        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        '''Add Hero object to self.heroes.'''
        self.heroes.append(hero)

    def attack(self, other_team):
        ''' Battle each team against each other.'''
        while len(self.alive_heroes()) > 0 and len(other_team.alive_heroes()) > 0:
            hero_1 = random.choice(self.alive_heroes())
            hero_2 = random.choice(other_team.alive_heroes())
            '''make the randomly selected alive heroes fight'''
            hero_1.fight(hero_2)

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

        for hero in self.heroes:
            hero.current_health = 100

    def find_hero(self, name):
        """Find index of specific hero on a team """
        hero_index = -1
        for x, hero in enumerate(self.heroes):
            if hero.name == name:
                hero_index = x
        return hero_index

    def stats(self):
        '''Loops through heroes and prints each heroes' stats'''

        for i in self.heroes:
            i.hero_stats()


class Arena:
    def __init__(self):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''
        self.team_one = None
        self.team_two = None

    '''Loops until user creates two teams and prompts 
    for ability, weapon, and/or armor for each hero'''


    def build_team_one(self):
        '''Prompt the user to build team_one'''
        team_name = input("What will be the name of Team One? ")
        team = Team(team_name)
        print("Lets start adding heroes to {}!".format(team_name))

        building_team = True
        while building_team:

            hero_name = input("Hero's name: ")
            new_hero = Hero(hero_name)
            print("What abilities/weapons do you want {} to have?".format(new_hero.name))
            #while loop to enter in as many abilities as wanted
            building_abilities = True
            while building_abilities:
                ability_name = input("Name of ability: ")
                ability_attack_strength = input("What attack strength should {} have? ".format(ability_name))
                new_ability = Ability(ability_name, ability_attack_strength)
                new_hero.add_ability(new_ability)
                abilities_finished = input("Add more abilities for {}? Enter (Y/N): ".format(new_hero.name))
                if abilities_finished == "y" or "Y" or "Yes":
                    building_abilities = False
                else:
                    continue
            print("Now let's give {} some armor".format(new_hero.name))

            building_armor = True
            while building_armor:
                armor_name = input("Name of armor: ")
                armor_defense = input("Defense score: ")
                new_armor = Armor(armor_name, armor_defense)
                new_hero.add_armor(new_armor)
                building_armor_finished = input("Add more armor for {}? Enter (Y/N): ".format(new_hero.name))
                if building_armor_finished == "n" or "N" or "No":
                    building_armor = False
                else:
                    team.add_hero(new_hero)


            building_team_finished = input("Are you done building {}? Enter (Y/N): ".format(team.name))
            if building_team_finished == "y" or "Y" or "Yes":
                building_team = False

        return team

    def build_team_two(self):
        '''Prompt the user to build team_two'''
        team_name = input("What will be the name of Team Two? ")
        team = Team(team_name)
        print("Lets start adding heroes to {}!".format(team_name))

        building_team = True
        while building_team:

            hero_name = input("Hero's name: ")
            new_hero = Hero(hero_name)
            print("What abilities/weapons do you want {} to have? ".format(new_hero.name))
            #while loop to enter in as many abilities as wanted
            building_abilities = True
            while building_abilities:
                ability_name = input("Name of ability: ")
                ability_attack_strength = int(input("What attack strength should {} have? ".format(ability_name)))
                new_ability = Ability(ability_name, ability_attack_strength)
                new_hero.add_ability(new_ability)
                abilities_finished = input("Add more abilities for {}? Enter (Y/N): ".format(new_hero.name))
                if abilities_finished == "y" or "Y" or "Yes":
                    building_abilities = False
                else:
                    continue
            print("Now let's give {} some armor".format(new_hero.name))

            building_armor = True
            while building_armor:
                armor_name = input("Name of armor: ")
                armor_defense = int(input("Defense score: "))
                new_armor = Armor(armor_name, armor_defense)
                new_hero.add_armor(new_armor)
                building_armor_finished = input("Add more armor for {}? Enter (Y/N): ".format(new_hero.name))
                if building_armor_finished == "y" or "Y" or "Yes":
                    building_armor = False
                else:
                    team.add_hero(new_hero)


            building_team_finished = input("Are you done building {}? Enter (Y/N): ".format(team.name))
            if building_team_finished == "y" or "Y" or "Yes":
                building_team = False

        return team

    def team_battle(self):
        '''Battle team_one and team_two together.'''

        battling = True
        while battling == True:
            self.team_one.attack(self.team_two)
            self.team_two.attack(self.team_one)

            winning_team = ""


            if self.is_team_dead(self.team_one) == True:
                winning_team = self.team_two.name
                print("Congrats to {} for killing all of their opponents!".format(winning_team))
                batting = False
                self.show_stats()
                break
            elif self.is_team_dead(self.team_two) == True:
                winning_team = self.team_one.name
                print("Congrats to {} for killing all of their opponents!".format(winning_team))
                battling = False
                self.show_stats()
                break
            else:
                continue



    def show_stats(self):
        '''Prints team statistics to terminal.'''

        self.team_one.stats()
        self.team_two.stats()


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
