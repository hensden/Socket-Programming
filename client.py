import socket as S
import os
def main():
    s = S.socket()
    host = S.gethostname()
    port = 12343
    
    s.connect((host,port))
    while True:
        print "$> ",
        command = raw_input()
        s.send(command)
        # data = s.recv(1024)
        # print('data=%s', (data))
        #vif not data:
        #    break
        # write data to a file
        # print data
        # break
    s.close()
    print('connection closed')

if __name__ == "__main__":
    main()
