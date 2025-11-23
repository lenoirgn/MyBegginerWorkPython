# Compléter ici (noms, groupe, contenu fichier, date)
# Mamadou Radjaye Sow, le 22/11/2025 — Traité du Jeu du Tic Tac Toe
# Ne pas supprimer cette ligne. <trace>tictactoe.py</trace>

# Développement du Jeu Tic Tac Toe — Journal détaillé

Ce document retrace l’ensemble du processus de création du fichier `tictactoe.py`.  
Il décrit non seulement le code, mais aussi **mon expérience personnelle**, les difficultés rencontrées, les idées que j’ai eues et les solutions trouvées.

---

## 1. Journal de développement

### 21/11/2025 — Premiers essais et alignements
- J’ai commencé par **réfléchir et coder les alignements horizontaux**.
- L’alignement vertical semblait simple, mais au début je ne savais pas comment parcourir les colonnes proprement.
- Pendant une **pause**, j’ai eu l’idée de créer une **liste intermédiaire** pour chaque colonne afin de vérifier si les trois symboles étaient identiques.
- Après cette solution, l’alignement vertical fonctionnait correctement.
- Pour les **diagonales**, j’ai utilisé la même logique que pour les lignes et colonnes, en créant deux listes intermédiaires pour les deux diagonales.  

---

### 22/11/2025 — Affichage et intégration
- J’ai travaillé sur l’**affichage de la grille**.  
  - J’ai utilisé `affiche_motif()` pour les lignes horizontales et `affiche_barre()` pour les lignes contenant les symboles.  
  - Je savais que ce n’était pas la meilleure solution possible, mais c’était **débrouillard** et fonctionnel.  
- Ensuite, j’ai intégré les fonctions restantes (saisie, mise à jour de la grille) sans difficulté majeure.
- Je pensais avoir fini le jeu et lancé ma première version complète.

---

### Première itération et corrections
- Lors du **premier lancement**, le jeu indiquait qu’un joueur avait gagné **alors que ce n’était pas correct**.
- J’ai appelé mon **débogueur** et constaté que mes tests étaient insuffisants.
- Problème identifié : **je n’avais pas géré les cases vides** dans `tous_sont_identique()`.  
  - Avant cette correction, un alignement vide pouvait être interprété comme une victoire.  
- Après ajustement, les fonctions d’alignement (horizontal, vertical et diagonal) détectent correctement la victoire uniquement si les cases sont remplies.

---

### Finalisation — Saisie et orchestration
- J’ai terminé par la **saisie des noms et des coordonnées** avec `saisie_nom()`, `saisie_nom_different()` et `saisie_coordonne()`.
- La fonction `jouer()` relie toutes les parties du programme et orchestre le jeu :
  - création de la grille vide
  - saisie des joueurs
  - alternance des tours
  - mise à jour et affichage de la grille
  - vérification des alignements horizontaux, verticaux et diagonaux
  - gestion de la victoire ou du match nul
- Le jeu est maintenant **entièrement fonctionnel**.

---

## 2. Difficultés et solutions
- **Alignement vertical** : difficulté à parcourir correctement les colonnes → solution : **liste intermédiaire**.  
- **Diagonales** : gestion similaire aux lignes et colonnes, création de deux listes pour chaque diagonale.  
- **Cases vides non prises en compte** → correction dans `tous_sont_identique()`.  
- **Affichage** : pas parfait mais suffisant pour tester et continuer le développement.  

---

## 3. Ce que j’ai appris
- La **modularité** du code facilite la maintenance et le débogage.
- Les **tests insuffisants** peuvent masquer des erreurs subtiles.
- Les pauses et la réflexion permettent souvent de trouver des solutions simples à des problèmes complexes.
- Même une solution "débrouillarde" peut être suffisante pour progresser rapidement.

---

## 4. Conclusion
Ce projet m’a permis de **vivre toutes les étapes du développement logiciel** : réflexion, codage, test, débogage et finalisation.  
Aujourd’hui, le jeu Tic Tac Toe fonctionne parfaitement avec :
- affichage correct
- saisie sécurisée
- alternance des tours
- détection des victoires (horizontal, vertical et diagonal)
- gestion du match nul

