import cv2
from keras.models import load_model
import numpy as np
import time
import random 
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
frame_width = cap.get(3)
frame_height = cap.get(4)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

class RockPaperScissors:
    def __init__(self):
        self.computer_wins = 0
        self.user_wins = 0
        self.move_list = ["Rock", "Paper", "Scissors", "Nothing"]
        self.result = None

    def run_model(self):
        start_time = time.time()
        countdown_start_time = 0
        n_second = 0
        total_seconds = 4
        seconds_string = '3321'
        time_elapsed = 0.0
        
        while time.time() < start_time + 5:
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            if n_second < total_seconds:
                cv2.putText(img = frame, text = seconds_string[n_second], org = (int(frame_width/2 - 20),int(frame_height/2)), fontScale = 6, fontFace = cv2.FONT_HERSHEY_COMPLEX, color = (255, 0, 0), thickness = 5)
                time_elapsed = (time.time() - countdown_start_time)
                if time_elapsed >= 1:
                    n_second += 1
                    time_elapsed = 0
                    countdown_start_time = time.time()
            else:
                prediction = np.argmax(model.predict(data))
                self.result = self.move_list[prediction]
            cv2.imshow('frame', frame)
            # Press q to close the window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break                
    
    def stop_video(self):
        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()

    def get_computer_choice(self):
        options = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(options)
        print(f"The computer chose {computer_choice}")
        return computer_choice
        
    def get_winner(self, computer_choice, user_choice):
        if user_choice == "Nothing":
            print("Could not identify your choice")
            return "nothing"
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
            self.run_model()
            winner = self.get_winner(computer_choice, self.result) 
            if winner == "user":
                self.user_wins += 1
            elif winner == "computer":
                self.computer_wins += 1
            elif winner == "nothing":
                pass
            print(self.computer_wins, self.user_wins)
        

            

game_one = RockPaperScissors()
while True:
    if game_one.computer_wins == 3:
            print("The computer won!")
            game_one.stop_video()
            break
    elif game_one.user_wins == 3:
            print("You won!")
            game_one.stop_video()
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


   
    
    




        









