from tkinter import *
from tkinter.ttk import Scale 
from tkinter import colorchooser,messagebox,filedialog
import PIL.ImageGrab as ImageGrab

class Paint():
  def __init__(self,window):
    self.window = window
    self.fill_colour = "white"
    self.canvas = Canvas(self.window, bg=self.fill_colour, bd=5, relief=GROOVE, height=450, width=700,cursor="circle")
    self.canvas.place(x=80,y=50)
    self.pen_colour = "black"
    self.x, self.y = 0,0
    self.window.title("Python Paint")
    self.window.geometry("800x520")
    self.window.configure(bg="white")
    self.window.resizable(0,0)
    
    self.colour_frame = LabelFrame(self.window,font= ("arial" ,15), bg="white")
    self.colour_frame.place(x=4, y=0, width=783, height=45)

    colourlist = ["black", "grey", "brown", "red", "orange", "yellow","lawn green","green", "cyan","blue", "purple", "magenta"]
    Button(self.colour_frame, bg="white", height=2, width=7, command=self.choose_colour).grid(row=1, column=len(colourlist)+1)
    for i in range(len(colourlist)):
      Button(self.colour_frame,bg=colourlist[i], height=2,width=7, command=lambda c = colourlist[i]: self.select_colour(c)).grid(row=1,column=i)

    self.eraser_button = Button(self.window, text="Eraser", bd=4, bg="white", command=self.eraser, width=9)
    self.eraser_button.place(x=0, y=50)

    self.clear_button = Button(self.window, text="Clear", bd=4, bg="white", command=self.clear, width=9)
    self.clear_button.place(x=0, y=85)

    self.save_button = Button(self.window, text="Save", bd=4, bg="white", command=self.save_drawing, width=9)
    self.save_button.place(x=0, y=120)

    self.fill_button= Button(self.window, text="Fill", bd=4, bg="white", command=self.background_colour, width=9)
    self.fill_button.place(x=0, y=155)

    self.pen_scale = LabelFrame(self.window, text="Size", bd=5, bg="white", font=("arial", 15, "bold"))
    self.pen_scale.place(x=0, y=310, height=200, width=70)
    self.pen_size = Scale(self.pen_scale, orient=VERTICAL, from_=100, to=0, length=170)
    self.pen_size.set(10)
    self.pen_size.grid(row=0,column=1, padx=15)

    self.canvas.bind("<Button-1>", self.locate_xy)
    self.canvas.bind("<B1-Motion>", self.paint)

  def locate_xy(self,event):
    self.x, self.y = event.x, event.y

  def paint(self,event):
    self.canvas.create_line((self.x, self.y,event.x, event.y),fill=self.pen_colour, width=self.pen_size.get(),capstyle=ROUND, smooth=TRUE, splinesteps=36)
    self.x, self.y = event.x, event.y

  def select_colour(self,c):
    self.pen_colour = c

  def eraser(self):
    self.pen_colour = self.fill_colour

  def background_colour(self):
    colour = colorchooser.askcolor()
    self.fill_colour = colour[1]
    self.canvas.configure(bg=self.fill_colour)

  def choose_colour(self):
    colour = colorchooser.askcolor()
    self.pen_colour = colour[1]

  def clear(self):
    self.canvas.delete("all")
    
  def save_drawing(self):
    try:
      filename = filedialog.asksaveasfilename(defaultextension=".jpg")
      x = self.window.winfo_rootx() + self.canvas.winfo_x()
      y = self.window.winfo_rooty() + self.canvas.winfo_y()
      x1 = x + self.canvas.winfo_width()
      y1 = y + self.canvas.winfo_height()
      ImageGrab.grab().crop((x,y,x1,y1).save(filename))
      messagebox.showinfo("Python Paint says", f"Image saved as {filename}")
    except:
      messagebox.showerror("Python Paint says", "Unable to save image")

if __name__ == "__main__":
  window = Tk()
  p = Paint(window)
  window.mainloop()