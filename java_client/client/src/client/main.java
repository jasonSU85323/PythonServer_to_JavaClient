package client;
//https://litotom.com/2016/05/11/java%E7%9A%84%E7%B6%B2%E8%B7%AF%E7%A8%8B%E5%BC%8F%E8%A8%AD%E8%A8%88/
import java.net.*;
import java.io.*;

public class main {
	private static String address = "127.0.0.1";
	private static int port = 8001;
	
	public static void main(String[] args) {
		
		byte buff[] = new byte[1024];
		
		try
		{
			System.out.println("正在與伺服器建立連線. . .");
			Socket s = new Socket(address, port);
			System.out.println("已經與伺服器取得連線");
			
			InputStream in = s.getInputStream();	//取得輸入串流
			OutputStream out = s.getOutputStream();	//取得輸出串流
			
			int n = in.read(buff);
			System.out.println("\n從伺服器端收到： " + new String (buff,0,n));
			
			
			String str = "4";  //←-------這裡修改要傳過去的字串
			System.out.println("現在開始傳送資料. . . ");
			out.write(str.getBytes());
			System.out.println("資料「" + str + "」傳送完成");
			
			in.close();
			out.close();
			s.close();
		}
		catch(Exception e)
		{
			System.out.println(e);
		}
	}

}
