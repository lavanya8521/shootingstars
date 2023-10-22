# Coursework 2 Game -- Shooting Stars
# Screen resolution: 1920 x 1080
from tkinter import Tk, messagebox, Button, Label
from tkinter import Canvas, Toplevel, PhotoImage, Frame, Text
from PIL import Image, ImageTk
from random import randint
from time import sleep
from threading import Thread, Timer


def leftKey(event):
	'''Tank moves if left key pressed'''
	global tank_on_screen
	canvas.move(tank_on_screen, -20, 0)


def rightKey(event):
	'''Tank moves if right key pressed'''
	global tank_on_screen
	canvas.move(tank_on_screen, 20, 0)


def upKey(event):
	'''Tank moves if up key pressed'''
	global tank_on_screen
	canvas.move(tank_on_screen, 0, -20)


def downKey(event):
	'''Tank moves if up down pressed'''
	global tank_on_screen
	canvas.move(tank_on_screen, 0, 20)


def shoot(event):
	'''Creates a bullet when the space bar is pressed'''
	global bullet
	global new_bullet
	pos = canvas.coords(tank_on_screen)
	bullet = canvas.create_rectangle(pos[0]-0.5, pos[1]-20, pos[0]+0.5, pos[1]-40)
	new_bullet = True


def double(event):
	'''Cheat Code: Doubles score'''
	global once
	global score
	if once:
		score = score * 2
		once = False
	canvas.itemconfigure(scoretext, text="Score:" + str(score))


def slow(event):
	'''Cheat code: Slows down falling objects for 5 seconds'''
	global times
	global speed
	global saved_speed
	if times <= 5:
		saved_speed = speed
		speed = 0.5
		t = Timer(5.0, restore_speed)
		t.start()
		times = times + 1


def add100(event):
	'''Cheat code: Adds 100 to the score'''
	global once
	global score
	if once:
		score = score  + 100
		once = False
	canvas.itemconfigure(scoretext, text="Score:" + str(score))



def boss_key(event):
	'''Boss key: Displays an image of a screenshot in a new window'''
	global boss_keys
	global stop
	stop = True
	bosskey = new_window()
	bosskey_screen = Canvas(bosskey, width=1600, height=900)
	bosskey_screen.pack()
	boss_keys = bosskey_screen.create_image(700, 500, image=bosskey_image)
	bosskey_screen.update()
	gamescreen.destroy()
	

def restore_screen(event):
	'''Opens a new window to continue game'''
	global restore
	restore = True
	game_screen()

def restore_speed():
	'''Retains speed of falling objects'''
	global speed
	speed = saved_speed


def configure_window():
	'''Opens the window of the main screen with the relevant settings'''
	window = Tk()

	window.geometry("1400x1080")
	window.configure(background="#101724")
	window.title("S H O O T I N G  S T A R S")
	return(window)


def new_window():
	'''Creates a new window that would open on top of the main window'''
	window = Toplevel()
	window.title("S H O O T I N G  S T A R S")
	window.geometry("1920x1080")
	window.configure(background="#101724")
	return(window)


def home_screen(window):
	'''Home screen with the relevant buttons linking to other windows'''
	title = Label(window, text="Shooting Stars", font=("Impact", 50), background="#101724")
	title.place(x=595, y=200)
	instructions = Button(window, text="How to Play", font=("Impact", 25), command=lambda: instructions_screen())
	instructions.place(x=650, y=300)
	new_game = Button(window, text="New Game", font=("Impact", 25), command=lambda: game_screen())
	new_game.place(x=655, y=400)
	cont_game = Button(window, text="Continue Game", font=("Impact", 25), command=lambda: cont())
	cont_game.place(x=630, y=500)
	leaderboard = Button(window, text="Leaderboard", font=("Impact", 25), command=lambda: leaderboard_screen())
	leaderboard.place(x=645, y=600)
	settings = Button(window, text="Settings", font=("Impact", 25), command=lambda: settings_screen())
	settings.place(x=670, y=700)
	userpage = Button(window, text="User", font=("Impact", 15), command=lambda: user_screen())
	userpage.place(x=1300, y=20)


