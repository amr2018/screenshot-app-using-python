

from datetime import datetime
from tkinter import *
from PIL import Image, ImageTk, ImageGrab


# create screenshot function
def screansot():
	image = ImageGrab.grab()
	filename = datetime.now().strftime('%H%M%S')
	image.save(f' {filename}.jpg')



# create window
win = Tk()
win.geometry('400x100')
win.title('screenshot App')

# create sreenshot bt image
image_bt = Image.open('screenshot.png').resize((50, 50))
image_bt = ImageTk.PhotoImage(image_bt)

# create bt
screansot_bt = Button(image = image_bt, bd = 0, command = screansot)
screansot_bt.image = image_bt
screansot_bt.place(x = 160, y = 20)

win.mainloop()
