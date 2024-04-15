import turtle
import answer
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = r"data\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
answers = answer.Answer()

dataframe = pd.read_csv(r"data\50_states.csv")

# game_is_on = True
# score = 0

while len(answers.all_answers) < 50:

    answer_state = screen.textinput(title = "Guess the State", prompt = "What's anothe state's name? Type exit to Exit the game").title()
    all_states = dataframe["state"].to_list()

    # if answer state is one of the states
    if answer_state in all_states:
        state_data = dataframe[dataframe["state"] == answer_state]
        answers.print_answer(state_data["state"].item(), int(state_data["x"].item()), int(state_data["y"].item())) 
        # score += 1
        
    elif answer_state == "Exit":
        break

print(f"Your score is {len(answers.all_answers)}")



# def get_mouse_click_coor(x, y):
#     print(x, y)
    
# turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()

# screen.exitonclick()