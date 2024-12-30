# 테스트 케이스의 개수 t를 입력받는다.
# 테스트 케이스만큼 반복:
#     암호화된 메세지를 입력받는다
#     변환 규칙을 입력받는다(26글자 알파벳 대응)
#     변환 규칙에 따른 암호화전 메세지를 출력한다.(공백도 출력)

def encrypt_char(crypt_char, crypt_rule):
    encrypted_rule = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if crypt_char == ' ':
        return ' '
    encrypted_char = crypt_rule[encrypted_rule.find(crypt_char)]
    return encrypted_char

t = int(input())
for i in range(t):
    crypt_message = input()
    crypt_rule = input()
    for j in range(len(crypt_message)):
        print(encrypt_char(crypt_message[j], crypt_rule), end='')
    print()