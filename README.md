# Tool SearchDb

Ce script Python permet de rechercher un motif spécifique dans les fichiers d'un répertoire donné.

## Fonctionnalités

- Recherche de motifs dans les fichiers texte
- Supporte l'utilisation d'expressions régulières pour des recherches avancées
- Affiche les résultats avec des couleurs pour une meilleure lisibilité

## Utilisation

1. Assurez-vous d'avoir Python installé sur votre système.
2. Téléchargez ou clonez ce dépôt sur votre machine.
3. Naviguez jusqu'au répertoire où se trouve le script.
4. Exécutez le script en utilisant la commande suivante :
5. Suivez les instructions pour entrer le motif à rechercher.

## Configuration

Le script par défaut recherche dans le dossier "database". Vous pouvez modifier ce répertoire en modifiant la variable `folder` dans le script.

## Exemple

Supposons que vous souhaitiez rechercher le motif "example" dans les fichiers du dossier "database". Voici comment vous pouvez le faire :

1. Exécutez le script.
2. Entrez le motif à rechercher : `example`
3. Le script affichera les résultats de la recherche dans les fichiers du dossier "database".

## Remarques

- Ce script utilise des expressions régulières pour effectuer la recherche. Assurez-vous de saisir un motif valide pour obtenir des résultats précis.
- Les fichiers encodés de manière non standard peuvent provoquer des erreurs de décodage Unicode. Ces fichiers seront ignorés lors de la recherche.
