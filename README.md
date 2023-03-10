# CahiersCitoyens
Projet CC

Résultats stage de Marjolaine Ray.

=> “**comparaison.py**” : en cours. ouvre les dataframes contrib_from_original.csv et contrib_from_csv.csv et teste des merge pour determiner les communes manquantes dans chacuns par rapport à l'autre et par rapport au csv fourni par l'insee.

=> "**parsezip_and_count.sh**” : parcourt les .zip des données archives (deux disque durs de la plateforme) et récupère le nom du dossier (tout les cahiers d’une commune) et le nombre de fichiers à l’intérieur.
output : nom du fichier commune + nombre de fichiers à l’intérieur. Stocké dans deux fichiers GDN_part1.txt et GDN_part2.txt

=> “**count_original_contrib.py**” : calculer le nombre de xml grâce au nombre de fichiers total, dispo dans les .txt créés par la fonction parsezip_and_count.sh, (à chaque xml correspond un .jpg, donc diviser par deux ; puis retirer 1 (le fichier pdf)). Produire un dataframe pour les parties 1 et 2, puis les concaténer.
output 1 : un seul dataframe enregistré sous forme de csv pour toutes les données : contrib_from_original.csv
output 2 : le nombre de dossiers, correspondant au nombre communes = 18 854
output 3 : le nombre de pages traitées (nombre de fichiers dans les dossiers) = 428 832

=> “**count_csv_contrib.py**” : parcourir tous les csv (35 fichiers) , les transforme en csv et les concatène. puis fait un groupby sur les numéro insee des communes et compte les contributions par communes :
output 1 : un seul dataframe enregistré sous forme de csv pour toutes les données : contrib_from_csv.csv
output 2 : un dataframe avec les communes et les nb de contrib : 16 420 communes
output 3 : un dataframe avec les pages : 196 821 pages
output 4 : un dataframe avec les numéro uniques (id de cahiers) : 19 250
