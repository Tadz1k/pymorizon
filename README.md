# pymorizon

pymorizon scrapping tool

Arguments:
* --adtype [buy/rent] - type of advertisment REQUIRED
* --btype [flat/house/commercial/plot/garage/room] - type of property REQUIRED
* --loc - localization. To get better search result script uses geopy lib
* --minprice - in PLN
* --maxprice - in PLN
* --rc - room count[0-10] where 10 means 10+
* --minsize - min size in m^2
* --maxsize - max size in m^2
* --minbuildyear - min year of build
* --maxbuildyear - max year of build
* --minfloor - min floor of property
* --maxfloor - max floor of property
* --adowner - advertisment owner [private/developer/agency/other]

Example usage:  

python main.py --adtype buy --btype plot --minsize 900 --maxsize 3000 --maxprice 700000 --adowner private --loc Warszawa

Generated link : https://www.morizon.pl/dzialki/Warszawa?ps%5Bowner%5D%5B0%5D=3&ps%5Bprice_to%5D=700000&ps%5Bliving_area_from%5D=900&ps%5Bliving_area_to%5D=3000&page=1

Script counts number of page automatically
