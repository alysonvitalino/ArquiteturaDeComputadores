def encode(plaintext: str, shift: int) -> str:
    result = []
    for ch in plaintext:
        if 'a' <= ch <= 'z':
            result.append(chr((ord(ch) - ord('a') + shift) % 26 + ord('a')))
        elif 'A' <= ch <= 'Z':
            result.append(chr((ord(ch) - ord('A') + shift) % 26 + ord('A')))
        elif '0' <= ch <= '9':
            result.append(chr((ord(ch) - ord('0') + shift) % 10 + ord('0')))
        else:
            result.append(ch)
    return ''.join(result)

def decode(ciphertext: str, shift: int) -> str:
    return encode(ciphertext, -shift)

while True:
    pt = input("Digite sua senha: ")
    qt = int(input("Digite quantas casa a cifra ira percorrer: "))
    ct = encode(pt, qt)
    print("Criptografia: ", ct)            
    print("Decodificação:", decode(ct, qt))
