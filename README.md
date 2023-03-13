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

dépendances : voici la liste des packages installés dans mon environment :

asttokens         2.2.1 | 
backcall          0.2.0 | 
comm              0.1.2 | 
contourpy         1.0.7 | 
cycler            0.11.0 | 
debugpy           1.6.6 | 
decorator         5.1.1 | 
executing         1.2.0 | 
fonttools         4.39.0 | 
ipykernel         6.21.2 | 
ipython           8.11.0 | 
jedi              0.18.2 | 
jupyter_client    8.0.3 | 
jupyter_core      5.2.0 | 
kiwisolver        1.4.4 | 
matplotlib        3.7.1 | 
matplotlib-inline 0.1.6 | 
matplotlib-venn   0.11.9 | 
nest-asyncio      1.5.6 | 
numpy             1.24.2 | 
packaging         23.0 | 
pandas            1.5.3 | 
parso             0.8.3 | 
pexpect           4.8.0 | 
pickleshare       0.7.5 | 
Pillow            9.4.0 | 
pip               22.0.2 | 
platformdirs      3.0.0 | 
prompt-toolkit    3.0.38 | 
psutil            5.9.4 | 
ptyprocess        0.7.0 | 
pure-eval         0.2.2 | 
Pygments          2.14.0 | 
pyparsing         3.0.9 | 
python-dateutil   2.8.2 | 
pytz              2022.7.1 | 
pyzmq             25.0.0 | 
scipy             1.10.1 | 
setuptools        59.6.0 | 
six               1.16.0 | 
stack-data        0.6.2 | 
tornado           6.2 | 
traitlets         5.9.0 | 
wcwidth           0.2.6 | 
