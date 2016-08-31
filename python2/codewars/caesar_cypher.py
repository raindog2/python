def encryptor(key, message):
    if message == '': return ''
    else:
        message = list(message)
        for c in message:
            if c.isalpha:
                if c.islower:
                    if 97 <= (ord(c) + key) <= 122:
                        message[message.index(c)] = chr(ord(c) + key)
                    elif (ord(c) + key) < 97: 
                        message[message.index(c)] = chr(ord(c) + key + 26)
                    else: 
                        message[message.index(c)] = chr(ord(c) + key -26)
                else:
                    if 65 <= (ord(c) + key) <= 90:
                        message[message.index(c)] = chr(ord(c) + key)
                    elif (ord(c) + key) < 65: 
                        message[message.index(c)] = chr(ord(c) + key + 26)
                    else: 
                        message[message.index(c)] = chr(ord(c) + key -26)
            else: 
                message[message.index(c)] = c
    print message
    message = "".join(message)
    return message

def main():
    encryptor(13, 'Caesar Cipher')

main()
