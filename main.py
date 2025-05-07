#Task4
from data_loading import load_data
from data_analysis import analyze_data
from visualization import create_visualizations

def main():
    print("Starting analysis...")
    df = load_data()
    analyze_data(df)
    create_visualizations(df)
    print("Analysis complete! Check the generated plots.")

if __name__ == "__main__":
    main()
