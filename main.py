
# import tkinter
import tkinter as tk
from UI.main_window import MainWindow
import tkinter.font as tkfont
from ttkthemes import ThemedTk

# # import the controller object
# # create a root window without the title argument
# root = tk.Tk()
# # set the title of the window to "Video Player"
# root.title("Video Player")
# # create an instance of the MainWindow class
# app = MainWindow(root)
# # pack the app frame
# app.pack()
# # start the main loop of the root window
# app.mainloop()

# pack the app frame
# start the main loop of the root window
 # Create a themed window with the desired theme name
window = ThemedTk(theme="arc")
# Create a style object
app = MainWindow(window)
app.pack()
app.mainloop()
