#!/usr/bin/env python
# coding: utf-8
🎯 Objectif :
Aider la banque à segmenter ses clients pour identifier les profils les plus rentables et proposer des offres adaptées.

❓ Problématique :
"Quels profils de clients (secteur, forme juridique, taille, localisation) génèrent le plus d’épargne et de patrimoine tout en présentant un risque faible (peu de découvert) ?"

🧩 Données à utiliser :
CLIENT : données financières et RH

TYPE_CLIENT : structure juridique

SECTEUR_ACTIVITE : secteur d’activité

ADRESSE, DEPARTEMENT, PAYS : localisation du client

🔧 Étapes détaillées :
1. 🔗 Jointures nécessaires :
CLIENT → TYPE_CLIENT → ajouter Libelle_Type_Client

CLIENT → SECTEUR_ACTIVITE → ajouter Libelle_Secteur_Activite

CLIENT → ADRESSE → DEPARTEMENT → PAYS → ajouter Ville, Département, Pays

2. 📐 Création d’indicateurs :
Ancienneté (en années) = Année actuelle - Année d’ouverture du premier compte

Taux_Epargne = Montant_Epargne / Montant_Total_Compte

Taux_Decouvert = Montant_Decouvert / Montant_Compte_Courant
(attention aux divisions par zéro !)

Rentabilité estimée = Montant_Patrimoine + Montant_Total_Compte - Montant_Decouvert

3. 📊 Analyses à produire :
Moyenne de Rentabilité estimée par :

Libelle_Secteur_Activite

Libelle_Type_Client

Taille d’entreprise (Nb_Salarie en classes : 0-10, 11-50, 51-250, >250)

Localisation géographique (Département ou Pays)

Répartition par Taux_Epargne (histogramme)

Répartition des clients anciens (>10 ans) par secteur

4. 📌 Question de synthèse :
Quels segments seraient prioritaires pour une nouvelle offre premium ?

Quel est le profil type du client « haute rentabilité » ?

📈 Tâche finale Power BI :
Créer un dashboard interactif permettant :

Le filtrage par secteur, type, taille, pays

L'affichage des KPI principaux : rentabilité, épargne, ancienneté

Un classement des 10 clients les plus rentablesObjectif :
Évaluer la performance des conseillers et agences à travers les portefeuilles clients pour identifier les écarts et opportunités d’amélioration.

❓ Problématique :
"Quels conseillers et agences gèrent les portefeuilles les plus solides en termes de volume, d'ancienneté et de diversité des comptes ?"

🧩 Données à utiliser :
CLIENT

SALARIE (conseiller client)

AGENCE, ADRESSE_AGENCE, DEPARTEMENT_AGENCE, PAYS_AGENCE

🔧 Étapes détaillées :
1. 🔗 Jointures nécessaires :
CLIENT → SALARIE → ajouter Nom_Salarie

SALARIE → AGENCE → ajouter Nom_Agence

AGENCE → ADRESSE_AGENCE → DEPARTEMENT_AGENCE → PAYS_AGENCE → ajouter Ville, Département, Pays

2. 📐 Création d’indicateurs :
Ancienneté Moyenne des comptes clients

Encours Total par conseiller et par agence = somme des Montant_Total_Compte

Diversité = nombre moyen de comptes par client (Nb_Compte)

Ratio Découvert / Encours = total des découverts sur total des comptes courants

Ratio Épargne / Encours = total épargne / total comptes

Nb_Clients par agence

3. 📊 Analyses demandées :
Top 5 des conseillers selon l’encours moyen/client

Top 5 des agences en encours total

Carte des agences par encours total

Histogramme du Ratio Découvert par agence

Classement des agences selon Rentabilité moyenne de leurs clients

4. 📌 Questions de synthèse :
Faut-il redistribuer les portefeuilles clients entre conseillers ?

Quelles agences justifient un renfort d’effectif ?

📈 Tâche finale Power BI :
Créer un dashboard :

Carte géographique des agences colorées par performance

Filtres par agence, conseiller, département, pays

KPIs dynamiques : encours, patrimoine, ratios

Liste des clients par agence triée par patrimoine
# In[ ]:




