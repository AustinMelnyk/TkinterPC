
import tkinter as tk #imports the whole tkinter library but each function must start with tk.###

class MyApp: #this creates a class that we can call back again and again
    def __init__(self, root): #this creates a function that is defined, then __intialized__ is going to take its self and also pass the "root" window I'm setting up in it
        root.title("My app")  #this is the name of the window that pops up on the desktop 
        root.geometry("500x500") #this is the starting geometry (notice it is a string) NOTE: if not used then app will choose size based on elements
        root.maxsize(800,800) #this is the max size that it will go to when the maximize button is hit NOTE: if not used then app will choose size based on elements

        #WIDGETS
        #self.label = tk.Label(root, text="Some Label Text", textvariable=self.label_text) #this creates a label for the root window, and then gives it some starting text
        self.label_text = tk.StringVar() #Change it to this to create a label_text referring to itself as the label and lets us enter a string for it later
        label = tk.Label(root, text="Some Label Text", textvariable=self.label_text) #add this in now to allow us to assign the textvariable whatever is entered from the entry text later
        label.pack() #this allows us to place it on the window in a "packed" orientation

        # label["text"] = "New Label Text" #label[key we want it to look for] = "what we want the label text to change to" 
        # label["font"] = ("Courier",40) #Apparently "font" and "bg" keys automatically exist already and they can be changed up there or here when calling them as a "key"
        label.configure(text="new label text", font=("Courier", 28)) #or you can use .configure to do them all at once with comma sep keys

        self.entry_text = tk.StringVar() #this creates a variable that will let us enter a string variable for later
        entry = tk.Entry(root, textvariable=self.entry_text) #this creates similar to a label an entry section for the "root" window and creates a new variable textvariable with value of entry_text
        entry.pack() #packs this entry underneath the other label

        #label["textvariable"] = entry_text # this will now automatically update the Label above with what is in the entry box

        button = tk.Button(root, text="Button text", command=self.press_button) #creates a variable for a button for the "root" window that says "Button text" in it at first, then when clicked it runs the command function
        button.pack()

    def press_button(self):
        #print("Button has been pressed")
        text = self.entry_text.get()
        self.label_text.set(text)

root=tk.Tk() #root is the name of my first tkinter window. This could be anything I am setting it up here
MyApp(root) #this calls the class with and allows me to call it multiple times
root.mainloop() #This runs the main function constantly ongoing