def settings_screen():
	'''Settings screen where movement keys can be changed'''
	global left
	global right
	global up
	global down
	set_screen = new_window()
	title = Label(set_screen, text="Settings", font=("Impact", 50), background="#101724")
	title.place(x=595, y=100)

	left_label = Label(set_screen, text="Left Key", font=("Impact", 20), background="#101724")
	left_label.place(x=640, y=270)
	left_box = Text(set_screen, height=1, width=20, bg='#FCF5E0', fg='black', font=("Impact", 20))
	left_box.place(x=570, y=300)

	right_label = Label(set_screen, text="Right Key", font=("Impact", 20), background="#101724")
	right_label.place(x=640, y=370)
	right_box = Text(set_screen, height=1, width=20, bg='#FCF5E0', fg='black', font=("Impact", 20))
	right_box.place(x=570, y=400)

	up_label = Label(set_screen, text="Up Key", font=("Impact", 20), background="#101724")
	up_label.place(x=640, y=470)
	up_box = Text(set_screen, height=1, width=20, bg='#FCF5E0', fg='black', font=("Impact", 20))
	up_box.place(x=570, y=500)
	
	down_label = Label(set_screen, text="Down Key", font=("Impact", 20), background="#101724")
	down_label.place(x=640, y=570)
	down_box = Text(set_screen, height=1, width=20, bg='#FCF5E0', fg='black', font=("Impact", 20))
	down_box.place(x=570, y=600)
	
	set_keys = Button(set_screen, text="Set Keys", font=("Impact", 25), command=lambda: setting_keys(left_box, right_box, up_box, down_box))
	set_keys.place(x=625, y=750)

	back = Button(set_screen, text="Back", font=("Impact", 15), command=lambda: set_screen.destroy())
	back.place(x=1300, y=20)


def setting_keys(left_box, right_box, up_box, down_box):
	'''Retreiving the user's input on the setting page of the keys'''
	global left
	global right
	global up
	global down
	left = left_box.get("1.0", "end-1c")
	right = right_box.get("1.0", "end-1c")
	up = up_box.get("1.0", "end-1c")
	down = down_box.get("1.0", "end-1c")

def cont():
	'''Opening a new game screen to continue playing'''
	global restore
	restore = True
	game_screen()

def leaderboard_screen():
	'''Leaderboard window that shows the top 5 scores'''
	leaderboard = new_window()
	title = Label(leaderboard, text="Leaderboard", font=("Impact", 50), background="#101724")
	title.place(x=600, y=20)
	back = Button(leaderboard, text="Back", font=("Impact", 15), command=lambda: leaderboard.destroy())
	back.place(x=1300, y=20)
	file = open("Scoreboard.txt", "r")
	readfile = file.readlines()
	sortedData = sorted(readfile, reverse=True)
	ranks = []
	for i in range(5):
		try:
			line = sortedData[i]
		except:
			line = "0:       "
		top_score = line.partition(":")[0]
		top_name = line.partition(":")[2]
		ranks.append(Label(leaderboard, text=(str(i + 1)+"               "+"       "+str(top_name)), font=("Impact", 40), background="#101724"))
		score = Label(leaderboard, text=top_score, font=("Impact", 40), background="#101724")
		y = (100 * (i + 1)) + 100
		ranks[i].place(x=400, y=y)
		score.place(x=900, y=y)
	file.close()


def instructions_screen():
	'''Instructions screen on how to play the game'''
	instructions = new_window()
	title = Label(instructions, text="How To Play", font=("Impact", 50), background="#101724")
	title.place(x=625, y=20)
	texts = """ The aim of the game is to not let the stars reach the bottom of the screen.
				The satellites minus 20 points from the score if they are hit.
				The moon is worth an extra 100 points if hit.
				The user's name must be submitted via the user button before playing.
				The 'b' key is used as the boss key.
				The space bar is to shoot.
				The arrow keys are the default ways to move on screen but this can be changed in settings."""
	instruct = Label(instructions, text=texts, font=("Impact", 20), background="#101724")
	instruct.place(x=200, y=200)

	back = Button(instructions, text="Back", font=("Impact", 15), command=lambda: instructions.destroy())
	back.place(x=1300, y=20)

	flower = PhotoImage(file="flower.png")
	flower_image = Label(instructions, image = flower).grid(row = 100, column = 100)

