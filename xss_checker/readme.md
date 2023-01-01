# XSS Checker

Ce projet a pour but de créer un outil qui permet de tester les sites Web pour la vulnérabilité à l'injection de code JavaScript (XSS).

**Il est important de noter que l'utilisation de payloads d'injection de code JavaScript pour accéder à des informations sensibles ou à des systèmes protégés sans autorisation est une violation de la loi dans de nombreux pays. De plus, cela peut causer des dommages à l'entreprise cible, tels que des fuites de données et des perturbations de service. Nous déconseillons fortement l'utilisation de ce projet à des fins illégales et vous encourageons à suivre les pratiques de sécurité éthiques et légales.**

## Prérequis

Pour utiliser ce projet, vous avez besoin de :

- Un système d'exploitation compatible (Linux, macOS, Windows)
- Python 3.6 ou supérieur
- La bibliothèque `requests` et `BeautifulSoup`

## Installation

Pour installer ce projet, suivez les étapes suivantes :

1. Téléchargez le code source du projet en cliquant sur le bouton "Clone or download"
2. Décompressez l'archive téléchargée
3. Ouvrez un terminal et naviguez jusqu'au répertoire décompressé
4. Exécutez la commande `pip install -r requirements.txt` pour installer les bibliothèques `requests` et `BeautifulSoup`

## Utilisation

Pour utiliser ce projet, suivez les étapes suivantes :

1. Ouvrez un terminal et naviguez jusqu'au répertoire du projet
2. Exécutez la commande `python xss_checker.py` en spécifiant l'URL à tester et le payload à utiliser en argument

## Contribuer

Si vous souhaitez contribuer à ce projet, veuillez suivre les étapes suivantes :

1. Fork the repository (https://github.com/your-username/xss-checker/fork)
2. Create your feature branch (git checkout -b my-new-feature)
3. Commit your changes (git commit -am 'Add some feature')
4. Push to the branch (git push origin my-new-feature)
5. Create a new Pull Request