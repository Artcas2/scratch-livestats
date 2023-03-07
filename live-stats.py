import os, time
import scratchattach as scratch3 # pip install scratchattach

# lists for encoding
chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "_"]
chars_maj = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

session = scratch3.Session("sessionid", username="your_username") # replace sessionid with your scratch token and your_username with your username
project_id = "your_project_id" # replace your_project_id with your project id
cloud = session.connect_cloud(project_id)
user = scratch3.get_user("your_username") # replace your_username with your username
project = session.connect_project(project_id)

def encode(text):
	result = ""
	for c in text:
		if c in chars:
			index = chars.index(c)
		elif c in chars_maj:
			index = chars_maj.index(c)
		else:
			return
		if index + 1 > 9:
			result += str(index + 1)
		else:
			result += "0" + str(index + 1)
	return result

time_var = 0 # time for status detector
cloud.set_var("TIME", 0)
print("Connected!")
while True:
	user.update()
	project.update()
	
	follower_count = user.follower_count()
	cloud.set_var("FOLLOWERS COUNT", follower_count)
	
	last_followers_list = user.followers(limit=6, offset=0)
	last_followers = ""
	for e in last_followers_list:
		tmp = encode(str(e)) + "99"
		last_followers += tmp
	
	cloud.set_var("LAST FOLLOWERS", last_followers)
	cloud.set_var("VIEWS", project.views)
	cloud.set_var("LOVES", project.loves)
	cloud.set_var("FAVORITES", project.favorites)
	
	time.sleep(1)
	time_var += 1
	cloud.set_var("TIME", time_var)
