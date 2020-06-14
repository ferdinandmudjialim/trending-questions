# Quora Questions Suggestions
# Ferdinand Mudjialim, 2020-05-11

from pytrends.request import TrendReq
import pandas as pd

def main(): 
    pytrends = TrendReq(hl='en-US', tz=360)

    # print('Trending Searches in the United States right now')
    # print(pytrends.trending_searches(pn='united_states')) # trending searches in US
    
    period_list = ['all', 'today 1-m', 'now 7-d', 'now 1-d']
    period = period_list[3]

    # keywords = ['what are', 'why is', 'why do', 'how should i', 'how to', 'who was']
    keywords = ['why do', 'why is', 'what is the best']

    for item in keywords: 
        pytrends.build_payload(kw_list=[item], cat=0, timeframe=str(period), geo='', gprop='')

        related_queries_dict = pytrends.related_queries()
        for key in related_queries_dict: 
            for subkey in related_queries_dict[key]:
                print('Query:', '"', key, '"', 'from Google Trends', subkey, 'category')
                print(related_queries_dict[key][subkey])
                print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')


if __name__ == "__main__":
    main()