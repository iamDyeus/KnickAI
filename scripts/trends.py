
#NOT YET WORKING PROPERLY
#NOT INTEGRATED WITH THE ASSISTANT YET


from rich import print
from pytrends.request import TrendReq

# Only need to run this once, the rest of requests will use the same session.
pytrend = TrendReq()

def trending_searches():
    # Get Google Hot Trends data
    trending_searches_df = pytrend.trending_searches()
    print(trending_searches_df.head())

def todays_trends():
    # Get Google Today's Trend data
    today_searches_df = pytrend.today_searches()
    print(today_searches_df.head())

def top_charts():
    # Get Google Top Charts
    top_charts_df = pytrend.top_charts(2018, hl='en-US', tz=300, geo='GLOBAL')
    print(top_charts_df.head())

def keyword_suggestions():
    # Get Google Keyword Suggestions
    kw=input("please enter the keyword you want to search:")
    suggestions_dict = pytrend.suggestions(keyword=kw)
    print(suggestions_dict)

def console_trends():
    print("Available Google Trends Research Options :")
    print("1. Trending Searches")
    print("2. Today's Trends")
    print("3. Top Charts")
    print("4. Keyword Suggestions")
    print("\n\n type Exit to leave the trends Research console")
    while True:
        choice = input("\n\nPlease enter your choice: ")
        if choice == "1" or choice == "Trending Searches":
            trending_searches()
        elif choice == "2" or choice == "Today's Trends":
            todays_trends()
        elif choice == "3" or choice == "Top Charts":
            top_charts()
        elif choice == "4" or choice == "Keyword Suggestions":
            keyword_suggestions()
        elif choice == "Exit" or choice == "exit" or choice == "quit":
            break
        else:
            print("\n\nInvalid choice, please try again, Dumbass!")
            continue


console_trends()