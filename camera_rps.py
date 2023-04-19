import cv2
from keras.models import load_model
import numpy as np
import time
import random 
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

class RockPaperScissors:
    def __init__(self):
        self.computer_wins = 0
        self.user_wins = 0

    def alt_timer(self):
        print("Counting down: 3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)

    @classmethod
    def timer():
        start_time = time.time()
        while (time.time() - start_time) < 1:
            print("Counting down: 3")
        while (time.time() - start_time) < 2:
            print("Counting down: 2")
        while (time.time() - start_time) < 3:
            print("Counting down: 1")

    def run_model(self):
        self.alt_timer()
        while True: 
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            cv2.imshow('frame', frame)
            # Press q to close the window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break             
        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
        return prediction

    def get_prediction(self):
        highest_probability_index = np.argmax(self.run_model())
        if highest_probability_index == 0:
            return "Rock"
        elif highest_probability_index == 1:
            return "Paper"
        elif highest_probability_index == 2:
            return "Scissors"
        else:
            return "Nothing"

    def get_computer_choice(self):
        options = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(options)
        print(f"The computer chose {computer_choice}")
        return computer_choice
        
    ### for some reason the printed bit of this (e.g. "You lost" prints twice each round, I have no idea why. The scores in play() only print once ###    
    def get_winner(self, computer_choice, user_choice):
        if computer_choice == user_choice:
            print("It is a tie!")
        elif computer_choice == "Rock":
            if user_choice == "Paper":
                print("You won!")
                return "user"
            else:
                print("You lost")
                return "computer"
        elif computer_choice == "Paper":
            if user_choice == "Scissors":
                print("You won!")
                return "user"
            else:
                print("You lost")
                return "computer"
        elif computer_choice == "Scissors":
            if user_choice == "Rock":
                print("You won!")
                return "user"
            else:
                print("You lost")
                return "computer"

    def play(self):
            computer_choice = self.get_computer_choice()
            user_choice = self.get_prediction()
            winner = self.get_winner(computer_choice, user_choice) 
            if winner == "user":
                self.user_wins += 1
            elif winner == "computer":
                self.computer_wins += 1
            print(self.computer_wins, self.user_wins)

game_one = RockPaperScissors()
while True:
    if game_one.computer_wins == 3:
            print("The computer won!")
            break
    elif game_one.user_wins == 3:
            print("You won!")
            break
    else:
        game_one.play()

""" def check_keep_playing():
    if c_wins == 3:
        print("The computer won!")
        return False
    elif u_wins == 3:
        print("You won!")
        return False
    else:
        return True
    
while check_keep_playing():     
    play() """


   
    
    




        









