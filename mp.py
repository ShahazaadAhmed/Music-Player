import os
import tkinter
import tkinter.font
import customtkinter as ck
import pygame
import math
import time
from threading import *
from PIL import Image, ImageTk
from tkinter import filedialog
root=ck.CTk()
root.title('Music Player')
root.geometry('350x470')
pygame.mixer.init()
n=0
ip = False
sk=None
t1 = None
los=['songs/Unravel Piano(Version).mp3','songs/Sudden Shower.mp3','songs/Unlasting.mp3','songs/Call of Silence.mp3']
lot=['img/unravel.png','img/ssimg.jpg','img/unlasting.jpeg','img/Call of Silence.jpeg']

def gt(q,w):
    global sk,th

    img1=Image.open(lot[w])
    img2=img1.resize((200,200))
    load=ImageTk.PhotoImage(img2)
    th=tkinter.Label(im, image=load)
    th.image=load
    th.place(relx=0.02,rely=0.02)
    sn = os.path.basename(q[:-4]) 
    if sk is None:
        sk=tkinter.Label(text=sn,bg='#2b2b2b',fg='white',font=('Lucida Sans Unicode',13,'bold'))
        sk.place(relx=0.5,rely=0.62,anchor='center')
    else:
        sk.config(text=sn)    
       
def upload_song():
    song_path = filedialog.askopenfilename(title="Select a Song", filetypes=(("MP3 files", "*.mp3"),))
    if song_path:
        los.append(song_path)
        print(f"Added song: {song_path}")
    image_path = filedialog.askopenfilename(title="Select an Image", filetypes=(("Image files", "*.png;*.jpg;*.jpeg"),))
    if image_path:
        lot.append(image_path)
        print(f"Added image: {image_path}")
def prs():
    a=pygame.mixer.Sound(f'{los[n]}')
    sl=a.get_length()*3
    for i in range(0,math.ceil(sl)):
        time.sleep(0.3)
        pro.set(pygame.mixer.music.get_pos()/1000)

def threading():
    t1=Thread(target=prs)
    t1.start()

def pll():
    threading()
    global n
    cs=n
    if n>2:
        n=0
    pygame.mixer.music.load(los[n])
    pygame.mixer.music.play(loops=0)
    pygame.mixer.music.set_volume(0.5)
    gt(los[n],n)

def plp():
    global ip
    if ip:
        pygame.mixer.music.pause()
        pl_ps.configure(text='▶')
    else:
        pygame.mixer.music.unpause()
        pl_ps.configure(text='||')
    ip=not ip

def next():
    global n,ip
    n=(n+1)%len(los) 
    pygame.mixer.music.load(los[n])
    pygame.mixer.music.play()
    gt(los[n],n)
    ip=True
    pl_ps.configure(text='||')

def back():
    global n,ip
    n=(n-1)%len(los) 
    pygame.mixer.music.load(los[n])
    pygame.mixer.music.play()
    gt(los[n],n)
    ip=True
    pl_ps.configure(text='||')

def vl(value):
    pygame.mixer.music.set_volume(value)
def lop():
    pass
def on_closing():
    global t1
    if t1 is not None:
        t1.join()
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    root.destroy()

ti=ck.CTkLabel(root,text='Music Player',font=ck.CTkFont(size=30,weight='bold',family='Tw cen MT'))
ti.pack(padx=20,pady=15,anchor=tkinter.CENTER)

fr=ck.CTkFrame(root,width=270,height=340)
fr.pack(pady=6,anchor=tkinter.CENTER)

im=ck.CTkFrame(fr,width=170,height=170)
im.place(relx=0.5,rely=0.34,anchor=tkinter.CENTER)

pro=ck.CTkSlider(fr,width=250,height=5,progress_color='#a61641',button_color='white',button_hover_color='white')
pro.place(relx=0.5,rely=0.5,y=80,anchor=tkinter.CENTER)

butt=ck.CTkButton(fr,text='⇚',width=0,height=40,fg_color='#a61641',corner_radius=2000,hover_color='#a82049',font=ck.CTkFont(size=25),command=back)
butt.place(relx=0.2,rely=0.52,y=120,anchor=tkinter.CENTER)

pl_ps=ck.CTkButton(fr,text='▶',width=0,height=40,fg_color='#a61641',corner_radius=2000,hover_color='#a82049',font=ck.CTkFont(size=20),command=plp)
pl_ps.place(relx=0.5,rely=0.52,y=120,anchor=tkinter.CENTER)

butt=ck.CTkButton(fr,text='⇛',width=0,height=40,fg_color='#a61641',corner_radius=2000,hover_color='#a82049',font=ck.CTkFont(size=25),command=next)
butt.place(relx=0.8,rely=0.52,y=120,anchor=tkinter.CENTER)

pl=ck.CTkButton(root,text='▶',width=10,height=10,fg_color='#242424',hover_color='#333333',command=pll)
pl.place(relx=0.1,rely=0.91)
vol=ck.CTkSlider(root,width=210,height=18,from_=0 ,to=1,progress_color='#a61641',button_color='white',button_hover_color='white',command=vl)
vol.pack(pady=10)
br=ck.CTkButton(root,text='X',width=10,height=10,fg_color='#242424',hover_color='#333333',command=lop)
br.place(relx=0.83,rely=0.91)
us=ck.CTkButton(root,text='♪',width=5,height=5,fg_color='#242424',hover_color='#333333',font=ck.CTkFont(weight='bold'),command=upload_song)
us.place(relx=0.77,rely=0.054)
root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
