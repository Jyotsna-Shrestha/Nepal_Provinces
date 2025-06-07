import turtle
import pandas as pd

image = "nepal.gif"
screen = turtle.Screen()
screen.setup(width=1100, height=700)
screen.title("Game: Nepal's Provinces")
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("Nepal_Provinces.csv")
province = data.province.to_list()
province_list = [string.title() for string in province]
guessed_provinces = []
guesses = 0

while len(guessed_provinces) < 7:
    answer = screen.textinput(f'Guess the province ({guesses}/7)', "Type name of a province").title()
    if answer in province_list:
        guessed_provinces.append(answer)
        coord = data[data.province == answer.title()]
        x = int(coord.x.iloc[0])
        y = int(coord.y.iloc[0])
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(x,y)
        t.write(answer,font=("Arial", 14, "bold"))
        guesses += 1
    elif answer == "Exit":
        missing_province = []
        for province in province_list:
            if province not in guessed_provinces:
                missing_province.append(province)
        remaining = pd.DataFrame(missing_province)
        remaining.to_csv("Provinces_to_learn.csv")
        break
    else:
       continue
if len(guessed_provinces)==7:
    pen = turtle.Turtle()
    pen.color("Red")
    pen.penup()
    pen.hideturtle()
    pen.goto(60, 229)
    pen.write("Great Job!", font=("Ariel", 25, "bold"))

turtle.mainloop()