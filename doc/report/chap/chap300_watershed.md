# Watershed

Ce présent chapitre documente l'utilisation d'un traitement d'image classique type *Watershed* sur les images de globules rouges.

## Définition

Watershed est un algorithme de segmentation d'image.
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

1. Effectuer une légère érosion sur l'image de base pour séparer un minimum les globules qui se chevauches
2. Transformer l'image en couleurs HSV
3. Récupérer uniquement la matrice de saturation
4. Effectuer un threshold pour récupérer uniquement les cellules
5. Appliquer un flou median
6. Appliquer Watershed
7. Compter les cellules trouvées

## Résultats

Application de l'algorithme Watershed sur une image. Les cellules trouvées se nombrent à 14 et sont entourées en rouge.
Le résultat n'est pas optimal. Pourtant, de nombreuses variantes et préparations d'images sont testées.
Il s'agit là du meilleur résultat obtenu avec un tel algorithme.

![Application de watershed sur une image](img/watershed-counting.png){ width=70% }

\newpage
