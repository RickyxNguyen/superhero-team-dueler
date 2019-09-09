import random
import system


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

        # TODO: Create instance variables for the values passed in.
    def defense(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''
        # TODO: Use random.randint(a, b) to select a random attack value.
        # Return an attack value between 0 and the full attack.
        # Hint: The constructor initializes the maximum attack value.
        defend = random.randint(0, self.block)
        return defend


class Weapon(Ability):
    def attack(self):
        '''  This method returns a random value
        between one half to the full attack power of the weapon.
        '''
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

    def add_weapon(self, weapon):
        ''' Add ability to abilities list '''
        # TODO: Add ability object to abilities:List
        self.abilities.append(weapon)

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
        for i in self.abilities:
            total_damage += i.attack()
        return total_damage

    def hero_stats(self):
        '''Print team statistics'''
        # TODO: This method should print the ratio of kills/deaths for each
        # member of the team to the screen.
        # This data must be output to the console.
        # Hint: Use the information stored in each hero.
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
            print('{} is dead'.format(self.name))
            return False

    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''

        # TODO: Refactor this method to update the
        # number of kills the hero has when the opponent dies.
        # Also update the number of deaths for whoever dies in the fight
        print('{} will be fighting {}'.format(self.name, opponent.name))
        while(self.is_alive() == True and opponent.is_alive() == True):
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())
            if opponent.is_alive() == False:
                self.kills += 1

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
        self.name = name
        self.heroes = []

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
            # make the randomly selected alive heroes fight
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
        # TODO: This method should reset all heroes health to their
        # original starting value.
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
        '''Print team statistics'''
        # TODO: This method should print the ratio of kills/deaths for each
        # member of the team to the screen.
        # This data must be output to the console.
        # Hint: Use the information stored in each hero.
        for i in self.heroes:
            i.hero_stats()


class Arena:
    def __init__(self):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''
        # TODO: create instance variables named team_one and team_two that
        # will hold our teams.
        self.team_one = None
        self.team_two = None

    def build_team(self):
        name = input('Enter a team name: ')
        new_team = Team(name)
        keep_adding_heroes = True
        while keep_adding_heroes:
            print(f'Adding a hero to {name}...')
            new_hero = Hero(input('Enter the name of the hero: '))
            new_hero.abilities = self.hero_additions('ability', new_hero.name)
            new_hero.abilities = self.hero_additions('weapon', new_hero.name)
            new_hero.armors = self.hero_additions('armor', new_hero.name)
            new_team.add_hero(new_hero)
            keep_adding_heroes = self.yes_or_no(
                f'Would you like to keep adding heroes to {name}? Answer ( y/n ): ')
        return new_team

    def yes_or_no(self, message):
        '''Method that returns false and will end a loop when user input n, will return True if user inputs y '''
        response = input(message)
        if response.lower() == 'y':
            return True
        elif response.lower() == 'n':
            return False
        else:
            print('Input not recognized')
        return self.yes_or_no(message)

    def hero_additions(self, addition_type, hero_name):
        '''Method that allows users to make additions to heros while building out the team (using Arena methods) '''
        additions = []
        if self.yes_or_no(f'Do you want to add {addition_type} to {hero_name}? ( y/n ): '):
            keep_asking = True
            addition = Ability if addition_type == 'ability' else Weapon if addition_type == 'weapon' else Armor
            while keep_asking:
                name = input(f'What is this {addition_type} called? ')
                block_or_attack = 'block' if addition_type == Armor else 'attack'
                strength = int(
                    input(f"What is {name}'s  {block_or_attack} strength? "))
                additions.append(addition(name, strength))
                keep_asking = self.yes_or_no(
                    f'Do you want to add another {addition_type}? ( y/n ): ')
            return additions

    def build_team_one(self):

        self.team_one = self.build_team()
        return self.team_one

    def build_team_two(self):
        '''Prompt the user to build team_two'''
        # TODO: This method should allow a user to create team two.
        # Prompt the user for the number of Heroes on team two
        # call self.create_hero() for every hero that the user wants to add to team two.
        #
        # Add the created hero to team two.
        self.team_two = self.build_team()
        return self.team_two

    def team_battle(self):
        '''Battle team_one and team_two together.'''
        # TODO: This method should battle the teams together.
        # Call the attack method that exists in your team objects
        # for that battle functionality.
        while self.team_one.alive_heroes() and self.team_two.alive_heroes():
            self.team_one.attack(self.team_two)
            self.team_two.attack(self.team_one)
            if self.team_one.alive_heroes():
                print(f'{self.build_team_one.name} won this battle.')
                self.team_one.update_kills(len(self.team_two.heroes))
                return False
            else:
                print(f'{self.build_team_two.name} won this battle.')
                self.team_two.update_kills(len(self.team_one.heroes))
                return False

    def show_stats(self):
        '''Prints team statistics to terminal.'''
        # TODO: This method should print out battle statistics
        # including each team's average kill/death ratio.
        # Required Stats:
        #     Declare winning team
        #     Show both teams average kill/death ratio.
        #     Show surviving heroes.
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
