from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
names = []


def rand_move():
    return 5 * random.randint(0, 3)


def winner():
    for n in range(len(names)):
        if names[n].pos()[0] > 230:
            return False
    return True


for option in range(len(colors)):
    names.append(Turtle(shape="turtle"))

pos = [-230, -150]
for individual in range(len(names)):
    pos = (pos[0], pos[1])

    names[individual].color(colors[individual])
    names[individual].penup()
    names[individual].goto(pos)

    pos = [pos[0], pos[1]]
    pos[1] += 60

first = names[0]
winning = colors[0]
while winner():
    for j in range(len(names)):
        names[j].forward(rand_move())
        if first.pos()[0] < names[j].pos()[0]:
            first = names[j]
            winning = colors[j]

for name in names:
    print(name.pos())

if winning == user_bet:
    print(f"Congratulations! The {user_bet} turtle won the race!")
else:
    print(f"So close! The {winning} turtle won the race! Try to get right the next one!")


screen.exitonclick()
