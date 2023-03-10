import pandas as pd
import os

# typer les colmones

path = "../../../mnt/c/Users/may-8/Transcriptions_CC/"
list_of_files = os.listdir(path)
# file_to_write = open("contrib_nb.txt", 'w+')
# csv_file = "i_am_not_a_csv.txt"
# nb_all_rows = 0
df_base = pd.DataFrame(columns=["Catégorie", "Date de réception", "Code postal", "Code INSEE", "Numéro d'ordre arbitraire", "Type Graphie TT","Numéro de page", "Numéro séquentiel","Contribution"],  dtype=str)
nbcsv = 0
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

print("nb de fichier csv", nbcsv)

print("taille finale (nombre de contributions)", df_base.shape)
print(df_base.sample(10))

communes_groupdf = pd.DataFrame({'count' : df_base.groupby( ["Code INSEE"] ).size()}).reset_index()
numeroaleatoire_groupdf = pd.DataFrame({'count' : df_base.groupby( ["Numéro d'ordre arbitraire"] ).size()}).reset_index()
pages_groupdf = pd.DataFrame({'count' : df_base.groupby( ["Numéro d'ordre arbitraire","Numéro de page"] ).size()}).reset_index()
cp_groupdf = pd.DataFrame({'count' : df_base.groupby( ["Code postal"] ).size()}).reset_index()

print("Code INSEE groupby shape : équivalent à nombre de comunes", communes_groupdf.shape)
print("numero aleatoire groupby shape : équivalent à nombre de cahiers?", numeroaleatoire_groupdf.shape)

print("pages groupby shape : équivalent à nombre de pages", pages_groupdf.shape)
print("code postal groupby shape :", cp_groupdf.shape)

print("toutes les contribs du groupby pages",pages_groupdf['count'].sum())
print("toutes les contribs du groupby communes",communes_groupdf['count'].sum())
print("toutes les contribs du groupby numero aleatoire",numeroaleatoire_groupdf['count'].sum())

df_base.to_csv("contrib_from_csv.csv", index = False)


