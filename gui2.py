import tkinter as tk
import subprocess 
from PIL import ImageTk, Image


def run_script():
    script_path = "C:/Users/prate/OneDrive/Desktop/motion detection/pro/main.py"   
    subprocess.run(["python", script_path])

def run_video():
    script_path = "C:/Users/prate/OneDrive/Desktop/motion detection/pro/video.py"   
    subprocess.run(["python", script_path])    
    
def exit_script():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Tkinter GUI with Labels and Buttons")

root.config(bg="pink")


root.attributes('-fullscreen',True)
# Create three labels
label1 = tk.Label(root, text="Select to run webcam ",height=8,width=70)
label1.pack(pady=10,side="top")
label1.config(font=("Algerian",14),fg="White",bg="Black")

label2 = tk.Label(root, text="Select to run sample video ",height=8,width=70)

label2.config(font=("Algerian",14),fg="White",bg="Black")
label3 = tk.Label(root, text="Select to exit the console ",height=8,width=70)

label3.config(font=("Algerian",14),fg="White",bg="Black")
# Create three buttons, each associated with a label
button1 = tk.Button(root, text="Run Webcam",bg="Yellow",height=5,width=50, command=run_script,bd=8)
button2 = tk.Button(root, text="Run Video",height=5,width=50,bg="Yellow", command=run_video,bd=8)
button3 = tk.Button(root,  text="Stop",height=5,width=50,bg="Yellow", command=exit_script,bd=8)

# Arrange widgets using the grid layout manager
label1.grid(row=0, column=0, padx=20, pady=40)
button1.grid(row=0, column=1, padx=20, pady=40)

label2.grid(row=1, column=0, padx=30, pady=40)
button2.grid(row=1, column=1, padx=30, pady=40)

label3.grid(row=2, column=0, padx=30, pady=40)
button3.grid(row=2, column=1, padx=30, pady=40)

# Start the Tkinter event loop
root.mainloop()
