# The class
class enemy:
    enemy_height = 6.2
    def __init__(self,name,width,weapon,health):
        self.name = name
        self.width = width
        self.weapon = weapon
        self.health = health
    

# The objects
enemy1 = enemy("Soap",2,"Dual Wielded Rivolver",100)
enemy2 = enemy("Nick",2.5,"A M4A1 and A glock with some tactical and lethal stuff",130)

# Display
print("Hey Bro! The name's",enemy1.name)
print("Looks like a guest has arrived. My name is",enemy2.name)
print("Trust me it won't be fun for you to fight us. I got a ",enemy1.weapon,"and I got",enemy2.weapon)

