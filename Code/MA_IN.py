import numpy as np
import random
import pygame
import os
import pickle
import mysql.connector as mc
from mutagen.mp3 import MP3
from tkinter import filedialog
from tkinter.filedialog import Listbox
from tkinter.filedialog import Tk
from tkinter.filedialog import askdirectory      #Importing all the required modules
from tkinter.filedialog import Scale
from tkinter.filedialog import RAISED
from tkinter.filedialog import GROOVE
from tkinter import Entry
from tkinter import messagebox
from tkinter import StringVar
from tkinter import PhotoImage
from tkinter import Text
from tkinter import OptionMenu
from tkinter import END
from tkinter import Label
from tkinter import Button
from tkinter import VERTICAL
from tkinter import HORIZONTAL
nb=0
abc=0
cd=os.getcwd()
################################################MP3PLAYER BLOCK###############################
def updatename():              #updates the name of the current song
    global m
    a=listofsongs2[i]            
    a=a.strip(".mp3")
    m.set(a)
def volume(val):   # Used to change the volume of the current playing song
    
    global xyt
    xyt=100
    xyt=int(val)/100
    pygame.mixer.music.set_volume(xyt)
def directory(event):      #Prompts the user to select a directory when the user chooses the play a folder option
    global conditionalval
    directory= askdirectory()
    os.chdir(directory)
    for j in os.listdir(directory):
        if j.endswith(".mp3"):
            listofsongs.append(j)
            j=j.strip(".mp3")
            listofsongs2.append(j)
    conditionalval=1
    print(listofsongs)
    MP3PLAYING()
def createplaylist(event):      #Creates a new playlist
    global conditionalval
    conditionalval=2
    filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A Song", filetype =(("Music File(MP3)","*.mp3"),))
    x1=list(filename)
    x1.reverse()
    z=[]
    y=""
    p=x1.index("/")
    x1.reverse()
    for ps in range(-1,-p-1,-1):
        z.append(x1[ps])
    z.reverse()
    for pk in z:
        y+=pk
    print(filename)
    listofsongs.append(filename)
    y=y.strip(".mp3")
    listofsongs2.append(y)
    MP3PLAYING()
def importplaylist(event): #Imports an already made playlist
    global root11
    global listofsongs
    global listofsongs2
    global conditionalval
    global playlist_1
    global playkey
    conditionalval=3
    dataopen=open("PlaylistData1.dat","rb")
    userkey=pickle.load(dataopen)
    playkey=userkey[user11]
    dataopen.close()
    root11=Tk()
    root11.resizable(0,0)
    root11.config(bg="#220047")
                  
    width=300
    height=300
    screen_width = root11.winfo_screenwidth()
    screen_height = root11.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root11.geometry('%dx%d+%d+%d' % (width, height, x, y))
    

    playlist_1=Listbox(root11,selectbackground="#CE9141",height=8,width=30,relief=GROOVE,bd=3,bg="#220047",fg="#CE9141",font=("fixedsys",10))
    playlist_1.place(x=20,y=70)
    
    text1_2=Label(root11,text="Playlist's for user:"+user11,font=("georgia",15),bg="#220047",fg="#CE9141")
    text1_2.place(x=50,y=10)
    
    okay1=Button(root11,text="Select",bg="#CE9141",relief=RAISED,fg="#220047",bd=1,activebackground="#220047",activeforeground="#CE9141",font=("fixedsys",10),command=okay)
    okay1.place(x=120,y=230)

    for i in playkey:
        playlist_1.insert(0,i)

    root11.mainloop()
def okay():
    global listofsongs
    global appendlist
    appendlist=playlist_1.get("active")
    listofsongs=playkey[appendlist]
    for filename in listofsongs:
        x1=list(filename)
        x1.reverse()
        z=[]
        y=""
        p=x1.index("/")
        x1.reverse()
        for ps in range(-1,-p-1,-1):
            z.append(x1[ps])
        z.reverse()
        for pk in z:
            y+=pk
        y=y.strip(".mp3")
        listofsongs2.append(y)
    root11.destroy()
    MP3PLAYING()
    

