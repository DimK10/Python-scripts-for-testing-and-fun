text = "Travhf jvgubhg rqhpngvba vf yvxr fvyire va gur zvar"

for i in range (0, 26):
    print("====test %d" % i)
    decrypt = ""
    for c in text:
        if ord(c)>= ord("a") and ord(c) <= ord("z"):
            decrypt += chr((((ord(c) - ord("a"))+i)%26)+ord("a"))
        elif ord(c) >= ord("A") and ord(c) <= ord("Z"):
            decrypt += chr((((ord(c) - ord("A"))+i)%26)+ord("A"))
        else:
            decrypt += c

    print(decrypt)

#====test 13
#Genius without education is like silver in the mine
            
    
