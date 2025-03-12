# Cahier des charges - Addon Blender : Instanciation de diamants

## 1. Objectif
Développer un addon pour Blender permettant d'instancier des diamants de différentes tailles sur une surface donnée selon différents patterns. Les diamants seront alignés avec la normale de la surface sélectionnée et un aperçu interactif sera proposé avant génération.

## 2. Variables d'entrée de l'interface

| Nom                      | Type      | Valeur par défaut | Description |
|--------------------------|----------|------------------|-------------|
| diamond_mesh            | Object   | N/A              | Objet Blender utilisé comme diamant |
| diamond_sizes           | List[float] | [1.0, 1.5, 2.0] | Liste des tailles de diamants |
| distance_offset         | Float    | 0.1 mm           | Distance minimale entre diamants |
| scattering_pattern      | Enum     | Pavé Setting     | Choix du mode de placement |
| bigger_diamond_prob     | Float | 0.1              | Probabilité d’instance des gros diamants (Snow Setting) |
| add_grain_setting       | Boolean  | False            | Ajoute des grains entre les diamants |
| grain_size              | Float    | 0.05 mm          | Taille des grains |
| grain_subdiv_lvl        | Int      | 1                | Niveau de subdivision des grains |
| random_rotation_amount  | Float    | 0.0              | Amplitude de rotation aléatoire des diamants |
| random_rotation_seed    | Int      | 0                | Seed pour la rotation aléatoire |
| merge_result            | Boolean  | False            | Fusionne les objets après génération |

## 3. Fonctionnalités principales

### 3.1 Sélection et validation de la surface
- Sélection de l'objet cible dans la scène Blender.
- Vérification de l'existence d'un Face Map pour définir la surface à remplir.
- Si aucun Face Map n'est détecté, affichage d'un message d'erreur : "Surface object: no face map detected".

### 3.2 Paramétrage des diamants
- **Mesh de diamant** : Objet fourni par l'utilisateur.
- **Tailles des diamants** : Liste de valeurs flottantes modifiable par l’utilisateur.
  - Longueur de la liste = 1 pour Pavé Setting et French Pavé.
  - Longueur de la liste > 1 pour Snow Setting.
- **Vérifications** :
  - Aucun élément de la liste ne peut être égal à 0.
  - Pour les patterns pavé setting et french pavé, une seule taille est autorisée.
- **Distance offset** : Float prérempli avec une valeur par défaut (0.1 mm).

### 3.3 Sélection du pattern de répartition
- **Pavé Setting** : Disposition hexagonale.
- **French Pavé** : Disposition en grille classique.
- **Snow Setting** :
  - Simulation basée sur la méthode Poisson Disk avec sphères de diamètre `(diamond size + distance offset / 2)`.
  - Placement aléatoire des plus gros diamants, avec une densité définie par `bigger_diamond_probability` (slider en % de 0.0 à 1.0, valeur par défaut 0.1).
  - Répartition successive des plus petits diamants pour combler les trous.
  - Aperçu interactif avec cercles colorés selon la taille et carrés pour les grains.

### 3.4 Ajout des grains (prongs)
- Si **add_grain_setting** est activé :
  - Les grains sont générés après le positionnement des diamants.
  - **Pavé & French Pavé** : Grains placés dans les espaces interstitiels (4 par diamant en French Pavé, 6 par diamant en Pavé Setting).
  - **Snow Setting** : Grains placés dans les trous restants (1 grain par trou max).
  - **Grains** : Cubes subdivisés (`grain_subdiv_lvl`, valeur par défaut 1).
  - **Taille des grains** : Ajustable avec `grain_size`.

### 3.5 Alignement et rotation aléatoire
- Alignement des diamants perpendiculaire à la surface (axe Z de chaque diamant).
- Rotation aléatoire sur l'axe Z de chaque diamant si activé.
- **Contrôles** :
  - `random_rotation_amount` (slider entre 0 et 1)
  - `random_rotation_seed` (int)
- Les grains ne subissent pas de rotation aléatoire.

### 3.6 Fusion des objets après génération
- Option **merge_result** pour fusionner les objets après génération :
  - Un seul objet contenant tous les diamants.
  - Un second objet contenant tous les grains.
- Vérification pour éviter les doublons (un seul grain par trou).
- Conservation des matériaux existants pour les diamants.
- Création d'un matériau par défaut **"grain_mat"** pour les grains (Base Color : blanc, Metallic : 1, Roughness : 0.1).

### 3.7 Interface utilisateur
- **Boutons disponibles** :
  - **Preview** : Génère un aperçu interactif (cercles et carrés).
  - **Update Preview** : Met à jour l'aperçu après modification des paramètres.
  - **Generate** : Lance la génération finale.
  - **Reset Settings** : Réinitialise les paramètres.
- **Barre de progression** pendant le chargement de l'aperçu et la génération.
- **Message récapitulatif après génération** :
  - Nombre de diamants de chaque taille générés.
  - Nombre total de carats représentés.

## 4. Roadmap

### Phase 1 : Définition du projet et setup
- ✅ Création du dépôt GitHub `diamond-scatter-addon`
- ✅ Rédaction du cahier des charges
- ✅ Initialisation du projet (dossier Blender Addon, structure des fichiers)

### Phase 2 : Développement du core
- 🔲 Implémentation de la sélection de la surface et validation (Face Map check)
- 🔲 Gestion des paramètres utilisateurs (diamants, offset, patterns, grains)
- 🔲 Algorithmes de distribution (Pavé, French Pavé, Snow Setting)
- 🔲 Génération des grains selon les patterns
- 🔲 Alignement et gestion des rotations

### Phase 3 : Aperçu interactif et UI
- 🔲 Développement du système de preview interactif
- 🔲 Intégration de la barre de progression
- 🔲 Création et optimisation de l’interface utilisateur

### Phase 4 : Finalisation et release
🔲 Ajout des options de fusion des objets
🔲 Tests et débogage
🔲 Documentation utilisateur
🔲 Release de la première version publique (GitHub, Gumroad, autres plateformes)

---

Ce document servira de référence tout au long du développement.
