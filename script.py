import serial
import customtkinter as ctk
import os

ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.geometry("1280x720")
app.resizable(False, False)
app.title("Robo Arm Control")

ser = serial.Serial("com6", 9600)


def send_base(value):
    value = int(value)
    ser.write(str(value).encode())
    print(value)


def send_elbow(value):
    value = int(value)
    ser.write(str(value).encode())
    print(value)


def send_hand(value):
    value = int(value)
    ser.write(str(value).encode())
    print(value)


def send_finger(value):
    value = int(value)
    ser.write(str(value).encode())


base_label = ctk.CTkLabel(master=app, width=1000, font=("Dongle", 100), text="BASE")
base_label.place(x=140, y=25)

base_slider = ctk.CTkSlider(app, from_=0, to=1024, width=1000, command=send_base)
base_slider.place(x=140, y=160)

elbow_label = ctk.CTkLabel(master=app, width=1000, font=("Dongle", 100), text="ELBOW")
elbow_label.place(x=140, y=185)

elbow_slider = ctk.CTkSlider(app, from_=2000, to=2180, width=1000, command=send_elbow)
elbow_slider.place(x=140, y=320)

hand_label = ctk.CTkLabel(master=app, width=1000, font=("Dongle", 100), text="HAND")
hand_label.place(x=140, y=345)

hand_slider = ctk.CTkSlider(app, from_=3000, to=3180, width=1000, command=send_hand)
hand_slider.place(x=140, y=480)

finger_label = ctk.CTkLabel(
    master=app, width=1000, font=("Dongle", 100), text="FINGERS"
)
finger_label.place(x=140, y=505)

finger_slider = ctk.CTkSlider(app, from_=4000, to=4180, width=1000, command=send_finger)
finger_slider.place(x=140, y=640)

app.mainloop()
