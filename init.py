from pypresence import Presence
import time
import os

client_id = '478889900964446211'  # Fake ID, put your real one here
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop

RPC.update(state="Description: Initializing...", details="Initializing...", start=int(time.time()),large_image="rmit-l")  # Set the presence
command = None
print("")
print("Discord Rich Presence has been started.")
print("")
def console(command):
    command = input("Type /help to see valid commands: ")
    return command

command = console(command)

while True:

    if (command == "/help"):
        print("")
        print("1. Type /update to change the status")
        print("2. Type /clear to clear the status")
        print("")
        command = console(command)

    elif (command == "/update"):
        print("")
        sub_display = input("Input subject: ")
        des_display = input("Input description: ")
        tol_display = input("Tooltip when hover RMIT logo: ")

        if(sub_display=="" or des_display=="" or tol_display==""):
            print("")
            print("Fields can't be empty")
            sub_display = input("Input subject: ")
            des_display = input("Input description: ")
            tol_display = input("Tooltip when hover RMIT logo: ")

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
    else:
        print("")
        print("Invalid command!")
        print("")
        command = console(command)

# while True:  # The presence will stay on as long as the program is running
#     time.sleep(15) # Can only update rich presence every 15 seconds