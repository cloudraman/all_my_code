#assuming a module requests ,
import requests

def get_trending_keywords(timeframe='today 12-m'):
    """
    Returns a list of trending keywords for the specified timeframe.
    The timeframe parameter can be one of the following values:
        'today 12-m' (default)
        'today 5-y'
        'all'
    """
    # Set the API endpoint and parameters
    endpoint = 'https://trends.google.com/trends/api/explore'
    params = {
        'hl': 'en-US',
        'tz': '-120',
        'req': '{"comparisonItem":[{"keyword":"%s","geo":"%s","time":"%s"}],"category":0,"property":""}' % ("", "", timeframe)
    }
    
    # Send the GET request
    response = requests.get(endpoint, params=params)
    
    # Extract the trending keywords from the response
    if response.status_code == 200:
        data = response.json()
        keywords = [trend['title']['query'] for trend in data['default']['trendingSearchesDays'][0]['trendingSearches']]
        return keywords
    else:
        return []

# Get the trending keywords for the past 12 months
keywords = get_trending_keywords()
print(keywords)