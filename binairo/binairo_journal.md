# Jeu du Binairo
# Compléter ici (noms, groupe, contenu fichier, date)
# Mamadou Radjaye Sow, le 28/11/2025 — Traité du Binairo



# Journal de développement du Binairo

## Jour 1 - 28/11/2025
**Activité :** Début du développement  

- J’ai commencé par coder la **vérification des cases** : droit, gauche, en haut et en bas.
- Objectif : détecter rapidement si une case adjacente est identique à la case sélectionnée.
- J’ai ajouté le **comptage des 0 et des 1** dans chaque ligne pour contrôler l’équilibre nécessaire dans le jeu.

---

## Jour 2 - 29/11/2025
**Activité :** Vérification des alignements  

- J’ai continué avec **l’alignement identique**.
- Ici, au lieu de comparer les listes entre elles, je comparais le **contenu des cases** entre eux.


---

## Jour 3 - 30/11/2025
**Activité :** Initialisation et fonction `gagner()`  

- J’ai continué avec l’**initialisation de la grille vide**, permettant de créer une base de jeu prête à recevoir des valeurs.
- J’ai codé la **grille avec les valeurs inchangeables**, correspondant aux cases fixes fournies dans le fichier de configuration.
- Début de la **fonction `gagner()`**, qui vérifie si le joueur a rempli correctement la grille selon les règles :
  - Égalité du nombre de 0 et 1 par ligne
  - Pas d’alignement identique
  - Pas de triplets dans les lignes et colonnes

---

## Jour 4 - 01/12/2025
**Activité :** Fonction principale et premiers tests  

- J’ai terminé la **fonction principale `jouer()`**, qui gère :
  - L’affichage de la grille
  - La saisie des coordonnées et des valeurs
  - La protection des cases inchangeables
  - Les mises à jour de la grille et l’affichage après chaque coup
- J’ai commencé à **jouer et tester le jeu** pour voir le comportement réel et détecter les erreurs.

---

## Jour 5 - 02/12/2025
**Activité :** Débogage et correction des fonctions critiques  

- Dès que je commençais à jouer et qu’un comportement inattendu apparaissait, je retournais dans la fonction **`a_gagner()`**.
- J’ai augmenté les tests et j’ai découvert des **insuffisances dans plusieurs fonctions** :
  - `position_trouver`
  - `alignement_identique`
  - `est_identique_audela`
- J’ai testé manuellement : ça fonctionnait, mais les tests à l’ordinateur échouaient.
- Après plusieurs heures sans solution, j’étais **découragé**. Un long repos m’a permis de regagner espoir.
- Stratégie utilisée :
  - Commenter certaines parties du code pour **isoler le vrai problème**
  - Identifier exactement où les règles du jeu étaient mal appliquées
- Corrections apportées :
  - Dans **`alignement_identique`**, comparaison des **listes entières** plutôt que des contenus individuels
  - Même correction appliquée pour les colonnes
  - Dans **`est_identique_audela`**, inclusion de la case sélectionnée dans les vérifications
  - Dans **`position_trouver`**, correction des conditions pour détecter correctement les triplets et doublons
- Tests intensifs réalisés sur toutes ces fonctions.
- Une erreur finale provenait d’un mauvais **index (1 à la place de i)**, résolue avec l’utilisation du **débogueur**.
- Résultat final :
  - Le jeu fonctionne comme prévu
  - Le joueur peut modifier les cases tant qu’il n’a pas gagné
  - Les cases inchangeables sont protégées
  - La détection de victoire est correcte et fiable
- Le processus m’a permis de comprendre l’importance de **tester étape par étape**, de **commenter pour isoler les problèmes**, et d’utiliser un **débogueur** pour résoudre les erreurs les plus subtiles.

---

## Conclusion

- Ce projet m’a permis de pratiquer :
  - La logique de vérification de contraintes complexes
  - La gestion des grilles en Python
  - Le débogage méthodique et les tests intensifs
- Le Binairo fonctionne correctement et respecte les règles du jeu.

