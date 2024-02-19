import cv2
import socket
import pickle
import struct

import numpy as np
from PIL import Image

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = 'server_ip'  # 서버의 IP 주소를 입력하세요
port = 9999
client_socket.connect((host_ip, port))

cap = cv2.VideoCapture(1)

# 웹캠의 해상도를 512x512로 설정
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 512)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 512)
data = b""
payload_size = struct.calcsize("Q")
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frame_cvt = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_pil = Image.fromarray(frame_cvt)
        a = pickle.dumps(frame_pil)
        message = struct.pack("Q", len(a)) + a
        client_socket.sendall(message)

        cv2.imshow('Sending Video', frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

        fps = cap.get(cv2.CAP_PROP_FPS)
        print(f"Current FPS: {fps}")

        while len(data) < payload_size:
            packet = client_socket.recv(4 * 1024)  # 버퍼 사이즈 4K
            if not packet: break
            data += packet
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("Q", packed_msg_size)[0]

        # 프레임 데이터를 받는 부분
        while len(data) < msg_size:
            data += client_socket.recv(4 * 1024)
        frame_data = data[:msg_size]
        data = data[msg_size:]

        # 변환된 이미지 프레임을 로드
        frame = pickle.loads(frame_data)
        frame = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)
        cv2.imshow('Received Transformed Video', frame)
    else:
        break

cap.release()
cv2.destroyAllWindows()
