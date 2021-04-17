def szyfruj():
    from Crypto.Hash import HMAC, SHA256
    haslo = input("Podaj hasło:")
    bhaslo = str.encode(haslo)
    h = HMAC.new(bhaslo, digestmod=SHA256)
    dg = h.hexdigest()
    print("dg", dg)
    return h.digest()

def sprawdz(digest):
    from Crypto.Hash import HMAC, SHA256
    haslo = input("Podaj hasło do weryfikacji:")
    bhaslo = str.encode(haslo)
    h = HMAC.new(bhaslo, digestmod=SHA256)
    dg = h.hexdigest()
    return h.verify(digest)
        
    
