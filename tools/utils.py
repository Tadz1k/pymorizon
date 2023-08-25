url_dict = {
   "buy": "",
    "rent": "/do-wynajecia", 
    "flat": "/mieszkania",
    "house": "/domy",
    "commercial": "/komercyjne",
    "plot": "/dzialki",
    "garage": "/garaze",
    "room": "/pokoje",
}

function_filters = ['loc', 'adowner']

filters_dict = {
    #"loc": "[loc_func]",
    "minprice": "ps%5Bprice_from%5D=[num]",
    "maxprice": "ps%5Bprice_to%5D=[num]",
    "roomcount": "ps%5Bnumber_of_rooms_from%5D=[num]",
    "minbuildyear": "ps%5Bbuild_year_from%5D=[num]",
    "maxbuildyear": "ps%5Bbuild_year_to%5D=[num]",
    "minfloor": "ps%5Bfloor_from%5D=[num]",
    "maxfloor": "ps%5Bfloor_to%5D=[num]",
    "minsize": "ps%5Bliving_area_from%5D=[num]",
    "maxsize": "ps%5Bliving_area_to%5D=[num]",
   # "adowner": "ps%5Bowner%5D%5B0%5D="
}


adowner_dict = {
    "private": "ps%5Bowner%5D%5B0%5D=3",
    "developer": "ps%5Bowner%5D%5B0%5D=2",
    "agency": "ps%5Bowner%5D%5B0%5D=1",
    "other": "ps%5Bowner%5D%5B0%5D=5"
}
