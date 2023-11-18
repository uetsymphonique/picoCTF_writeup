import base64
import urllib.parse

encoded_string = "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm" + \
                 "JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2" + \
                 "JTM0JTVmJTM4JTM0JTY2JTY0JTM1JTMwJTM5JTM1"
base64_decoded_string = base64.b64decode(encoded_string).decode()
print(base64_decoded_string)
url_decoded_string = urllib.parse.unquote(base64_decoded_string)
print(url_decoded_string)
print('The flag is: picoCTF{' + url_decoded_string + '}')
