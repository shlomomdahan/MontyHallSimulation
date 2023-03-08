import random

class MontyHall:
    
    
    doors = ['car', 'goat', 'goat']
    choice = None
    goat_door = None
    switch = None

    def __init__(self):
        # print("Monty Hall Simulation")
        random.shuffle(self.doors)
            
    
    def pick_random_door(self):
        self.choice = random.choice([0, 1, 2])
        # print("Player chooses door {}".format(self.choice))
        
    def host_reveals_goat(self):
        self.goat_door = random.choice([x for x in [0, 1, 2] if x != self.choice and self.doors[x] == 'goat'])
        # print("Host reveals door {} has a goat".format(self.goat_door))
        
    def player_switches(self):
        
        if self.switch:
            self.choice = [x for x in [0, 1, 2] if x not in [self.choice, self.goat_door]][0]
            # print("Player switches to door {}".format(self.choice))
            
    def get_wins(self):
        return self.wins
            
            

if __name__ == '__main__':
    games = 10000 # Number of times to play the game
    switch_wins = 0
    switch_success_rate = 0
    no_switch_wins = 0
    no_switch_success_rate = 0
    
    
    for x in range(games):
        game_switch = MontyHall()
        game_switch.switch = True
        game_switch.pick_random_door()
        game_switch.host_reveals_goat()
        game_switch.player_switches()
        if game_switch.doors[game_switch.choice] == 'car':
            switch_wins += 1
    
    
    
    for y in range(games):
        game_no_switch = MontyHall()
        game_no_switch.switch = False
        game_no_switch.pick_random_door()
        game_no_switch.host_reveals_goat()
        game_no_switch.player_switches()
        if game_no_switch.doors[game_no_switch.choice] == 'car':
            no_switch_wins += 1
        
        
    sucess_rate_no_switch = no_switch_wins / games
    print(sucess_rate_no_switch)    
        
    success_rate_switch = switch_wins / games
    print(success_rate_switch)
    

    
    