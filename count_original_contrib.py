import pandas as pd
import os

part1 = "GDN_part1.txt"
part2 = "GDN_part2.txt"

def map(part):
    with open(part) as my_file :
        print(f"starting {part}")
        df = pd.read_csv(my_file, sep = ":", names = ["filename","nb_of_file" ])
        # le nombre de xml :
        df["xml"] = (df["nb_of_file"]-1)/2
        split_slash = lambda x : x.str.split("/", expand = True)
        name_spliteed = split_slash(df["filename"])
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
df_concat = pd.concat([df1, df2])
df_concat.to_csv("contrib_from_original.csv")

print("groupby id",df_concat.groupby(["Numéro d'id_cc"]).size())
print("nombre total de fichiers", df_concat["xml"].sum())
print("size of final concatenated",df_concat.shape)
print(df_concat)

