Download source:
```commandline
wget https://artifacts.picoctf.net/c/314/imp.red
```
I just solved the problem accidentally when trying to modify the ```imp.red```, from the original:
```
┌──(stupidhacker㉿kali)-[~/Downloads/pico/tmp]
└─$ cat imp.red               
;redcode
;name Imp Ex
;assert 1
mov 0, 1
end
```
To:
```
┌──(stupidhacker㉿kali)-[~/Downloads/pico/tmp]
└─$ cat imp.red               
;redcode
;name Imp Ex
;assert 1
mov 1, 0
end
```
Connect to the server
```
┌──(stupidhacker㉿kali)-[~/Downloads/pico/tmp]
└─$ nc saturn.picoctf.net 60081 < imp.red

;redcode
;name Imp Ex
;assert 1
mov 1, 0
end
Submit your warrior: (enter 'end' when done)

Warrior1:
;redcode
;name Imp Ex
;assert 1
mov 1, 0
end

Rounds: 100
Warrior 1 wins: 0
Warrior 2 wins: 100
Ties: 0
You did it!
picoCTF{h3r0_t0_z3r0_4m1r1gh7_e1610ed2}
```
The flag: ```picoCTF{h3r0_t0_z3r0_4m1r1gh7_e1610ed2}```