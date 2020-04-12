Emotion based music player

This project decides emotion based on your facial expression, it checks for
7 expressions, anger, disgust, happy, sad, surprise, neutral and fear. Based
on the decided expression it will play music from the designated folder. The 
dataset used here is Kaggle dataset. Follow step by step instructions to run 
and execute the project:
step 1: Run the following in anaconda command prompt
		1.1 : conda create -n tensorflow_env tensorflow
		1.2 : conda activate tensorflow_env
		1.3 : conda install matplotlib
		1.4 : conda install pandas
		1.5 : conda install keras
		1.6 : conda install opencv
		1.7 : conda install pygame
		1.8 : conda install mutagen
step 2: open anaconda navigator, change the value next to "Applications on" 
to tensorflow_env 
step 3: install spyder for it
step 4: open google drive link, to find the required data and other files.
step 5: now first run the trainer.py file
step 6: run the music_try.py file
step 7: and you have a working application of "Emotion based music player"

note: you can download kaggle dataset from, 
https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/data

it isn't needed as required files are already included.

note: change the directory path for songs, in music_try.py file