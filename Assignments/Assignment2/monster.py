# Imports and Useful Variables
import random
from character import Character
small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))

# Hero Class
class Monster(Character):
    # Construtor
    def __init__(self):
        super().__init__()
        self.combat_strength = random.choice(small_dice_options)
        self.health_points = random.choice(big_dice_options)

    def __del__(self):
        super().__del__()
    
    # Monster Attack method
    # Params: m_combat_strength, health_points
    # Output: new health_points
    def monster_attacks(self, player_health):
        ascii_image2 = """                                                                 
           @@@@ @                           
      (     @*&@  ,                         
    @               %                       
     &#(@(@%@@@@@*   /                      
      @@@@@.                                
               @       /                    
                %         @                 
            ,(@(*/           %              
               @ (  .@#                 @   
                          @           .@@. @
                   @         ,              
                      @       @ .@          
                             @              
                          *(*  *      
             """
        print(ascii_image2)
        print(f"    |    Monster's Claw ({self.combat_strength}) ---> Player ({player_health})")
        if self.combat_strength >= player_health:
            player_health = 0
            print("    |    Player is dead")
        else:
            player_health -= self.combat_strength
            print(f"    |    The monster has reduced Player's health to: {player_health}")
        return player_health