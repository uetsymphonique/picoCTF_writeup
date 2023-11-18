Download file:
```commandline
wget https://artifacts.picoctf.net/c/47/bbbbloat
```
Decompile with Ghidra:
![image](https://github-production-user-asset-6210df.s3.amazonaws.com/89717384/283989860-c7c89967-b0fd-4b5f-8e3c-4870375bf507.png)
Concentrate on function ```FUN_00101307``` to realize that the number to obfuscate the input of the ```bbbbloat``` file is ```0x86187```(549225)
```
┌──(stupidhacker㉿kali)-[~/Downloads/pico/tmp]
└─$ chmod +x bbbbloat      
                                                                                                                                                                                                                                           
┌──(stupidhacker㉿kali)-[~/Downloads/pico/tmp]
└─$ ./bbbbloat  
What's my favorite number? 549255 
picoCTF{cu7_7h3_bl047_44f74a60}
```