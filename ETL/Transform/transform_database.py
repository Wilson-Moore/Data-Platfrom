import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def review_text_to_score() -> None:
    dataframe=pd.read_csv("staging/database/table_reviews.csv")
    sid_obj=SentimentIntensityAnalyzer()
    
    score=[]
    
    for product in dataframe.groupby("Product_ID"):
        count=0
        sum=0
        for sentence in product[1]["Review_Text"]:
            sentiment_dict=sid_obj.polarity_scores(sentence)
            count+=1
            sum+=sentiment_dict['compound']
        score.append(sum/count)
    
    dataframe=pd.read_csv("staging/database/table_products.csv")
    dataframe.sort_values(by=["Product_ID"])
    dataframe["Score"]=score

    dataframe.to_csv("staging/database/table_products.csv",index=False)

def transform_erp() -> None:
    review_text_to_score()