def MP3PLAYING():  #Main interface which initiates the MP3 player
    global seek
    global oc2
    global listofsongs
    global listofsongs2
    global songlist
    global songname 
    global len1
    global time1
    songname=Label(root5,textvariable=m,width=90,bg="#220047",fg="#CE9141",font=("roboto",13))
    songname.place(x=-120,y=450)
        
    pygame.mixer.init()
    songlist=Listbox(root5,selectbackground="#CE9141",height=14,width=60,relief=GROOVE,bd=3,bg="#220047",fg="#CE9141",font=("fixedsys",10))
    songlist.place(x=20,y=205)
  
    a=StringVar()
    a.set("Default")
    
    oc=StringVar(root5)
    oc.set("Select")
    
    
    listofsongs2.reverse()
    for h in listofsongs2:
        songlist.insert(0,h)
    listofsongs2.reverse()
    
    #currentsong=Label(root5,text="Current Song:",font=("georgia",15),bg="#220047",fg="#CE9141")
    #currentsong.place(x=230,y=500)
    
    orderofsongs=Label(root5,text="Your Playlist",font=("georgia",15),bg="#220047",fg="#CE9141")
    orderofsongs.place(x=40,y=170)
    
    startbutton=Button(root5,text="Start",bg="#CE9141",relief=RAISED,fg="#220047",bd=1,activebackground="#220047",activeforeground="#CE9141",font=("fixedsys",10))
    startbutton.place(x=400,y=480)
    
    playnext=Button(root5,text=">>>",bg="#CE9141",relief=RAISED,fg="#220047",bd=1,activebackground="#220047",activeforeground="#CE9141",font=("fixedsys",10))
    playnext.place(x=355,y=480)
    
    
    playbefore=Button(root5,text="<<<",bg="#CE9141",fg="#220047",relief=RAISED,bd=1,activebackground="#220047",activeforeground="#CE9141",font=("fixedsys",10))
    playbefore.place(x=190,y=480)
    
    stop=Button(root5,text="Stop",bg="#CE9141",fg="#220047",relief=RAISED,bd=1,activebackground="#220047",activeforeground="#CE9141",font=("fixedsys",10))
    stop.place(x=137,y=480)
    
    pause=Button(root5,text="Pause",bg="#CE9141",fg="#220047",relief=RAISED,bd=1,activebackground="#220047",activeforeground="#CE9141",font=("fixedsys",10))
    pause.place(x=237,y=480)
     
    play=Button(root5,text="Play",bg="#CE9141",fg="#220047",relief=RAISED,bd=1,activebackground="#220047",activeforeground="#CE9141",font=("fixedsys",10))
    play.place(x=300,y=480)

    volume1=Label(root5,text="Volume",font=("georgia",11),fg="#CE9141",bg="#220047")
    volume1.place(x=533,y=190)
    
    selection=MP3(listofsongs[0])
    len1=selection.info.length
    len1//=1
 
    seek=Scale(root5,from_=0,to=len1,orient=HORIZONTAL,length=400,cursor="cross",bd=1,bg="#CE9141",fg="#220047",activebackground="#220047",command=seek1)
    seek.place(x=100,y=530)
    
    oc1=StringVar(root5)
    oc1.set("Welcome"+ " "+ user11)
    
    options=["Home","Back","Close"]
    dropdown=OptionMenu(root5,oc1,*options,command=choice1)
    dropdown.configure(font=("georgia",15),fg="#220047",bg="#CE9141",activebackground="#CE9141",activeforeground="#220047")
    dropdown.place(x=200,y=110)
    
    oc2=StringVar(root5)
    oc2.set("Options")
    
    options1=["Shuffle[]","Random[?]","Delete[-]","Add[+]"]
    dropdown1=OptionMenu(root5,oc2,*options1,command=choice2)
    dropdown1.configure(text="Options",font=("georgia",10),fg="#220047",bg="#CE9141",activebackground="#220047",activeforeground="#CE9141")
    dropdown1.place(x=500,y=50)
    
    volume2=Scale(root5,from_=100,to=0,orient=VERTICAL,length=210,cursor="cross",bd=1,bg="#CE9141",fg="#220047",activebackground="#220047",command=volume)
    volume2.set(100)
    volume2.place(x=540,y=215)
    pygame.mixer.music.set_volume(100)
    
    if conditionalval==2:
        saveplaylist=Button(root5,text="Save",bg="#CE9141",fg="#220047",relief=RAISED,bd=1,activebackground="#220047",activeforeground="#CE9141",font=("fixedsys",10))
        saveplaylist.place(x=40,y=560)
        saveplaylist.bind("<Button>",createplay)
    elif conditionalval==3:
        orderofsongs.place_forget()
        defer="Your Playlist :"+" "+appendlist
        orderofsongs=Label(root5,text=defer,font=("georgia",15),bg="#220047",fg="#CE9141")
        orderofsongs.place(x=40,y=170)
        
    else:
        print("okay")

    
    """time1=IntVar()
    time1.set(0)

    timer1= Label(root5, textvar= time1,font=("georgia",8),fg="#220047",bg="#CE9141")
    timer1.place(x= 250, y= 550)"""
    
    pause.bind("<Button-1>",pausesong)
    play.bind("<Button-1>",unpause)
    startbutton.bind("<Button-1>",playmusic)
    playnext.bind("<Button-1>",nextsong)
    playbefore.bind("<Button-1>",previous)
    stop.bind("<Button-1>",stopmusic)

    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()


    updatename()
    """timer()
   

def timer():
    global nb
    global time1

    if nb < len1:
        new_time = time1.get()+1
        time1.set(new_time)
        root5.after(1000, timer) # call this function again in 1,000 milliseconds
        nb += 1
def timer2(xcv):
    global nb
    new_time = xcv
    time1.set(new_time)
    nb += 1 """

