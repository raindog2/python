def alphabet_position(text):
    text = text.lower()
    result = ""
    nums = list(range(1,27))
    letts = []
    for i in range(ord('a'), ord('z')+1):
        letts.append(chr(i))        
    dicto = zip(letts, nums)
    for c in text:
        for (a,b) in dicto:
            if c == a: result = result + str(b) + " "
    result = result.replace(result[-1],"")
    return result

def main():
    print alphabet_position("Hello world")
    print alphabet_position("Mark Purcell")
    print alphabet_position("beaNs and Cornbread")

main()
