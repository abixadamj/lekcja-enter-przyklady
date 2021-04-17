from Crypto.Hash import HMAC, SHA256
haslo = input("Podaj hasło:")
bhaslo = str.encode(haslo)
h = HMAC.new(bhaslo, digestmod=SHA256)
dg = h.hexdigest()
print(f"Skrót hasła: {dg}")
