from turtle import Turtle, Screen
import pandas as pd

IMAGE_FILE_PATH = './blank_states_img.gif'
TOTAL_STATES_AMOUNT = 50
MOVE = False
ALIGN = 'center'
FONT = ('Dubai', 8, 'normal')
STOP_THE_GAME = 'Exit'
title = 'Guess the state!'
correct_guesses = []
score = 0

screen = Screen()
screen.title(titlestring='U.S States Game')
screen.addshape(name=IMAGE_FILE_PATH)

turtle = Turtle()
turtle.hideturtle()
turtle.penup()

Turtle().shape(name=IMAGE_FILE_PATH)

us_states_data = pd.read_csv(filepath_or_buffer='./50_states.csv')
# us_states_list = us_states_data['state'].tolist()

while score != TOTAL_STATES_AMOUNT:
# while len(correct_guesses) < 50:
    user_state_guess = screen.textinput(title=title, prompt='What\'s another state\'s name?').title()

    if user_state_guess == STOP_THE_GAME:
        # break
        # us_missed_states = []
        # for state in us_states_list:
        #     if state not in correct_guesses:
        #         us_missed_states.append(state)
        # # print(us_missed_states)
        # new_data = pd.DataFrame(us_missed_states)  # <--- learned something new
        # new_data.to_csv('states_to_learn.csv')
        # us_missed_states = [state for state in us_states_list if state not in correct_guesses]
        # pd.DataFrame(us_missed_states).to_csv('states_to_learn.csv')
        break

    if us_states_data[us_states_data['state'] == user_state_guess].empty:
    # if user_state_guess not in us_states_list:
        continue

    x_coordinate, y_coordinate = tuple(us_states_data[us_states_data['state'] == user_state_guess][['x', 'y']].iloc[0])
    turtle.goto(x=x_coordinate, y=y_coordinate)
    turtle.write(arg=user_state_guess, move=MOVE, align=ALIGN, font=FONT)
    # ---
    # us_state_data = us_states_data[us_states_data.state == user_state_guess]
    # turtle.goto(x=int(us_state_data.x), y=int(us_state_data.y))
    # turtle.write(arg=us_states_data.state.item(), move=MOVE, align=ALIGN, font=FONT)  # <--- learned something new

    score += 1
    correct_guesses.append(user_state_guess)
    title = f'{score}/{TOTAL_STATES_AMOUNT} States Correct'
    # title = '{user_score}/{total_states} States Correct'.format(user_score=len(correct_guesses),
    #                                                             total_states=TOTAL_STATES_AMOUNT)

missed_states_check = ~us_states_data.state.isin(correct_guesses)
us_states_missed = us_states_data[missed_states_check].state
missed_us_states = us_states_missed.to_csv(path_or_buf='states_to_learn.csv')
