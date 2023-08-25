import argparse
import adfinder

def main():
    parser = argparse.ArgumentParser("Program to parse morizon.pl website")
    parser.add_argument("-a", "--adtype", help="REQUIRED: Type of advertisment. [buy / rent]", required=True)
    parser.add_argument("-t", "--btype", help="REQUIRED: Type of item. [flat / house / commercial / plot / garage / room]", required=True)
    parser.add_argument("-l", "--loc", help="Localization (city, street etc.)", required=False)
    parser.add_argument("-min", "--minprice", help="Min. price (PLN)", required=False)
    parser.add_argument("-max", "--maxprice", help="Max. price (PLN)", required=False)
    parser.add_argument("-rc", "--roomcount", help="Number of rooms [1 - 9]. More than 9 is 10+", required=False)
    parser.add_argument("-ms", "--minsize", help="Min. size of item in m2", required=False)
    parser.add_argument("-mxs", "--maxsize", help="Max. size of item in m2", required=False)
    parser.add_argument("-bymi", "--minbuildyear", help="Min. build year", required=False)
    parser.add_argument("-byma", "--maxbuildyear", help="Max. build year", required=False)
    parser.add_argument("-fmi", "--minfloor", help="Min. floor number", required=False)
    parser.add_argument("-fma", "--maxfloor", help="Max. floor number", required=False)
    parser.add_argument("-ao", "--adowner", help="Ad owner [private / developer / agency, other]", required=False)
    args = parser.parse_args()
    adfinder.find(args)
    pass


if __name__ == '__main__':
    main()