from stockfish import Stockfish
from datetime import datetime
import os

month = datetime.now().month
year = datetime.now().month

printed = False
if year > 2:
    print("A new version is available.\nGo to https://hudsonrocke1.github.io/website/html.html to get a new version.\n")
    printed = True
if month > 2 and printed == False:
    print("A new version is available.\nGo to https://hudsonrocke1.github.io/website/html.html to get a new version.\n")

def ask_elo():
    elo = input("What elo yould you like the engine to be (should be a whole number that is at least 1 and below 3000)?: ")
    return elo


while 1:
    elo = ask_elo()
    try:
        elo = int(elo)
        break
    except:
        print("Enter a number.\n")

elo = int(elo)
if elo < 100:
    depth_for_engine = 5
else:
    depth_for_engine = elo/100


parameters = {
    "Debug Log File": "",
    "Contempt": 0,
    "Min Split Depth": 0,
    "Threads": 3, # More threads will make the engine stronger, but should be kept at less than the number of logical processors on your computer.
    "Ponder": "false",
    "Hash": 2048, # Default size is 16 MB. It's recommended that you increase this value, but keep it as some power of 2. E.g., if you're fine using 2 GB of RAM, set Hash to 2048 (11th power of 2).
    "Skill Level": elo/100
}

stockfish = Stockfish(path="/Users/Rocke/Documents/stockfish", depth = depth_for_engine, parameters = parameters)
white_or_black = True

def get_move():
    move = stockfish.get_best_move()
    return move

def set_pos(move_made):
    stockfish.make_moves_from_current_position([move_made])
    return

get_move()

stockfish.set_depth(depth_for_engine)
stockfish.set_elo_rating(elo)
#move = stockfish.get_best_move()
#print(move)

print("\n", stockfish.get_board_visual())
while 1:
    board = False
    self_move = False
    #print(stockfish.get_evaluation())
    print("")
    input_question = input("Would you like the engine to move now?(1) or enter your own location(2) : ")
    if input_question == "1":
        move = get_move()
        set_pos(move)
        text = f"Stockfish moves {move}"
        board = True
    elif input_question == "2":
        move_ques = input("What move do you want to make?(ex: b2b4 for b2 piece to go to b4): ")
        self_move = True
        try:
            set_pos(move_ques)
            board = True
        except:
            print("Illegal position, try again.")
    else:
        print("Enter a number between 1 and 2.")
        self_move = True
    if board:
        print("\n\n", stockfish.get_board_visual())
    if not self_move:
        print(text, "\n")