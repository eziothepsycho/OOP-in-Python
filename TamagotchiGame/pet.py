class Pet:
    def __init__(self, name, hunger=5, happiness=5, energy=5, alive=True):
        self.name = name
        self.hunger = max(0, min(hunger, 10))  # 0-10 range
        self.happiness = max(0, min(happiness, 10))
        self.energy = max(0, min(energy, 10))
        self.alive = alive

    def feed(self):
        if self.hunger > 0:
            self.hunger -= 1
            print(f"\n{self.name} has been fed. Hunger level: {self.hunger}")
        else:
            print(f"\n{self.name} is already full!")
    
    def check_alive(self):
        if self.hunger >= 10 or self.energy <= 0:
            self.alive = False
            print(f"\n{self.name} has passed away... :<")
            return False
        return True
    
    def play(self):
        if not self.alive:
            print(f"\n{self.name} can't play...")
            return
        
        if self.energy > 0:
            self.happiness += 1
            self.energy -= 1
            print(f"\n{self.name} played and is now happier! Happiness: {self.happiness}")
        else:
            print(f"\n{self.name} is too tired to play.")

    def sleep(self):
        if not self.alive:
            print(f"\n{self.name} can't play...")
            return
        
        if self.energy < 10:
            self.energy += 1
            print(f"\n{self.name} is sleeping right now. Energy: {self.energy}")
        else:
            print(f"\n{self.name} is not in the mood to sleep.")
    
    def status(self):
        print(f"\n{self.name}'s Status:")
        print(f"Hunger: {self.hunger}\nHappiness: {self.happiness}\nEnergy: {self.energy}\nAlive:{self.alive}")
    
    def pass_time(self):
        if not self.alive:
            print(f"\n{self.name} can't play...")
            return
        
        self.hunger = min(self.hunger + 2, 10)
        self.energy = max(self.energy - 2, 0)
        print(f"{self.name} is passing time.")
