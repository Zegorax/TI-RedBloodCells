# Guide utilisateur

Ce présent chapitre sert de guide utilisateur pour :

- Lancer le projet
  - Utilisation de YOLO
  - Utilisation de Watershed
- Lancer divers analyses
- Dessiner plusieurs graphiques

## Utilisation de YOLO

Afin d'utiliser notre projet, il est nécessaire d'installer Docker Desktop. Il est disponible ici : https://www.docker.com/products/docker-desktop

Une fois installé, il faut ouvrir notre dossier de projet dans Visual Studio Code. Une popup apparaîtra afin de vous demander d'installer les extensions recommandées. Acceptez cette popup.

Une fois l'extension installée, une nouvelle pop-up apparaîtra vous demandant de rouvrir le projet dans un conteneur. Acceptez cette popup.

Le conteneur sera construit, et toutes les dépendances installées automatiquement sans polluer votre machine hôte. Il suffit ensuite d'ouvrir `sources/project.ipynb` et le notebook Jupyter s'ouvrira dans VSCode.

### Lancer une analyse

Pour analyser une image à l'aide de YOLOv5 et de notre modèle pré-entraîné, il faut lancer la commande suivante:

```{.sh caption="Lancement d'une analyse via YOLO v5"}
python3 detect.py --weights best.pt --source /path/to/the/folder/containing/images --project ./detection_results
```

Dans cet exemple, le dossier `/path/to/the/folder/containing/images` sera analysé et les résultats seront enregistrés dans le dossier `./detection_results`. Les résultats consistent en de nouvelles images au format .png avec des rectangles indiquant où des globules rouges et blancs sont détectés.

\newpage

## Utilisation de Watershed

Ce sous-chapitre explique comment utiliser la partie **Watershed** implémentée.

### Pré-requis

Les pré-requis sont les suivants :

- cv2
- numpy
- scipy
- matplotlib
- skimage
- seaborn
- pandas
- Jupyter Notebook

Tous ces pré-requis sont disponibles au sein du conteneur Docker construit au démarrage du projet.

### Guide

Le script de démonstration de Watershed est disponible au sein d'un notebook Jupyter.
Ce dernier se trouve via le chemin suivant `./sources/project.ipynb`.

Au sein du notebook sont expliquées les différentes phases de l'algorithme.
Chacune est illustrée avec une image correspondant au traitement lancé.

### Lancer une analyse

Pour lancer l'analyse Watershed, il faut lancer toutes les cellules du notebook Jupyter.

\newpage

## Supprimer le contenu téléchargé (Docker)
Pour supprimer toutes les images et conteneurs Docker, il suffit de lancer la commande suivant sur votre hôte (pas dans le conteneur):

```{.sh caption="Suppression des conteneurs Docker"}
docker system prune -a
```

\newpage

# Références
