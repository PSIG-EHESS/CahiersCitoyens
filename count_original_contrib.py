import pandas as pd
import os

# à partir des fichiers des archives nationales,
# traités par parsezip_and_count.sh et sauvegardés en 2 parties,
# vers ces deux fichiers textes (un pour chaque disque dur) avec l'id carnet + le nombre de fichers
part1 = "GDN_part1.txt"
part2 = "GDN_part2.txt"

# fonction qui ouvre un fichier .txt
def map(part):
    with open(part) as my_file :
        print(f"starting {part}")
        # lit les csv (ici des txt mais stockés avec un format qui lui pose pas de pb)
        df = pd.read_csv(my_file, sep = ":", names = ["filename","nb_of_file" ])
        # calculer le nombre de xml grâce au nombre de fichiers total, 
        # créés par la fonction parsezip_and_count.sh, 
        # (à chaque xml correspond un .jpg, donc diviser par deux ; 
        # puis retirer 1 (le fichier pdf))

        df["xml"] = (df["nb_of_file"]-1)/2

        # récuperer l'id de carnet à partir du path
        
        split_slash = lambda x : x.str.split("/", expand = True)
        name_spliteed = split_slash(df["filename"])
        
        # créer les colonnes correspondant aux infos contenues dans chaque id de carnet
        
        df["categorie_region"] = name_spliteed[6]
        split_point = lambda x : x.str.split(".", expand = True)
        df["info_communes"] = split_point(name_spliteed[7])[0]
        split_underscore = lambda x : x.str.split("_", expand = True)
        buff = split_underscore(df["info_communes"])
        df = pd.concat([df, buff], axis=1)
        df = df.rename(columns = {0 : "Catégorie", 1 : "Code postal", 2 : "Date de réception", 3 : "Code INSEE", 4 : "Type Graphie TT", 5 : "Numéro d'id_cc"})
        
        # nb = la date de réception est plutôt la date d'ocr, mais elle est notée comme ça dans les autres csv.
        
        return df

df1 = map(part1)
df2 = map(part2)

# concatène les 2 parties

df_concat = pd.concat([df1, df2])

# enregistre le dataframe obetnu

df_concat.to_csv("contrib_from_original.csv")

# montre les infos du dataframe

print(df_concat.info)

