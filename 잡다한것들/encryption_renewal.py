K_consonant = ['ㄱ','ㄴ','ㄷ','ㄹ','ㅁ','ㅂ','ㅅ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
K_vowel = ['ㅏ','ㅑ','ㅓ','ㅕ','ㅗ','ㅛ','ㅜ','ㅠ','ㅡ','ㅣ']
KC_encrypt = [format(each, 'b') for each in range(1, len(K_consonant))]
KV_encrypt = ['R1','R2','L1','L2','U1','U2','D1','D2','RUDL1','RUDL2']
exception = ['ㅔ','ㅖ','ㅐ','ㅒ']
exception_encrypt = ['L1 + RUDL2', 'L2 + RUDL2', 'R1 + RUDL2', 'R2 + RUDL2']
print(KC_encrypt)
inp = [each for each in input()]
inp_encrypted = []
for each in inp:
    if each in K_consonant:
        inp_encrypted.append(' ' + KC_encrypt[K_consonant.index(each)])
    elif each in K_vowel:
        inp_encrypted.append(' ' + KV_encrypt[K_vowel.index(each)])
    elif each in exception:
        inp_encrypted.append(' ' + exception_encrypt[exception.index(each)])
print(inp_encrypted, inp)
for each in inp_encrypted:
    print(each, end = ' +')