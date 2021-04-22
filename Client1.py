from tkinter import *
import emoji
import socket
from threading import Thread

HEADER_LENGTH = 10
BUFFER_SIZE = 4096
IP = "127.0.0.1"
PORT = 1234



def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = conn.recv(4096).decode("utf8")
            TextBox.insert(INSERT, msg)
        except OSError:  # Possibly client has left the chat.
            print("")

root = Tk()
root.title("Project2_CIS452")
root.geometry("750x750")

myLabel = Label(root, text="Text Chat")
myLabel.pack()

TextBox = Text(root, height=25, width=70)
TextBox.pack()

L1 = Label(root, text="Message")
L1.place(anchor='center', relx=.05, rely=.65)

def func(event):
    if len(message.get()) > 0:
        TextBox.insert(INSERT, "You: " + message.get() + "\n")

        mess_to_send = "Friend: " + message.get() + "\n"
        conn.send(mess_to_send.encode('utf-8'))
        
        SendMessage.delete(0, END)
        SendMessage.insert(0, "")

root.bind('<Return>', func)

def click():
    if len(message.get()) > 0:
        TextBox.insert(INSERT, "You: " + message.get() + "\n")

        mess_to_send = "Friend: " + message.get() + "\n"
        conn.send(mess_to_send.encode('utf-8'))
        
        SendMessage.delete(0, END)
        SendMessage.insert(0, "")


def InsertEmoji(emoji):
    index = len(message.get()) + 1
    SendMessage.insert(index, emoji)

message = StringVar()
SendMessage = Entry(root, bd=5, textvariable=message)
SendMessage.place(anchor='center', x=365, y=480, height=50, width=565)

SendButton = Button(root, text="Send", command=click)
SendButton.place(anchor='center', relx=.9, rely=.65)

