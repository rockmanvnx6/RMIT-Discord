from pypresence import Presence
import time
import os

client_id = '478889900964446211'
RPC = Presence(client_id)
RPC.connect()

RPC.update(state="Description: Initializing...", details="Initializing...", start=int(time.time()),large_image="rmit-l")
command = None
print("")
print("Discord Rich Presence has been started.")
print("")
def console(command):
    command = input("Type /help to see valid commands: ")
    return command

def check(sub_display,des_display,tol_display):
    if (sub_display == "" or des_display == "" or tol_display == "" or len(sub_display) < 2 or len(sub_display) > 128
        or len(des_display) < 2 or len(des_display) > 128 or len(tol_display) < 2 or len(tol_display) > 128):
        print("")
        print("* Fields can't be empty and must be between 2 and 128 characters")
        print("")
        sub_display = input("Input subject: ")
        des_display = input("Input description: ")
        tol_display = input("Tooltip when hover RMIT logo: ")
        return check(sub_display,des_display,tol_display)
    else:
        return sub_display,des_display,tol_display

command = console(command)

while True:

    if (command == "/help"):
        print("")
        print("1. Type /update to change the status")
        print("2. Type /clear to clear the status")
        print("3. Type /quit to quit the program")
        print("")
        command = console(command)

    elif (command == "/update"):
        print("")
        sub_display = input("Input subject: ")
        des_display = input("Input description: ")
        tol_display = input("Tooltip when hover RMIT logo: ")

        sub_display,des_display,tol_display = check(sub_display,des_display,tol_display)

        RPC.update(state="Description: " + des_display, details="" + sub_display, start=int(time.time()),large_text=tol_display, large_image="rmit-l")
        print("Updated Successfully !!!")
        print("")
        command = console(command)

    elif (command == "/clear"):
        print("")
        RPC.clear(pid=os.getpid())
        print("Cleared the status")
        print("")
        command = console(command)

    elif (command == "/quit"):
        print("")
        print("Thank you for using !")
        os._exit(1)

    else:
        print("")
        print("Invalid command!")
        print("")
        command = console(command)