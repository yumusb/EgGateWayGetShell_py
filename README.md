### EgGateWayGetShell_py



### 免责声明

由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。

### 使用

python3 eg.py urls.txt

### 目标

title:锐捷网络-EWEB网管系统  
~~port:4430~~

### 漏洞成因

```
<?php
    //查询用户是否上线了
    $userip = @$_POST['ip'];
    $usermac = @$_POST['mac'];
    
    if (!$userip || !$usermac) {
        exit;
    }
    /* 判断该用户是否已经放行 */
    $cmd = '/sbin/app_auth_hook.elf -f ' . $userip;
    $res = exec($cmd, $out, $status);
    /* 如果已经上线成功 */
    if (strstr($out[0], "status:1")) {
        echo 'true';
    }
?>
```

### 漏洞修复

替换本项目目录下的 guestIsUp.php 到 /tmp/html/guest_auth/guestIsUp.php。亦或者直接执行以下脚本

`wget -O /tmp/html/guest_auth/guestIsUp.php https://cdn.jsdelivr.net/gh/yumusb/EgGateWayGetShell_py/guestIsUp.php`
