from src.data_load import load_data
if __name__ == "__main__":
    # Example usage of the load_data function
    file_path = "data/MachineLearningRating_v3.txt"  # Adjust the path as needed
    data = load_data(file_path)
    
    if not data.empty:
        print("Data loaded successfully:")
        print(data.head())
    else:
        print("No data loaded.")