def createplay(event):
    global name12
    global root12
    root12=Tk()
    root12.resizable(0,0)
    root12.title("Create Playlist")
    root12.config(bg="#220047")
    width=400
    height=150
    screen_width = root12.winfo_screenwidth()
    screen_height = root12.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root12.geometry('%dx%d+%d+%d' % (width, height, x, y))
    
    name12=StringVar(root12)
    todo1=Label(root12,text="Name your playlist",font=("roboto",20),bg="#220047",fg="#CE9141")
    todo1.pack()
    
    input0=Entry(root12,textvar=name12,width=50)
    input0.place(x=50,y=60)
    
    submit0=Button(root12,text='Submit',font=("georgia",15),width=10,fg='#220047',bg='#CE9141',activeforeground="#CE9141",activebackground="#220047",height=1,)
    submit0.place(x=135,y=100)
    submit0.bind("<Button-1>",savelist)
    
    root12.mainloop()

def savelist(event):
    root12.destroy()
    listname=name12.get()
    dataopen=open("PlaylistData1.dat","rb")
    userkeys=pickle.load(dataopen)
    playkey=userkeys[user11]
    dataopen.close()
    if listname not in playkey:
        datafile1=open("PlaylistData1.dat","wb")
        playkey[listname]=listofsongs
        pickle.dump(userkeys,datafile1)
        datafile1.close()    
        print("Playlist added successfully")
    else:
        print("try again")
        createplay(1)

def seek1(val):
    val=int(val)
    try:
        pygame.mixer.music.rewind()
        pygame.mixer.music.set_pos(val)
        #timer2(val)
    except:
        m.set("Song Ended")
        print("song ended")
    
def reset1():
    global seek
    global len1
    selection=MP3(listofsongs[i])
    len1=selection.info.length
    len1//=1
    seek.place_forget()
    seek=Scale(root5,from_=0,to=len1,orient=HORIZONTAL,length=400,cursor="cross",bd=1,bg="#CE9141",fg="#220047",activebackground="#220047",command=seek1)
    seek.place(x=100,y=530)
    
  
def shuffle(event):
    global m
    global i
    global listofsongs
    global listofsongs2
    xy=listofsongs2[i]
    a=np.array(listofsongs)
    b=np.array(listofsongs2)
    s=np.arange(a.shape[0])
    np.random.shuffle(s)
    listofsongs=list(a[s])
    listofsongs2=list(b[s])
    songlist.delete(0,END)
    print(listofsongs)
    print(listofsongs2)
    vbnm=0
    for ln in listofsongs2:
        ln=ln.strip(".mp3")
        songlist.insert(vbnm,ln)
        vbnm+=1
    ax=listofsongs2.index(xy)
    i=ax

def choice1(x):
    if x=="Home":
        root5.destroy()
        pygame.mixer.quit()
        MAIN(1)
    if x=="Back":
        root5.destroy()
        pygame.mixer.quit()
        mp3player()
    if x=="Close":
        pygame.mixer.quit()
        root5.destroy()
