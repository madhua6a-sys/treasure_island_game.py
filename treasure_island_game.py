import turtle
import random
import os
os.system("clear")

print(''' ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/
''')

print("🏝️ Welcome to Treasure Island!")
print("🗺️ Your mission is to find the treasure. 💎")

choice1 = input(
    '🚶 You\'re at a crossroad, where do you want to go?\n'
    '⬅️ Type "left" or ➡️ "right".\n'
).lower()

if choice1 == "left":

    choice2 = input(
        '🌊 You\'ve come to a lake.\n'
        '🏝️ There is an island in the middle of the lake.\n'
        '⛵ Type "wait" to wait for a boat.\n'
        '🏊 Type "swim" to swim across.\n'
    ).lower()

    if choice2 == "wait":

        choice3 = input(
            "🏝️ You arrived at the island unharmed.\n"
            "🏠 There is a house with 3 doors.\n"
            "🔴 One red, 🟡 one yellow and 🔵 one blue.\n"
            "🚪 Which door do you choose?\n"
        ).lower()

        if choice3 == "red":
            print("🔥 It's a room full of fire. Game over. ☠️")
            screen = turtle.Screen()
            screen.bgcolor("black")
            screen.title("Game Over 💀")
            t = turtle.Turtle()
            t.speed(0)
            t.width(2)
            t.hideturtle()
            colours = ["red", "yellow", "blue", "pink", "green", "orange", "purple"]
            t.penup()
            t.goto(0, 60)
            t.pendown()
            t.color("red")
            t.write("GAME OVER", align="center", font=("Arial Black", 72, "bold"))
            t.penup()
            t.goto(0, -20)
            t.color("orange")
            t.write("🔥 It's a room full of fire!", align="center", font=("Arial", 26, "bold"))
            while True:
                x = random.randint(-250, 250)
                y = random.randint(-150, 250)
                t.penup()
                t.goto(x, y)
                t.pendown()
                for i in range(36):
                    t.color(random.choice(colours))
                    t.forward(60)
                    t.backward(60)
                    t.right(10)
            turtle.done()

        elif choice3 == "yellow":
            print("💎 You found the treasure. 🎉 You win! 🏆")
            screen = turtle.Screen()
            screen.bgcolor("black")
            screen.title("Endless fireworks 🎇")
            t = turtle.Turtle()
            t.speed(0)
            t.width(2)
            t.hideturtle()
            colours = ["red", "yellow", "blue", "pink", "green", "orange", "purple"]
            t.penup()
            t.goto(0, 60)
            t.pendown()
            t.color("gold")
            t.write("YOU WIN!", align="center", font=("Arial Black", 72, "bold"))
            t.penup()
            t.goto(0, -20)
            t.color("yellow")
            t.write("💎 You found the treasure! 🏆", align="center", font=("Arial", 26, "bold"))
            while True:
                x = random.randint(-250, 250)
                y = random.randint(-150, 250)
                t.penup()
                t.goto(x, y)
                t.pendown()
                for i in range(36):
                    t.color(random.choice(colours))
                    t.forward(60)
                    t.backward(60)
                    t.right(10)
            turtle.done()

        elif choice3 == "blue":
            print("🐺 You entered a room full of beasts. Game over. ☠️")
            screen = turtle.Screen()
            screen.bgcolor("black")
            screen.title("Game Over 💀")
            t = turtle.Turtle()
            t.speed(0)
            t.width(2)
            t.hideturtle()
            colours = ["red", "yellow", "blue", "pink", "green", "orange", "purple"]
            t.penup()
            t.goto(0, 60)
            t.pendown()
            t.color("red")
            t.write("GAME OVER", align="center", font=("Arial Black", 72, "bold"))
            t.penup()
            t.goto(0, -20)
            t.color("orange")
            t.write("🐺 You entered a room full of beasts!", align="center", font=("Arial", 26, "bold"))
            while True:
                x = random.randint(-250, 250)
                y = random.randint(-150, 250)
                t.penup()
                t.goto(x, y)
                t.pendown()
                for i in range(36):
                    t.color(random.choice(colours))
                    t.forward(60)
                    t.backward(60)
                    t.right(10)
            turtle.done()

        else:
            print("🚫 You chose a door that doesn't exist. Game over. ☠️")
            screen = turtle.Screen()
            screen.bgcolor("black")
            screen.title("Game Over 💀")
            t = turtle.Turtle()
            t.speed(0)
            t.width(2)
            t.hideturtle()
            colours = ["red", "yellow", "blue", "pink", "green", "orange", "purple"]
            t.penup()
            t.goto(0, 60)
            t.pendown()
            t.color("red")
            t.write("GAME OVER", align="center", font=("Arial Black", 72, "bold"))
            t.penup()
            t.goto(0, -20)
            t.color("orange")
            t.write("🚫 That door doesn't exist!", align="center", font=("Arial", 26, "bold"))
            while True:
                x = random.randint(-250, 250)
                y = random.randint(-150, 250)
                t.penup()
                t.goto(x, y)
                t.pendown()
                for i in range(36):
                    t.color(random.choice(colours))
                    t.forward(60)
                    t.backward(60)
                    t.right(10)
            turtle.done()

    else:
        print("🐟 You got attacked by an angry trout. Game over. ☠️")
        screen = turtle.Screen()
        screen.bgcolor("black")
        screen.title("Game Over 💀")
        t = turtle.Turtle()
        t.speed(0)
        t.width(2)
        t.hideturtle()
        colours = ["red", "yellow", "blue", "pink", "green", "orange", "purple"]
        t.penup()
        t.goto(0, 60)
        t.pendown()
        t.color("red")
        t.write("GAME OVER", align="center", font=("Arial Black", 72, "bold"))
        t.penup()
        t.goto(0, -20)
        t.color("orange")
        t.write("🐟 You got attacked by an angry trout!", align="center", font=("Arial", 26, "bold"))
        while True:
            x = random.randint(-250, 250)
            y = random.randint(-150, 250)
            t.penup()
            t.goto(x, y)
            t.pendown()
            for i in range(36):
                t.color(random.choice(colours))
                t.forward(60)
                t.backward(60)
                t.right(10)
        turtle.done()

else:
    print("🕳️ You fell into a hole. Game over. ☠️")
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Game Over 💀")
    t = turtle.Turtle()
    t.speed(0)
    t.width(2)
    t.hideturtle()
    colours = ["red", "yellow", "blue", "pink", "green", "orange", "purple"]
    t.penup()
    t.goto(0, 60)
    t.pendown()
    t.color("red")
    t.write("GAME OVER", align="center", font=("Arial Black", 72, "bold"))
    t.penup()
    t.goto(0, -20)
    t.color("orange")
    t.write("🕳️ You fell into a hole!", align="center", font=("Arial", 26, "bold"))
    while True:
        x = random.randint(-250, 250)
        y = random.randint(-150, 250)
        t.penup()
        t.goto(x, y)
        t.pendown()
        for i in range(36):
            t.color(random.choice(colours))
            t.forward(60)
            t.backward(60)
            t.right(10)
    turtle.done()