def user_screen():
	'''Screen where the user inputs their name'''
	global user_input
	userscreen = new_window()
	name = Label(userscreen, text="Name", font=("Impact", 50), background="#101724")
	name.place(x=625, y=200)
	user_input = Text(userscreen, height=5, width=50, bg='#FCF5E0', fg='black', font=("Impact", 20))
	user_input.place(x=420, y=300)
	set_name = Button(userscreen, text="Set Name", font=("Impact", 25), command=lambda: set_name())
	set_name.place(x=625, y=450)
	back = Button(userscreen, text="Back", font=("Impact", 15), command=lambda: userscreen.destroy())
	back.place(x=1300, y=20)


def set_name():
	'''Sets the name of the user'''
	global name
	if 'name' not in globals():
		name = user_input.get("1.0", "end-1c")


def game_screen():
	'''Main game screen with the canvas'''

	#Global variables to use across functions
	global star
	global canvas
	global score
	global new_bullet
	global stop
	global speed
	global moon
	global scoretext
	global once
	global times
	global gamescreen
	global name

	num_of_falling = 5
	new_bullet = False

	gamescreen = new_window()

	if restore:
		file = open("Save_game.txt", "r")
		score_line = file.readline()
		score = int(score_line.partition(":")[2])
		name_line = file.readline()
		names = str(name_line.partition(":")[2])
		name = names.strip()
		speed_line = file.readline()
		speed = float(speed_line.partition(":")[2])
		once_line = file.readline()
		once = bool(once_line.partition(":")[2])
		times_line = file.readline()
		times = float(times_line.partition(":")[2])
		file.close()
	
	else:
		score = 0
		speed = 1.0
		once = True
		times = 1


	canvas = Canvas(gamescreen, width=1600, height=900)
	canvas.config(bg='#101724')
	canvas.pack()
	scoretext = canvas.create_text(1200, 10, text="Score:" + str(score), fill='white', font=("Impact", 15), anchor="nw")

	# Binding keys for the game
	canvas.bind('<'+left+'>', leftKey)
	canvas.bind('<'+right+'>', rightKey)
	canvas.bind('<'+up+'>', upKey)
	canvas.bind('<'+down+'>', downKey)
	canvas.bind('<space>', shoot)
	canvas.bind('<d>', double)
	canvas.bind('<e>', slow)
	canvas.bind('<b>', boss_key)
	canvas.bind('<q>', add100)
	canvas.focus_set()

	# star image from https://www.freepnglogos.com/pics/falling
	img = Image.open("star.png")
	resized_image = img.resize((100, 100))
	star = ImageTk.PhotoImage(resized_image)

	# image made on paint
	global tank
	img = Image.open("tank.png")
	resized_image = img.resize((50, 50))
	tank = ImageTk.PhotoImage(resized_image)

	# moon image from www.canva.com
	global moon_image
	img = Image.open("moon.png")
	resized_image = img.resize((100, 100))
	moon_image = ImageTk.PhotoImage(resized_image)

	# moon image from www.canva.com
	global satellite_image
	img = Image.open("satellite.png")
	resized_image = img.resize((100, 100))
	satellite_image = ImageTk.PhotoImage(resized_image)

	# image was a screenshot
	global bosskey_image
	img = Image.open("bosskey.png")
	resized_image = img.resize((1500, 1000))
	bosskey_image = ImageTk.PhotoImage(resized_image)

	global satellite
	satellite = 0

	global falling
	falling = []
	create_falling(canvas)

	move_tank(canvas)

	pause = Button(gamescreen, text="Pause", font=("Impact", 15), command=lambda: pause_screen())
	pause.place(x=1300, y=5)

	# Make all the falling objects fall down
	bullets = []

	stop = False
	finish = False

	while not stop:
		for i in range(1, len(falling) + 1):
			if i > len(falling):
				break
			if len(falling) == 1:
				create_falling(canvas)
			pos = canvas.coords(falling[i - 1])
			y = pos[1]
			if pos[1] > 760 and falling[i-1] != satellite:
				stop = True
				canvas.create_text(650, 500, fill='white', font=('Impact', 50), text='Game Over!')
			canvas.move(falling[i - 1], 0, speed)
			if new_bullet:
				bullets.append(bullet)
				new_bullet = False
			for b in range(0, len(bullets)):
				if b > len(bullets) - 1:
					b = len(bullets) - 1

				canvas.move(bullets[b], 0, -20)
				canvas.update()

				bullet_pos = canvas.coords(bullets[b])
				if bullet_pos[3] < 0:
					bullets.pop(b)

				falling_coords = [pos[0] - 50, pos[1] - 50, pos[0] + 50, pos[1] + 50]

				if overlapping(bullet_pos, falling_coords):
					next_level()
					if 'moon' not in globals():
						moon = 0

					if falling[i - 1] == moon:
						score = score + 100
					elif falling[i-1] == satellite:
						score = score - 20
					else:
						score = score + 10
					comparing_star = falling[i - 1]
					canvas.itemconfigure(scoretext, text="Score:" + str(score))
					canvas.delete(comparing_star)
					falling.pop(i - 1)

					canvas.update()

				sleep(0.0005)

		canvas.update()

	finish_game()


