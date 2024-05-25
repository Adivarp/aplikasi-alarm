import tkinter
import time
import datetime
import pygame
from tkinter import *
from tkinter import messagebox

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

start = tkinter.Tk()

# Tampil title aplikasi
start.title("Times Up")
start.geometry('600x280+300+200')

# Isi list pilihan
options_list = ["Sound iPhone", "Sound Samsung", "Sound Bis"]

value_inside = tkinter.StringVar(start)

value_inside.set("Sound Timer")

# Tampilkan menu untuk memilih dari isi list pilihan
options_menu = tkinter.OptionMenu(start, value_inside, *options_list)
options_menu.config(font=('Consolas 15'))
options_menu.pack()
options_menu.place(x=80, y=20)

# Tampilkan label timer
TimerLabel = Label(start, text="SET TIMER :", font=('Consolas 15'))
TimerLabel.pack()
TimerLabel.place(x=80, y=80)

# Deklarasi variable
hour = StringVar()
minute = StringVar()
second = StringVar()

timer = datetime
jam_sisa = int
total_detik = int
menit_sisa = int

# Isi default timer
hour.set("00")
minute.set("00")
second.set("00")

# Tampilkan Hour label
HourLabel = Label(start, text="Hour :", font=('Arial 18'))
HourLabel.pack()
HourLabel.place(x=80, y=110)

# Tampilkan entry Hour
HourEntry = Entry(start, width=3, font=("Arial", 18, ""), textvariable=hour)
HourEntry.place(x=150, y=110)

# Tampilkan Menit label
MinuteLabel = Label(start, text="Minute :", font=('Arial 18'))
MinuteLabel.pack()
MinuteLabel.place(x=200, y=110)

# Tampilkan entry Minute
MinuteEntry = Entry(start, width=3, font=("Arial", 18, ""), textvariable=minute)
MinuteEntry.place(x=290, y=110)

# Tampilkan Second label
SecondLabel = Label(start, text="Second :", font=('Arial 18'))
SecondLabel.pack()
SecondLabel.place(x=340, y=110)

# Tampilkan entry Second
SecondEntry = Entry(start, width=3, font=("Arial", 18, ""), textvariable=second)
SecondEntry.place(x=440, y=110)

def popup_pesan1():
    win = tk.Toplevel()
    win.wm_title("P e r h a t i a n . . !")
    win.geometry('270x80+500+300')

    l = tk.Label(win, text="Masukkan Timer Terlebih Dahulu")
    l.place(x=26, y=10)

    b = ttk.Button(win, text="Oke", command=win.destroy)
    b.place(x=85, y=40)

def popup_pesan2():
    win = tk.Toplevel()
    win.wm_title("P e r h a t i a n . . !")
    win.geometry('270x80+500+300')

    l = tk.Label(win, text="Pilih Sound Timer Terlebih Dahulu")
    l.place(x=26, y=10)

    b = ttk.Button(win, text="Oke", command=win.destroy)
    b.place(x=85, y=40)

def start_music():
    # Ini kalau timer gak diisi
    if int(hour.get()) + int(minute.get()) + int(second.get()) == 0:
        # Print("Masukkan Timer Terlebih Dahulu")
        popup_pesan1()

    elif value_inside.get() == "Sound iPhone":
        def CountDown():
            temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())

            while temp > -1:

                mins, secs = divmod(temp, 60)

                hours = 0
                if mins > 60:
                    hours, mins = divmod(mins, 60)

                hour.set("{0:2d}".format(hours))
                minute.set("{0:2d}".format(mins))
                second.set("{0:2d}".format(secs))

                start.update()
                time.sleep(1)

                if (temp == 0):
                    pygame.init()
                    pygame.mixer.init()
                    pygame.mixer.music.load("C:/Users/USER/OneDrive/Felisha Putri Firdy/Sound Times Up/Sound iPhone.mpeg")
                    pygame.mixer.music.play(loops=-1)

                temp -= 1

        CountDown()

    elif value_inside.get() == "Sound Samsung":
        def CountDown():
            temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())

            while temp > -1:

                mins, secs = divmod(temp, 60)

                hours = 0
                if mins > 60:
                    hours, mins = divmod(mins, 60)

                hour.set("{0:2d}".format(hours))
                minute.set("{0:2d}".format(mins))
                second.set("{0:2d}".format(secs))

                start.update()
                time.sleep(1)

                if (temp == 0):
                    pygame.init()
                    pygame.mixer.init()
                    pygame.mixer.music.load("C:/Users/USER/OneDrive/Felisha Putri Firdy/Sound Times Up/Sound Samsung.mpeg")
                    pygame.mixer.music.play(loops=-1)

                temp -= 1

        CountDown()

    elif value_inside.get() == "Sound Bis":
        def CountDown():
            temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())

            while temp > -1:

                mins, secs = divmod(temp, 60)

                hours = 0
                if mins > 60:
                    hours, mins = divmod(mins, 60)

                hour.set("{0:2d}".format(hours))
                minute.set("{0:2d}".format(mins))
                second.set("{0:2d}".format(secs))

                start.update()
                time.sleep(1)

                if (temp == 0):
                    pygame.init()
                    pygame.mixer.init()
                    pygame.mixer.music.load("C:/Users/USER/OneDrive/Felisha Putri Firdy/Sound Times Up/Sound Bis.mpeg")
                    pygame.mixer.music.play(loops=-1)

                temp -= 1

        CountDown()

    else:
        # Print("Pilih Sound Timer Terlebih Dahulu")
        popup_pesan2()

    return None

def stop_music():
    pygame.mixer.music.stop()
    return None


play_button = tkinter.Button(start, text='START', command=start_music)
play_button.config(font=('Consolas 15'))
play_button.pack()
play_button.place(x=80, y=160)

stop_button = tkinter.Button(start, text='STOP', command=stop_music)
stop_button.config(font=('Consolas 15'))
stop_button.pack()
stop_button.place(x=180, y=160)