import cv2
import socket
import pickle
import struct
from PIL import Image

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = '서버의 IP 주소'  # 서버의 IP 주소를 입력하세요
port = 9999
client_socket.connect((host_ip, port))

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = Image.fromarray(frame)
        a = pickle.dumps(frame)
        message = struct.pack("Q", len(a)) + a
        client_socket.sendall(message)

        cv2.imshow('Sending Video', frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()