def choice2(x):
    if x=="Shuffle[]":
        shuffle(1)
        oc2.set("Options")
    if x=="Random[?]":
        random1(1)
        oc2.set("Options")
    if x=="Delete[-]":
        delete(1)
        oc2.set("Options")
    if x=="Add[+]":
        addasong(1)
        oc2.set("Options")
def addasong(event):
    filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A Song", filetype =(("Music File","*.mp3"),))
    x=list(filename)
    x.reverse()
    z=[]
    y=""
    p=x.index("/")
    x.reverse()
    for ps in range(-1,-p-1,-1):
        z.append(x[ps])
    z.reverse()
    for pk in z:
        y+=pk

    l=len(listofsongs)
    listofsongs.append(filename)
    y=y.strip(".mp3")
    listofsongs2.append(y)
    songlist.insert(l,y)
def delete(event):
    global listofsongs
    global songlist
    current2=songlist.get("active")
    current3=songlist.curselection()
    lo=listofsongs2.index(current2)
    listofsongs.pop(lo)
    listofsongs2.remove(current2)
    songlist.delete(current3)
        
def random1(event):
   global i
   global time1
   l=len(listofsongs)
   i=random.randint(0,l-1)
   pygame.mixer.music.load(listofsongs[i])
   pygame.mixer.music.play()
   
   selection=MP3(listofsongs[i])
   len1=selection.info.length
   print(len1)
   reset1()
   updatename()
      
def pausesong(event):
    pygame.mixer.music.pause()
    m.set("Music Paused")   
def unpause(event):
    pygame.mixer.music.unpause()
    a=listofsongs2[i]
    a=a.strip(".mp3")
    m.set(a)
    
        
def nextsong(event):
    global i
    global time1
    i+=1
    l=len(listofsongs)
    if i>=l:
        i=0
        pygame.mixer.music.load(listofsongs[i])
        pygame.mixer.music.play()
        
        selection=MP3(listofsongs[i])
        len1=selection.info.length
        print(len1)
        updatename()
        reset1()
    else:
        pygame.mixer.music.load(listofsongs[i])
        pygame.mixer.music.play()
        
        selection=MP3(listofsongs[i])
        len1=selection.info.length
        print(len1)
        updatename()
        reset1()
def previous(event):
    global i
    global time1
    i-=1
    l=len(listofsongs)
    if i<0:
        i=l-1
        pygame.mixer.music.load(listofsongs[i])
        pygame.mixer.music.play()
        selection=MP3(listofsongs[i])
        len1=selection.info.length
        print(len1)
        updatename()
        reset1()
    else:   
        pygame.mixer.music.load(listofsongs[i])
        pygame.mixer.music.play()
        selection=MP3(listofsongs[i])
        len1=selection.info.length
        print(len1)
        updatename()
        reset1()
def stopmusic(event):
    pygame.mixer.music.stop()
    m.set("Music Stopped")
        
def playmusic(event):
    global i
    global time1
    current1=songlist.get("active")
    f=songlist.get(0,"end").index(current1)
    i=f
    pygame.mixer.music.load(listofsongs[i])
    pygame.mixer.music.play()
    updatename()

    reset1()
def mp3player():
    global root5
    global i
    global listofsongs
    global listofsongs2
    global songlist
    global songname 
    global m
    root5=Tk()
    root5.resizable(0,0)
    root5.title("MP3 Player")
    root5.config(bg="#220047")
    
    width=600
    height=600
    screen_width = root5.winfo_screenwidth()
    screen_height = root5.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root5.geometry('%dx%d+%d+%d' % (width, height, x, y))
    
    
    filename = PhotoImage(file ="player.png")
    background_label = Label(image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)    
             
    listofsongs=[]
    listofsongs2=[]
    m=StringVar()
    i=0
    
    

    
    addd=Button(root5,text="Play A Folder",bg="#CE9141",fg="#220047",activebackground="#220047",activeforeground="#CE9141",font=("georgia",25))
    addd.place(x=100,y=205)
    addd.bind("<Button>",directory)
    
    createplay=Button(root5,text="Create Playlist",bg="#CE9141",fg="#220047",activebackground="#220047",activeforeground="#CE9141",font=("georgia",25))
    createplay.place(x=100,y=285)
    createplay.bind("<Button>",createplaylist)
    
    importplay=Button(root5,text="Import Playlist",bg="#CE9141",fg="#220047",activebackground="#220047",activeforeground="#CE9141",font=("georgia",25))
    importplay.place(x=100,y=365)
    importplay.bind("<Button-1>",importplaylist)

    root5.mainloop()

