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
      attacks = random.randint(0,self.max_damage)
      return attacks
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())
    pass


class Armor:
    def __init__(self, name, max_block):
            '''Instantiate instance properties.
                name: String
                max_block: Integer
            '''
            self.name = name
            self.max_block= max_block

            # TODO: Create instance variables for the values passed in.
            
            pass

# class Hero:
#     def __init__(name, starting_health:100):
#         self.name = name
#         self.breed = breed
#     def add_ability(ability:Ability):
#         print('apple')
#     def attack():
#         print('apple')
#     def block(incoming_damage):
#         print('apple')
#     def take_damage(damage):
#         print('apple')
#     def is_alive():
#         print('apple')
#     def fight(opponent: Hero):
#         print('apple')