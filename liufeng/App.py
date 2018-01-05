#!/usr/bin/python3

# @author liu-feng
# @email w710989327@foxmail.com
# @time 2018/1/5 16:48
from tkinter import Frame, Label, Button, Entry, messagebox

__author__ = 'liu-feng'
__email__ = 'w710989327@foxmail.com'


# gui? so easy?
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello Python GUI')
        self.helloLabel.pack()
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.quitButton = Button(self, text='Hello', command=self.hello)
        self.quitButton.pack()
        pass

    def hello(self):
        name = self.nameInput.get() or 'python'
        messagebox.showinfo('Message', 'hello %s ' % name)
        pass


app = Application()
app.master.title('Hello Python!')
app.mainloop()
