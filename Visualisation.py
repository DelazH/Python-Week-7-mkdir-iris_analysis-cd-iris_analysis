#Task3
import matplotlib.pyplot as plt
import seaborn as sns

def create_visualizations(df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species')
    plt.title('Sepal vs Petal Length')
    plt.savefig('scatterplot.png')
    plt.close()
    
    # Add other visualizations here...
    
if __name__ == "__main__":
    from data_loading import load_data
    df = load_data()
    create_visualizations(df)
