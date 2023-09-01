**Intercepting http traffic from an Android emulated phone using Burp Suite**

# Steps

1. Install android studio 
2. Install openSSL
3. Install burp
4. Generate Burp CA 
5. (OPTIONAL) Add adb & emulator to the path
	- https://www.c-sharpcorner.com/article/how-to-addedit-path-environment-variable-in-windows-11/
6. Android Studio > Virtual Device Manager > create a phone: Pixel 5 with Pie (28) android version
7. Copy the CA to system as a root
	- I installed WSL on my Windows machine
	- Need to mount the path where the executable is: cd /mnt/path...
	- https://blog.ropnop.com/configuring-burp-suite-with-android-nougat

```cmd
C:\Users\2no\AppData\Local\Android\Sdk\platform-tools
C:\Users\2no\AppData\Local\Android\Sdk\emulator
```

# 1. Run emulator with cmd 

```cmd
.\emulator.exe -avd Pixel_5_API_28 -writable-system
```

# 2. List Android Studio - Virtual Device

```
➜ emulator.exe -list-avds
Pixel_5_API_28
```

# 3. Convert the CA to PEM key

```
openssl x509 -inform DER -in cacert.der -out cacert.pem
openssl x509 -inform PEM -subject_hash_old -in cacert.pem |head -1 //on linux

notepad cacert.pem  // On windows first line is the hash

mv cacert.pem 9a5ba575.0
chmod 644 9a5ba575.0
```

# 4. Certificate
To copy the certificate (!!make sure the phone emulator is on!!)

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
# 5. Burp suite and Android emulator

- https://blog.yarsalabs.com/setting-up-burp-for-android-application-testing/
- https://medium.com/mii-cybersec/how-to-connect-burp-suite-to-an-android-emulator-9da19b0ad2c3

When setting up burpsuite's proxy, make sure to use your computer's IP address, not localhost. 

Then, on the phone emulator, use the IP address and the port you configured on burpsuite. 

# MISC

## Adb list devices 

```cmd
adb devices
```

Adb shell 

```cmd
adb shell
```

## If you choose a device with the playstore enabled, you'll not be able to root. 

Switch to root. 

```
su
```

## Then go to the phone storage 

```
cd storage 
cd self 
cd primary 
```

## To upload file to the phone 

```cmd
adb.exe push
```

Download 

```cmd
adb.exe pull
```

## Acces WSL file from windows 

```
\\wsl$
```


[Aurora Store](https://f-droid.org/repo/com.aurora.store_47.apk) 

[Get APK](https://apkpure.com/fr/)  not legit be carefull ...