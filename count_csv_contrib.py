import pandas as pd
import os


path = "../../../mnt/c/Users/may-8/Transcriptions_CC/"
list_of_files = os.listdir(path)


# créer un df vide à remplir au fur à mesure de l'ouverture des csv
df_base = pd.DataFrame(columns=["Catégorie", "Date de réception", "Code postal", "Code INSEE", "Numéro d'ordre arbitraire", "Type Graphie TT","Numéro de page", "Numéro séquentiel","Contribution"],  dtype=str)
nbcsv = 0

# ouvrir tous les csv et typer les colonnes en str
for name_file in list_of_files :
    print("starting ", path+name_file)
    nbcsv += 1

    with open(path+name_file) as myfile :
#       les 0 au début des id sont supprimés par pandas sauf en indiquant dtype = str :
        df = pd.read_csv(myfile, sep = ";",  dtype=str)
    #   il faut indiquer que ls headers seront ceux du concat avant sinon ils seront inclus dans les data
        df.columns =  df_base.columns
        print(df.shape)
        df_base = pd.concat([df_base, df], ignore_index = True)

print(f"nombre de fichier csv traité {nbcsv}")


# RESOUDRE LES NAN
# les codes postaux : 265 nan, associés à des codes insee 00000
# les Types Graphie TT : 2 nan
dicfill = {"Code postal" : "0000", "Type Graphie TT" : "MD"}
df_base = df_base.fillna(dicfill)
# Done : résolu avc dtype : str <- ajouter 0 devant les code posatux trop court (accidents excel)
# Done : résolu avec fillna : remplacer les NaN par des codes postaux 00000 pour conserver leurs contribs

# RECREE LE NUMERO ID pour comparer avec les noms de fichiers originaux
s1, s2 = df_base.shape
chgd = list(["MD"]*s1)
md_change = pd.DataFrame(data = {"MD": chgd})
test = df_base["Code INSEE"].str.len
df_base["joined_id"] = df_base["Catégorie"].astype(str) + "_" + df_base["Code postal"].astype(str) + "_" + df_base["Date de réception"].astype(str) + "_" + df_base["Code INSEE"].astype(str) + "_" + md_change["MD"].astype(str) + "_" + df_base["Numéro d'ordre arbitraire"] 


print("nb de fichier csv", nbcsv)

print("taille finale (nombre de contributions)", df_base.shape)
print(df_base.sample(10))

# créer des groupby pour afficher des informations sur chaque type de colonnes
communes_groupdf = pd.DataFrame({'count' : df_base.groupby( ["Code INSEE"] ).size()}).reset_index()
numeroaleatoire_groupdf = pd.DataFrame({'count' : df_base.groupby( ["Numéro d'ordre arbitraire"] ).size()}).reset_index()
pages_groupdf = pd.DataFrame({'count' : df_base.groupby( ["Code INSEE","Numéro de page"] ).size()}).reset_index()
cp_groupdf = pd.DataFrame({'count' : df_base.groupby( ["Code postal"] ).size()}).reset_index()

print("Code INSEE groupby shape : équivalent à nombre de comunes", communes_groupdf.shape)
print("numero aleatoire groupby shape : équivalent à nombre de cahiers?", numeroaleatoire_groupdf.shape)

print("pages groupby shape : équivalent à nombre de pages", pages_groupdf.shape)
print("code postal groupby shape :", cp_groupdf.shape)

print("somme des contrib pour total des pages (devrait être égal au nb de contrib total)",pages_groupdf['count'].sum())
print("sample les pages du groupby insee",pages_groupdf['count'].sample(10))
print("moyenne les pages du groupby insee",pages_groupdf['count'].mean())
print("max les pages du groupby insee",pages_groupdf['count'].max())
print(pages_groupdf[pages_groupdf.idxmax()])

print("min les pages du groupby insee",pages_groupdf['count'].min())



# print("toutes les contribs du groupby communes",communes_groupdf['count'].sum())
# print("toutes les contribs du groupby numero aleatoire",numeroaleatoire_groupdf['count'].sum())

df_base.to_csv("contrib_from_csv.csv", index = False)


