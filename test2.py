# -*- coding: utf-8 -*-
"""
Olivier Girou 2021

https://www.data.gouv.fr/fr/datasets/demandes-de-valeurs-foncieres/

"""


import pandas as pd
import matplotlib.pyplot as plt

debug=1

codePostal = 75014

fichier = "valeursfoncieres-2022.txt"

df=pd.read_csv(fichier, sep="|", dtype={
                      "Code service CH ": str,
                      "Reference document " : str,
                      "1 Articles CGI" : str,
                      "2 Articles CGI" : str,
                      "3 Articles CGI" : str,
                      "4 Articles CGI" : str,
                      "5 Articles CGI" : str, 
                      "No disposition" : str,
                      "Date mutation" : str, 
                      "Nature mutation" : str,
                      "Valeur fonciere" : str,
                      "No voie" : str,
                      "B/T/Q" : str,
                      "Type de voie" : str,
                      "Code voie" : str,
                      "Voie" : str,
                      "Code postal" : str,
                      "Commune" : str,
                      "Code departement" : str,
                      "Code commune" : int,
                      "Prefixe de section" : str,
                      "Section" : str,
                      "No plan" : int,
                      "No Volume" : str,
                      "1er lot" : str,
                      "Surface Carrez du 1er lot"  : str,
                      "2eme lot" : str,
                      "Surface Carrez du 2eme lot" : str,
                      "3eme lot" : str,
                      "Surface Carrez du 3eme lot" : str,
                      "4eme lot" : str,
                      "Surface Carrez du 4eme lot" : str,
                      "5eme lot" : str,
                      "Surface Carrez du 5eme lot" : str,
                      "Nombre de lots" : int,
                      "Code type local" : str,
                      "Type local" : str,
                      "Identifiant local" : str,
                      "Surface reelle bati" : float,
                      "Nombre pieces principales"  : str,
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
    
df["Code postal float"] = df["Code postal"].astype(float)    

dfVille = df[df["Code postal float"] == codePostal]

#df2=df[(df["Code postal"]>74999)&(df["Code postal"]<76000)]

dfVilleAppt = dfVille[(dfVille["Type local"] == "Appartement")
                      &(dfVille["Surface reelle bati"] > 20)
                      &(dfVille["Surface reelle bati"] < 60)
                      &(dfVille["Valeur fonciere float"] > 100000)
                      &(dfVille["Valeur fonciere float"] < 1200000)
                      ]

dfVilleAppt = dfVille[(dfVille["Type local"] == "Appartement")]

dfVilleApptPrixm2 = (dfVilleAppt["Valeur fonciere float"] / dfVilleAppt["Surface reelle bati"]).astype(float)

print(dfVilleAppt["Valeur fonciere float"].describe())

print(dfVilleAppt["Surface reelle bati"].describe())

print(dfVilleApptPrixm2.describe())


plt.figure()
dfVilleApptPrixm2.plot.hist(bins=1000)
plt.xlim(0,20000)
plt.grid(True)
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

