#!/bin/bash

dir="../../../mnt/d/CahiersCitoyensGDNpart2"

# outputs de zipinfo : type'archive', name, size, nb of files, type'file'
# option -h de zipinfo renvoie le header -> path, weight, nb of files
# tr transforme la chaîne1 en la chaîne2 : avec c est le param $5, sans, c'est le param $3
# awk -F = trois paramètres du header zipinfo sans les séparator

# > nb prend la valeur de la sortie totale de zipinfo, pkoi?
for zipped in $dir/*/*.zip;do zipinfo -h $zipped | tr '\n' ':' | awk -F: '{print $2, ":", $5}' ; done
#ne voit que le zip, qu'un seul fichier > ls -1 $dir | wc -l

#error > nb_file=$(awk -F: $3) | nb=$(($nb += $nb_file)); done

#only each nb file, doesnt increment nb > awk -F: '{ $nb =+ $3 }; END { print $3, $nb }' ; done 
#only each nb file, doesnt increment nb > awk -F: '{ nb=nb + $3 }; END { print $3, nb }' ; done


#error > nb_file=$(awk -F : $3) | nb=$(($nb += $nb_file)); done
#error > nb_file=$(awk -F : $3) | echo $nb_file; done

#work basic > awk -F: '{print $3}' ; done

#error > nb_file=$(awk -F : $3) | nb=$(($nb += $nb_file)); done

#work, each file size, origonal from stackoverfl > do zipinfo -h $zipped | tr '\n' ':' | awk -F: '{print $5}' ; done
#work, each file size > awk -F: '{print $3}' ; done
#error > awk -F nb=$(($3 + nb));done

#help exemples :
#        awk '{ somme += $1 }; END { print somme }' fichier
#        awk -F: '{ print $1 }' /etc/passwd
