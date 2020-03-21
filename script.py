from pynput.keyboard import Key, Controller
import time

comments = "good"   # Enter your comments here
rating = 5          # 1=Strongly Disagree, 2=Disagree, 3=Neutral, 4=Agree, 5=Strongly Agree
wait = 3            # Time you need between running the program and selecting the faculty
type = 'External'   # Choose between Internal and External feedback

print("Amizone feedback tool (2019), By: Akshansh Kumar,AIIT")
print("Now Select a faculty for feedback, and give the first rating")
while (wait > 0):
    print("Select within:", wait, "Seconds")
    time.sleep(1)
    wait -= 1
keyboard = Controller()
time.sleep(1)

def fill(n):
    for i in range(n):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        for j in range(rating):
            keyboard.press(Key.left)
            keyboard.release(Key.left)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)

def yes_no():
    for i in range(3):
        for j in range(1):
            keyboard.press(Key.left)
            keyboard.release(Key.left)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)

def external_feedback():
    fill(3)
    fill(7)
    fill(6)
    fill(4)
    fill(4)
    yes_no()
    keyboard.type(comments)

def internal_feedback():
    fill(2)
    fill(7)
    fill(4)
    fill(2)
    fill(4)
    yes_no()
    keyboard.type(comments)

if(type=='External'):
    external_feedback()
elif(type=='Internal'):
    internal_feedback()
