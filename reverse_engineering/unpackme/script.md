Download files: 
```commandline
wget https://artifacts.picoctf.net/c/205/unpackme-upx
``` 
Installing udx from github [upx](https://github.com/upx/upx/releases)

Using upx to unpack the ```unpackme-upx``` file:
```
┌──(stupidhacker㉿kali)-[~/upx-4.2.1-amd64_linux]
└─$ ./upx -d ~/Downloads/pico/tmp/unpackme-upx 
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2023
UPX 4.2.1       Markus Oberhumer, Laszlo Molnar & John Reiser    Nov 1st 2023

        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
   1006445 <-    379188   37.68%   linux/amd64   unpackme-upx

Unpacked 1 file.

```
Using Ghidra to decompiler the unpacked ```unpackme-upx```:
![image](https://github-production-user-asset-6210df.s3.amazonaws.com/89717384/284242487-6749c6db-bdc4-40a2-be03-10946475307e.png)

Focus on the ```main``` function to know the answer of the question ```What's my favourite number?``` is ```0xb83cb```(754635)

Run ```unpackme-upx```:
```
┌──(stupidhacker㉿kali)-[~/Downloads/pico/tmp]
└─$ ./unpackme-upx         
What's my favorite number? 754635
picoCTF{up><_m3_f7w_5769b54e}
```

The flag: ```picoCTF{up><_m3_f7w_5769b54e}```