############################################DATA BLOCK#################################

def checkdata1(event):
    global user11
    user11=Username.get()
    password11=Password.get()
        
    if not CheckUserExists(user11,password11):
        error1()
    else:
        root2.destroy()
        mp3player()
def checkdata2(event):
    global user11
    user11=Username.get()
    password11=Password.get()
        
    if not CheckUserExists(user11,password11):
        error1()
    else:
        root10.destroy()
        mp3player()
    
def CheckUserExists(user,password):
    global cd
    os.chdir(cd)
    print(cd)
    try:
        
        f=user+".txt"
        a=open(f,"r")
        b=a.readlines()
        c=b[2].strip()
        d=b[3].strip()
        if user==c and password==d:
            a.close()
            return True
        if user !=c or password!=d:
            a.close()
            return False
    except:
        print("none")

def error1():
    global root4
    root4=Tk()
    root4.title("Error1")
    root4.resizable(0,0)
    root4.config(bg="#220047")
    
    width=500
    height=250
    screen_width = root4.winfo_screenwidth()
    screen_height = root4.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root4.geometry('%dx%d+%d+%d' % (width, height, x, y))
   
    errortxt1=Label(root4,text="Error!",font=("georgia",30),bg="#220047",fg="#CE9141")
    errortxt1.place(x=195,y=10)

    errortxt2=Label(root4,text="The error has occurred due to one of the following reasons:  ",font=("georgia",10),bg="#220047",fg="#CE9141")
    errortxt2.place(x=55,y=70)
  

    error1=Label(root4,text="(i) The Password and Username do not match please try again . ",font=("georgia",10),bg="#220047",fg="#CE9141")
    error1.place(x=50,y=100)
  

    error2=Label(root4,text="(ii) The username is not registered with us please register with us . ",font=("georgia",10),bg="#220047",fg="#CE9141")
    error2.place(x=50,y=120)


    bt1=Button(root4,text="Register",font=("georgia",20),bg="#CE9141",fg="#220047",activebackground="#220047",activeforeground="#CE9141")
    bt1.place(x=100,y=160)
    bt1.bind("<Button-1>",register1)

    bt2=Button(root4,text="Try Again",font=("georgia",20),bg="#CE9141",fg="#220047",activebackground="#220047",activeforeground="#CE9141")
    bt2.place(x=250,y=160)
    bt2.bind("<Button-1>",tryagain1)

    root4.mainloop()

def error2(): 
    global root6       
    root6=Tk()
    root6.resizable(0,0)
    root6.title("Error")
    root6.config(bg="#220047")
    
    width=450
    height=200
    screen_width = root6.winfo_screenwidth()
    screen_height = root6.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root6.geometry('%dx%d+%d+%d' % (width, height, x, y))
 
    errortxt1=Label(root6,text="Error!",font=("georgia",30),bg="#220047",fg="#CE9141")
    errortxt1.place(x=165,y=7)
    
    errortxt2=Label(root6,text="The email id  entered is not valid , please enter a valid email id  ",font=("georgia",10),bg="#220047",fg="#CE9141")
    errortxt2.place(x=30,y=70)
  
    bt2=Button(root6,text="Try Again",font=("georgia",20),bg="#CE9141",fg="#220047",activebackground="#220047",activeforeground="#CE9141")
    bt2.place(x=165,y=120)
    bt2.bind("<Button-1>",tryagain2)

    root6.mainloop()
def error3():
    global root7
    root7=Tk()
    root7.resizable(0,0)
    root7.title("Error")
    root7.config(bg="#220047")
    
    width=450
    height=240
    screen_width = root7.winfo_screenwidth()
    screen_height = root7.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root7.geometry('%dx%d+%d+%d' % (width, height, x, y))
 
    errortxt1=Label(root7,text="Error!",font=("georgia",30),bg="#220047",fg="#CE9141")
    errortxt1.place(x=165,y=7)

    errortxt2=Label(root7,text="Please fulfill the following requirements for a strong password: ",font=("georgia",10),bg="#220047",fg="#CE9141")
    errortxt2.place(x=30,y=65)

    errortxt3=Text(root7,font=("georgia",10),height=4,width=45,bg="#220047",fg="#CE9141")
    errortxt3.place(x=20,y=100) 
    errortxt3.insert(END," 1.Password should be atleast 8 character long. \n 2.Must contain atleast one uppercase and lowercase character. \n 3.No special characters are allowed. \n 4. No whitespaces are allowed. ")

    bt2=Button(root7,text="Try Again",font=("georgia",20),bg="#CE9141",fg="#220047",activebackground="#220047",activeforeground="#CE9141")
    bt2.place(x=250,y=180)
    bt2.bind("<Button-1>",tryagain3)

    bt1=Button(root7,text="Get Password",font=("georgia",20),bg="#CE9141",fg="#220047",activebackground="#220047",activeforeground="#CE9141",command=getpass)
    bt1.place(x=50,y=180)
 

    root7.mainloop()
