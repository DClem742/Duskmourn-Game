import random
from Characters import Sean, Pat, TheMeg, Enemy
from Rooms import TheMistmoors, TheFloodpits, TheBalemurk, TheBoilerbilges, TheHauntwoods

class Game:
    def __init__(self):
        self.characters = [Sean(), Pat(), TheMeg()]
        self.rooms = [TheMistmoors(), TheFloodpits(), TheBalemurk(), TheBoilerbilges(), TheHauntwoods()]
        self.final_boss = Enemy("Valgavoth", 100, 20, 13)
        self.player_health_potions = 0

    def select_character(self):
        print("Select your character:")
        for i in range(len(self.characters)):
            print(f"{i+1}. {self.characters[i].name}")
        while True:
            choice = input("Enter the number of your choice: ")
            if choice.isdigit():
                choice = int(choice) - 1
                if 0 <= choice < len(self.characters):
                    return self.characters[choice]
            print("Invalid choice. Please enter a valid number.")
    def battle(self, player, enemy):
        print(f"A {enemy.name} sees you enter and attacks!")
        while player.health > 0 and enemy.health > 0:
            print(f"{player.name} HP: {player.health} | {enemy.name} HP: {enemy.health}")
            print("Choose your action:")
            print("1. Attack")
            print("2. Use Special Ability")
            print("3. Use Health Potion")
            
            choice = input("Enter the number of your choice: ")
            
            if choice == '1':
                damage = max(0, player.attack - enemy.defense)
                enemy.health -= damage
                print(f"You deal {damage} damage to {enemy.name}")
            elif choice == '2':
                print(f"You use {player.special_ability}!")
                damage = max(0, player.attack * 1.5 - enemy.defense)
                enemy.health -= damage
                print(f"You deal {damage} damage to {enemy.name}")
            elif choice == '3':
                if self.player_health_potions > 0:
                    heal_amount = 50  # You can adjust this value
                    player.health = min(player.health + heal_amount, 100)  # Assuming max health is 100
                    self.player_health_potions -= 1
                    print(f"You used a health potion and restored {heal_amount} HP!")
                else:
                    print("You don't have any health potions!")
                continue
            else:
                print("Invalid choice. Please try again.")
                continue
            
            if enemy.health <= 0:
                print(f"You defeated {enemy.name}!")
                if random.random() < 0.5:  # 50% chance to drop a health potion
                    self.player_health_potions += 1
                    print("The enemy dropped a health potion!")
                return True
            
            player.health -= max(0, enemy.attack - player.defense)
            print(f"{enemy.name} attacks you for {max(0, enemy.attack - player.defense)} damage")
        
        print("Game Over! You have been defeated.")
        return False    
    
    def print_separator(self):
        print("\n" + "-" * 50 + "\n")

    def play(self):
        self.print_separator()
        print("Welcome to Duskmourn, House of Horror, a haunted mansion full of eerie rooms that are ever shifting...")
        print("Your goal is to venture through the House, solve it's puzzles and defeat it's enemies, and ultimately face  and defeat the demon Valgavoth, the Devouring Father.")
        print("Good luck, and be wary of your surroundings. This place isn't like other houses...\n")
        self.print_separator()

        player = self.select_character()
        self.print_separator()
        print(f"You selected {player.name}!")
        self.print_separator()
        
        random.shuffle(self.rooms)
        
        for room in self.rooms:
            room.enter(player)
            self.print_separator()
            player.display_inventory()
            self.print_separator()
            if room.name == "The Floodpits":
                while not room.puzzle_solved:
                    if room.solve_puzzle():
                        break
                    else:
                        print("You must solve the riddle to advance.")
            elif room.name == "The Hauntwoods":
                while not room.maze_solved:
                    if room.solve_maze():
                        break
                    else:
                        print("You must solve the maze to advance.")
            elif room.name == "The Balemurk":
                while not room.puzzle_solved:
                    if room.solve_puzzle():
                        break
                    else:
                        print("You must solve the lock puzzle to advance.")
            elif room.enemy:
                if not self.battle(player, room.enemy):
                    return
        
        print("You've made it to the final room. Valgavoth awaits!")
        if self.battle(player, self.final_boss):
            print("Congratulations! You've defeated Valgavoth and escaped the House!")
        else:
            print("Valgavoth has defeated you. The House always wins")        

def main():
    game = Game()
    game.play()
if __name__ == "__main__":
    main()

