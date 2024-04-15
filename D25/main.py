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
all_states = dataframe["state"].to_list()


while len(answers.all_answers) < 50:

    answer_state = screen.textinput(title = "Guess the State", prompt = "What's anothe state's name? Type exit to Exit the game").title()

    # if answer state is one of the states
    if answer_state in all_states:
        state_data = dataframe[dataframe["state"] == answer_state]
        answers.print_answer(state_data["state"].item(), int(state_data["x"].item()), int(state_data["y"].item())) 
        all_states.remove(answer_state)
        # print(all_states)
    elif answer_state == "Exit":
        break

# states_to_learn.csv
states_to_learn = pd.DataFrame(all_states, columns = ['state'])
states_to_learn.to_csv(r"D25\states_to_learn.csv", index = False)
print(f"Your score is {len(answers.all_answers)}")



# turtle.mainloop()
# screen.exitonclick()