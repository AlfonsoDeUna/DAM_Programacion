import socket
import threading
import tkinter
from tkinter.scrolledtext import ScrolledText

# client handler
def handler(client):
    while True:
        try:
            message = client.recv(1024)
            if not message: break
            message = message.decode('utf-8')
            update_balance(int(message)) # or float(message)?
        except Exception as ex:
            print("Client handler exception:", ex)
            break
    client.close()

# socket server function
def server():
    host = '127.0.0.1'
    port = 6005
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()

    while True:
        try:
            client, address = server.accept()
            print(f"connected with {address}")
            thread = threading.Thread(target=handler, args=(client,), daemon=True)
            thread.start()
        except Exception as ex:
            print("Server exception:", ex)
            break

    server.close()

# function to show the update balance in the text box
def update_balance(amount=0):
    global balance
    balance += amount
    # avoid updating tkinter widget in a thread
    root.after(1, lambda: logbox.insert("end", f"Your current balance is {balance}\n"))

balance = 0

root = tkinter.Tk()
root.title("Server")
#root.geometry("300x200")

logbox = ScrolledText(root, width=60, height=20)
logbox.pack()
update_balance() # show the initial balance

# create thread for socket server
threading.Thread(target=server, daemon=True).start()

root.mainloop()    
