from tkinter import *
from random import randint

BACKGROUND_COLOR = "#263c4e"
TEXT_COLOR = "#18d7e8"

level = 3
target_shown_number = 0
target_buttons_list = []
buttons_pressed_by_player = []
end_of_turn = False


def start_game():
    global end_of_turn
    # start the turn of game
    end_of_turn = False
    state_label.config(text="WATCH", fg=TEXT_COLOR)
    disable_buttons()
    # show the targets to player
    simon_says()
    # check users answer every 1 min
    check_users_pressed_buttons()


def simon_says():
    global target_shown_number, target_buttons_list
    target_shown_number += 1

    # picking random button as target for players
    random_button_num = randint(1, 4)

    # adding this button id to identify which buttons showed to be pressed
    target_buttons_list.append(random_button_num)

    if random_button_num == 1:
        top_left_button.config(bg="#77cee1")

    elif random_button_num == 2:
        top_right_button.config(bg="#e66")

    elif random_button_num == 3:
        bottom_left_button.config(bg="#71d7a9")

    elif random_button_num == 4:
        bottom_right_button.config(bg="#dfdb7e")

    window.after(1000, change_back_buttons_color)


def change_back_buttons_color():
    top_left_button.config(bg="#1f8fa7")
    top_right_button.config(bg="#a72501")
    bottom_left_button.config(bg="#289262")
    bottom_right_button.config(bg="#b5af19")

    # check if targets count reached the player level...level here is for difficulty and number of targets to memorize
    if target_shown_number <= level:
        window.after(1000, simon_says)
    else:
        state_label.config(text="PRESS")
        activate_buttons()


def check_users_pressed_buttons():
    for i in range(len(buttons_pressed_by_player)):
        # check if buttons pressed by player is what was on targets shown
        if target_buttons_list[i] != buttons_pressed_by_player[i]:
            reset_score()
            player_lose()
        # check if player completed the level and level up game difficulty
        elif buttons_pressed_by_player == target_buttons_list:
            reset_score()
            player_win()
    if not end_of_turn:
        print(target_buttons_list)
        print(buttons_pressed_by_player)
        # check buttons every one second
        window.after(1000, check_users_pressed_buttons)


def disable_buttons():
    # disable buttons so not be pressed when showing targets or when number of targets reached
    top_left_button.config(state="disabled")
    top_right_button.config(state="disabled")
    bottom_left_button.config(state="disabled")
    bottom_right_button.config(state="disabled")


def activate_buttons():
    # activates buttons to pressed by player
    top_left_button.config(state="normal")
    top_right_button.config(state="normal")
    bottom_left_button.config(state="normal")
    bottom_right_button.config(state="normal")


def reset_score():
    global target_buttons_list, buttons_pressed_by_player, target_shown_number, end_of_turn
    target_shown_number = 0
    end_of_turn = True
    target_buttons_list.clear()
    buttons_pressed_by_player.clear()


def player_lose():
    state_label.config(text="try again", fg="red")
    window.after(3000, start_game)


def player_win():
    global level
    state_label.config(text="done....level up", fg="green")
    level += 1
    window.after(3000, start_game)


def button_1_pressed():
    buttons_pressed_by_player.append(1)


def button_2_pressed():
    buttons_pressed_by_player.append(2)


def button_3_pressed():
    buttons_pressed_by_player.append(3)


def button_4_pressed():
    buttons_pressed_by_player.append(4)


# ------------------- user interface ----------------#
window = Tk()
window.title("simon game")
window.config(pady=40, padx=40, bg="#263c4e")
window.minsize(300, 500)

state_label = Label(text="START...in 3 sec", font=("arial", 25, "bold"), bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
state_label.grid(column=0, columnspan=2, row=0, pady=15)

top_left_button = Button(width=20, height=10, bg="#1f8fa7", command=button_1_pressed, state="disabled")
top_left_button.grid(column=0, row=1)

top_right_button = Button(width=20, height=10, bg="#a72501", command=button_2_pressed, state="disabled")
top_right_button.grid(column=1, row=1)

bottom_left_button = Button(width=20, height=10, bg="#289262", command=button_3_pressed, state="disabled")
bottom_left_button.grid(column=0, row=2)

bottom_right_button = Button(width=20, height=10, bg="#b5af19", command=button_4_pressed, state="disabled")
bottom_right_button.grid(column=1, row=2, padx=10, pady=10)

# start game after 3 second passed opening of program
window.after(3000, start_game)

window.mainloop()
