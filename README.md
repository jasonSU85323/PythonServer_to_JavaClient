PythonServer to JavaClient
=================================

### 將實作以下內容
* 用python寫server
* 用java寫client

```
1. client若連線成功，server會回傳I am server
2. 這時client會傳"I am client"或"2"或"3"給server(請自行在code更改)
3. server接收後會顯示接收data
3. 若client傳"4"給server，server會結束服務(註:這是server結束條件，否則不會結束)
4. 若client傳其他值，server接收後會顯示"all"
```

### 執行環境
* 版本
	* python 2.7
	* java version "1.8.0_144"
* 編輯器
	* python用一般文字編輯器即可
	* java用eclipse
* 執行
	* python：
		1. 打開cmd
		2. cd 到 PythonServer_to_JavaClient\python_server
		3. 執行python python_server.py
	* java：
		1. 打開PythonServer_to_JavaClient\java_client
		2. 將client資料夾匯入到自己的eclipse
		3. 然後執行即可

### 後續
至於程式上的小變化，我在code裡都有註解  
剩下就請各位自行發揮囉~

檔案「Python和java互連」後面名子是我寫的版本號碼，數字越大越新。
