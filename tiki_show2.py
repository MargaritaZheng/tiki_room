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

# START PLAYING BACKGROUND MUSIC
pygame.mixer.init()
pygame.mixer.music.load("tiki_room_audio_short.mp3")
pygame.mixer.music.play()

# INITIALIZE LED POSITIONS FOR EACH BIRD

# Jose = [8]
# Michael = [3]
# Pierre = [1]
# Fritz = [10]
# sides = [2,9]
# top = [4,5,6]
# flowers = [7]

# create dictionaries for each bird

Jose = {'led': 8, 'r':255, 'g':0, 'b':0}
Michael = {'led': 3, 'r':0, 'g':255, 'b':0}
Pierre = {'led': 1, 'r':0, 'g':0, 'b':255}
Fritz = {'led': 10, 'r':255, 'g':255, 'b':0}
# purple = {r:138, g:43, b:226}

# BEGIN SONG SEQUENCE
lpack.setbrightness:100
time.sleep(.3)

bird = Jose
lpack.setColor(bird['led'], bird['r'], bird['g'], bird['b'])
time.sleep(14.2)

bird = Michael
lpack.setColor(bird['led'], bird['r'], bird['g'], bird['b'])
time.sleep(8.5)

print("setColorToAll: %s" % lpack.setColorToAll(0, 0, 0))
print("turnOff: %s" % lpack.turnOff());

lpack.disconnect()
