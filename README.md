# StGobain Case Study
Repository to store code &amp; notebooks for St Gobain's 2nd round interview

The goal of this case study is to analyze a mock Referundum's data.
In addition to the actual referundum results (by townhall) that are provided by StGobain, I dediced to use the following datasets :

* The official admnitrative division provided by the French governement [here](https://www.data.gouv.fr/fr/datasets/r/0e117c06-248f-45e5-8945-0e79d9136165)

It is provided in shapefile format, projection WGS84.

Sadly the last official import is from 1st January 2022, and former ones aren't available...

It is extracted from OpenStreetData that themselves take it from the Cadastre.


* The "recensement", i.e. number of person by age class in each city taken [here](https://www.insee.fr/fr/statistiques/fichier/2044751/base-cc-evol-struct-pop-2013.zip). It also gives the socio-professional split but *only* for town with more than 2k people.

* The distribution of the level of education in each city or departement taken [here](https://www.insee.fr/fr/statistiques/fichier/1893149/pop-16ans-dipl6817.zip). The last closest point is 2012. The next one 2017.

* The distribution of income in each city/departement or region taken from [here](https://www.insee.fr/fr/statistiques/fichier/2388572/filo-revenu-pauvrete-menage-2013.zip). Depending of the number of people in each area, not all observables are available. They are all availables only for regions above 2k people.
