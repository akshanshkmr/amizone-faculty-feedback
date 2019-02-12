from pynput.keyboard import Key, Controller
import time

comments="good"    #Enter your comments here 
rating=3           #1=Strongly Disagree, 2=Disagree, 3=Neutral, 4=Agree, 5=Strongly Agree
wait=3             #Time you need between running the program and selecting the faculty

print("Amizone feedback tool (2019), By: Akshansh Kumar,AIIT")
print("Now Select a faculty for feedback, and give the first rating")
while(wait>0):
    print("Select within:",wait,"Seconds")
    time.sleep(1)
    wait-=1

keyboard=Controller()
time.sleep(1)
for i in range(2):
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    for j in range(rating):
        keyboard.press(Key.left)
        keyboard.release(Key.left)

keyboard.press(Key.tab)
keyboard.release(Key.tab)

for i in range(7):
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    for j in range(rating):
        keyboard.press(Key.left)
        keyboard.release(Key.left)

keyboard.press(Key.tab)
keyboard.release(Key.tab)

for i in range(4):
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    for j in range(rating):
        keyboard.press(Key.left)
        keyboard.release(Key.left)


keyboard.press(Key.tab)
keyboard.release(Key.tab)

for i in range(2):
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    for j in range(rating):
        keyboard.press(Key.left)
        keyboard.release(Key.left)

keyboard.press(Key.tab)
keyboard.release(Key.tab)

for i in range(4):
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    for j in range(rating):
        keyboard.press(Key.left)
        keyboard.release(Key.left)

for i in range(4):
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.press(Key.down)
    keyboard.release(Key.down)

keyboard.press(Key.tab)
keyboard.release(Key.tab)
    
keyboard.type(comments)

