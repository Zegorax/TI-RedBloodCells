---
# Title page
title: "Red Blood Cells Analysis"
author: Dos Santos Ferreira Julien, Fridez Lucas, Verardo Luca
date: \today
subject: "Markdown"
keywords: [Markdown, Example]
subtitle: "Traitement d'Image"
desc: |
    todo

typedoc: "Rapport"
lang: "fr"
titlepage: true
titlepage-color: "FFFFFF"
titlepage-text-color: "000000"
titlepage-rule-color: "FF0000"
titlepage-rule-height: 2
titlepage-background: "./../theme/frontpage.pdf"
page-background: "./../theme/page.pdf"
page-background-opacity: 1

# Info Bottom titlepage
supervisor: François Tièche
version: 1.0.0


links-as-notes: true
numbersections: true

# Table des matières
toc: true
toc-depth: 2
lof: true
lot: true
lol: true
tblPrefix: tab
toc-title: Table des matières
lol-title: Liste des extraits de code
lof-title: Liste des figures
codes-title: Liste des codes
code-abrev: Code
listingtitle: Extrait de code

bibliography: bib-refs.bib
csl: ../theme/iso690-author-date-fr.csl

header-includes:
- |
  \usepackage{lmodern}
  \usepackage{xspace}
  \usepackage{listings}
---
