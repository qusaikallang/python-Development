from search_engine_parser import GoogleSearch


def main(search_query,numRes):
    page_num =1
    query = (search_query)
    result_count = 1
    file  = open('data.txt','a')
    google = GoogleSearch()
    res = google.search(query,page_num)

    while 1:
        for i in range(0,10):
            result_count +=1
            file.write('tilte -'+res['titles'][i]+'\n'+'link -'+res['links'][i]+'\n'+'Description -'+res['descriptions'][i]+'\n')
        if result_count < numRes:
            page_num +=1
            res = google.search(query,page_num)
        else:
            break

if __name__=='__main__':
    main("web crawling king",50)