def create_satellites():
	'''Create the satellite images'''
	x = randint(100, 1400)
	satellite = canvas.create_image(x, 30, image=satellite_image)
	return (satellite)



def next_level():
	'''Checking the score to see if they match the conditions to make the game harder'''
	global speed
	global moon
	global satellite

	if score % 50 == 0 and score != 0:
		speed = speed + 0.5

	if score % 100 == 0 and score != 0:
		moon = create_moon()
		falling.append(moon)

	if score > 150 and score % 60 == 0:
		satellite = create_satellites()
		falling.append(satellite)


def create_moon():
	'''Creates moon image and places on screen'''
	x = randint(100, 1400)
	moon = canvas.create_image(x, 60, image=moon_image)
	return (moon)


def move_tank(canvas):
	'''Creates tank image and places on screen'''
	global tank_on_screen
	tank_on_screen = canvas.create_image(60, 500, image=tank)
	position = canvas.coords(tank_on_screen)
	canvas.update()


def create_falling(canvas):
	'''Create all the  stars and adds to list'''
	global falling
	for i in range(num_of_falling):
	 	x = randint(10, 1400)
	 	y = randint(0, 60)
	 	falling.append(canvas.create_image(x, y, image=star))


def overlapping(a, b):
	'''Check to see if there has been a collision between objects'''
	if a[0] < b[2] and a[2] > b[0] and a[1] < b[3] and a[3] > b[1]:
		return True
	else:
		return False


def finish_game():
	'''Writing to file once the game finishes'''
	file = open("Scoreboard.txt", "a")
	file.write(str(score) + ": " + name + "\n")
	file.close()

	file = open("Save_game.txt", "w")
	file.write("Score:"+str(score)+ "\n")
	file.write("Name:"+str(name) + "\n")
	file.write("Speed:"+str(speed)+ "\n")
	file.write("Once:"+str(once) + "\n")
	file.write("Times:"+str(times) + "\n")
	file.close()


def unpauses():
	'''Restoring gamescreen to unpause game'''
	global restore
	restore = True
	pausescreen.destroy()
	game_screen()


def pause_screen():
	'''Pause screen'''
	global stop
	global pausescreen
	stop = True
	pausescreen = new_window()
	pause_text = Label(pausescreen, text="Game Paused", font=("Impact", 50), background="#101724")
	pause_text.place(x=625, y=200)
	unpause = Button(pausescreen, text="Unpause", font=("Impact", 20), command=lambda: unpauses())
	unpause.place(x=700, y=300)
	save = Button(pausescreen, text='Save Game and Exit', font=("Impact", 20), command=lambda: save_game())
	save.place(x=690, y=370)
	gamescreen.destroy()


def save_game():
	finish_game()
	window.destroy()


# Main code
window = configure_window()
star = None
tank = None
rank = None
restore = False

left = "Left"
right = "Right"
up = "Up"
down = "Down"

num_of_falling = 5

home_screen(window)

direction = 'right'

window.mainloop()
