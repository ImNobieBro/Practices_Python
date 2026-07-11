#i dont have idea how write third before lol

health = 100
print("--- Battle of the Hens: Running in system lol")

while health > 0:
    print(f"Your current health is: {health}")

    action = input("Choose an action: (1) Fight | (2) Heal: ")

    if action == "1":
        print("The chicken attacks! But.. takes 25 damage from the enemy.")
        health = health - 25
    elif action == "2":
        print("The chicken eats corn and restores 20 health!")
        health = health + 20
    else:
        print("Invalid choice! You wasted your turn.")
    
print("Game over. The chicken dead F :(")
