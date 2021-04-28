# Comparaison

Ce présent chapitre compare les résultats obtenus entre *YOLO* et *Traitement d'Image classique Watershed*.

## Résultats YOLO

Le résultat de l'analyse d'image dans le chapitre **2.5** est retranscrite ci-dessous
dans une matrice de confusion :

![Matrice de confusion YOLO v5](img/confusion-yolo.png){ width=70% }

La matrice de confusion est analysée ci-dessous :

: Analyse de la matrice de confusion pour Watershed

| Valeur           | Nombre                                                  |
|------------------|---------------------------------------------------------|
| **Vrai positif** | 25 cellules sont correctement détectées                 |
| **Vrai négatif** | *Cette mesure ne correspond pas aux données présentées* |
| **Faux positif** | 0                                                       |
| **Faux négatif** | 0                                                       |


L'algorithme **YOLO v5** détecte les 25 cellules de l'images.
Ainsi, le 100% des cellules sont retrouvées.

\newpage

## Résultats Watershed

Le résultat de l'analyse d'image dans le chapitre **3.4** est retranscrite ci-dessous
dans une matrice de confusion :

![Matrice de confusion Watershed](img/confusion-watershed.png){ width=70% }

La matrice de confusion est analysée ci-dessous :

: Analyse de la matrice de confusion pour Watershed

| Valeur           | Nombre                                                         |
|------------------|----------------------------------------------------------------|
| **Vrai positif** | 11 cellules sont correctement détectées                        |
| **Vrai négatif** | *Cette mesure ne correspond pas aux données présentées*        |
| **Faux positif** | 3 zones sont détectées mais correspondent à plusieurs cellules |
| **Faux négatif** | 9 cellules ne sont pas détectées du tout                       |

Ainsi, Watershed dispose d'un taux de réussite de $\frac{11}{25} = 44$%.

\newpage

## Comparaison des résultats

Dans le but de comparer les résultats des deux algorithmes,
les algorithmes **YOLO v5** et **Watershed** sont lancés sur un ensemble d'images donné.
Celui-ci, disponible dans le dossier `dataset/test/PBC_dataset_normal_DIB/platelet` contient **2348 images**.

: Comparaison des algorithmes pour un ensemble d'images

| Algorithme | Cellules trouvées                    |
|------------|--------------------------------------|
| YOLO v5    | 36'821 gl. rouges + 2'609 gl. blancs |
| Watershed  | 1'169 régions                        |

\newpage
