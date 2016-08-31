def encryptor(key, message):
    
    def lowerlet2int(c):
        return ord(c) - ord('a')
    def int2lowerlet(n):
        return chr(ord('a') + n)
        
    def upperlet2int(c):
        return ord(c) - ord('A')
    def int2upperlet(n):
        return chr(ord('A') + n)

    if message == '': return ''
    else:
        message = list(message)
        for i in range (len(message)):
            if message[i].isalpha():
                if message[i].islower(): 
                    message[i] = int2lowerlet((lowerlet2int(message[i]) + key) % 26)
                else:
                    message[i] = int2upperlet((upperlet2int(message[i]) + key) % 26)
            else: 
                message[i] = message[i]

    message = "".join(message)
    return message
