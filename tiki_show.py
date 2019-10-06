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

# Jose = [8]
# Michael = [3]
# Pierre = [1]
# Fritz = [10]
# sides = [2,9]
# top = [4,5,6]
# flowers = [7]

# create alltogether function
def alltogether(time_diff):
    lpack.setSmooth(10)	# Tiny Cylone
    lpack.setColorToAll(0,0,0)
    top = [3, 4, 5, 6]
    bottom = [1, 10, 9, 8]
    left = [1, 2, 3]
    right = [6, 7, 8]
    on = [255, 0, 0]
    off = [0, 0, 0]
    lpack.setSmooth(45)

    lpack.setColor(top[0], on[0], on[1], on[2])
    lpack.setColor(bottom[0], on[0], on[1], on[2])
    for k in range (0, 3) :
        lpack.setColor(left[k], on[0], on[1], on[2])

    t_end = time.time() + time_diff - 0.45
    while time.time() < t_end:
        for i in range (1, 4) :
            lpack.setColor(top[i], random.randint(0,255), random.randint(0,255), random.randint(0,255))
            lpack.setColor(bottom[i], random.randint(0,255), random.randint(0,255), random.randint(0,255))
            if i == 3 :
                for n in range (0, 3) :
                    lpack.setColor(right[n], on[0], on[1], on[2])
            if i >= 1 :
                lpack.setColor(top[i-1], off[0], random.randint(0,255), off[2])
                lpack.setColor(bottom[i-1], random.randint(0,255), off[1], off[2])
                lpack.setColor(left[1], off[0], off[1], random.randint(0,255))
            time.sleep(0.2)
        for m in [2,1,0] :
            lpack.setColor(top[m], random.randint(0,255), random.randint(0,255), random.randint(0,255))
            lpack.setColor(bottom[m], random.randint(0,255), random.randint(0,255), random.randint(0,255))
            if m == 2 :
                lpack.setColor(right[1], off[0], off[1], off[2])
            elif m == 0 :
                lpack.setColor(left[1], on[0], random.randint(0,255), random.randint(0,255))
            lpack.setColor(top[m+1], off[0], off[1], off[2])
            lpack.setColor(bottom[m+1], off[0], off[1], off[2])
            time.sleep(0.2)
    lpack.setColorToAll(0, 0, 0)

def swing(time_df):
    lpack.setColorToAll(0,0,0)
    right = [1, 2, 3]
    top = [4, 5, 6, 7, 4, 5, 6, 7, 4, 5, 6, 7]
    left = [8, 9, 10]
    lpack.setSmooth(45)

    t_end = time.time() + time_diff - 0.45
    while time.time() < t_end:
        a = random.randint(0,255)
        b = random.randint(0,255)

        for i in range (1, 10):
            lpack.setColor(right[1], a, b, 0)
            lpack.setColor(left[1], a, b, 0)
            time.sleep(0.2)
            lpack.setColorToAll(0, 0, 0)

            lpack.setColor(top, a, b, 0)
            time.sleep(0.2)
            lpack.setColorToAll(0, 0, 0)

def finale(time_df):
    right = [1, 2, 3]
    top = [4, 5, 6, 7]
    left = [8, 9, 10]

    lag = time_df/4

    lpack.setColorToAll(0,0,0)
    lpack.setColor(1, a, b, 0)
    lpack.setColor(10, a, b, 0)
    time.sleep(lag)
    lpack.setColorToAll(0, 0, 0)
    lpack.setColor(2, a, b, 0)
    lpack.setColor(9, a, b, 0)
    time.sleep(lag)
    lpack.setColorToAll(0, 0, 0)
    lpack.setColor(3, a, b, 0)
    lpack.setColor(8, a, b, 0)
    time.sleep(lag)
    lpack.setColor(5, a, b, 0)
    lpack.setColor(6, a, b, 0)
    time.sleep(lag)
    lpack.setColorToAll(0, 0, 0)

def whistle(time_df):
    t_end = time.time() + time_df - 0.2
    while time.time() < t_end:
    	lpack.setSmooth(10)	# 4 basic flashes
    	lpack.setColorToAll(0,0,0)
    	time.sleep(0.1)
    	for k in range(0,10):
    		lpack.setColorToAll(255,255,255)
    		time.sleep(0.1);
    		lpack.setColorToAll(0,0,0)
    		time.sleep(0.1);
    	lpack.setColorToAll(0,0,0)

def sing(bird, time_df):
    lpack.setColor(bird['led'], bird['r'], bird['g'], bird['b'])
    time.sleep(time_df)
    lpack.setColorToAll(0, 0, 0)
    time.sleep(0.2)

# create dictionaries for each bird

Jose = {'led': 8, 'r':255, 'g':0, 'b':0}
Michael = {'led': 3, 'r':0, 'g':255, 'b':0}
Pierre = {'led': 1, 'r':0, 'g':0, 'b':255}
Fritz = {'led': 10, 'r':255, 'g':255, 'b':0}
# purple = {r:138, g:43, b:226}

# BEGIN SONG SEQUENCE
print("setColorToAll: %s" % lpack.setColorToAll(0, 0, 0))

# START PLAYING BACKGROUND MUSIC
pygame.mixer.init()
pygame.mixer.music.load("tiki_room_audio_short.mp3")
pygame.mixer.music.play()
music_start = time.time()

time.sleep(1.4)
# if time.time() == music_start + 0.35:
sing(Jose, 14.2)
sing(Michael, 8.5)
sing(Pierre, 10.2)
sing(Fritz, 14.1)
whistle(4)

alltogether(3.2)

sing(Jose, 3.3)

alltogether(5.1)

sing(Jose, 0.8)
sing(Pierre, 2.1)

alltogether(2.8)

sing(Jose, 9.8)

alltogether(6)

sing(Jose, 1.3)
sing(Pierre, 1.3)

alltogether(3.1)

sing(Michael, 4)
sing(Jose, 2.4)
sing(Pierre, 4.8)
sing(Fritz, 8.6)
sing(Jose, 6.5)
sing(Pierre, 2.8)
sing(Jose, 1.1)
sing(Pierre, 7.1)

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

sing(Jose, 10.7)

# recalculate the timings
alltogether(5.1)
sing(Michael, 1)
alltogether(5)
sing(Michael, 1)
alltogether(13.7)

finale(1.6)

sing(Jose, 1.5)
sing(Pierre, 3.9)
sing(Jose, 3)

print("setColorToAll: %s" % lpack.setColorToAll(0, 0, 0))
print("turnOff: %s" % lpack.turnOff());

lpack.disconnect()
