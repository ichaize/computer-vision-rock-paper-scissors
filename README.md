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