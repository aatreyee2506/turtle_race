from turtle import Turtle,Screen
import random


screen=Screen()

game=False
screen.setup(width=500,height=400)
u_bet=screen.textinput(title='Make a bet.', prompt='Which turtle wins the race? Enter a color:')
color=["red","orange","blue","green","purple","violet"]
new_list=[]
y_pos=[-70,-40,-10,20,50,80]


for index in range(0,6):

    tim=Turtle(shape="turtle")
    tim.color(color[index])
    tim.penup()
    tim.goto(x=-250,y=y_pos[index])
    new_list.append(tim)

if u_bet:
    game=True

while game:
    for turtle in new_list:
        if turtle.xcor()>230:
            winner=turtle.pencolor()
            if winner==u_bet:
                print(f'You won! {winner} turtle won!')
                game=False
            else:
                print(f"You lost! {winner} turtle is the winner!")
                game=False    
        distance=random.randint(0, 10)
        turtle.forward(distance)
         

screen.exitonclick()