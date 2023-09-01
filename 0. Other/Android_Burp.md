- Install android studio 
- Install openSSL
- Install burp
- Generate Burp CA 
- Add adb & emulator to the path
	- https://www.c-sharpcorner.com/article/how-to-addedit-path-environment-variable-in-windows-11/
- Android Studio > Virtual Device Manager > create a phone: Pixel 5 with Pie (28) android version
- Copy the CA to system as a root
	- I installed WSL on my Windows machine
	- Need to mount the path where the executable is: cd /mnt/path...
	- https://blog.ropnop.com/configuring-burp-suite-with-android-nougat

```cmd
C:\Users\2no\AppData\Local\Android\Sdk\platform-tools
C:\Users\2no\AppData\Local\Android\Sdk\emulator
```

List Android Studio - Virtual Device

```
➜ emulator.exe -list-avds
Pixel_3a_API_34_extension_level_7_x86_64
```

Run emulator with cmd 

```cmd
.\emulator.exe -avd Pixel_5_API_28 -writable-system
```

Adb list devices 

```cmd
adb devices
```

Adb shell 

```cmd
adb shell
```

If you choose a device with the playstore enabled, you'll not be able to root. 
Switch to root. 

```
su
```

Then go to the phone storage 

```
cd storage 
cd self 
cd primary 
```

To upload file to the phone 

```cmd
adb.exe push
```

Download 

```cmd
adb.exe pull
```

Convert the CA to PEM key

```
openssl x509 -inform DER -in cacert.der -out cacert.pem
openssl x509 -inform PEM -subject_hash_old -in cacert.pem |head -1 //on linux

notepad cacert.pem  // On windows first line is the hash

mv cacert.pem 9a5ba575.0
chmod 644 9a5ba575.0
```

To copy the certificate (!!make sure the phone emulator is on!!)

```cmd 
./emulator.exe -avd Pixel_5_API_28 -writable-system -http-proxy 127.0.0.1:8080
```
Once done, leave the terminal open and open a new one.
Note that the adb or emulator files should be called within their paths.
Make a copy of the certificate to the adb folder. It makes your life much easier.

```
./adb.exe root
./adb.exe remount
./adb.exe push ./<hash.O> /sdcard/
adb shell
# mv ~/<hash.O> /system/etc/security/cacerts
```


Acces WSL file from windows 

```
\\wsl$
```


[Aurora Store](https://f-droid.org/repo/com.aurora.store_47.apk) 

[Get APK](https://apkpure.com/fr/)  not legit be carefull ...