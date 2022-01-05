
#NOT YET WORKING PROPERLY
#NOT INTEGRATED WITH THE ASSISTANT YET

from pytrends.request import TrendReq



# Only need to run this once, the rest of requests will use the same session.
pytrend = TrendReq()

def trending_searches():
    # Get Google Hot Trends data
    trending_searches = pytrend.trending_searches()
    print(trending_searches.head())

def todays_trends():
    # Get Google Today's Trend data
    today_searches = pytrend.today_searches()
    print(today_searches.head())

def top_charts():
    # Get Google Top Charts
    top_charts = pytrend.top_charts(2018, hl='en-US', tz=300, geo='GLOBAL')
    print(top_charts.head())

def keyword_suggestions():
    # Get Google Keyword Suggestions
    kw=input("please enter the keyword you want to search:")
    suggestions_dict = pytrend.suggestions(keyword=kw)
    if suggestions_dict==[]:
        print("No suggestions found for the keyword: " + kw)
    else:
        print(suggestions_dict)

def console_trends():
    print("Available Google Trends Research Options :\n1. Trending Searches\n2. Today's Trends\n3. Top Charts\n4. Keyword Suggestions\n\n type Exit to leave the trends Research console")
    while True:
        choice = input("\n\nPlease enter your choice: ")
        if choice == "1" or choice == "Trending Searches": trending_searches()
        elif choice == "2" or choice == "Today's Trends": todays_trends()
        elif choice == "3" or choice == "Top Charts":
            top_charts()
        elif choice == "4" or choice == "Keyword Suggestions": keyword_suggestions()
        elif choice == "Exit" or choice == "exit" or choice == "quit": break
        else:
            print("\n\nInvalid choice, please try again, Dumbass!")
            continue

if __name__ == '__main__':
    console_trends()