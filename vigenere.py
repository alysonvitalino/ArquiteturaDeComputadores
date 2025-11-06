def _shift_alpha(ch, shift):
    if 'a' <= ch <= 'z':
        base = ord('a')
        return chr((ord(ch) - base + shift) % 26 + base)
    if 'A' <= ch <= 'Z':
        base = ord('A')
        return chr((ord(ch) - base + shift) % 26 + base)
    return ch

def _key_shifts_from_text(key):
    shifts = []
    for c in key:
        if 'a' <= c <= 'z':
            shifts.append(ord(c) - ord('a'))
        elif 'A' <= c <= 'Z':
            shifts.append(ord(c) - ord('A'))
    return shifts

def vigenere_encrypt(texto, chave):
    shifts = _key_shifts_from_text(chave)
    if not shifts:
        raise ValueError("A chave deve conter letras.")
    out = []
    j = 0
    for c in texto:
        if c.isalpha():
            out.append(_shift_alpha(c, shifts[j % len(shifts)]))
            j += 1
        else:
            out.append(c)
    return ''.join(out)

def vigenere_decrypt(texto, chave):
    shifts = _key_shifts_from_text(chave)
    if not shifts:
        raise ValueError("A chave deve conter letras.")
    out = []
    j = 0
    for c in texto:
        if c.isalpha():
            out.append(_shift_alpha(c, (-shifts[j % len(shifts)]) % 26))
            j += 1
        else:
            out.append(c)
    return ''.join(out)

if __name__ == "__main__":
    texto = input("Texto: ")
    chave = input("Chave: ")
    modo = input("Digite E para encriptar ou D para decriptar: ").upper()
    if modo == "E":
        print("Criptografado:", vigenere_encrypt(texto, chave))
    elif modo == "D":
        print("Descriptografado:", vigenere_decrypt(texto, chave))
    else:
        print("Modo inválido.")
