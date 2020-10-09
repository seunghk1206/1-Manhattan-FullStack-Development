K_consonant = ['ㄱ','ㄴ','ㄷ','ㄹ','ㅁ','ㅂ','ㅅ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ','ㄲ','ㄸ','ㅃ','ㅉ']
K_vowel = ['ㅏ','ㅑ','ㅓ','ㅕ','ㅗ','ㅛ','ㅜ','ㅠ','ㅡ','ㅣ']
KC_encrypt = [format(each, 'b') for each in range(1, len(K_consonant)+1)]
KV_encrypt = ['R1','R2','L1','L2','U1','U2','D1','D2','RUDL1','RUDL2']
exception = ['ㅔ','ㅖ','ㅐ','ㅒ']
exception_encrypt = ['L1 + RUDL2', 'L2 + RUDL2', 'R1 + RUDL2', 'R2 + RUDL2']
print(KC_encrypt)
inp = input()
inp_encrypted = ''
answer = ''
for each in inp:
    if each in K_consonant:
        inp_encrypted = inp_encrypted + ' ' + KC_encrypt[K_consonant.index(each)]
    if each in K_vowel:
        inp_encrypted = inp_encrypted + ' ' + KV_encrypt[K_vowel.index(each)]
    if each in exception:
        inp_encrypted = inp_encrypted + ' ' + exception_encrypt[exception.index(each)]
    if each == ' ':
        inp_encrypted = inp_encrypted + ' / '
print(inp_encrypted, inp)
for each in range(len(inp_encrypted.split(' '))):
    answer += inp_encrypted.split(' ')[each]
    if each != len(inp_encrypted.split(' '))-1:
        answer += ' + '
for each in answer[3::].split('+ / +  + '):
    print(each)
print(answer[3::])