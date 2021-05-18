from Crypto.Hash import HMAC, SHA256

def szyfruj():
    haslo = input("Podaj hasło:")
    bhaslo = haslo.encode()
    h = HMAC.new(bhaslo, digestmod=SHA256)
    return h.hexdigest()

def sprawdz(podpis):
    haslo = input("Podaj hasło:")
    bhaslo = haslo.encode()
    h = HMAC.new(bhaslo, digestmod=SHA256)
    return h.hexdigest() == podpis

digest_1 = szyfruj()
print(digest_1)
wynik = sprawdz(digest_1)

if wynik:
    print("Hasło poprawne")
else:
    print("hasło błędne")

# Podaj hasło:Adam200202
# '3e2bdfb2c05039b8324a12b8aae2acce74f5f4a781fa0ac43b6b8ba293cb3ad3'
# >>> szyfruj()
# Podaj hasło:Tajne5673
# '3442053d04fe5a4d0ed2c01fa95f4d8f9b3845d790f5d1c48d410a6245f65a56'
# >>> szyfruj()
# Podaj hasło:Hasełko211
#'cf72c1d2c0c8ebcddbd6d54c64a71e780a6efa9afb110fc0879237df6ee07748'
