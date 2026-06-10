import pandas as pd
from textblob import TextBlob

def perform_sentiment_analysis():
    print("--- TASK 4: SENTIMENT ANALYSIS ---\n")

    # 1. Load Data: Creating a mock dataset of reviews & social media (Task Step 3)
    # In a real scenario, you would use pd.read_csv('amazon_reviews.csv')
    sample_data = [
        "I absolutely love this product! It works perfectly and saves me so much time.", 
        "Terrible experience. The item broke after two days of use. Do not buy.",        
        "It's okay. Does the job, but nothing special for the price.",                 
        "Amazing customer service! They replaced my defective unit immediately.",        
        "The delivery was late and the packaging was damaged. Very disappointed."        
    ]
    
    df = pd.DataFrame(sample_data, columns=['Text_Data'])

    # 2. Define the NLP classification function (Task Step 1 & 2)
    def classify_sentiment(text):
        """
        Uses TextBlob to calculate polarity (how positive or negative a text is).
        Polarity ranges from -1.0 (very negative) to 1.0 (very positive).
        """
        # Create a TextBlob object (this applies the NLP lexicon)
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        
        # Classify as Positive, Negative, or Neutral based on the score
        if polarity > 0.1:
            return 'Positive'
        elif polarity < -0.1:
            return 'Negative'
        else:
            return 'Neutral'

    # Apply the classification function to our text dataset
    print("Analyzing text data...\n")
    df['Sentiment_Category'] = df['Text_Data'].apply(classify_sentiment)

    # 3. View the classified data
    print("--- ANALYSIS RESULTS ---")
    # Display the full width of the text column for easy reading
    pd.set_option('display.max_colwidth', None) 
    print(df[['Text_Data', 'Sentiment_Category']], "\n")

    # 4. Understand public opinion and trends (Task Step 4)
    print("--- PUBLIC OPINION TRENDS ---")
    sentiment_counts = df['Sentiment_Category'].value_counts()
    print("Total Sentiment Breakdown:")
    print(sentiment_counts.to_string())
    
    # 5. Business Insights (Task Step 5)
    print("\n--- BUSINESS ACTION INSIGHTS ---")
    positive_pct = (sentiment_counts.get('Positive', 0) / len(df)) * 100
    negative_pct = (sentiment_counts.get('Negative', 0) / len(df)) * 100
    
    if negative_pct > 30:
        print("Insight: High negative sentiment detected. Immediate product development or customer service review required.")
    elif positive_pct > 50:
        print("Insight: Strong positive public opinion. Use these positive reviews in upcoming marketing campaigns.")
    else:
        print("Insight: Sentiment is mixed or neutral. Monitor trends closely for shifts in public opinion.")

# --- Main Execution ---
if __name__ == "__main__":
    perform_sentiment_analysis()
