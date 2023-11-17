Download source file
```
┌──(stupidhacker㉿kali)-[~/Downloads/pico/tmp]
└─$ wget https://artifacts.picoctf.net/c/513/picker-I.py
--2023-11-17 12:34:00--  https://artifacts.picoctf.net/c/513/picker-I.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 108.157.14.31, 108.157.14.48, 108.157.14.62, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|108.157.14.31|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 3419 (3.3K) [application/octet-stream]
Saving to: ‘picker-I.py’

picker-I.py                  100%[==============================================>]   3.34K  --.-KB/s    in 0s      

2023-11-17 12:34:01 (45.4 MB/s) - ‘picker-I.py’ saved [3419/3419]
```
Check the source code and pay attention to this function
```python
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
Seeing that the server will run the function input
```
┌──(stupidhacker㉿kali)-[~]
└─$ nc saturn.picoctf.net 57841
Try entering "getRandomNumber" without the double quotes...
==> getRandomNumber
4
Try entering "getRandomNumber" without the double quotes...
==> help

Welcome to Python 3.8's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.8/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> print
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

help> quit

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
Try entering "getRandomNumber" without the double quotes...
==> win
0x70 0x69 0x63 0x6f 0x43 0x54 0x46 0x7b 0x34 0x5f 0x64 0x31 0x34 0x6d 0x30 0x6e 0x64 0x5f 0x31 0x6e 0x5f 0x37 0x68 0x33 0x5f 0x72 0x30 0x75 0x67 0x68 0x5f 0x62 0x35 0x32 0x33 0x62 0x32 0x61 0x31 0x7d 
Try entering "getRandomNumber" without the double quotes...
==> quit           
```
The flag in hex format: ```0x70 0x69 0x63 0x6f 0x43 0x54 0x46 0x7b 0x34 0x5f 0x64 0x31 0x34 0x6d 0x30 0x6e 0x64 0x5f 0x31 0x6e 0x5f 0x37 0x68 0x33 0x5f 0x72 0x30 0x75 0x67 0x68 0x5f 0x62 0x35 0x32 0x33 0x62 0x32 0x61 0x31 0x7d```

The flag: ```picoCTF{4_d14m0nd_1n_7h3_r0ugh_b523b2a1}```
