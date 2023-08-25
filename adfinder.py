import tools.utils as utils
import tools.loc_finder as loc_finder
import webscrapper.page_scrapper as page_scrapper

def find(args):
    try:
        url = build_url(args)
        max_pages = page_scrapper.get_max_pages(url)
        for page in range(max_pages):
            page_url = url + f"&page={page+1}"
            print(page_url)
            #page_scrapper.get_page(page_url)
        
    except Exception as e:
        print(e)
        return

def build_url(args):
    err_arr = get_logic_errors(args)
    if len(err_arr) > 0:
        raise Exception(err_arr)
    url = "https://www.morizon.pl"
    all_args = vars(args)
    modif = False
    first_filter = True
    keys = [key for key, value in all_args.items() if value is not None]
    #get starting keys
    starting_keys = [key for key, value in all_args.items() if value is not None and value in utils.url_dict.keys()]
    function_keys = [key for key, value in all_args.items() if value is not None and key in utils.function_filters]
    filter_keys = [key for key, value in all_args.items() if value is not None and key not in utils.function_filters and key in utils.filters_dict.keys()]
    for key in starting_keys:
        url += utils.url_dict[all_args[key]]
    for key in function_keys:
        if key == 'loc':
            address_url = loc_finder.get_url_location(all_args[key])
            if address_url is None:
                raise Exception("Couldn't find location.")
            url += address_url
        if key == 'adowner':
            if not modif:
                url += "?"
                modif = True
            if first_filter:
                url += utils.adowner_dict[all_args[key]]
                first_filter = False
    for key in filter_keys:
        if not modif:
            url += "?"
            modif = True
        if first_filter:
            url += utils.filters_dict[key].replace("[num]", all_args[key])
            first_filter = False
        else:
            url += "&" + utils.filters_dict[key].replace("[num]", all_args[key])
        
    return url


def get_logic_errors(args):
    err_arr = []
    if args.adtype == "buy" and args.btype == "room":
        err_arr.append("You can't buy a room.")
    
    if args.adtype == "rent" and args.btype == "plot":
        err_arr.append("You can't rent a plot.")
    
    if (args.btype == 'house' or args.btype == 'garage' or args.btype == 'plot') and (args.minfloor is not None or args.maxfloor is not None):
        err_arr.append("You can't specify floor for house or garage.")
    
    if args.minfloor is not None and args.maxfloor is not None and int(args.minfloor) > int(args.maxfloor):
        err_arr.append("Min. floor can't be greater than max. floor.")
    
    if args.minprice is not None and args.maxprice is not None and int(args.minprice) > int(args.maxprice):
        err_arr.append("Min. price can't be greater than max. price.")
    
    if args.minbuildyear is not None and args.maxbuildyear is not None and int(args.minbuildyear) > int(args.maxbuildyear):
        err_arr.append("Min. build year can't be greater than max. build year.")

    return err_arr
    
    
    


