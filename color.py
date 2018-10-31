from phue import Bridge
import time 
import sys
import colorsys

ip ='192.168.2.3'
connect = False

#check in hue connect 
try:
    b= Bridge('192.168.2.3')
#b = Bridge('bridge')
    connect = True
    print("Connection to bridhe sucessful")

except ConnectionError:
    print("Could not connect to hue bridge")
    print("Waiting for pairing button to be press")


#fail to connection hue bridge 
while not connect:
    try:
        b = Bridge(ip)
        print("\nConnection to bridge successful")
        connect = True
    except ConnectionError:
        print(".", end='')
        sys.stdout.flush()
        time.sleep(1)

lights = b.lights

#change color class
#class change_color:
def wine_color():
    rgb = [127,0,127]
    rgb[0] = rgb[0]/254
    rgb[1] = rgb[1]/254
    rgb[2] = rgb[2]/254

    r = rgb[0] / (rgb[0] + rgb[1] + rgb [2])
    g = rgb[1] / (rgb[0] + rgb[1] + rgb [2])
    lights[0].on = True
    lights[0].brightness = 60
    lights[0].xy =[r,g]

#green_color 薄緑
def green_color():
    rgb = [103,228,126]
    rgb[0] = rgb[0]/254
    rgb[1] = rgb[1]/254
    rgb[2] = rgb[2]/254

    r = rgb[0] / (rgb[0] + rgb[1] + rgb [2])
    g = rgb[1] / (rgb[0] + rgb[1] + rgb [2])
    b = rgb[2] / (rgb[0] + rgb[1] + rgb [2])


    #for light in range(10):
    lights[5].on = True
    lights[5].brightness = 220
    lights[5].xy =[r,g]


#blue_color aquamarin color  
def blue_color():
    rgb = [127,200,255]
    rgb[0] = rgb[0]/254
    rgb[1] = rgb[1]/254
    rgb[2] = rgb[2]/254

    r = rgb[0] / (rgb[0] + rgb[1] + rgb [2])
    g = rgb[1] / (rgb[0] + rgb[1] + rgb [2])
    b = rgb[2] / (rgb[0] + rgb[1] + rgb [2])
 
    for light in range(7):
        lights[light].on = True
        lights[light].brightness = 180
        lights[light].xy =[r,b]

#
#def test_color():
#    lights[1].on = True
#    lights[1].hue = 5000
#    lights[1].brightness = 90
#    lights[1].saturation = 120




#wine_color();
#green_color();
blue_color();

