from Crypto.Hash import HMAC, SHA256

def szyfruj():
    haslo = input("Podaj hasło:")
    bhaslo = str.encode(haslo)
    h = HMAC.new(bhaslo, digestmod=SHA256)
    dg = h.hexdigest()
    return dg

def sprawdz(digest):
    haslo = input("Podaj hasło do weryfikacji:")
    bhaslo = str.encode(haslo)
    h = HMAC.new(bhaslo, digestmod=SHA256)
    dg = h.hexdigest()
    return dg == digest
        
d = szyfruj()
sprawdz(d)
