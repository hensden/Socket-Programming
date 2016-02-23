import socket
import os

def to_string(lst):
    s = ""
    for i in range(len(lst)):
        s += (str(lst[i]) + " ")
    return s

def main():
    port = 12343
    s = socket.socket()
    host = socket.gethostname()
    
    s.bind((host,port))
    s.listen(5)  #waits for one client connection
    
    print 'Server listening ... '
    
    while 1:
        c, addr = s.accept() #accept connection with client
        print 'Connected to ', addr
        # l = os.listdir(os.getcwd())
        # ls = to_string(l)
        data = c.recv(1024)
        print data
        #print('Server received', repr(data))
    c.close()

if __name__ == "__main__":
    main()
