# Imports and Useful Variables
from character import Character
import random

small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))

# Hero Class
class Hero(Character):
    # Construtor
    def __init__(self):
        super().__init__()

    def __del__(self):
        super().__del__()

    def hero_attacks(self, m_health_points):
        ascii_image = """
                                @@   @@ 
                                @    @  
                                @   @   
               @@@@@@          @@  @    
            @@       @@        @ @@     
           @%         @     @@@ @       
            @        @@     @@@@@     
               @@@@@        @@       
               @    @@@@                
          @@@ @@                        
       @@     @                         
   @@*       @                          
   @        @@                          
           @@                                                    
         @   @@@@@@@                    
        @            @                  
      @              @                  

  """
        print(ascii_image)
        print(f"    |    Player's weapon ({self.combat_strength}) ---> Monster ({m_health_points})")
        if self.combat_strength >= m_health_points:
            m_health_points = 0
            print("    |    You have killed the monster")
        else:
            m_health_points -= self.combat_strength
            print(f"    |    You have reduced the monster's health to: {m_health_points}")
        return m_health_points
    
