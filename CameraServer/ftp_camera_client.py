from ftplib import FTP
import time
import camera
import os
import threading
import TCPServer


ftp = FTP('')

def send_photos():
    while True:
        camera.take_photo()  # Take photo and store it in the /images directory
        image_list = os.listdir('images')
        most_recent = open('images/' + image_list[-1], 'rb')
        ftp.storbinary('STOR ' + most_recent.name[7:], most_recent)
        time.sleep(5)  # Wait five seconds before taking and sending next photo

def close_connection():
    ftp.close()

def main(host, port):
    ftp.connect(host, port)
    ftp.login(user="webcam", passwd="1234")
    send_photos()

if __name__ == "__main__":
    ftp_host = 'localhost'
    ftp_port = 21
    try:
        ftp_send = threading.Thread(target=main(ftp_host, ftp_port))
    except IOError:
        print("Could not connect to FTP server!")
    TCPServer.start_server()



