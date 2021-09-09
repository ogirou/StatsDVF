# -*- coding: utf-8 -*-
"""
Olivier Girou 2021

# Statistiques de prix de ventes immobilières en France

Ce programme Python dresse un portrait statistique par code postal des prix de ventes immobilières d'une année à partir des données Open Data DVF (https://www.data.gouv.fr/fr/datasets/demandes-de-valeurs-foncieres/)

Les données sont disponibles par année et pour toute la France. Il faut enregistrer un des fichiers `*.csv` dans le même répertoire que le Jupyter Notebook ou le fichiers Python. Le code lit d'abors l'ensemble du tableau de données et réalise les statistiques uniquement pour le code postal choisi.

URL "stables" pour le téléchargement direct :
- 2020 https://www.data.gouv.fr/fr/datasets/r/90a98de0-f562-4328-aa16-fe0dd1dca60f
- 2019 https://www.data.gouv.fr/fr/datasets/r/3004168d-bec4-44d9-a781-ef16f41856a2
- 2018 https://www.data.gouv.fr/fr/datasets/r/1be77ca5-dc1b-4e50-af2b-0240147e0346
- 2017 https://www.data.gouv.fr/fr/datasets/r/7161c9f2-3d91-4caf-afa2-cfe535807f04
- 2016 https://www.data.gouv.fr/fr/datasets/r/0ab442c5-57d1-4139-92c2-19672336401c

Autres sources différentes :
- https://www.data.gouv.fr/fr/datasets/demandes-de-valeurs-foncieres-geolocalisees/
- https://www.data.gouv.fr/fr/datasets/r/e756e8d1-83f3-490b-a5fb-7649b9463f6d


"""


import pandas as pd
import matplotlib.pyplot as plt


debug=1

codePostal = 64600


fichier = "valeursfoncieres-2020.txt"

df=pd.read_csv(fichier, sep="|", dtype={
                      "Code service CH ": float,
                      "Reference document " : float,
                      "1 Articles CGI" : float,
                      "2 Articles CGI" : float,
                      "3 Articles CGI" : float,
                      "4 Articles CGI" : float,
                      "5 Articles CGI" : float, 
                      "No disposition" : int,
                      "Date mutation" : str, 
                      "Nature mutation" : str,
                      "Valeur fonciere" : str,
                      "No voie" : float,
                      "B/T/Q" : str,
                      "Type de voie" : str,
                      "Code voie" : str,
                      "Voie" : str,
                      "Code postal" : float,
                      "Commune" : str,
                      "Code departement" : str,
                      "Code commune" : int,
                      "Prefixe de section" : float,
                      "Section" : str,
                      "No plan" : int,
                      "No Volume" : str,
                      "1er lot" : str,
                      "Surface Carrez du 1er lot"  : str,
                      "2eme lot" : str,
                      "Surface Carrez du 2eme lot" : str,
                      "3eme lot" : str,
                      "Surface Carrez du 3eme lot" : str,
                      "4eme lot" : float,
                      "Surface Carrez du 4eme lot" : str,
                      "5eme lot" : float,
                      "Surface Carrez du 5eme lot" : str,
                      "Nombre de lots" : int,
                      "Code type local" : float,
                      "Type local" : str,
                      "Identifiant local" : float,
                      "Surface reelle bati" : float,
                      "Nombre pieces principales"  : float,
                      "Nature culture" : str,
                      "Nature culture speciale" : str,
                      "Surface terrain" : float,
                      })
                                                                           

if debug:
    print(df.dtypes)
    print(df.index)

df["Valeur fonciere float"]=df["Valeur fonciere"].str.replace(",",".").astype(float)

if debug:
    print(df.dtypes)
    print(df.index)

dfVille = df[df["Code postal"] == codePostal]

#df2=df[(df["Code postal"]>74999)&(df["Code postal"]<76000)]

# dfVilleAppt = dfVille[(dfVille["Type local"] == "Appartement")
#                       &(dfVille["Surface reelle bati"] > 20)
#                       &(dfVille["Surface reelle bati"] < 60)
#                       &(dfVille["Valeur fonciere float"] > 100000)
#                       &(dfVille["Valeur fonciere float"] < 1200000)
#                       ]

dfVilleAppt = dfVille[(dfVille["Type local"] == "Appartement")]

dfVilleApptPrixm2 = dfVilleAppt["Valeur fonciere float"] / dfVilleAppt["Surface reelle bati"]

print(dfVilleAppt["Valeur fonciere float"].describe())

print(dfVilleAppt["Surface reelle bati"].describe())

print(dfVilleApptPrixm2.describe())

plt.figure()
dfVilleApptPrixm2.plot.hist(bins=100)
plt.show()

print("END")



"""

df=pd.read_csv(fichier, sep="|", dtype={
                      "Code service CH ": float,
                      "Reference document " : float,
                      "1 Articles CGI" : float,
                      "2 Articles CGI" : float,
                      "3 Articles CGI" : float,
                      "4 Articles CGI" : float,
                      "5 Articles CGI" : float, 
                      "No disposition" : int,
                      "Date mutation" : str, 
                      "Nature mutation" : str,
                      "Valeur fonciere" : float,
                      "No voie" : float,
                      "B/T/Q" : str,
                      "Type de voie" : str,
                      "Code voie" : str,
                      "Voie" : str,
                      "Code postal" : float,
                      "Commune" : str,
                      "Code departement" : str,
                      "Code commune" : int,
                      "Prefixe de section" : float,
                      "Section" : str,
                      "No plan" : int,
                      "No Volume" : str,
                      "1er lot" : str,
                      "Surface Carrez du 1er lot"  : float,
                      "2eme lot" : str,
                      "Surface Carrez du 2eme lot" : float,
                      "3eme lot" : str,
                      "Surface Carrez du 3eme lot" : float,
                      "4eme lot" : float,
                      "Surface Carrez du 4eme lot" : float,
                      "5eme lot" : float,
                      "Surface Carrez du 5eme lot" : float,
                      "Nombre de lots" : int,
                      "Code type local" : float,
                      "Type local" : str,
                      "Identifiant local" : float,
                      "Surface reelle bati" : float,
                      "Nombre pieces principales"  : float,
                      "Nature culture" : str,
                      "Nature culture speciale" : str,
                      "Surface terrain" : float,
                      })
                            

"""

