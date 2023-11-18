Download files:

```commandline
wget https://jupiter.challenges.picoctf.org/static/48babf8f8c4c6b8baf336680ea5b9ddf/rev https://jupiter.challenges.picoctf.org/static/48babf8f8c4c6b8baf336680ea5b9ddf/rev_this
```

Using Ghidra to decompiler the ```rev``` file:
![image](https://github-production-user-asset-6210df.s3.amazonaws.com/89717384/283988146-de886f82-cd04-4f0a-89a7-416ef8686e80.png)
Pay attention to the main function

```cpp
void main(void)

{
  size_t sVar1;
  char local_58 [23];
  char local_41;
  int local_2c;
  FILE *local_28;
  FILE *local_20;
  uint local_14;
  int local_10;
  char local_9;
  
  local_20 = fopen("flag.txt","r");
  local_28 = fopen("rev_this","a");
  if (local_20 == (FILE *)0x0) {
    puts("No flag found, please make sure this is run on the server");
  }
  if (local_28 == (FILE *)0x0) {
    puts("please run this on the server");
  }
  sVar1 = fread(local_58,0x18,1,local_20);
  local_2c = (int)sVar1;
  if ((int)sVar1 < 1) {
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  for (local_10 = 0; local_10 < 8; local_10 = local_10 + 1) {
    local_9 = local_58[local_10];
    fputc((int)local_9,local_28);
  }
  for (local_14 = 8; (int)local_14 < 0x17; local_14 = local_14 + 1) {
    if ((local_14 & 1) == 0) {
      local_9 = local_58[(int)local_14] + '\x05';
    }
    else {
      local_9 = local_58[(int)local_14] + -2;
    }
    fputc((int)local_9,local_28);
  }
  local_9 = local_41;
  fputc((int)local_41,local_28);
  fclose(local_28);
  fclose(local_20);
  return;
}
```
Seeing that the cipher working by following steps:
+ The first 8 characters of ciphertext is the same as plaintext: ```picoCTF{```
+ With ```local_14``` is the index of the plaintext, from ```local_14 = 8```:
  - If ```local_14 & 1 == 0```(not divisible by 2), plus ```\x05```(5) into current character
  - If not, subtract the current character by 2
+ The last character is ```}```

Reverse the ciphertext:
```python
cipher_text = "picoCTF{w1{1wq8/7376j.:}"
tmp = ''
for i, c in enumerate(cipher_text[8:-1]):
    if i & 1 == 0:
        tmp += chr(ord(c) - 5)
    else:
        tmp += chr(ord(c) + 2)
print("picoCTF{" + tmp + "}")
```