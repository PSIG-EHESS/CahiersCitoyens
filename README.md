# CahiersCitoyens
Projet CC
stage de Marjolaine Ray.
pipeline dans lordre antéchronologique :

=> "**preprocess_and_split**" : input = df_CC_cleaned_lemmas_postag_stopwords.csv, save = pickle_sentence_df.pkl
* découpe les phrases de chaque contribution (nlp.sents par Spacy avec "core_news_fr_md")
* crée un dataframe avec les phrases et les métadonnées associées à leur contributions d'origine et le sauvegarde

=> "**preprocess_and_lemmatize.ipynb**" : input = df_CC_cleaned.csv, save = dataframe as df_CC_lemmas_postag, df_CC_cleaned_lemmas_postag_stopwords.csv
* tokenise + lemmatise chaque contribution et sauvegarde les lemmes + leurs postag associés (modèle "core_news_fr_md" de Spacy) 
* tokenise + lemmatise chaque contribtion et ne sauvegarde que les lemmes VERB, ADV, ADJ, NOUN et leurs postags. L'objectif était d'éliminer plus que des stopwords pour faciliter la tâche du LDA
* supprime les stopwords à partir du lexique de spacy fr 

=> "**preprocess_and_clean.ipynb**" : input = contrib_from_csv.csv, save = dataframe as df_CC_cleaned.csv
* supprime toutes les notations d'"illisibles", les traces de mises en forme, les mail, les sites, normalise les acronymes (I.S.F. -> ISF), etc

=> “**comparaison.py**” : ouvre les dataframes contrib_from_original.csv (df_original) et contrib_from_csv.csv (df_processed)
* teste des merge pour déterminer les communes manquantes / les départements manquants / les cahiers manquants, entre les deux corpus et entre les stats 2019 de l'insee.
1 : teste les communes / départements / cahiers entre les deux corpus (original vs. processed)
2 : teste les communes / départements entre l'insee et le processed
3 : teste les communes / départements entre l'insee et l'original
4 : affiche des diagram de venn pour représenter ces inclusions / exclusions entre communes ou départements
5 : affiche les nombre de communes ou département pour chacuns

* affiche et sauvegarde des diagrammes de venn + représentatifs

=>"**test_content_from_xml**" : input = dossiers du corpus brut des cahier, output = strings contenues dan les balises <content> de ces xml
* écrit les textes qui ont été océrisés par la BnF (lisibles si imprimés, illisibles si écrit)
* le fichier "output_xml_content.txt" est stocké aussi pour exemple

=> "**parsezip_and_count.sh**” : parcourt les .zip des données archives (deux disque durs de la plateforme) et récupère le nom du dossier (tout les cahiers d’une commune) et le nombre de fichiers à l’intérieur.

output : nom du fichier commune + nombre de fichiers à l’intérieur. Stocké dans deux fichiers GDN_part1.txt et GDN_part2.txt

=> “**count_original_contrib.py**” : calculer le nombre de xml grâce au nombre de fichiers total, dispo dans les .txt créés par la fonction parsezip_and_count.sh, (à chaque xml correspond un .jpg, donc diviser par deux ; puis retirer 1 (le fichier pdf)). Produire un dataframe pour les parties 1 et 2, puis les concaténer.

output 1 : un seul dataframe enregistré sous forme de csv pour toutes les données : contrib_from_original.csv

output 2 : le nombre de dossiers, correspondant au nombre communes = 18 854

output 3 : le nombre de pages traitées (nombre de fichiers dans les dossiers) = 428 832

=> “**count_csv_contrib.py**” : parcourt tous les csv (35 fichiers) , les transforme en csv et les concatène. puis fait un groupby sur les numéro insee des communes et compte les contributions par communes :

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
