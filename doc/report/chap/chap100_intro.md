# Introduction

Ce projet prend part au cours de **Traitement d'Image**, en troisième année à la haute école Arc ingénierie, enseigné par François Tièche.
A travers ce dernier, le groupe d'étudiants formé par Julien Dos Santos Ferreira, Lucas Fridez et
Luca Verardo étudient le modèle de deep learning YOLOv5 sur des images annotés de globules rouges.
Les résultats obtenus sont comparés aux résultats obtenu par un algorithme de traitement d'image plus classique, sans réseaux de neurones, WaterShed.

## Objectifs

Les objectifs du projet sont les suivants :

- Annoter des données pour l’entraînement de YOLOv5
- Entraîner YOLOv5 sur le data set annoté
- Inférer sur des images non connus avec YOLOv5 dans le but de dénombré le nombre de cellules dans l'image
- Comparer les résultats avec un algorithme de traitement d'image classique, WaterShed

## Cahier des charges

Ce cahier des charges se base sur la définition [MoSCoW](https://fr.wikipedia.org/wiki/M%C3%A9thode_MoSCoW) 

### But du projet

Ce projet a pour but de mettre en place une solution permettant de compter le nombre de globules (blancs ou rouges) dans une image de sang au microscope.
L'intelligence artificielle permet la reconnaissance des cellules au travers du modèle **Yolo v5**.

**Must have**

- Dataset annoté
- Implémentation du modèle YoloV5
- Dénombrement des cellules reconnues

**Should have**

- Analyse des résultats obtenus

**Could have**

- Comparaison avec une méthode plus classique du traitement d'image.

**Won't have**

- Comparaison avec un autre modèle tel que CNN

\newpage