def error4():
    global root9
    root9=Tk()
    root9.resizable(0,0)
    root9.title("Error")
    root9.config(bg="#220047")
                 
    width=450
    height=230
    screen_width = root9.winfo_screenwidth()
    screen_height = root9.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root9.geometry('%dx%d+%d+%d' % (width, height, x, y))
 
    errortxt1=Label(root9,text="Error!",font=("georgia",30),bg="#220047",fg="#CE9141")
    errortxt1.place(x=162,y=7)

    errortxt2=Label(root9,text="No field should be left empty! Make sure you have filled \n the following fields correctly: \n 1.Username \n 2. Fullname ",font=("georgia",12),bg="#220047",fg="#CE9141")
    errortxt2.place(x=25,y=65)

    bt2=Button(root9,text="Try Again",font=("georgia",20),bg="#CE9141",fg="#220047",activebackground="#220047",activeforeground="#CE9141")
    bt2.place(x=160,y=155)
    bt2.bind("<Button-1>",tryagain4)
    root9.mainloop()

def regenerate(event):
    root8.destroy()
    getpass()
def getpass():
    global root8
    x1=""
    b=random.randint(8,12)
    while b!=0:
        a=random.randint(0,2)
        if a==0:
            c=random.randint(48,57)
            chars=chr(c)
            x1+=chars
            b-=1
        if a==1:
            c=random.randint(65,90)
            chars=chr(c)
            x1+=chars
            b-=1
        if a==2:
            c=random.randint(97,122)
            chars=chr(c)
            x1+=chars
            b-=1
    root8=Tk()
    root8.resizable(0,0)
    root8.title("Pass")
    root8.config(bg="#220047")
    
    width=650   
    height=240
    screen_width = root8.winfo_screenwidth()
    screen_height = root8.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root8.geometry('%dx%d+%d+%d' % (width, height, x, y))
             
    getpass=Label(root8,text="Get Password",font=("georgia",30),bg="#220047",fg="#CE9141")
    getpass.place(x=200,y=7)

    instructions=Label(root8,text="Following is a randomly generated password for your convenience , you can copy the password:",font=("georgia",10),bg="#220047",fg="#CE9141")
    instructions.place(x=30,y=80)

    passwordgiven=Text(root8,font=("georgia",10),height=2,width=45,bg="#220047",fg="#CE9141")
    passwordgiven.place(x=120,y=120) 
    passwordgiven.insert(END,x1)
    
    bt1=Button(root8,text="Regenerate",font=("georgia",20),bg="#CE9141",fg="#220047",activebackground="#220047",activeforeground="#CE9141")
    bt1.place(x=250,y=170)
    bt1.bind("<Button-1>",regenerate)
    
    bt2=Button(root8,text="Close",font=("georgia",10),bg="#CE9141",fg="#220047",activebackground="#220047",activeforeground="#CE9141")
    bt2.place(x=500,y=170)
    bt2.bind("<Button-1>",close)
    
    root8.mainloop()
def close(event):
    root8.destroy()
