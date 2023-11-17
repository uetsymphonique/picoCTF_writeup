Download the apk file
```
┌──(stupidhacker㉿kali)-[~/Downloads/pico/tmp]
└─$ wget https://artifacts.picoctf.net/c/449/timer.apk
--2023-11-17 11:53:46--  https://artifacts.picoctf.net/c/449/timer.apk
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 108.157.14.62, 108.157.14.48, 108.157.14.31, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|108.157.14.62|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 4678467 (4.5M) [application/octet-stream]
Saving to: ‘timer.apk’

timer.apk                                                  100%[========================================================================================================================================>]   4.46M  3.00MB/s    in 1.5s    

2023-11-17 11:53:49 (3.00 MB/s) - ‘timer.apk’ saved [4678467/4678467]

```
Decompile the apk file
```
┌──(stupidhacker㉿kali)-[~/Downloads/pico/tmp]
└─$ apktool d timer.apk 
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
I: Using Apktool 2.6.0 on timer.apk
I: Loading resource table...
I: Decoding AndroidManifest.xml with resources...
I: Loading resource table from file: /home/stupidhacker/.local/share/apktool/framework/1.apk
I: Regular manifest package...
I: Decoding file-resources...
I: Decoding values */* XMLs...
I: Baksmaling classes.dex...
I: Baksmaling classes3.dex...
I: Baksmaling classes2.dex...
I: Copying assets and libs...
I: Copying unknown files...
I: Copying original files...
```
Find the flag
```
┌──(stupidhacker㉿kali)-[~/Downloads/pico/tmp/timer]
└─$ grep "picoCTF" *
apktool.yml:  versionName: picoCTF{t1m3r_r3v3rs3d_succ355fully_17496}
grep: kotlin: Is a directory
grep: original: Is a directory
grep: res: Is a directory
grep: smali: Is a directory
grep: smali_classes2: Is a directory
grep: smali_classes3: Is a directory
```