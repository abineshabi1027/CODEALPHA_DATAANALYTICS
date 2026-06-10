import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_dashboard(file_path):
    print("--- TASK 3: DATA VISUALIZATION ---")
    print("Loading data and generating portfolio dashboard...")

    # 1. Load the dataset
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: Could not find {file_path}. Please run the scraper first.")
        return

    # 2. Prepare Data (Transforming raw data for visuals)
    # Calculate quote lengths
    df['Quote_Length'] = df['Quote'].astype(str).apply(len)
    
    # Process Tags to find the most popular topics
    df['Tags'] = df['Tags'].fillna('')
    # Split the comma-separated tags and create a massive list of all individual tags
    all_tags = df['Tags'].str.split(', ').explode()
    # Count the occurrences, ignoring empty strings
    top_tags = all_tags[all_tags != ''].value_counts().head(10)
    
    # Get top authors
    top_authors = df['Author'].value_counts().head(10)

    # 3. Design Visuals (Set up a 2x2 grid for a 'Dashboard' feel)
    sns.set_theme(style="whitegrid") # Sets a clean, professional theme
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('Quotes Dataset Analysis Dashboard', fontsize=20, fontweight='bold', y=0.98)

    # --- Visual 1: Top Authors (Top Left) ---
    sns.barplot(
        ax=axes[0, 0], 
        x=top_authors.values, 
        y=top_authors.index, 
        hue=top_authors.index,
        palette='magma', 
        legend=False
    )
    axes[0, 0].set_title('Top 10 Most Quoted Authors', fontsize=14)
    axes[0, 0].set_xlabel('Number of Quotes')
    axes[0, 0].set_ylabel('')

    # --- Visual 2: Top Topics/Tags (Top Right) ---
    sns.barplot(
        ax=axes[0, 1], 
        x=top_tags.values, 
        y=top_tags.index, 
        hue=top_tags.index,
        palette='crest', 
        legend=False
    )
    axes[0, 1].set_title('Top 10 Most Popular Topics (Tags)', fontsize=14)
    axes[0, 1].set_xlabel('Frequency of Tag')
    axes[0, 1].set_ylabel('')

    # --- Visual 3: Distribution of Quote Lengths (Bottom Left) ---
    sns.histplot(
        ax=axes[1, 0], 
        data=df, 
        x='Quote_Length', 
        bins=20, 
        kde=True, 
        color='teal'
    )
    axes[1, 0].set_title('Distribution of Quote Lengths', fontsize=14)
    axes[1, 0].set_xlabel('Number of Characters in Quote')
    axes[1, 0].set_ylabel('Count')

    # --- Visual 4: Boxplot of Quote Lengths by Top 5 Authors (Bottom Right) ---
    # Filter data to only include the top 5 authors for a cleaner chart
    top_5_authors = top_authors.head(5).index
    df_top_5 = df[df['Author'].isin(top_5_authors)]
    
    sns.boxplot(
        ax=axes[1, 1], 
        data=df_top_5, 
        x='Quote_Length', 
        y='Author',
        hue='Author',
        palette='Set2',
        legend=False
    )
    axes[1, 1].set_title('Quote Length Variability among Top 5 Authors', fontsize=14)
    axes[1, 1].set_xlabel('Number of Characters')
    axes[1, 1].set_ylabel('')

    # 4. Craft Compelling Data Stories (Final layout adjustments)
    plt.tight_layout()
    # Add a small buffer at the top so the main title doesn't overlap
    plt.subplots_adjust(top=0.92) 
    
    print("Dashboard generated successfully! Close the window to exit.")
    # Display the dashboard
    plt.show()

# --- Main Execution ---
if __name__ == "__main__":
    dataset_file = "scraped_quotes_dataset.csv"
    create_dashboard(dataset_file)
