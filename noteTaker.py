from tkinter import *
from datetime import datetime
from time import sleep
import sys

class Application(Frame):
    def __init__(self,master):
        super(Application, self).__init__(master)
        self.pack(expand=1,fill=BOTH)
        # self.master.overrideredirect(1)
        self.createWidgets()
        current = datetime.now().strftime("\n\n%d-%m-%Y %H:%M\n")
        self.textBox.insert(0.0, current)
        with open('Notes/firstTest.txt','r') as fileObj:
            content = fileObj.read()
        self.textBox.insert(1.0, content)
        # self.master.protocol('WM_DELETE_WINDOW',self.exit)
        # self.textBox.bind('<Ctrl + V>',)

    def reset(self):
        main()
        # self.destroy()
        # self.__init__(self.master)
        # if __name__ == '__main__':
        # __name__ == '__main__'

    def timeAndDate(self):
        current = datetime.datetime.now().strftime("\n%d-%m-%Y %H:%M\n")
        # self.textBox.delete(0.0,END)
        self.textBox.insert(END, current)

    def operation(self):
        pass

    def zoomIn(self):
        pass

    def zoomOut(self):
        pass

    def normal(self):
        pass

    def save(self):
        text = self.textBox.get(1.0, 'end-1c')
        with open('Notes/firstTest.txt','w') as fileObj:
            fileObj.write(text)
        self.master.after(100, self.save)


        # while True:
        #     self.save()
        #     sleep(10)


    # def saveAs(self):
    #     text = self.textBox.get(0.0, 'end-1c')
    #     with open('Notes/firstTest.txt', 'w+') as fileObj:
    #         fileObj.write(text)

    #this method is only here temporarily
    def exitsaveAs(self):
        text = self.textBox.get(0.0, END)
        with open('Notes/firstTest.txt', 'w+') as fileObj:
            fileObj.write(text)
        self.quit()

    def about(self):
        self.aboutWindow = Toplevel(self.master,bg="black")
        self.aboutWindow.title("About Us")
        self.aboutWindow.geometry('350x250')

        labelFrame = Frame(self.aboutWindow,bg='black')
        Label(labelFrame,text="NoteTaker 0.0",font=('Verdana',12),bg="black",fg="white").grid(row=0,column=2,sticky='w')
        Label(labelFrame,text="This is a really simple notetaker made using Tkinter\nMake your notes people",font=('Arial',11),bg="black",fg="white").grid(row=1, column=1,columnspan=2, sticky='w')
        labelFrame.pack(side=TOP,pady=50,anchor=CENTER)

        buttonFrame = Frame(self.aboutWindow,bg="black")
        self.creditsButton = Button(buttonFrame,text='Credits', command=self.displayCredits,bg="black",fg="white")
        self.creditsButton.pack(side=LEFT,anchor=W)

        self.closeButton = Button(buttonFrame,text='Close', command=self.aboutWindow.destroy,bg="black",fg="white")
        self.closeButton.pack(side=LEFT,anchor=E)
        buttonFrame.pack(side=TOP)



    def displayCredits(self):
        self.creditsWindow = Toplevel(self.aboutWindow,bg="black")
        self.creditsWindow.title("Credits")
        self.creditsWindow.geometry("350x250")

        creditsLabelFrame = Frame(self.creditsWindow,bg="black")
        Label(creditsLabelFrame,text="Written by:\nRomeo Nutifafa Folie",font=('Verdana',12),bg="black",fg="white").pack()

        self.closeButton = Button(creditsLabelFrame, text='Close', command=self.creditsWindow.destroy,bg="black",fg="white")
        self.closeButton.pack(anchor=CENTER,pady=5)

        creditsLabelFrame.pack(side=TOP, pady=80)


    def setFont(self):
        pass

    def print(self):
        pass

    # def exit(self):
    #     if len(self.textBox.get(2.0, END)) == 0:
    #         self.quit()
    #     else:
    #         exitWindow = Toplevel(self.master,bg="black")
    #         exitWindow.title("Save Changes")
    #         exitWindow.geometry('400x90')
    #         textFrame = Frame(exitWindow,bg="black")
    #         Label(textFrame, text="Do you want to save your changes before closing?", font=('Verdana', 10),bg="black",fg="white").grid(row=1,columnspan=3)
    #         Label(textFrame, text="If you don't save the document, all changes will be lost", font=('Verdana', 9),bg="black",fg="white").grid(row=2, columnspan=3)
    #         textFrame.pack(side=TOP, pady=7)
    #
    #         buttonFrame = Frame(exitWindow,bg="black")
    #         self.dontSaveButton = Button(buttonFrame, text="Don't Save", command=self.quit,bg="black",fg="white")
    #         # self.dontSaveButton.grid(row=3,column=0,sticky='nsew')
    #         self.dontSaveButton.pack(side=LEFT)
    #         self.cancelButton = Button(buttonFrame, text="Cancel", command=exitWindow.destroy,bg="black",fg="white")
    #         # self.cancelButton.grid(row=3,column=1,sticky='nsew')
    #         self.cancelButton.pack(side=LEFT, padx=4)
    #         self.saveButton = Button(buttonFrame, text="Save", command=self.exitsaveAs,bg="black",fg="white")
    #         # self.saveButton.grid(row=3,column=2,sticky='nsew'
    #         self.saveButton.pack(side=LEFT)
    #         buttonFrame.pack(side=TOP)

    def exit(self):
        self.save()
        self.quit()


    def createWidgets(self):
        #let's create the text entry first
        self.textBox = Text(self,width=70,height=30,wrap=WORD,relief=FLAT)
        # self.textBox.bind('<Control-v>', self.textBox.event_generate('<<Paste>>'))
        # self.textBox.event_generate('<<Paste>>')
        self.textBox.pack(expand=1, fill=BOTH)

        #let's deal with the small menu inside this note taker
        self.menubar = Menu(self.master,relief=FLAT)
        self.master.config(menu=self.menubar)
        # File menu
        self.filemenu = Menu(self.menubar)
        self.filemenu.add_command(label="New", command = self.reset)
        # self.filemenu.add_command(label="Open..", command=self.operation)
        self.filemenu.add_command(label="Save", command= self.save)
        # self.filemenu.add_command(label="Save As...", command= self.saveAs)
        # self.filemenu.add_command(label="Page Setup", command= self.operation)
        self.filemenu.add_command(label="Print...", command= self.print)
        self.filemenu.add_command(label="Exit", command= self.exit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)


        #Edit menu
        self.editmenu = Menu(self.menubar)
        self.editmenu.add_command(label="Find", command='keystroke')
        # self.editmenu.add_command(label="Find Next", command="keystroke")
        # self.editmenu.add_command(label="Replace..", command="keystroke")
        # self.editmenu.add_command(label="Go To..", command="keystroke")
        self.editmenu.add_command(label="Time/Date", command=self.timeAndDate)
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)


        #Format menu
        self.formatmenu = Menu(self.menubar)
        # self.formatmenu.add_checkbutton(label="Word Wrap", command=self.setWrap)
        self.formatmenu.add_command(label="Font..", command=self.setFont)
        self.menubar.add_cascade(label="Format", menu = self.formatmenu)


        #View menu
        # self.viewmenu = Menu(self.menubar)
        # self.viewmenu.add_checkbutton(label="Status Bar", command=self.setStatusBar)
        # self.menubar.add_cascade(label="View", menu=self.viewmenu)


        self.helpmenu = Menu(self.menubar)
        self.menubar.add_cascade(label="Help",menu=self.helpmenu)
        self.helpmenu.add_command(label="About",command=self.about)


def main():
# if __name__ == '__main__':
    root = Tk()
    root.title("Notes")
    noteTaker = Application(root)
    root.after(100, noteTaker.save)
    root.mainloop()

main()

