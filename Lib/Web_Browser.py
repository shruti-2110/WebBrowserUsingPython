import tkinter as tk
import webbrowser
root=tk.Tk()
root.geometry('400x150')
root.title("Web Broswser")

def fb():
    webbrowser.open_new("www.facebook.com")
def yt():
    webbrowser.open_new("www.youtube.com")
def ig():
    webbrowser.open_new("www.instagram.com")
def tw():
    webbrowser.open_new("www.twitter.com")
def ac():
    webbrowser.open_new("www.aryacollege.in")
def search():
    word=x.get()
    search="https://www.google.com/search?q="+word
    webbrowser.open_new(search)


    
x=tk.StringVar()


b1=tk.Button(root,text="Facebook",fg="White",bg="Blue",command=fb)
b2=tk.Button(root,text="Youtube",fg="White",bg="Green",command=yt)
b3=tk.Button(root,text="Instagram",fg="White",bg="Red",command=ig)
b4=tk.Button(root,text="Twitter",fg="White",bg="Black",command=tw)
b5=tk.Button(root,text="Aryacollege",fg="White",bg="pink",command=ac)
b1.place(x=10,y=70,width=80,height=30)
b2.place(x=100,y=70,width=80,height=30)
b3.place(x=190,y=70,width=80,height=30)
b4.place(x=10,y=105,width=135,height=30)
b5.place(x=155,y=105,width=135,height=30)
b6=tk.Button(root,text="Search",fg="White",bg="Blue",command=search)
b6.place(x=320,y=10,width=70,height=50)
e1=tk.Entry(root,textvariable=x)
e1.place(x=10,y=10,width=300,height=40)
root.mainloop()
