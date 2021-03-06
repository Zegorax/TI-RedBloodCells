# Conclusion

Ce présent chapitre conclut le projet de Traitement d'Images.

## Résultats obtenus

On constate dans un premier temps que les deux solutions étudiées, YOLO v5 et Watershed, fournissent un résultat. Les deux approches sont fonctionnelles et permettent la comparaison.

Les résultats obtenus ont permis l'analyse des résultats des approches dans le but de les comparer.

## Comparaison

La comparaison des deux approches s'est faite sur le dénombrement des globules blancs et rouges d'une image.

Les résultats obtenus permettent d'affirmer que la meilleures des deux approches est sans aucuns doute l'approche deep learning avec le modèle YOLO v5.

Dans les test réalisés, l'approche avec YOLO v5 dénombrait quasiment à chaque fois la totalité des globules présents dans l'image. Malgré le fait que sur la plupart des images les globules se chevauchent ou même sont tronqués sur les bords.

A contrario, l'approche avec l'algorithme Watershed a de la peine à dénombrer la totalité des globules. De plus lorsque dans l'image un globule blanc est présent, l'algorithme  détoure et dénombre uniquement ce dernier. L'idée d'augmenter l’érosion sur l'image de base ne peut être appliquée que de manière faible car un globule n'as pas une couleur uniforme. Si l'érosion est trop importante, le centre commence à se démarquer et l'algorithme dénombre deux globules au lieu d'un.

## Rapidité

La rapidité peut être un facteur clé, mais l'inférence du modèle YOLO v5 est très rapide. Et donc il n'y a presque pas de différence concernant la rapidité de l'un ou l'autre de ces deux approches.

Malgré tout, il faut tenir compte de temps d'apprentissage du modèle YOLOv5  qui lui est assez long. Environ deux heures par entraînement sont nécessaires en utilisant un GPU de type Tesla V100.

## Finalité

Pour terminer, ce travail a permis à chaque membre du groupe de prendre en main et d'utiliser un modèle de deep learning et de l'appliquer concrètement sur un problème de traitement d'images. Le cours se concentre sur toutes les étapes qui précèdent ce point. Il est très intéressant d'aller jusqu'à la finalité du traitement d'images.

\newpage
