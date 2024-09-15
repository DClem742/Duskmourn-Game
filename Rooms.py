from Characters import Enemy

class Rooms:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.enemy = None

    def set_enemy(self, enemy):
        self.enemy = enemy

    def enter(self, character):
        print(f"\nYou enter {self.name}. {self.description}")
        # Room-specific logic follows

class TheMistmoors(Rooms):
    def __init__(self):
        super().__init__("The Mistmoors", "Empty foyers that ring with eerie silence. Corridors lined with uncanny marble statues and draped with white fabric that ripples in unfelt breezes. Cobwebbed attics beneath towering arched eaves. Stacked terraces drowning beneath ceaseless eroding sand.")
        self.survivor_present = True

    def enter(self, player):
        print(f"\nYou enter {self.name}. {self.description}")
        if self.survivor_present:
            print("You encounter a weary survivor in the mist!")
            print("Survivor: 'Take these health potions. You'll need them against Valgavoth!'")
            player.add_health_potions(2)
            self.survivor_present = False

class TheFloodpits(Rooms):
    def __init__(self):
        super().__init__("The Floodpits", "Frozen subterranean lakes. Screen-lined corridors that breathe a cold, obscuring fog. Twisting staircases that you can walk onto but never off of. Libraries where waterfalls pour into waist-high lakes of sodden pages. Damp, musty bedrooms mottled with unsettling water stains.")
        self.puzzle_solved = False
        self.riddle = "In sadness or joy forever I weep\nBut behind my tears\nLies what you seek.\nWhat am I?"
    
    def enter(self, player):
        print(f"\nYou enter {self.name}. {self.description}")
        while not self.puzzle_solved:
            if self.solve_puzzle():
                break
            else:
                print("You must solve the riddle to advance.")
    def solve_puzzle(self):
        print("You encounter a mysterious inscription on the wall.")
        print(self.riddle)
        
        answer = input("Enter your answer: ").lower().strip()
        if answer == "waterfall":
            print("Correct! The sound of rushing water grows louder, revealing a hidden passage.")
            self.puzzle_solved = True
            return True
        else:
            print("The inscription remains unchanged. Try again!")
            return False
class TheBalemurk(Rooms):
    def __init__(self):
        super().__init__("The Balemurk", "Lightless foyers of rotting floorboards knit together by unpleasantly dripping spiderwebs. Bogs riddled with gravestones and punctuated by withered, grasping trees. Basements sunk in ominous gloom, whose shadowy corners seem to move when glimpsed from the corner of your eye")
        self.puzzle_solved = False
        self.lock_combination = ['L', 'R', 'L']
        self.current_combination = ['', '', '']

    def enter(self, player):
        print(f"You enter {self.name}. {self.description}")
        while not self.puzzle_solved:
            if self.solve_puzzle():
                break
            else:
                print("You must solve the lock puzzle to advance.")

    def solve_puzzle(self):
        print("You encounter a giant slab door with three concentric rings.")
        print("Each ring can be turned left (L) or right (R).")
        print("Align the rings correctly to open the door.")

        for i in range(3):
            direction = input(f"Turn ring {i+1} left or right (L/R): ").upper()
            while direction not in ['L', 'R']:
                direction = input("Invalid input. Please enter L or R: ").upper()
            self.current_combination[i] = direction

        if self.current_combination == self.lock_combination:
            print("The rings align with a satisfying click. The door swings open...")
            self.puzzle_solved = True
            return True
        else:
            print("The rings don't align. The door remains closed.")
            return False

class TheHauntwoods(Rooms):
    def __init__(self):
        super().__init__("The Hauntwoods", "Hallways choked with thorny vines and brambles. Overgrown greenhouses full of specimens both venomous and carnivorous. Isolated cabins in the middle of dense, lightless woods. Crumbling domes strung with wicker hexes and strangled by trees shaped like human hands.")
        self.maze_solved = False
        self.correct_path = ["north", "east", "north", "west", "north"]

    def enter(self, player):
        print(f"You enter {self.name}. {self.description}")
        while not self.maze_solved:
            if self.solve_maze():
                break
            else:
                print("You must solve the maze to advance.")

    def solve_maze(self):
        print("You find yourself in a maze of twisted trees.")
        print("To escape, you must navigate through the maze.")
        player_path = []
        
        for step in range(5):
            direction = input("Choose a direction (north/south/east/west): ").lower()
            player_path.append(direction)
            
            if player_path != self.correct_path[:len(player_path)]:
                print("You've hit a dead end. Start over!")
                return False
        
        print("You've successfully navigated the maze!")
        self.maze_solved = True
        return True
    
class TheBoilerbilges(Rooms):
    def __init__(self):
        super().__init__("The Boilerbilges", "Furnace rooms full of suffocating heat. Stairways that end in abrupt drops into vents of sulfurous fire. Hallways whose walls are slashed with rips glowing a vivid, infected red. Scorched, blackened, fire-ravaged junk rooms. ")
        self.enemy = Enemy("Razorkin", 40, 10, 5)

    def enter(self, player):
        print(f"You enter {self.name}. {self.description}")
        if self.enemy:
            print(f"{self.enemy.name} appears!")
            return False  # Indicates that a battle should occur
        return True  # No enemy, player can proceed
