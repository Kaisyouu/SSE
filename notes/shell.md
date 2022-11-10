### 1. 解释器路径

在创建一个shell脚本后，在第一行加上`#!<bash path>`——在终端使用`which bash`找到bash路径，它告诉系统这个脚本将用什么解释器来执行，即使用哪一种Shell，一般为`/usr/bin/bash`或`/bin/bash`

### 2. 应用

#### 2.1 交互会话工具Expect

Expect能与交互式程序进行会话

For example 有这样一个交互式程序`hello.sh`：

```bash
#!/usr/bin/bash

echo "What is your name? "
read name
if [ $name ]; then
	echo "Hello, $name"
else
	echo "Doesn't sound like anything to me."
fi
```

使用Expect可以与之对话，比如：

```bash
#!/usr/bin/expect

spawn ./hello.sh
expect "What is your name? "
send "Kaisyouu"
expect eof
```



#### 2.2 利用分界符输入

在使用ftp等工具时，需要不断交互式输入账号密码等命令，也可以利用分界符一次性键入，例如：

```bash
ftp -ni <ip address> <<!
user n <username> <password>
bin
lcd <dir/subdir>
cd <dir/subdir>
get <file>
#...more
!
```



