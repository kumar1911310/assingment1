 k = k%26
    sk = ''
    for char in s:
        if char.isalpha() == True:
            if ord(char) >= 65 and ord(char) <= 90:
                if k + ord(char) <= 90:
                    sk += chr(ord(char) + k)
                else:
                    sk += chr(ord(char) + k - 90 + 64)
            elif ord(char) >= 97 and ord(char) <= 122:
                if k + ord(char) <= 122:
                    sk += chr(ord(char) + k)
                else:
                    sk += chr(ord(char) + k - 122 + 96)
        else:
            sk += char
    return sk