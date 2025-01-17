import turtle
from turtle import Turtle,Screen

#Instances mean two or more different objects of same class
#eg timmy.color() here colr assigned is the state of object
import random
is_race_on=False
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make Your bet",prompt="Which turtle will win the race ? Enter a color: ")
colors=["red","orange","yellow","green","blue","purple"]
y_positions=[-70,-40,-10,20,50,80]
all_turtles=[]
for turtle_index in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_positions[turtle_index])
    all_turtles.append(new_turtle)
    


if user_bet:
    is_race_on=True


#print(all_turtles)

while is_race_on:
    for turtle in all_turtles:
        
        if turtle.xcor()>230:
            is_race_on=False
            winnig_color=turtle.color()
            if winnig_color==user_bet:
                print(f"You Have Won! The {winnig_color}turtle is the winner!")
            else:
                print(f"You Have Lost! The {winnig_color}turtle is the winner!")
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)   
            

screen.exitonclick()