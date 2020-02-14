# tkSliderWidget
Implementation of a slider widget using tkinter, multiple slider supported

for an example see:
`main.py`

![Slider](http://i.ibb.co/zRYP9Fv/Annotation-2020-02-13-172914.png)

```python
	
import tkinter as tk
from tkSliderWidget import Slider

root = tk.Tk()

slider = Slider(root, width = 400, height = 60, min_val = -100, max_val = 100, init_lis = [-50,0,75], show_value = True)
slider.pack()
root.title("Slider Widget")
root.mainloop()

print(slider.getValues())

```
