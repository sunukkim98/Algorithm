import sys
input = sys.stdin.readline

while True:
    crypto_text = input().replace('\n', '')
    if crypto_text == 'END':
        exit(0)
    crypto_text = list(crypto_text)
    crypto_text.reverse()
    plain_text = ''.join(crypto_text)
    print(plain_text)