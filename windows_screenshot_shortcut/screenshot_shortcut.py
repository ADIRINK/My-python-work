import keyboard
from customtkinter import *
from pystray import MenuItem as item
import pystray
from PIL import Image

win = CTk()
win.title("Windows screenshot")
win.geometry("300x200")

def shortcut():
    keyboard.press_and_release('win+shift+s')

def quit_window(icon):
    icon.stop()
    win.destroy()

def show_window(icon):
    icon.stop()
    win.after(0, win.deiconify())

def hide_window():
    win.withdraw()
    image = Image.open("favicon.ico")
    menu = (item('Show', show_window), item('Quit', quit_window))
    icon = pystray.Icon('name', image, "My System Tray Icon", menu)
    icon.run()

    while True:
        try:
          if keyboard.is_pressed('insert'):
              shortcut()
              print('Key pressed!')
              break

        except:
           break


win.protocol('WM_DELETE_WINDOW', hide_window)
win.mainloop()
