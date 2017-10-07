#coding=utf-8
import socket
import thread

#以下三行是來匯入外部py檔
import sys
sys.path.append("C:/Users/ASUS/Documents/5.Gitthub/PythonServer_to_JavaClient/python_server") #←匯入檔案目錄
from f import *                                                                               #←檔案名稱(檔名即可)


#雙方協定
#(key = 雙方協定名稱, value = 功能), 功能就寫在外部py檔
protocol =      {    
                "one"   : one(), 
                "two"   : two(),
                "three" : three(),
                "four"  : four()
                }

#---------Main-------//這裡開始!!!!
if __name__ == '__main__':
        HOST = ''               #符號名稱，表示所有可用的接口
        PORT = 8001             #任意port

        #[1]產生socket
        try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except:
                print("Create socket FALL!!")                   #請創建套接字!!
        else:
                print("Socket created")                         #套接字創建

        #[2給socket一個名字
        try:
                s.bind((HOST, PORT))
        except socket.error as msg:
                print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
                sys.exit()
        else:
                print("Binding the address OK!")                #綁定地址OK！

        #[3]等待連接...
        s.listen(5)                                             #用來控制程序忙時可保持等待狀態的連接數
        print('Socket is listening')                            #Socket正在收聽

        print("\ntry to accept the connect:")                   #嘗試接受連接!!!!

        #[4]Stat servwe GO!!!
        switch = 1
        while switch:
                conn, addr = s.accept()                                         
                print '\nConnected with ' + addr[0] + ':' + str(addr[1])
                conn.send("I am server")                                     #傳給客戶端
                
                data = str(conn.recv(1024))                                  #接收客戶端傳來的資料
                print("client: " + data)
                switch = protocol[data]
                
                print("switch: "+ str(switch))

        conn.close()
        s.close()
        sys.exit()
