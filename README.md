# getpass
A python 3 script that creates a file with all known WiFi Passwords and saved passwords on Chrome.

# Information

Google Chrome stores all passwords you saved by pressing 'REMEMBER ME' in a database at
 >Appdata\Local\Google\Chrome\User Data\Default\Login Data
 
 The scrypt simply finds all known WiFi-s and their passwords, all Chrome passwords stored in database, and it creates a txt file with all the information gathered.
 The txt file will be created at the same directory where the scrypt is executed.
 
 On Windows, install [PyWin32](https://sourceforge.net/projects/pywin32/) before running the scrypt

### Running

Run the scrypt with the following command:
```sh
python getpass.py
```
