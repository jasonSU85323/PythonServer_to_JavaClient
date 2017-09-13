#coding=utf-8
import socket
import thread
import sys

#[4]接受連接
def accept_aonn(conn):
	conn.send("I am server")                                #傳給客戶端

	data = conn.recv(1024)                                  #接收客戶端傳來的資料
	if data == "I am client":
                print "client:I am clinet"
                return 1
	elif data == "2":
                print "client:two"
                return 1
	elif data == "3":
		print "client:three"
                return 1
	elif data == "4":
                print "client:close server socker!!!"
                return 0                                        #return 0，關閉socket
	else:
		print "client:All"
                return 1

#---------Main-------//這裡開始!!!!
if __name__ == '__main__':
        HOST = ''		#符號名稱，表示所有可用的接口
        PORT = 8001		#任意port

        #[1]產生socket
        try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except:
                print("Create socket FALL!!")			#請創建套接字!!
        else:
        	print("Socket created")				#套接字創建

        #[2給socket一個名字
        try:
        	s.bind((HOST, PORT))
        except socket.error as msg:
        	print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        	sys.exit()
        else:
        	print("Binding the address OK!") 		#綁定地址OK！

        #[3]等待連接...
        s.listen(5)						#用來控制程序忙時可保持等待狀態的連接數
        print('Socket is listening') 				#Socket正在收聽

        print("\ntry to accept the connect:") 		        #嘗試接受連接!!!!

        #Stat servwe GO!!!
        switch = 1
        while switch:
                conn, addr = s.accept()
                print '\nConnected with ' + addr[0] + ':' + str(addr[1])
                switch = accept_aonn(conn)
                
        conn.close()
        s.close()
        sys.exit()
