import re
data = '''<body>
	<form action="" method="post" name="form1">
		<input type="hidden" id="usertype" name="usertype" value="xs">
		<input type="hidden" id="username" name="username" value="U201417238">
		<input type="hidden" id="password" name="password" value="feefcbfd8a350051f03b0787a4838cda">
		<input type="hidden" id="url" name="url" value="http://s.hub.hust.edu.cn/">
		<input type="hidden" name="key1" value="020401"/>
		<input type="hidden" name="key2" value="a98fe76cb4841a1b51ac4ddc9ba8fafc"/>
		<input type="hidden" name="F_App" value="From kslgin. App:app610.dc.hust.edu.cn|app6102|IP:10.10.10.245"/>
	</form>
	<script type="text/javascript">
	var url = document.getElementById("url").value;
	var to_url = "";
	if(url == "http://curriculum.hust.edu.cn/"){
		to_url = url+'userLoginAction.do';
	}else{
		to_url = url+'hublogin.action';
	}'''

re1 = re.compile(r'<input type="hidden" name="(.*?)" value="(.*?)"/>')
re2 = re.compile(r'<input type="hidden" id="password" name="password" value="(.*?)">')
result1 = re1.findall(data)
result2 = re2.findall(data)
print (result1[0][0],result1[0][1],result1[2][1])
print (result2[0])