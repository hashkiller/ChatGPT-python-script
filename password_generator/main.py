import random
import string

def generate_password():
  # Génère un mot de passe de 8 caractères aléatoires
  password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
  return password

def check_password_security(password):
  # Vérifie si le mot de passe contient au moins un chiffre et une lettre majuscule et une lettre minuscule
  if any(char.isdigit() for char in password) and any(char.isupper() for char in password) and any(char.islower() for char in password):
    return True
  else:
    return False

# Génère un mot de passe aléatoire
password = generate_password()
print(f"Mot de passe généré : {password}")

# Vérifie la sécurité du mot de passe
if check_password_security(password):
  print("Le mot de passe est sécurisé.")
else:
  print("Le mot de passe n'est pas assez sécurisé. Il devrait contenir au moins un chiffre, une lettre majuscule et une lettre minuscule.")