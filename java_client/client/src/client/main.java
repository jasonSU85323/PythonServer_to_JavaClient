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
			System.out.println("���b�P���A���إ߳s�u. . .");
			Socket s = new Socket(address, port);
			System.out.println("�w�g�P���A�����o�s�u");
			
			InputStream in = s.getInputStream();	//���o��J��y
			OutputStream out = s.getOutputStream();	//���o��X��y
			
			int n = in.read(buff);
			System.out.println("\n�q���A���ݦ���G " + new String (buff,0,n));
			
			
			String str = "4";  //��-------�o�̭ק�n�ǹL�h���r��
			System.out.println("�{�b�}�l�ǰe���. . . ");
			out.write(str.getBytes());
			System.out.println("��ơu" + str + "�v�ǰe����");
			
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
