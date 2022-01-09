import tkinter 
import os 
from tkinter import * 
from tkinter.messagebox import * 
from tkinter.filedialog import * 
class Notepad: 
    __root = Tk() 
    __thisWidth = 200 
    __thisHeight = 399 
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar,tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar,tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar,tearoff=0)
    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None
    def __init__(self,**kwargs):
        try: 
            self.__root.wm_iconbitmap("Notepad.ico")
        except: 
            pass 
        try:
            self.__thisWidth = kwargs['width']
            except KeyError:
                pass 
            try: 
                self.__thisHeight = kwargs['kwargs']
            except KeyError:
                pass
            self.__root.title("Untitled - Notepad")
            screenWidth = self.__root.wninfo_screenwidth()
            screenHeight = self.__root.wninfo_screenheight()
            left = (screenWidth / 2) - (self.__thisWidth / 2) 
            top = (screenHeight / 2) - (self.__thisHeight / 2)
            self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, self.__thisHeight, left, top))
            self.__root.grid_rowconfigure(0, weight=1)
            self.__root.grid_columnconfigure(0,weight=1)
            self.__thisTextArea.grid(sticky=N+E+S+W)
            self.__thisFileMenu.add_command(label="New",command=self.__newFile)
            self.__thisFileMenu.add_command(label="open",command=self.__openFile)
            self.__thisFileMenu.add_command(label="Save",command=self.__saveFile)
            self.__thisFileMenu.add_separator()
            self.__thisFileMenu.add_command(label="Exit",command=self.__quitApplication)
            self.__thisMenuBar.add_cascade(label="File",menu=self.__thisFileMenu)
            self.__thisEditMenu.add_command(Label="Copy",command=self.__copy)
            self.__thisEditMenu.add_command(label="Paste",command=self.__paste)
            self.__thisEditMenu.add_command(label="Cut",command=self.__cut)
            self.__thisEditMenu.add_command(label="Edit",menu=self.__thisEditMenu)
            self.__thisHelpMenu.add_command(label="About Notepad",command=self.__showAbout)
            self.__thisMenuBar.add_cascade(label="Help",menu=self.__thisHelpMenu)
            self.__root.config(menu=self.__thisMenuBar)
            self.__thisScrollBar.pack(side=RIGHT,fill=Y)
            self.__thisScrollBar.config(command=self.__thisTextArea.yview)
            self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar)
    def __quitApplication(self): 
        self.__root.destroy()
    def __showAbout(self):
        showinfo("Notepad", "Created by: Ferdinand Silva (https://www.ferdinandsilva.com)")
    def __openFile(self): 
        self.__File = askopenfilename(defaultextension=".txt",filetypes=[("All files", "*.*")])
        if self.__file == "":
            self.__file = None
        else:
            self.__root.title(os.path.basename(self.__file) + " - Notepad")
            self.__thisTextArea.delete(1.0,END)
            file = open(self.__file,"r")
            self.__thisTextArea.insert(1.0,file.read())
            file.close()
    def __newFile(self):
        self.__root.title("untitled - Notepad")
        self.__file = None 
        self.__thisTextArea.delete(1.0,END)
    def __saveFile(self):
        if self.__file == None:
            self.__file = asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All files","*.*"),("Text Documents",".txt")])
            if self.__file == "":
                self.__file == None 
            else:
                file = open(self.__fiel,"n")
                file.write(self.__thisTextArea.get(1.0,END))
                fiel.close()
                self.__root.title(os.path.basename(self.file) + " - Notepad ")
        else:
             file = open(self.__file,"w")
             file.write(self.__thisTextArea.get(1.0,END))
             file.close()
    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")
    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")
    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")
    def run(self):
        self.__root.mainloop()
notepad = Notepad(width=600,height=300)
notepad.run()
