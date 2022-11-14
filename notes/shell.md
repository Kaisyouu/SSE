### 1. 解释器路径

在创建一个shell脚本后，在第一行加上`#!<bash path>`——在终端使用`which bash`找到bash路径，它告诉系统这个脚本将用什么解释器来执行，即使用哪一种Shell，一般为`/usr/bin/bash`或`/bin/bash`



### 2. 语法

#### 2.1 变量与数组

声明变量可以直接赋值，也可以使用`declare`关键字声明

> declare [-aAfFgilnrtux] [-p] [name[=value] ...]
>
> -f 将操作或显示限制为函数名及函数定义。
> -F 只显示函数名（调试时附加行号和源文件）。
> -g 在shell函数中使用时创建全局变量；其他情况下忽略。
> -p 显示每个名称的属性和值。
>
> *设置属性的选项:
> -a 创建数组（如果支持）。
> -A 创建关联数组（如果支持）。
> -i 增加整型属性。
> +i 删除整型属性。
> -l 增加小写属性，变量的值将转换为小写。
> +l 删除小写属性。
> -n 增加引用属性（如果该选项存在）。
> +n 删除引用属性（如果该选项存在）。
> -r 增加只读属性。
> -t 增加追踪属性。
> +t 删除追踪属性。
> -u 增加大写属性，变量的值将转换为大写。
> +u 删除大写属性。
> -x 增加导出属性。
> +x 删除导出属性。

字符串变量注意双引号里可以有变量和转义字符，而单引号不能，例如：

```bash
my_name="Kaisyouu"
greeting="hello, "$my_name" !"
greeting_1="hello, ${my_name} !"
# greeting=greeting_1="hello, Kaisyouu !"

greeting_2='hello, '$my_name' !'
greeting_3='hello, ${my_name} !'
# greeting_2="hello, Kaisyouu !"
# greeting_3="hello, ${my_name} !"
```

字符串操作：

```bash
# 字符串长度
string="abcd efg"
echo ${#string}			# 输出 8

# 提取子字符串
echo ${string:1:5}	# 输出 bcd e

# 查找子字符串
echo `expr index "$string" cd`	# 输出3
```

数组操作：

```bash
# 定义数组
array_name=(value0 value1 value2 value3)

# 读取数组
valuen=${array_name[n]}

# 获取数组长度
length=${#array_name[@]}
length=${#array_name[*]}

# 获取数组单个元素长度
lengthn=${#array_name[n]}
```



#### 2.2 传递参数

| 参数处理 | 说明                                                         |
| -------- | ------------------------------------------------------------ |
| $#       | 传递到脚本的参数个数                                         |
| $*       | 以一个单字符串显示所有向脚本传递的参数。<br/>如"$*"用「"」括起来的情况、以"$1 $2 … $n"的形式输出所有参数。 |
| $$       | 脚本运行的当前进程ID号                                       |
| $!       | 后台运行的最后一个进程的ID号                                 |
| $@       | 与$*相同，但是使用时加引号，并在引号中返回每个参数，用空格分隔 |
| $-       | 显示Shell使用的当前选项，与set命令功能相同。                 |
| $?       | 显示最后命令的退出状态。0表示没有错误，其他任何值表明有错误。 |



#### 2.3 运算符

1. 算数运算符

   原声bash不支持基本数学运算，而是通过awk和expr等工具来实现，例如:

   ```bash
   val=`expr $a + $b`
   val=`expr $a \* $b`	# 乘号前面需要加反斜杠
   ```

2. 关系运算符

   关系运算只支持数字和值为数字的字符串：

   * -eq 检测两个数是否相等，相等返回 true
   * -ne 检测两个数是否不相等，不相等返回 true
   * -gt 检测左边的数是否大于右边的，如果是，则返回 true
   * -lt 检测左边的数是否小于右边的，如果是，则返回 true
   * -ge 检测左边的数是否大于等于右边的，是则返回 true
   * -le 检测左边的数是否小于等于右边的，是则返回 true

3. 布尔运算符

   * ! 非运算
   * -o 或运算
   * -a 与运算

4. 逻辑运算符与C++相同