Emoji1 = Button(root, text=emoji.emojize(":grinning_face:"), command=lambda x=emoji.emojize(":grinning_face:"): InsertEmoji(x))
Emoji1.place(anchor='center', relx=.13, rely=.7)
Emoji2 = Button(root, text=emoji.emojize(":grinning_face_with_big_eyes:"), command=lambda x=emoji.emojize(":grinning_face_with_big_eyes:"): InsertEmoji(x))
Emoji2.place(anchor='center', relx=.17, rely=.7)
Emoji3 = Button(root, text=emoji.emojize(":grinning_face_with_smiling_eyes:"), command=lambda x = emoji.emojize(":grinning_face_with_smiling_eyes:"):InsertEmoji(x))
Emoji3.place(anchor='center', relx=.21, rely=.7)
Emoji4 = Button(root, text=emoji.emojize(":beaming_face_with_smiling_eyes:"), command=lambda x = emoji.emojize(":beaming_face_with_smiling_eyes:"):InsertEmoji(x))
Emoji4.place(anchor='center', relx=.25, rely=.7)
Emoji5 = Button(root, text=emoji.emojize(":grinning_squinting_face:"), command=lambda x = emoji.emojize(":grinning_squinting_face:"):InsertEmoji(x))
Emoji5.place(anchor='center', relx=.29, rely=.7)
Emoji6 = Button(root, text=emoji.emojize(":grinning_face_with_sweat:"), command=lambda x = emoji.emojize(":grinning_face_with_sweat:"): InsertEmoji(x))
Emoji6.place(anchor='center', relx=.33, rely=.7)
Emoji7 = Button(root, text=emoji.emojize(":rolling_on_the_floor_laughing:"), command=lambda x = emoji.emojize(":rolling_on_the_floor_laughing:"): InsertEmoji(x))
Emoji7.place(anchor='center', relx=.37, rely=.7)
Emoji8 = Button(root, text=emoji.emojize(":face_with_tears_of_joy:"), command=lambda x = emoji.emojize(":face_with_tears_of_joy:"): InsertEmoji(x))
Emoji8.place(anchor='center', relx=.41, rely=.7)
Emoji9 = Button(root, text=emoji.emojize(":slightly_smiling_face:"), command=lambda x = emoji.emojize(":slightly_smiling_face:"): InsertEmoji(x))
Emoji9.place(anchor='center', relx=.45, rely=.7)
Emoji10 = Button(root, text=emoji.emojize(":upside-down_face:"), command=lambda x = emoji.emojize(":upside-down_face:"): InsertEmoji(x))
Emoji10.place(anchor='center', relx=.49, rely=.7)
Emoji11 = Button(root, text=emoji.emojize(":winking_face:"), command=lambda x = emoji.emojize(":winking_face:"): InsertEmoji(x))
Emoji11.place(anchor='center', relx=.53, rely=.7)
Emoji12 = Button(root, text=emoji.emojize(":smiling_face_with_smiling_eyes:"), command=lambda x = emoji.emojize(":smiling_face_with_smiling_eyes:"):InsertEmoji(x))
Emoji12.place(anchor='center', relx=.57, rely=.7)
Emoji13 = Button(root, text=emoji.emojize(":smiling_face_with_halo:"), command=lambda x = emoji.emojize(":smiling_face_with_halo:"):InsertEmoji(x))
Emoji13.place(anchor='center', relx=.61, rely=.7)
Emoji14 = Button(root, text=emoji.emojize(":star-struck:"), command=lambda x = emoji.emojize(":star-struck:"):InsertEmoji(x))
Emoji14.place(anchor='center', relx=.65, rely=.7)
Emoji15 = Button(root, text=emoji.emojize(":face_blowing_a_kiss:"), command=lambda x = emoji.emojize(":face_blowing_a_kiss:"):InsertEmoji(x))
Emoji15.place(anchor='center', relx=.69, rely=.7)
Emoji16 = Button(root, text=emoji.emojize(":kissing_face:"), command=lambda x = emoji.emojize(":kissing_face:"):InsertEmoji(x))
Emoji16.place(anchor='center', relx=.73, rely=.7)
Emoji17 = Button(root, text=emoji.emojize(":smiling_face:"), command=lambda x = emoji.emojize(":smiling_face:"):InsertEmoji(x))
Emoji17.place(anchor='center', relx=.77, rely=.7)
Emoji18 = Button(root, text=emoji.emojize(":kissing_face_with_closed_eyes:"), command=lambda x = emoji.emojize(":kissing_face_with_closed_eyes:"):InsertEmoji(x))
Emoji18.place(anchor='center', relx=.81, rely=.7)
Emoji19 = Button(root, text=emoji.emojize(":kissing_face_with_smiling_eyes:"), command=lambda x = emoji.emojize(":kissing_face_with_smiling_eyes:"):InsertEmoji(x))
Emoji19.place(anchor='center', relx=.85, rely=.7)
Emoji20 = Button(root, text=emoji.emojize(":face_savoring_food:"), command=lambda x = emoji.emojize(":face_savoring_food:"):InsertEmoji(x))
Emoji20.place(anchor='center', relx=.13, rely=.75)
Emoji21 = Button(root, text=emoji.emojize(":face_with_tongue:"), command=lambda x = emoji.emojize(":face_with_tongue:"):InsertEmoji(x))
Emoji21.place(anchor='center', relx=.17, rely=.75)
Emoji22 = Button(root, text=emoji.emojize(":winking_face_with_tongue:"), command=lambda x = emoji.emojize(":winking_face_with_tongue:"):InsertEmoji(x))
Emoji22.place(anchor='center', relx=.21, rely=.75)
Emoji23 = Button(root, text=emoji.emojize(":zany_face:"), command=lambda x = emoji.emojize(":zany_face:"):InsertEmoji(x))
Emoji23.place(anchor='center', relx=.25, rely=.75)
Emoji24 = Button(root, text=emoji.emojize(":squinting_face_with_tongue:"), command=lambda x = emoji.emojize(":squinting_face_with_tongue:"):InsertEmoji(x))
Emoji24.place(anchor='center', relx=.29, rely=.75)
Emoji25 = Button(root, text=emoji.emojize(":money-mouth_face:"), command=lambda x = emoji.emojize(":money-mouth_face:"):InsertEmoji(x))
Emoji25.place(anchor='center', relx=.33, rely=.75)
Emoji26 = Button(root, text=emoji.emojize(":hugging_face:"), command=lambda x = emoji.emojize(":hugging_face:"):InsertEmoji(x))
Emoji26.place(anchor='center', relx=.37, rely=.75)
Emoji27 = Button(root, text=emoji.emojize(":face_with_hand_over_mouth:"), command=lambda x = emoji.emojize(":face_with_hand_over_mouth:"):InsertEmoji(x))
Emoji27.place(anchor='center', relx=.41, rely=.75)
Emoji28 = Button(root, text=emoji.emojize(":shushing_face:"), command=lambda x = emoji.emojize(":shushing_face:"):InsertEmoji(x))
Emoji28.place(anchor='center', relx=.45, rely=.75)
Emoji29 = Button(root, text=emoji.emojize(":thinking_face:"), command=lambda x = emoji.emojize(":thinking_face:"):InsertEmoji(x))
Emoji29.place(anchor='center', relx=.49, rely=.75)
Emoji30 = Button(root, text=emoji.emojize(":zipper-mouth_face:"), command=lambda x = emoji.emojize(":zipper-mouth_face:"):InsertEmoji(x))
Emoji30.place(anchor='center', relx=.53, rely=.75)
Emoji31 = Button(root, text=emoji.emojize(":face_with_raised_eyebrow:"), command=lambda x = emoji.emojize(":face_with_raised_eyebrow:"):InsertEmoji(x))
Emoji31.place(anchor='center', relx=.57, rely=.75)
Emoji32 = Button(root, text=emoji.emojize(":neutral_face:"), command=lambda x = emoji.emojize(":neutral_face:"):InsertEmoji(x))
Emoji32.place(anchor='center', relx=.61, rely=.75)
Emoji33 = Button(root, text=emoji.emojize(":expressionless_face:"), command=lambda x = emoji.emojize(":expressionless_face:"):InsertEmoji(x))
Emoji33.place(anchor='center', relx=.65, rely=.75)
Emoji34 = Button(root, text=emoji.emojize(":face_without_mouth:"), command=lambda x = emoji.emojize(":face_without_mouth:"):InsertEmoji(x))
Emoji34.place(anchor='center', relx=.69, rely=.75)
Emoji35 = Button(root, text=emoji.emojize(":smirking_face:"), command=lambda x = emoji.emojize(":smirking_face:"):InsertEmoji(x))
Emoji35.place(anchor='center', relx=.73, rely=.75)
Emoji36 = Button(root, text=emoji.emojize(":unamused_face:"), command=lambda x = emoji.emojize(":unamused_face:"):InsertEmoji(x))
Emoji36.place(anchor='center', relx=.77, rely=.75)
Emoji37 = Button(root, text=emoji.emojize(":face_with_rolling_eyes:"), command=lambda x = emoji.emojize(":face_with_rolling_eyes:"):InsertEmoji(x))
Emoji37.place(anchor='center', relx=.81, rely=.75)
Emoji38 = Button(root, text=emoji.emojize(":grimacing_face:"), command=lambda x = emoji.emojize(":grimacing_face:"):InsertEmoji(x))
Emoji38.place(anchor='center', relx=.85, rely=.75)
Emoji39 = Button(root, text=emoji.emojize(":lying_face:"), command=lambda x = emoji.emojize(":lying_face:"):InsertEmoji(x))
Emoji39.place(anchor='center', relx=.13, rely=.8)
Emoji40 = Button(root, text=emoji.emojize(":relieved_face:"), command=lambda x = emoji.emojize(":relieved_face:"):InsertEmoji(x))
Emoji40.place(anchor='center', relx=.17, rely=.8)
Emoji41 = Button(root, text=emoji.emojize(":pensive_face:"), command=lambda x = emoji.emojize(":pensive_face:"):InsertEmoji(x))
Emoji41.place(anchor='center', relx=.21, rely=.8)
Emoji42 = Button(root, text=emoji.emojize(":sleepy_face:"), command=lambda x = emoji.emojize(":sleepy_face:"):InsertEmoji(x))
Emoji42.place(anchor='center', relx=.25, rely=.8)
Emoji43 = Button(root, text=emoji.emojize(":drooling_face:"), command=lambda x = emoji.emojize(":drooling_face:"):InsertEmoji(x))
Emoji43.place(anchor='center', relx=.29, rely=.8)
Emoji44 = Button(root, text=emoji.emojize(":sleeping_face:"), command=lambda x = emoji.emojize(":sleeping_face:"):InsertEmoji(x))
Emoji44.place(anchor='center', relx=.33, rely=.8)
Emoji45 = Button(root, text=emoji.emojize(":face_with_medical_mask:"), command=lambda x = emoji.emojize(":face_with_medical_mask:"):InsertEmoji(x))
Emoji45.place(anchor='center', relx=.37, rely=.8)
Emoji46 = Button(root, text=emoji.emojize(":face_with_thermometer:"), command=lambda x = emoji.emojize(":face_with_thermometer:"):InsertEmoji(x))
Emoji46.place(anchor='center', relx=.41, rely=.8)
Emoji47 = Button(root, text=emoji.emojize(":face_with_head-bandage:"), command=lambda x = emoji.emojize(":face_with_head-bandage:"):InsertEmoji(x))
Emoji47.place(anchor='center', relx=.45, rely=.8)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("server started")
server_socket.bind((IP, PORT))
print("server bound")
server_socket.listen()
print("server listening...")
conn, addr = server_socket.accept()

receive_thread = Thread(target=receive)
receive_thread.start()

root.mainloop()