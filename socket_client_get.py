import cv2
import socket
import pickle
import struct

# 서버의 호스트 IP와 포트 번호를 설정하세요.
HOST_IP = "서버의 IP 주소"
PORT = 9999

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST_IP, PORT))

data = b""
payload_size = struct.calcsize("Q")

while True:
    # 메시지 크기를 받는 부분
    while len(data) < payload_size:
        packet = client_socket.recv(4*1024)  # 버퍼 사이즈 4K
        if not packet: break
        data += packet
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("Q", packed_msg_size)[0]

    # 프레임 데이터를 받는 부분
    while len(data) < msg_size:
        data += client_socket.recv(4*1024)
    frame_data = data[:msg_size]
    data = data[msg_size:]

    # 변환된 이미지 프레임을 로드
    frame = pickle.loads(frame_data)
    cv2.imshow('Received Transformed Video', frame)

    # 'q'를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

client_socket.close()
cv2.destroyAllWindows()
