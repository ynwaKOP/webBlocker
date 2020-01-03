import time
from datetime import datetime


host = r"/etc/hosts"  ##the real system host path. but don't want to change it.

#host = "hosts"
web_list = {"www.facebook.com","facebook.com", "www.microsoft.com","microsoft.com"}
redirct = "127.0.0.1"

while True:
    if datetime(datetime.now().year, datetime.now().month,
                datetime.now().day,0) < datetime.now() < datetime(datetime.now().year,datetime.now().month,
                                                                  datetime.now().day, 1):
        with open(host, 'r+') as file:
            sys_host = file.read()

            for web in web_list:
                 if web in sys_host:
                     pass
                 else:
                     file.write(redirct+" "+web+"\n")
        print("😞" + "working hour")




    else:
        with open(host, "r+") as file:
            sys_host = file.readlines()
            file.seek(0)

            for line in sys_host:
                if not any(web in line for web in web_list):
                    file.write(line)
            file.truncate()

        print("🤯"+"fun hour")

    time.sleep(4)