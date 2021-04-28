# YOLO

Ce présent chapitre documente l'utilisation d'un traitement d'image type neuronal **YOLO** sur les images de globules rouges.

## Définition

YOLO signifie *You Only Look Once*. Il s'agit d'un algorithme de détection d'objets.
Cet algorithme ne regarde "qu'une seule fois" [@yoloMedium] dans le sens que l'image ne passe **qu'une seule fois** dans le réseau de neurones pour obtenir des prédictions.

YOLO est un algorithme qui est disponibles dans plusieurs versions.
La plus récente se nomme **YOLO v5**. Cette dernière est utilisée à travers le projet complet.
Cette version est sortie courant Juin 2020 [@releaseDateYoloV5]

### Caractéristiques

YOLO dispose de plusieurs caractéristiques [@yoloMedium] :

- Il est extrêmement rapide
- Il analyse l'image entièrement durant l'entraînement et les tests
- Il apprend de manière généralisable les représentations d'objets de sorte qu'il surpasse les autres méthodes de détection

\newpage

## Fonctionnement

L'anatomie d'une détecteur d'objet YOLO [@objectYoloDetector] se schématise ainsi :

![Schéma d'un détecteur d'objets au sein de YOLO v5](img/object-detection.png)

## Modèle utilisé

Nous avons utilisé le modèle de machine learning nommé YOLOv5 (Disponible [ici](https://github.com/ultralytics/yolov5)). YOLO signifie "You Only Look Once", qui, comme son nom l'indique, passe l'image entière une seule fois et en entier à travers le réseau de convolution.


## Apprentissage

L'apprentissage s'est réalisé en plusieurs étapes.

1. Annotation d'une trentaine d'images dans le dataset et entrainement du modèle avec uniquement celles-ci
2. Utilisation du modèle entraîné pour annoter automatiquement d'autres images
3. Ajout de ces nouvelles images dans le dataset (quelques centaines)
4. Contrôle manuel des images annotées et correction si besoin
5. Ré-entrainement du modèle avec le nouveau dataset et les images nouvellement annotées
6. Utilisation de ce dernier modèle pour faire la détection finale

\newpage

Pour chaque entraînement du modèle, le déroulement est le suivant :

1. Division du dataset en deux :
   1. 60% pour le training set (choix aléatoire)
   2. 40% pour le validation set (choix aléatoire)
2. L'entraînement est lancé et un modèle est généré
3. Répétition des étapes 1 et 2, avec un nouveau choix aléatoire de training set et validation set, mais en repartant du modèle pré-entraîné précédent. (Consolidation du modèle)

Le modèle final est utilisé pour faire de l'inférence. Il se nomme `best.pt`

## Résultats

Le comptage des cellules avec YOLO est optimal et presque parfait dans la plupart des cas. Dans notre exemple, le nombre de cellules détectées est 25, et il y a effectivement 25 cellules dans l'image.

YOLOv5 est très performant et très fiable même avec une faible quantité d'images présentes dans le dataset d'entraînement.

\newpage
