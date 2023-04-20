# Computer Vision RPS

# Milestone 1

A github repo was set up to store the files associated with the project.

# Milestone 2

Teachable Machine was used to train a model with four classes: Rock, Paper, Scissors, and Nothing (for when the player is not doing a pose). Around 300 images were added to each class. The images were taken from as many different directions and with as many different variations of the hand positions as possible. It seems to be very good at detecting the Nothing position, pretty good at detecting Scissors and Paper, and not very good at detecting Rock. 

The model was downloaded via Tensorfile in two files, keras_model.h5 and labels.txt. The files were added to the computer vision repo on github.

# Milestone 3

A conda environment for running the model was created with opencv-python, tensorflow, and ipykernel. The opencv-python library is used for computer vision and image processing. The tensorflow library is used for machine learning and AI. Keras acts as the Python interface for the TensorFlow library. The ipykernel library is used for working with Python code in Jupyter notebooks. The functionality of the model was checked using the code in RPS-Template.py. 

# Milestone 4

A python file, manual_rps.py, was created to store the code for manually playing a game of Rock, Paper, Scissors. Three functions were created: one to get the computer's choice, picked randomly from a list using random.choice, one to get the user choice using input(), and one to compare the two choices and determine a winner. The three functions were then encapsulated into a function called play() which runs the entire game from start to finish. 

# Milestone 5

The file camera_rps.py was created to store the code for playing the game using the camera and model to get the user's choice. The game was encapsulated into a class called RockPaperScissors that initializes with variables for counting the computer's wins, the user's wins, a list of possible moves (Rock, Paper, Scissors, Nothing), and a result for storing the user's choice. 

The run_model method runs the video capture and uses the model to predict the user's choice. The prediction works by using the argmax function from the numpy module to find the index of the highest number in the list of 4 probabilities (one for each move plus Nothing) returned by the model. This index is then used to index the class's move_list variable to give a string representing the user's choice. This string is saved to self.result.

The functionality for stopping the video capture was placed into another method because keeping it inside the run_model method made the video crash. I needed to keep the video capture open during the entire gameplay and only shut it once a winner had been determined. 

The gameplay methods are get_computer_choice, which returns a computer_choice randomly selected from the list of options, and get_winner, which checks computer_choice against self.result to determine a winner. The get_winner method returns either "user", "computer", or "nothing" if the model could not identify a choice. 

The play method gets the computer choice, runs the model to get the new user choice (self.result), then runs the get_winner method using these choices as parameters. It then updates the scores. 

To play the game a while loop was created outside the class that checks the victory condition (either player reaches 3 wins) and if not met, runs game.play. 

To expand the project a countdown was added in text to the video between each round using cv2.putText. The countdown works by taking a string "4321" (the first number never shows up for some reason) and indexing it using the number of seconds elapsed, which updates every second. The time_elapsed counter also resets every second. The time is counted using time.time(). When the number of seconds elapsed exceeds 4, the prediction runs.