import pynput
from pynput.keyboard import Key, Listener


count = 0
keys = []
world=""
def on_press(key):
    print(key)
    word=word+key
    
    print("pressed")
    global keys, count
    keys.append(str(key))
    print(keys)
    count += 1
    
    
def on_release(key):
    if key == Key.esc:
        return


with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()