def datauser(event):
    global user11
    os.chdir(cd)
    pt1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    pt2=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    pt3=['1','2','3','4','5','6','7','8','9','0']
    zxcv=0
    ZXCV=0
    NUM=0
    name1=Fullname.get()
    email1=Email.get()
    user11=Username.get()
    pass1=Password.get()
    l=len(pass1)
    if name1=="" or user11=="":
        error4()
    elif "@" and ".com" not in email1:
        error2()
    else:
        pass
    for n in pass1:
        if n in pt1:
            zxcv+=1
        elif n in pt2:
            ZXCV+=1
        elif n in pt3:
            NUM+=1
        else:
            error3()
    if not l>=8:
        error3()
    elif zxcv==0 or ZXCV==0 or NUM==0:
        error3()
    else:
        try:
           mydb=mc.connect(host="localhost",user="root",passwd="amity",database="ayush",auth_plugin="mysql_native_password")
           cursor=mydb.cursor()
           var1=(user11,pass1)
           sql1=("insert ignore into userdata values(%s,%s)")
           cursor.execute(sql1,var1)
           mydb.commit()
           a=user11+".txt"
           filetxt=open(a,'w') 
           filetxt.write(name1 +"\n" + email1 + "\n" + user11 + "\n" + pass1 ) 
           filetxt.close()
           dataopen=open("PlaylistData1.dat","rb")
           userkeys=pickle.load(dataopen)
           dataopen.close()
           userkeys[user11]={}
           datafile1=open("PlaylistData1.dat","wb")
           pickle.dump(userkeys,datafile1)
           datafile1.close() 
           root3.destroy()
           mp3player()

        except:
            messagebox.showwarning("Error","Username already exists,try logging in instead.")
def register1(event):
    root4.destroy()
    root2.destroy()
    pureregister(1)
def register2(event):
    root1.destroy()
    pureregister(1)
def pureregister(event):
    global Fullname
    global Email
    global Username
    global Password
    global root3
    root3=Tk()
    root3.resizable(0,0)
    root3.config(bg="#220047")
    root3.title("Registration Form")
    
    width=500
    height=450
    screen_width = root3.winfo_screenwidth()
    screen_height = root3.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root3.geometry('%dx%d+%d+%d' % (width, height, x, y))
    
    Fullname=StringVar()
    Email=StringVar()
    Username=StringVar()
    Password =StringVar()
    
    signup_1=Label(root3, text="Sign Up",fg="#CE9141",bg="#220047",width=20,font=("georgia", 40))
    signup_1.place(x=-50,y=20)
    
    back=Button(root3,text="Back",font=("georgia",10),width=10,fg='#220047',bg='#CE9141',activeforeground="#CE9141",activebackground="#220047")
    back.place(x=400,y=10)
    back.bind("<Button-1>",back1)
    
    name=Label(root3, text="FullName",fg="#CE9141",bg="#220047",width=20,font=("georgia", 15))
    name.place(x=-10,y=125)

    input1=Entry(root3,textvar=Fullname,width=40)
    input1.place(x=200,y=130)

    email= Label(root3, text="Email",fg="#CE9141",bg="#220047",width=20,font=("georgia", 15))
    email.place(x=-29,y=175)
    
    input2 = Entry(root3,textvar=Email,width=40)
    input2.place(x=200,y=180)

    user1= Label(root3,text="Username",fg="#CE9141",bg="#220047",width=20,font=("georgia", 15))
    user1.place(x=-10,y=225)

    input3=Entry(root3,textvar=Username,width=40)
    input3.place(x=200,y=230)

    pass1= Label(root3, text="Password",fg="#CE9141",bg="#220047",width=20,font=("georgia", 15))
    pass1.place(x=-10,y=275)

    input4=Entry(root3,textvar=Password,width=40,show="**")
    input4.place(x=200,y=280)

    submit1=Button(root3,text='Submit',font=("georgia",20),width=10,fg='#220047',bg='#CE9141',activeforeground="#CE9141",activebackground="#220047",height=1)
    submit1.place(x=165,y=345)
    submit1.bind("<Button-1>",datauser)

    root3.mainloop()
def back1(event):
    root3.destroy()
    MAIN(1)
def back2(event):
    root2.destroy()
    MAIN(1)
def back3(event):
    root10.destroy()
    mp3player()
def tryagain1(event):
    root4.destroy()
def tryagain2(event):
    root6.destroy()
def tryagain3(event):
    root7.destroy()
def tryagain4(event):
    root9.destroy()
