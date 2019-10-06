import lightpack, time, pygame
lpack = lightpack.lightpack('127.0.0.1', 3636, [2,3,6,7,1,1,1,4,5,1] )
lpack.connect()

print("Lock: %s" % lpack.lock())
print("turnOn: %s" % lpack.turnOn())

print("LED map: %s" % lpack.getLeds())

num = int(lpack.getCountLeds())
print("Num leds: %s" % num)

print("Status: %s" % lpack.getStatus())
print("Profile: %s" % lpack.getProfile())
print("Profiles: %s" % lpack.getProfiles())
print("getAPIStatus: %s" % lpack.getAPIStatus())

pygame.mixer.init()
pygame.mixer.music.load("tiki_room_audio_short.mp3")
pygame.mixer.music.play()

for i in range(1, num+1):
    print("setColor%d: %s" % (i, lpack.setColor(i, 255, 0, 0)))
    time.sleep(0.1)
time.sleep(1)

for i in range(1, num+1):
    print("setColor%d: %s" % (i, lpack.setColor(i, 0, 255, 0)))
    time.sleep(0.1)
time.sleep(1)

lpack.setSmooth(10)	# Tiny Cylon
lpack.setColorToAll(0,0,0)
time.sleep(1)
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
l = 0
while l < 15 :
    for i in range (1, 4) :
        lpack.setColor(top[i], on[0], on[1], on[2])
        lpack.setColor(bottom[i], on[0], on[1], on[2])
        if i == 3 :
            for n in range (0, 3) :
                lpack.setColor(right[n], on[0], on[1], on[2])
        if i >= 1 :
            lpack.setColor(top[i-1], off[0], off[1], off[2])
            lpack.setColor(bottom[i-1], off[0], off[1], off[2])
            lpack.setColor(left[1], off[0], off[1], off[2])
        time.sleep(0.2)
    for m in [2,1,0] :
        lpack.setColor(top[m], on[0], on[1], on[2])
        lpack.setColor(bottom[m], on[0], on[1], on[2])
        if m == 2 :
            lpack.setColor(right[1], off[0], off[1], off[2])
        elif m == 0 :
            lpack.setColor(left[1], on[0], on[1], on[2])
        lpack.setColor(top[m+1], off[0], off[1], off[2])
        lpack.setColor(bottom[m+1], off[0], off[1], off[2])
        time.sleep(0.2)
    l += 1
lpack.setColorToAll(0,0,0)
time.sleep(5)

lpack.setSmooth(250)	# Random color fluid
lpack.setGamma(2.00)
lpack.setColorToAll(255, 255, 255)
ark= []
for i in range (0, 101) :
    n = i % 2
    if n == 0 :
        ark.append(0)
    else:
        ark.append(random.randint(200, 255))
random.shuffle(ark)
#print ark
while True :
    num = random.randint(1, 10)
    r = random.choice(ark)
    g = random.choice(ark)
    b = random.choice(ark)
    if num != 1 and num != 10 :
        lpack.setColor(num, r, g, b)
        time.sleep(random.uniform(0, 1))
        lpack.setColor(num-1, r, g, b)
        lpack.setColor(num+1, r, g, b)
    elif num == 1 :
        lpack.setColor(num+1, r, g, b)
        time.sleep(random.uniform(0, 1))
        lpack.setColor(num, r, g, b)
        lpack.setColor(num+2, r, g, b)
    elif num == 10 :
        lpack.setColor(num-1, r, g, b)
        time.sleep(random.uniform(0, 1))
        lpack.setColor(num, r, g, b)
        lpack.setColor(num-2, r, g, b)
    time.sleep(random.uniform(1, 3))

print("setColorToAll: %s" % lpack.setColorToAll(127, 127, 127))
time.sleep(1)

print("setColorToAll: %s" % lpack.setColorToAll(0, 0, 0))
print("turnOff: %s" % lpack.turnOff());

lpack.disconnect()
