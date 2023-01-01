import random

def generate_poem():
  # Liste de mots pour le poème
  nouns = ["chat", "oiseau", "arbre", "fleur", "ciel", "nuage"]
  verbs = ["courir", "voler", "grandir", "fleurir", "briller"]
  adjectives = ["beau", "joyeux", "doux", "coloré"]
  adverbs = ["lentement", "rapidement", "calmement", "évident", "négligent"]

  # Génère un poème de 4 vers
  poem = []
  for i in range(4):
    # Génère un vers en utilisant une rime en "-at"
    if i % 2 == 0:
      line = f"Le {random.choice(nouns)} {random.choice(verbs)} {random.choice(adverbs)}"
      poem.append(line)
    else:
      line = f"Avec un {random.choice(adjectives)} {random.choice(nouns)}"
      poem.append(line)

  return "\n".join(poem)

# Génère un poème
for x in range(3):
  poem = generate_poem()
  print(poem)