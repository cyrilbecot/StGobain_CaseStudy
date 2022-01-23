# Should run within a Dockerfile that already provide a /input_data directory

cd /input_data # If this gets run from another directory
for id in https://www.data.gouv.fr/fr/datasets/r/0e117c06-248f-45e5-8945-0e79d9136165 https://www.insee.fr/fr/statistiques/fichier/2044751/base-cc-evol-struct-pop-2013.zip https://www.insee.fr/fr/statistiques/fichier/1893149/pop-16ans-dipl6817.zip https://www.insee.fr/fr/statistiques/fichier/2388572/filo-revenu-pauvrete-menage-2013.zip
do
    wget -nv ${id}
done

mkdir GeoShapeCommunes
mv 0e117c06-248f-45e5-8945-0e79d9136165* GeoShapeCommunes
cd GeoShapeCommunes
unzip 0e117c06-248f-45e5-8945-0e79d9136165*
rm 0e117c06-248f-45e5-8945-0e79d9136165*

for id in base-cc-evol-struct-pop-2013 pop-16ans-dipl6817 filo-revenu-pauvrete-menage-2013
do
    mkdir /input_data/${id}
    cd /input_data/${id}
    mv ../${id}.zip .
    unzip ${id}.zip
    rm ${id}.zip
done

mv /input_data/filo-revenu-pauvrete-menage-2013/filo-revenu-pauvrete-menage-2013/filo-revenu-pauvrete-menage-2013.xls /input_data/filo-revenu-pauvrete-menage-2013/filo-revenu-pauvrete-menage-2013.xls
rmdir /input_data/filo-revenu-pauvrete-menage-2013/filo-revenu-pauvrete-menage-2013
