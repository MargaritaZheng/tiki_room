import lightpack, time, pygame, random

# CONNECT TO LOCALHOST
lpack = lightpack.lightpack('127.0.0.1', 3636, [2,3,6,7,1,1,1,4,5,1] )
lpack.connect()

print("Lock: %s" % lpack.lock())
print("turnOn: %s" % lpack.turnOn())

print("LED map: %s" % lpack.getLeds())

# COUNT NUMBER OF LEDs to control
num = int(lpack.getCountLeds())
print("Num leds: %s" % num)

print("Status: %s" % lpack.getStatus())
print("Profile: %s" % lpack.getProfile())
print("Profiles: %s" % lpack.getProfiles())
print("getAPIStatus: %s" % lpack.getAPIStatus())

# INITIALIZE LED POSITIONS FOR EACH BIRD

# create alltogether function
def alltogether(time_diff):
    lpack.setSmooth(10)	# Tiny Cylone
    lpack.setColorToAll(0,0,0)
    left = [10, 9, 8, 10]
    top = [7,6,5,4,7]
    right = [3,2,1,3]

    lpack.setSmooth(45)

    a = random.randint(0,255)
    b = random.randint(0,255)
    c = random.randint(0,255)

    t_end = time.time() + time_diff - 0.75
    while time.time() < t_end:
        for i in range(1, 3) :
            lpack.setColor(left[i], c, a, b)
            lpack.setColor(right[i], a, b, c)
            if i == 3 :
                for n in range (0, 3) :
                    lpack.setColor(right[n], a, 0, 0)
            if i >= 1 :
                lpack.setColor(top[i-1], 0, c, 0)
                lpack.setColor(top[i-1], b, 0, 0)
                lpack.setColor(left[1], 0, 0, c)
            time.sleep(0.2)
        for m in [2,1,0] :
            lpack.setColor(left[m], a, b, c)
            lpack.setColor(right[m], c, a, b)
            if m == 2 :
                lpack.setColor(right[1], c, a, 0)
                # lpack.setColor(left[0], c, a, 0)
            elif m == 0 :
                lpack.setColor(left[1], 0, a, c)

            lpack.setColor(left[m+1], b, c, 0)
            lpack.setColor(right[m+1], a, 0, b)
            time.sleep(0.2)
    lpack.setColorToAll(0, 0, 0)

def swing(time_df):
    lpack.setColorToAll(0,0,0)
    lpack.setSmooth(45)

    t_end = time.time() + time_df - 0.65
    while time.time() < t_end:
        a = random.randint(0,255)
        b = random.randint(0,255)

        lpack.setColor(1, a, b, 0)
        lpack.setColor(10, a, b, 0)
        time.sleep(0.3)
        lpack.setColorToAll(0, 0, 0)

        lpack.setColor(4, a, b, 0)
        lpack.setColor(5, a, b, 0)
        lpack.setColor(6, a, b, 0)
        lpack.setColor(7, a, b, 0)
        time.sleep(0.3)
        lpack.setColorToAll(0, 0, 0)

def finale():

    a = 255
    b = 200

    lpack.setColorToAll(0,0,0)
    lpack.setColor(1, a, b, 0)
    lpack.setColor(10, a, b, 0)
    time.sleep(0.25)
    lpack.setColorToAll(0, 0, 0)
    lpack.setColor(2, b, a, 0)
    lpack.setColor(9, b, a, 0)
    time.sleep(0.32)
    lpack.setColorToAll(0, 0, 0)
    lpack.setColor(3, 0, a, b)
    lpack.setColor(8, 0, a, b)
    time.sleep(0.31)
    lpack.setColor(5, 0, b, a)
    lpack.setColor(6, 0, b, a)
    time.sleep(0.93)
    lpack.setColorToAll(0, 0, 0)

def whistle(time_df):
    t_end = time.time() + time_df - 0.2
    while time.time() < t_end:
    	lpack.setSmooth(50)	# 4 basic flashes
    	lpack.setColorToAll(0,0,0)
    	time.sleep(0.1)
    	for k in range(0,10):
    		lpack.setColorToAll(150,150,150)
    		time.sleep(0.15);
    		lpack.setColorToAll(0,0,0)
    		time.sleep(0.15);
    	lpack.setColorToAll(0,0,0)

def sing(bird, time_df):
    lpack.setColor(bird['led'], bird['r'], bird['g'], bird['b'])
    time.sleep(time_df)
    lpack.setColorToAll(0, 0, 0)
    # time.sleep(0.1)

# create dictionaries for each bird

Jose = {'led': 8, 'r':255, 'g':255, 'b':255}
Michael = {'led': 3, 'r':0, 'g':255, 'b':0}
Pierre = {'led': 1, 'r':0, 'g':0, 'b':255}
Fritz = {'led': 10, 'r':255, 'g':255, 'b':0}

# BEGIN SONG SEQUENCE
print("setColorToAll: %s" % lpack.setColorToAll(0, 0, 0))

# START PLAYING BACKGROUND MUSIC
pygame.mixer.init()
pygame.mixer.music.load("two_track_stereo_Jose_v2.mp3")
# pygame.mixer.music.load("tiki_room_audio_short.mp3")
pygame.mixer.music.play()

# ind = 1
# while ind == 1:
#     pos = pygame.mixer.music.get_pos()
#     if pos > 1000:
#         ind = 2
time.sleep(.5)
sing(Jose, 14.2)
sing(Michael, 8.5)
sing(Pierre, 10.2)
sing(Fritz, 13.8)
sing(Michael, 3.4)

whistle(3.2)

sing(Jose, 3.3)

alltogether(5.1)

sing(Jose, 0.8)
sing(Pierre, 2.1)

alltogether(2.8)

sing(Jose, 9.8) # Welcome to our tropical hideaway

alltogether(6) # ALLTOGETHER!

sing(Jose, 1.3)
sing(Pierre, 1.3)

alltogether(2.8)

sing(Michael, 4) # I sing so beautifully, I should sing solo
sing(Jose, 2.4)
sing(Pierre, 4.8)
sing(Fritz, 8.6)
sing(Jose, 6.5)
sing(Pierre, 2.7) # because of their claws?
sing(Jose, 1.1)
sing(Pierre, 7)

swing(5)

sing(Jose, 10.7)
alltogether(5.2)
sing(Jose, 1.4)
sing(Pierre, 1.4)

alltogether(2.6)

sing(Michael, 10.7)

alltogether(5.2)

sing(Jose, 1.4)
sing(Pierre, 1.4)

alltogether(2.7)

sing(Jose, 10.7) # All my magnificent produc-ti-on is yet to come

# recalculate the timings
alltogether(5.1)
sing(Michael, 0.6)
alltogether(4.7)
sing(Michael, 1)
alltogether(9.8) # something is running for too long down here

finale()

sing(Michael, 2.8)
sing(Jose, 1.5)
sing(Pierre, 3.9)
sing(Jose, 4)

print("setColorToAll: %s" % lpack.setColorToAll(0, 0, 0))
print("turnOff: %s" % lpack.turnOff());

lpack.disconnect()
    # else:
    #     continue
