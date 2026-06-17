# 敏感数据库  
# 敏感路径比较多，这里只选几个比较关键的，可作为自定义内容添加。
# 基于操作的敏感文件不同，可以大概判断出攻击者实施该步骤的意图，但在本研究不做过多解释。
# 如果关注系统实体，也会有很多进程常被用来发起攻击，如powershell和wmic等，但该部分被我们放在敏感命令中检测，在敏感路径中不考虑。
SenDirLinux = ['/etc/','/root/.bash_history','/proc','/bin/bash','/bin/dash','uname']
SenInsLinux = ['wget','scp','python','perl','uname','lsmod','systemctl','curl','procstat','/bin/bash','/bin/dash','uname','/bin/sh']

SenDirWindows = ['C:/Windows/system.ini','C:/Windows/PFRO.log','C:/Windows/SysWOW64','lsass.exe','HKLM',"c:/programdata/microsoft/crypto","c:/windows/system32/config","c:/windows/security","c:/windows/microsoft.net/framework","c:/windows/servicing","c:/windows/inf",'/appdata/roaming/microsoft/systemcertificates/','c:/programdata/microsoft/devicestage']
# 在windows体系中，只要想拿到域管/本地管理员级别的横向移动凭据，几乎绕不开对 lsass.exe 的读取
SenInsWindows =['lsass.exe','powershell','msiexec','mahta.exe','wmic','rundll32.exe','python','whoami','systeminfo','reg query','ipconfig']