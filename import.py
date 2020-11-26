import tkinter 

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import ( FigureCanvasTkAgg, NavigationToolbar2Tk)

root = tkinter.Tk()

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

fig = Figure(figsize=(5, 4), dpi=100)

fig.add_subplot(111).plot(x, y)

canvas = FigureCanvasTkAgg(fig, master=root)

canvas.draw()

canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)

toolbar.update()

canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

root.mainloop()