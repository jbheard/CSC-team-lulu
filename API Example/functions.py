import os, random
import flask

# Logic can be split up into different files (modules), 
# then used in your api
def get_random_image():
	return random.choice(os.listdir('./img'))