5. 字符串运算符

   * = 检测两个字符串是否相等，相等返回 true
   * != 检测两个字符串是否不相等，不相等返回 true
   * -z 检测字符串长度是否为0，为0返回 true
   * -n 检测字符串长度是否不为 0，不为 0 返回 true
   * $ 检测字符串是否不为空，不为空返回 true

6. 文件测试运算符

   用于检测Unix文件的各种属性，[描述参考runoob](https://www.runoob.com/linux/linux-shell-basic-operators.html)

#### 2.4 echo

echo用于显示字符和变量，唯一需要注意的是换行，例如：

```bash
echo -e "OK! \n"	# -e开启转义
echo -e "OK! \c"	# \c不换行
```



#### 2.5 流程控制

1. if else

   if else可以使用`[...]`或`((...))`作为条件判断句，写在一行则用分号隔开，以下为几个例子：

   ```bash
   if [$a == $b]
   then
   	...
   elif (($a > $b))	# 使用括号可以直接写>和<
   then
   	...
   elif [$a -lt $b]; then	# 写作一行用分号分隔
   	...
   else
   	...
   fi
   ```

2. for

   ```bash
   for i in 1 2 3 4 5
   do
   	echo "i=$i"
   done
   ```

3. while

   ```
   i=1
   while (($i<=5))
   do
   	echo "i=$i"
   	let "i++"	# Bash let命令
   done
   ```



#### 2.6 函数

shell中函数定义格式如下：

```bash
[ function ] funname [()]

{

    action;

    [return int;]

}
```

函数传递参数如下：

```bash
funWithParam(){
    echo "第一个参数为 $1 !"
    echo "第二个参数为 $2 !"
    echo "第十个参数为 $10 !"
    echo "第十个参数为 ${10} !"
    echo "第十一个参数为 ${11} !"
    echo "参数总数有 $# 个!"
    echo "作为一个字符串输出所有参数 $* !"
}
funWithParam 1 2 3 4 5 6 7 8 9 34 73
```

**注：函数return的结果需要用`$?`获取**



### 3. 应用

#### 3.1 交互会话工具Expect

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



#### 3.2 利用分界符输入

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



#### 3.3 FTP（written by jhlu）

"ftp" - 网络文件传输程序
	功能概述: 
		允许用户和另一个网络远程站点之间相互传输文件
		ftp host表示连接服务器host; 也可以省略ftp, 在ftp命令行上用open命令连接服务器
		注意 提示'using binary mode to transfer files'并非表示当前是二进制模式

	用法: 
		ftp [-pinegvd] [host] [port]
	
	说明: 
		1. 主动模式和被动模式的区别: http://www.cnblogs.com/xiaohh/p/4789813.html
		2. 自动登录: 自动登录时ftp程序会检查用户家目录下的.netrc文件中的ftp服务器的账户条目. 如果没有条目存在则ftp程序提示输入用户名(默认为客户端当前用户)和密码. 
	选项: 
		-i	关闭交互模式. 包括但不止多文件传输
		-v	程序运行时显示详细的处理信息
		-d	允许调试、显示客户机和服务器之间传递的全部ftp命令
		-n	关闭自动登录功能. 不会主动提示用户输入用户名和密码, 也不会自动读取文件填写用户名/密码. 常用于脚本
		-g	禁止文件名通配符和tab补足
		-m	??针对多被动模式下的多家目录用户
		-e	禁止编辑命令和记录历史命令
		-p	用被动(passive)模式传输数据. 但现在为了安全都使用主动(port)模式. 保留这个选项只是出于兼容性的考虑. 
	
	ftp命令: 
		//ftp命令都支持缩写, 只要不和其他命令冲突, ftp都能够识别, 例如: binary可以写成bi, bye可以写成by. 
		'连接/断开'
		open IP [port] 建立指定ftp服务器连接,可指定连接端口
		user username [password] [account] 向远程主机表明自己的身份
			username 登录远程计算机所使用的用户名
			password username 的密码. 如果省略, ftp 会提示输入密码
			account 登录到远程计算机所使用的帐户. 如果省略, ftp 会提示您输入帐户. 
		account [password]提供登录远程系统成功后访问系统资源所需的补充口令. ??例子
		close 中断与远程服务器的ftp会话(与open对应). 但不退出ftp命令行. 
		disconnection同close. 
		bye 退出ftp会话过程. 
		quit同bye,退出ftp会话. 
		exit 同bye,退出ftp会话. 
	
		'远程命令'
		cd		进入远程主机目录. 
		cdup	相当于cd ..
		pwd		显示远程主机的当前工作目录. 
		ls		显示远程目录下文件. ls -l显示详细信息. 也可以带pattern. 但不能同时有-l和pattern 
		//ls也无法精准指定文件
		dir [rfile][lfile] 
			显示远程主机文件/目录的详细信息(相当于: ls -l),并将结果重定向到本地lfile
			前者省略则默认当前目录, 后者省略则输出到stdout. 
			支持通配符, 因此可以查看多个文件的详细信息 
		mdir	与dir类似,但可指定多个远程文件, 即mdir rfile1 rfile2 ... rfileN lfile
		mkdir	在远程主机中创建一个目录
		rmdir	删除一个远程主机空目录. 隐藏文件都不能有(.和..不算)
		delete	删除一个远程主机文件
		mdelete	删除远程主机的多个文件, 但会提示是否确定删除
		rename 更改远程主机文件名. 如果新文件名已存在则覆盖(删除)原文件
		chmod 将远程主机文件file的权限设置为mode. 同site chmod //只能用数字模式不能用符号模式
		umask 查看或设置远程服务器的umask. 同site umask
		rstatus 若未指定文件名,则显示远程主机的状态,否则显示文件状态(和ls显示的内容一样). 
		nlist [rfile] [lfile]	显示远程主机rfile的文件名清单, 并存入本地的lfile. 如果rfile是目录, 则列出目录下的文件, 如: rfile/file1
			rfile 省略, 则默认显示当前目录下的文件清单
			lfile 省略, 则默认输出到stdout
		mls		同nlist,但可指定多个文件名. 
		size 显示远程主机单个文件大小, 不支持通配符 
		modtime 显示远程主机文件的最后修改时间
		idle [seconds] 将远程服务器的休眠计时器设为[seconds]秒. 对应vsftpd.conf中的idle_session_timeout
		??测试发现很多系统中都用不了idle命令, 即便ftp命令help能查到idle命令.
		rhelp 请求获得远程主机的帮助. ??相当于quote help
		system 显示远程主机的操作系统类型. 同quote syst
	
		'本地命令'
		lcd [dir] 将本地工作目录切换至dir, 省略dir时显示当前本地工作目录. # !cd dir 没报错, 但ftp中的本地路径没有变化
		status 显示当前ftp状态. 
	
		'传输命令'
		put [lname] [rname]		将本地文件传送至远程主机. 省略rname, 则使用lname, 都省略则ftp提示输入lname rname
		send					同put. 
		append [lname] [rname]	将本地文件lname追加到远程主机文件rname. 若未指定rname,则使用lname
		get [rfile] [lfile]		将远程主机的文件rfile复制为本地为lfile. 如果省略lfile, 则使用lfile
		recv					同get
		mput					将多个文件传输至远程主机
		mget					传输多个远程文件
		newer [rfile] [lfile] 远程rfile比本地lfile更新则重传该文件. 
			lfile省略, 则默认lfile和rfile同名
			rfile和lfile都省略, 则ftp提示输出rfile和lfile
		restart marker从指定的标志marker处,重新开始get或put. 如: restart 130 ??什么鬼
		regetremote 类似于 get ,但若存在,则从上次传输中断处续传. 
	
		'各种设置'
		//binary模式不对数据进行任何处理, ASCII模式要进行回车字符的转换. 
		ascii	使用ascii类型传输方式(文本传送)
		cr		使用ascii方式传输文件时,将回车换行转换为回行. 
		binary	使用二进制文件传输方式(应用程序等文件传送). 默认传输方式. //Windows默认使用Ascii模式
		image	设置二进制传输方式(同binary)
		type	设置文件传送类型, 例如: type ascii. 单独type则显示当前的文件传输类型
		prompt	设置多个文件传输时的交互提示. 
		glob	关/开mdelete、mget、mput的文件名扩展. 关闭时相当于ftp -g
		verbose 同命令行的－v参数,即设置详尽报告方式,ftp服务器的所有响应都将显示给用户,缺省为on.
		debug	设置调试方式,显示发送至远程主机的每条命令. 
		case	在使用mget时, 是否将远程主机文件名中的大写转为小写字母
		hash	每传输1K,打印一个#. 
		passive	进入被动传输方式. 
		bell	每个命令执行完毕后计算机响铃一次. 
		form	将文件传输方式设置为format,缺省为file方式 ??提示只支持non-print, 可用格式和服务器有关吗
		mode	将文件传输方式设置为mode－name,缺省为stream方式. ??提示只支持stream, 可用模式和服务器有关吗
	
		'辅助'
		help [cmd]显示ftp所有内部命令列表; help cmd显示cmd的帮助信息,如help get. 
		? 同help. 
		! 调用shell或者执行shell命令. 
			1. 在ftp命令行上调用交互shell, 在交互shell中exit可以退回ftp命令行. 
			2. !cmd为执行指定shell命令行命令, 结束后自动退回ftp命令行. //特别有用
		macdef 按照提示定义一个宏,遇到macdef下的空行时,宏定义结束. //所谓宏可能和shell的命令别名差不多. 
		$ 执行macdef定义的宏定义, 例如: $name
	
		nmap [inpattern outpattern] 设置文件名映射机制, 用于文件传输时文件名的变幻. 当参数省略时, 表示关闭文件映射; 否则就是表示设置了映射机制. 当使用mput/put/mget/get传输文件且没有指定远程主机/本地主机上的文件名时, ftp通过映射设置生成新的文件名. 通常用于和非unix主机进行ftp文件传输的情况. 映射把inpattern转换为outpattern. inpattern是原文件的模板, outpattern是新文件的模板. pattern中可以使用$1 $2...$9来表示变量. $0表示原文件名. 例如: 
			inpattern是$1.$2, 原文件名是mybook.txt, 则$1是mybook, $2是txt
			[$1,$2] 表示如果$非空则整个表达式为$1, 否则整个表达式是$2
			nmap $1.$2.$3 [$1,$2].[$2,file] 把原文件名按照模型$1.$2.$3拆解再组装成[$1,$2].[$2,file]
			//太过深入知识点的省略
		ntrans [inchars [outchars]]设置文件名字符的翻译机制. 参数省略表示关闭字符翻译机制. 
			例如: 
			ntrans L R, 则文件名LL将变为RR. 
			ntrans AB C, 则文件名的A会替换为C, B被删除. 
		proxy ftp-command 在次要控制连接中执行一个ftp命令. 该命令允许同时连接两个ftp服务器来在两个服务器间传输文件. 第一个proxy命令应该是open来建立一个次要控制连接. 'proxy ?'可以查看在次要控制连接中可以用的ftp命令. 以下ftp命令在次要控制连接(proxy后面)中和主要控制连接中表现不同: //相当于客户端代理了次服务器
			open在自动登录进程中不会定义新宏; 
			close不会擦除存在的宏定义; 
			get/mget是从主服务器传文件到次服务器; 
			put/mput/append是从次服务器传文件到主服务器. 
			这种第三方的文件传输依赖于次服务器上的ftp协议PASV命令. 
		quote arg1,arg2……	将参数逐字发至远程ftp服务器. quote支持的子命令可以用quote help查看, 部分子命令的使用参考: http://blog.csdn.net/qq981378640/article/details/52265835
			abor	中断传输
		reset 清除回答队列. ??
		runique 设置文件名唯一性存储,若文件存在,则在原文件后加后缀. 
		sunique 将远程主机文件名存储设置为唯一(与runique对应). 
		sendport 设置PORT命令的使用. 
		site arg1,arg2……将参数作为SITE命令逐字发送至远程ftp主机
			site help	查看site支持的所有子命令
			site umask	查看或设置远程服务器的umask 
			??初始umask好像和shell中的不同, 修改profile文件或者umask都无法让site umask的初始值变化
			site chmod	设置远程服务器文件的权限. 只支持八进制数模式, 不支持符号模型. 
		struct 将文件传输结构设置为缺省时使用stream结构. 
		tenex 将文件传输类型设置为TENEX机所需的类型. 
		tick 设置传输时的字节计数器. 
		trace 设置包跟踪. 

