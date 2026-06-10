import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def perform_eda(file_path):
    print("--- TASK 2: EXPLORATORY DATA ANALYSIS (EDA) ---\n")

    # 1. Ask meaningful questions before analysis
    print("Questions we are asking:")
    print("- What is the overall structure of our scraped data?")
    print("- Are there any missing or duplicate quotes (data issues)?")
    print("- Who are the most prolific authors in this dataset (trends)?")
    print("- Is there a correlation between the length of a quote and how many tags it has (hypothesis testing)?\n")

    # Load the dataset
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: Could not find {file_path}. Please run the scraper first.")
        return

    # 2. Explore the data structure (Variables and Data Types)
    print("--- DATA STRUCTURE ---")
    print("First 3 rows of data:")
    print(df.head(3), "\n")
    print("Data Types and Non-Null Counts:")
    print(df.info(), "\n")

    # 3. Detect potential data issues or problems
    print("--- DATA ISSUES ---")
    missing_values = df.isnull().sum()
    print(f"Missing values per column:\n{missing_values}\n")
    
    duplicates = df.duplicated().sum()
    print(f"Number of duplicate rows: {duplicates}")
    if duplicates > 0:
        df = df.drop_duplicates()
        print("-> Duplicates removed for cleaner analysis.\n")
    else:
        print("\n")

    # --- Feature Engineering (Adding numbers to text data for statistical analysis) ---
    # To find trends and test hypotheses, we need numbers. Let's calculate them.
    df['Quote_Length'] = df['Quote'].astype(str).apply(len)
    
    # Handle NaN values in Tags before splitting
    df['Tags'] = df['Tags'].fillna('')
    df['Tag_Count'] = df['Tags'].apply(lambda x: len(x.split(',')) if x != '' else 0)


    # 4. Identify trends, patterns, and anomalies
    print("--- TRENDS & PATTERNS ---")
    top_authors = df['Author'].value_counts().head(5)
    print(f"Top 5 Authors by number of quotes:\n{top_authors}\n")

    print("Basic Statistics on Quote Length and Tag Count:")
    print(df[['Quote_Length', 'Tag_Count']].describe(), "\n")

    # 5. Test hypotheses and validate assumptions using visualization
    # Hypothesis: Longer quotes naturally have more tags to describe them.
    
    # Visualization 1: Top Authors (Bar Chart)
    plt.figure(figsize=(10, 5))
    sns.barplot(x=top_authors.values, y=top_authors.index, hue=top_authors.index, palette='viridis', legend=False)
    plt.title('Top 5 Most Frequent Authors')
    plt.xlabel('Number of Quotes')
    plt.ylabel('Author')
    plt.tight_layout()
    plt.show()

    # Visualization 2: Testing the Hypothesis (Scatter Plot)
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x='Quote_Length', y='Tag_Count', alpha=0.7, color='coral')
    plt.title('Hypothesis Test: Quote Length vs. Number of Tags')
    plt.xlabel('Length of Quote (Characters)')
    plt.ylabel('Number of Tags')
    plt.tight_layout()
    plt.show()

# --- Main Execution ---
if __name__ == "__main__":
    dataset_file = "scraped_quotes_dataset.csv"
    perform_eda(dataset_file)
