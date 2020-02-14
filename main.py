
import tkinter as tk
from tkSliderWidget import Slider

root = tk.Tk()

slider = Slider(root, width = 400, height = 60, min_val = -100, max_val = 100, init_lis = [-50,0,75], show_value = True)
slider.pack()
root.title("Slider Widget")
root.mainloop()

print(slider.getValues())
