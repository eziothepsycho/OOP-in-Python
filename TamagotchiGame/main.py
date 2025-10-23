# main.py
from pet import Pet

class PetGame:
    def __init__(self):
        self.pet = None
        self.running = True
    
    def create_pet(self):
        name = input("What would you like to name your pet? ")
        self.pet = Pet(name)
        print(f"Welcome {name} to the virtual pet world!")
    
    def show_menu(self):
        
        print("\n--- Pet Care Menu ---")
        print("1. Feed your pet")
        print("2. Play with your pet")
        print("3. Put pet to sleep")
        print("4. Check status")
        print("5. Pass time")
        print("6. Quit game")
    
    def handle_choice(self, choice):
        
        if choice == "1":
            self.pet.feed()
        elif choice == "2":
            self.pet.play()
        elif choice == "3":
            self.pet.sleep()
        elif choice == "4":
            self.pet.status()
        elif choice == "5":
            self.pet.pass_time()
        elif choice == "6":
            self.running = False
            print("Thanks for playing!")
        else:
            print("Invalid choice. Please try again.")
    
    def check_game_over(self):
        self.pet.check_alive()
        if not self.pet.alive:
            print("Game Over!")
            self.running = False
    
    def run(self):
        self.create_pet()
    
        while self.running:
            self.show_menu()
            choice = input("Enter your choice (1-6): ")
            self.handle_choice(choice)
            
            if self.pet.alive and choice in ["1", "2", "3", "5"]:
                self.check_game_over()

if __name__ == "__main__":
    game = PetGame()
    game.run()