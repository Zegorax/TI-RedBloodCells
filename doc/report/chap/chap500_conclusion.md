# Conclusion

## Résultats obtenus

On constate dans une premier temps que les deux solutions étudiées, YOLOv5 et Watershed, fournissent un résultat. Les deux approches sont fonctionnelles et permettent la comparaison.

Les résultats obtenus on permis l'analyse des résultats des approche dans le but de les comparés.

## Comparaison

La comparaison des deux approches s'est faites sur le dénombrement des globules blanche et rouge d'une image.

Les résultats obtenus permette d'affirmer que la meilleures des deux approche est sans aucuns doute l'approche deep learning avec le modèle YOLOv5.

Dans les test réalisés, l'approche avec YOLOv5 dénombrais quasiment a chaque fois la totalité des globules présents dans l'image et ce malgré le faite que sur la plus part des images les globules se chevauchent ou même sont tronqués sur les bord de l'image.

A contrario, l'approche avec l'algorithme Watershed à de la peine à dénombrer la totalité des globules. De plus lorsque dans l'image un globule blanc est présent, l'algorithme de détoure et dénombre que ce dernier. l'idée d'augmenter l’érosion sur l'image de base ne peut être appliqué que de manière faible car un globule n'as pas une couleur uniforme. Si l'érosion est trop importante, le centre commence à se démarquer et l'algorithme dénombre deux globule pour une seule.

## Rapidité

La rapidité pour être un facteur clé, mais l'inférence du modèle YOLOv5 est très rapide. Et donc il n'y a presque pas de différence concernant la rapidité de l'un ou l'autre de ces deux approches.

Malgré tout, il faut tenir compte de temps d'apprentissage du modèle YOLOv5  qui lui est assez long : VALEUR A METTRE AVEC CONFIG XXX

## Finalité

Pour terminé, ce travail à permis à chaque membre du groupe de prendre en main et d'utiliser un modèle de deep learning et de l'appliquer concrètement sur un problème de traitement d'image. Le cours se concentre sur toutes les étapes précédent ce point et c'est très intéressant d'aller jusqu'à la finalité du traitement d'image.

\newpage
