import pandas as pd

df_original = pd.read_csv("contrib_from_original.csv", sep = ",", dtype= str)
df_processed = pd.read_csv("contrib_from_csv.csv", sep = ",", dtype= str)

#  AFFICHER LES NAN codes postaux

def print_full(df):
    import pandas as pd
    pd.set_option('display.max_rows', len(df))
    print(df)
    pd.reset_option('display.max_rows')
# print_full(df_processed[df_processed.isna().any(axis=1)])
# print(df_processed["Code postal"].isnull().sum)

# testé : AUCUN DUPLICATE

# AFFICHER les df et leur taille:

# print("XML :\n", df_original)
print ("xml", df_original.columns)
# print("XML shape :\n", df_original.shape)
print("csv", df_processed.columns)
# print("CSV shape :\n",df_processed.shape)
# print("CSV :\n", df_processed)

# SUPPR LES NAN (des contribs disparaissent)
print("shape with null",df_processed.shape)
df_processed = df_processed.dropna()
print("shape without null",df_processed.shape)
# RECREER LE NUMERO ID pour comparer avec les noms de fichiers originaux
s1, s2 = df_processed.shape
chgd = list(["MD"]*s1)
md_change = pd.DataFrame(data = {"MD": chgd})
print("size insee")
test = df_processed["Code INSEE"].str.len
df_processed["joined_id"] = df_processed["Catégorie"].astype(str) + "_" + df_processed["Code postal"].astype(str) + "_" + df_processed["Date de réception"].astype(str) + "_" + df_processed["Code INSEE"].astype(str) + "_" + md_change["MD"].astype(str) + "_" + df_processed["Numéro d'ordre arbitraire"] 
group1 = pd.DataFrame({'count' : df_processed.groupby( ["joined_id"] ).size()}).reset_index()
# affiche les contrib d'un cahier
# print(df_processed.query('joined_id == "CC_70000_190225_70163_MD_06225"'))

# les codes postaux : 265 nan, associés à des codes insee 00000
print(df_processed["Code INSEE"].isna().sum)
# CC_79800_190225_79319_MD_11361
df_original = df_original.rename(columns={"info_communes": "joined_id"})
mergedStuff = pd.merge(df_original, group1, left_on=["joined_id"], 
               right_on=["joined_id"],
            #    on=['joined_id'], 
                how='inner', indicator=True)
print(mergedStuff.shape)
# print(mergedStuff.query("_merge" == "left_only").shape)
print(mergedStuff.head)
# print(mergedStuff.query('_merge == "right_only"').sample(10))
# print(mergedStuff.query('joined_id == "CC_70000_190225_70163_MD_06225"'))

