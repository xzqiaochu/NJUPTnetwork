# 南京邮电大学校园网自动登录脚本 - 使用指南

1. 复制项目根目录下的NJUPTnetwork文件夹到C盘根目录

2. 修改 NJUPTnetwork.vbs，设置自己的账号密码

   >如果是NJUPT校园网的账号，正常填入账号即可
   >
   >如果是NJUPT-CMCC移动的账号，请在账号后面添加@cmcc后缀
   >
   >如果是NJUPT-CHINANET电信的账号，请在账号后面添加@njxy后缀

3. 按win+R，输入 shell:startup，回车会弹出一个目录，把 NJUPTnetwork.vbs 复制到这个目录下

这样，每次开机后，脚本会进入后台自动运行。一旦连接上校园网，便会自动登录（5秒以内）
如果想结束后台进程，双击 C:\NJUPTnetwork\stop.bat，手动启动双击 NJUPTnetwork.vbs