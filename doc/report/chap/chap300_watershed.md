# Watershed

Ce présent chapitre documente l'utilisation d'un traitement d'image classique type *Watershed* sur les images de globules rouges.

## Définition

Watershed est un algorithme de segmentaion d'image.
Il utilise les lignes de partages des eaux pour délimiter plusieurs zones au sein de l'image.

Ci-dessous se trouve une définition [@WikipediaWatershed] :

> En traitement d'images, la segmentation par ligne de partage des eaux désigne une famille de méthodes de segmentation d'image issues de la morphologie mathématique qui considèrent une image à niveaux de gris comme un relief topographique, dont on simule l’inondation.

## Fonctionnement

Watershed est un algorithme de traitement d'image qui utilise principalement l'opération de **dilatation**.
Il n'est que très rarement utilisé à même l'image source.
Généralement, les images sont filtrées de manière à faire ressortir uniquement les régions ciblées. La sortie des filtres rend des images en niveaux de gris ou binaires.

L'algorithme prend en compte plusieurs régions et les dilate par itération.
Au moment ou les dilatations se rencontrent, des points de collisions sont notés.
Ces dernier jouent le rôle de digue. Ils permettent de séparer les régions.

Le principe de dilatation est illustré sur l'image ci-dessous [@ImageWatershed] : 

![Watershed après deux dilatations successives](img/watershed.png){ width=100% }

\newpage

## Implémentation

Au sein de ce projet, l'algorithme Watershed est utilisé de la manière suivante :

1. 
2. 
3. 
4. 

## Résultats

todo

\newpage