def login1(event):
    global Username
    global Password
    global root2
    root1.destroy()
    root2=Tk()
    root2.resizable(0,0)
    root2.config(bg="#220047")
    root2.title("Log In")
    
    
    width=500
    height=300
    screen_width = root2.winfo_screenwidth()
    screen_height = root2.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root2.geometry('%dx%d+%d+%d' % (width, height, x, y))
    
    Username=StringVar()
    Password=StringVar()


    login_1=Label(root2, text="Log In",fg="#CE9141",bg="#220047",width=20,font=("georgia", 40))
    login_1.place(x=-50,y=20)

   
    

    user2= Label(root2, text="Username",fg="#CE9141",bg="#220047",width=20,font=("georgia", 15))
    user2.place(x=-10,y=115)

    input3=Entry(root2,textvar=Username,width=40)
    input3.place(x=200,y=120)


    pass2= Label(root2, text="Password",fg="#CE9141",bg="#220047",width=20,font=("georgia", 15))
    pass2.place(x=-10,y=165)

    input4=Entry(root2,textvar=Password,width=40,show="**")
    input4.place(x=200,y=170)

    submit1=Button(root2,text='Submit',font=("georgia",20),width=10,fg='#220047',bg='#CE9141',activeforeground="#CE9141",activebackground="#220047",height=1,)
    submit1.place(x=170,y=225)
    submit1.bind("<Button-1>",checkdata1)
    
    back=Button(root2,text="Back",font=("georgia",10),width=10,fg='#220047',bg='#CE9141',activeforeground="#CE9141",activebackground="#220047")
    back.place(x=400,y=10)
    back.bind("<Button-1>",back2)
    
    root2.mainloop()  

def login2(event):
    global root10
    root10=Tk()
    root10.resizable(0,0)
    root10.config(bg="#220047")
    root10.title("Log In")
    
    width=500
    height=300
    screen_width = root10.winfo_screenwidth()
    screen_height = root10.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root10.geometry('%dx%d+%d+%d' % (width, height, x, y))

    
    Username=StringVar()
    Password=StringVar()


    login_1=Label(root10, text="Log In",fg="#CE9141",bg="#220047",width=20,font=("georgia", 40))
    login_1.place(x=-50,y=20)



    user2= Label(root10, text="Username",fg="#CE9141",bg="#220047",width=20,font=("georgia", 15))
    user2.place(x=-10,y=115)

    input3=Entry(root10,textvar=Username,width=40)
    input3.place(x=200,y=120)


    pass2= Label(root10, text="Password",fg="#CE9141",bg="#220047",width=20,font=("georgia", 15))
    pass2.place(x=-10,y=165)

    input4=Entry(root10,textvar=Password,width=40,show="**")
    input4.place(x=200,y=170)

    submit1=Button(root10,text='Submit',font=("georgia",20),width=10,fg='#220047',bg='#CE9141',activeforeground="#CE9141",activebackground="#220047",height=1,)
    submit1.place(x=170,y=225)
    submit1.bind("<Button-1>",checkdata2)
    
    back=Button(root10,text="Back",font=("georgia",10),width=10,fg='#220047',bg='#CE9141',activeforeground="#CE9141",activebackground="#220047")
    back.place(x=400,y=10)
    back.bind("<Button-1>",back3)
    
    root10.mainloop()  

def signup(event):
    register2(1)

def MAIN(event):

    global root1
    root1=Tk()
    width=700
    height=250
    screen_width = root1.winfo_screenwidth()
    screen_height = root1.winfo_screenheight()

    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root1.geometry('%dx%d+%d+%d' % (width, height, x, y))
    
    root1.resizable(0,0)
    root1.config(bg="#220047")
    root1.title("Welcome")
    
    

    filename = PhotoImage(file ="welcome.png")
    background_label = Label(image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    login=Button(root1,text="Log In",font=("roboto",30),bg="#CE9141",fg="#220047",activeforeground="#b2995d",activebackground="#220047",height=1,width=10)
    login.place(x=60,y=120)
    login.bind("<Button-1>",login1)


    signup1=Button(root1,text="Sign Up",font=("roboto",30),bg="#CE9141",fg="#220047",activeforeground="#b2995d",activebackground="#220047",height=1,width=10)
    signup1.place(x=390,y=120)
    signup1.bind("<Button-1>",signup)

    root1.mainloop()
def splash():
    global root0
    root0= Tk()
    root0.lift()
    
    width=850
    height=425
    screen_width = root0.winfo_screenwidth()
    screen_height = root0.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root0.geometry('%dx%d+%d+%d' % (width, height, x, y))
    
    filename = PhotoImage(file ="splah.png")
    background_label = Label(image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    root0.overrideredirect(True)
    
    root0.after(5000, destroy1)
    root0.mainloop()
def destroy1():
    root0.destroy()
    MAIN(1)
splash()