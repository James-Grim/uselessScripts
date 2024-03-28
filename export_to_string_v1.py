import pandas as pd

def csv_column_to_string(file_path):
    """
    Reads a CSV file with one column and returns all the values as a comma-separated string,
    with each value wrapped in single quotation marks.

    :param file_path: Path to the CSV file.
    :return: A string containing all values from the column, separated by commas and each value wrapped in single quotation marks.
    """
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Convert the first column to a list
    values_list = df.iloc[:, 0].tolist()
    
    # Join the list into a single string, separated by commas, with each value wrapped in single quotation marks
    values_string = ','.join(f"'{value}'" for value in values_list)
    
    return values_string

# Example usage
file_path = 'you_csv_file.csv'  # Replace with your CSV file path
result_string = csv_column_to_string(file_path)
print(result_string)
