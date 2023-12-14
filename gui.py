import tkinter as tk
from tkinter import *
import subprocess
from PIL import ImageTk, Image


def run_script():
    script_path = "C:/Users/prate/OneDrive/Desktop/motion detection/pro/main.py"   
    subprocess.run(["python", script_path])

def run_video():
    script_path = "C:/Users/prate/OneDrive/Desktop/motion detection/pro/video.py"   
    subprocess.run(["python", script_path])    
    
def exit_script():
    window.destroy()

window = tk.Tk()
window.title("Motion Detection")

window.geometry("700x600")
window.config(bg="khaki")


window.attributes('-fullscreen',True)

frame = Frame(window, width=100, height=500)
frame.pack()
frame.place(anchor='e', relx=1, rely=0.2)

image=Image.open("C:/Users/prate/OneDrive/Desktop/motion detection/pro/p1.jpg")
resize_image = image.resize((1600, 1600))

img = ImageTk.PhotoImage(resize_image)


label = Label(frame, image = img)
label.pack()


l=tk.Label(window,text="Select Run button to Execute Webcam",height=5,width=60,bg="Black",fg="White",bd=6)
l.pack(pady=10,side="top")
l.config(font=("Algerian",14))



run_button = tk.Button(window, text="Run Webcam",height=5,width=20,bg="Yellow", command=run_script,bd=8)
run_button.pack(pady=10,padx=40)
run_button.config(font=("Courier",14))

l=tk.Label(window,text="Select Run button to Execute a vedio",height=5,width=60,bg="Black",fg="White",bd=6)
l.pack(pady=10,side="top")
l.config(font=("Algerian",14))

run_button = tk.Button(window, text="Run Video",height=5,width=20,bg="Yellow", command=run_video,bd=8)
run_button.pack(pady=10,padx=40)
run_button.config(font=("Courier",14))

l=tk.Label(window,text="Select Exit button to Shut the System",height=5,width=60,bg="Black",fg="White",bd=6)
l.pack(pady=10)
l.config(font=("Algerian",14))

btn_stop = tk.Button(window, text="Stop",height=5,width=20,bg="Yellow", command=exit_script,bd=8)
btn_stop.pack(pady=10)
btn_stop.config(font=("Courier",14))


window.mainloop()
