# Compléter ici (noms, groupe, contenu fichier, date)
# Mamadou Radjaye Sow, le 22/11/2025 — Traité du Jeu du Tic Tac Toe
# Ne pas supprimer cette ligne. <trace>tictactoe.py</trace>

# Traité du Jeu du Tic Tac Toe

Ce document décrit le développement du fichier `tictactoe.py` et explique les étapes de création du jeu Tic Tac Toe en Python.

---

## 1. Développement et journal de bord

### 21/11/2025 — Gestion des alignements
- Début du codage des alignements horizontaux et verticaux.
- Création d’une **liste intermédiaire** pour vérifier correctement les colonnes.
- Alignements horizontaux et verticaux fonctionnels après ajustement.

### 22/11/2025 — Affichage et premières itérations
- Codage de l’affichage de la grille avec `affiche_motif()`, `affiche_barre()` et `affichage_grille()`.
- Les autres parties du jeu (saisie et traitement) codées sans difficulté majeure.
- Première itération complète testée.

### Correction et finalisation
- Débogage suite à un problème de victoire incorrecte.
- Ajustement de la fonction `tous_sont_identique` pour ignorer les cases vides.
- Finalisation de la saisie des noms et coordonnées, et orchestration via `jouer()`.

---

## 2. Organisation du code

### Affichage
- Séparation motif et barre pour faciliter l’affichage de la grille.
- `affichage_grille()` combine les motifs et barres pour afficher correctement la grille.

### Saisie
- `saisie_nom()` et `saisie_nom_different()` pour les noms des joueurs.
- `saisie_coordonne()` pour récupérer ligne et colonne avec validation.

### Traitement
- `tous_sont_identique(liste)` pour vérifier que trois symboles sont identiques et non vides.
- Alignements :
  - Horizontal → `est_aligne_hori()`
  - Vertical → `est_aligne_verti()`
  - Diagonal → `est_aligne_diago()`
- `est_vide()` pour vérifier si une case est libre.
- `mise_Ajour()` pour mettre à jour la grille sans modifier l’originale.
- `trouver()` combine les trois fonctions d’alignement pour détecter une victoire.

### Initialisation
- `grille_vide()` crée une grille 3×3 vide.

### Fonction principale
- `jouer()` relie toutes les fonctions :
  - Création de la grille.
  - Saisie des joueurs.
  - Boucle de jeu avec alternance des tours.
  - Mise à jour de la grille, affichage et vérification des victoires (y compris diagonales).
  - Gestion du match nul.

---

## 3. Conclusion

- Chaque fonction est **modulaire et reliée aux autres**.  
- Les difficultés ont été résolues via débogage et ajustement des tests.  
- Le jeu final est **fonctionnel, clair et interactif**, avec une bonne gestion des entrées et des conditions de victoire, y compris pour les alignements horizontaux, verticaux et diagonaux.

