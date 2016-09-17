import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def new_thread(conn,addr):
    while(1):
        data = conn.recv(1024).decode('utf8')
        if (data[0:4] != "exit"):
            data = data[::-1]
            conn.send(data.encode('utf8'))
        else:
            print('Disconnect from:' + addr)
            break
    conn.close()


def main():
    HOST = '127.0.0.1'
    PORT = 3333

    s.bind((HOST,PORT))
    s.listen()
    while(1):
        conn,addr = s.accept()
        print('Connecting from:',addr)
        thread = threading.Thread(target = new_thread,args=(conn,addr))
        thread.start()

if __name__ == '__main__':
    main()


