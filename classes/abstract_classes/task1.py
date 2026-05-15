'''TASK 6 — Gaming inheritance
Ssenari

Bir oyun sistemi qurursan.'''

class Character :
    def __init__(self,name,power):
        self.name=name
        self.power=power

    def attack(self):
        return f"{self.name} attacks with {self.power} power"
    
class Warrior (Character):
    def sword(self):
        return f"Warrior uses sword"
    
class Knight (Warrior) :
    def shield(self):
        return f"Knight uses shield"
    

obj=Knight("Arthur" , 100)

print(obj.name)
print(obj.attack())
print(obj.sword())
print(obj.shield())
