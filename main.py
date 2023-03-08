import turtle
import pandas

FONT = ("Courier", 10, "normal")
data = pandas.read_csv("50_states.csv")
user_missed_states = data["state"].to_list()
screen = turtle.Screen()
screen.title("US States Quiz")
screen.bgpic("blank_states_img.gif")
screen.setup(730, 500)
turtle.hideturtle()

## get the x,y coor for mouse click on map ##
# screen.listen()
# def get_mouse_click_coor(x, y):
#   print(x, y)
# screen.onclick(get_mouse_click_coor)

game_is_on = True
score = 0
user_typed_states = []
user_guess = ""
while game_is_on:
  if score == 50 or user_guess == "Exit":
    break
  user_guess = (screen.textinput(f"{score}/50 correct", "Guess the name of a US state:")).title()
  
  if user_guess in data.values:
    score += 1
    user_missed_states.remove(user_guess)
    user_typed_states.append(user_guess)
    x = float(data[data["state"] == user_guess]["x"])
    y = float(data[data["state"] == user_guess]["y"])
    turtle.penup()
    turtle.goto(x, y)
    turtle.write(user_guess, move=False, align="center", font=FONT)

missing_states = pandas.DataFrame(user_missed_states)
missing_states.to_csv("user_missed_states.csv")
# screen.mainloop()
screen.exitonclick()