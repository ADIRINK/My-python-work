import random

hp = 50
difficulty = 2
print("Starting HP",hp)

potion_hp = random.randint(25, 50)
print("HP potion will restore",potion_hp,"health")
potion_hp = int(potion_hp / difficulty)
print("HP potion will restore",potion_hp,"health after difficulty adjustment")

hp = hp+potion_hp
print("You have",hp,"health")


