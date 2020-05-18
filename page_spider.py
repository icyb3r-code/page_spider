import os
import argparse
from utilities import url_utils , database_util
from utilities.bcolors import bcolors

def main(database: str, url_list_file: str,top_n: int):

    # web spider code
    big_word_list = []
    blue = f"{bcolors.OKBLUE}[!]{bcolors.ENDC} "

    print(f"{blue} Database working with: " + database)
    print(f"{blue} URL file to Scan: " + url_list_file)
    urls = url_utils.load_urls_from_file(url_list_file)
    for url in urls:
        print (f"{blue} Reading " + url.strip())
        page_content = url_utils.load_pages(url=url.strip())
        words = url_utils.scrape_page(page_contents=page_content)
        big_word_list.extend(words)

    # database code
    #os.chdir(os.path.dirname(__file__)) # this will get the script current directory
    path = os.path.join(os.getcwd(),database)
    database_util.create_database(databse_path=path)
    database_util.save_words_2_databsae(database_path=path,words_list=big_word_list)
    database_util.top_n_rows(database_path=path,top_n=n_rows)
    print()
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-db", "--database", help="SQLite File Name", required=True)
    parser.add_argument("-i", "--input", help="File containing urls to read",required=True,type=str)
    parser.add_argument("-n", "--top_n", help="List Top N word usage Max 15, Min 1",type=int,default=0)
    args = parser.parse_args()
    database_file = args.database
    input_file = args.input
    n_rows = args.top_n
    main(database=database_file, url_list_file=input_file,top_n=n_rows)
