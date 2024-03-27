import pandas as pd
from tkinter import Tk, filedialog

def select_files():
    """Open a file dialog to select multiple CSV files."""
    root = Tk()
    root.withdraw()  # Hide the Tkinter root window
    # Open file dialog and return selected file paths
    file_paths = filedialog.askopenfilenames(title='Select CSV Files', filetypes=[('CSV Files', '*.csv')])
    return root.tk.splitlist(file_paths)

def compile_csv_columns_to_rows(file_paths, column_names, output_file_path):
    """
    Compile specified columns from multiple CSVs into rows in a new CSV.
    
    :param file_paths: List of paths to the CSV files.
    :param column_names: List of column names to extract from each CSV.
    :param output_file_path: Path for the output CSV file.
    """
    compiled_data = []

    for file_path in file_paths:
        # Read the CSV file, focusing on the specified columns
        df = pd.read_csv(file_path, usecols=column_names)
        # Append each row of the specified columns to the compiled data
        for index, row in df.iterrows():
            compiled_data.append(row.values)

    # Create a new DataFrame from the compiled data
    compiled_df = pd.DataFrame(compiled_data, columns=column_names)
    # Save the new DataFrame to a CSV file
    compiled_df.to_csv(output_file_path, index=False)
    print(f"Data compiled and saved to {output_file_path}")

if __name__ == "__main__":
    selected_files = select_files()  # Let the user select files
    if selected_files:
        columns_to_extract = ['coalitionId', 'scoir_id', 'guardian_live_with',	'guardian_live_with_other',	'parents_marital_status',	'parents_marital_status_other',	'guardian_deceased_yn_1', 'guardian_name_first_1', 'guardian_name_last_1','guardian_relationship_1',	'guardian_relationship_other_1',	'guardian_email_1',	'guardian_country_1',	'guardian_street_1',	'guardian_street2_1',	'guardian_city_1',	'guardian_state_1',	'guardian_province_1',	'guardian_postal_code_1',	'guardian_addr_verification_1',	'guardian_phone_country_code_1',	'guardian_phone_1',	'guardian_phone_type_1',	'guardian_education_level_1',	'guardian_occupation_title_1',	'guardian_employed_university_1',	'guardian_university_employer_1',	'guardian_employer_1',	'guardian_birth_country_1',	'guardian_deceased_yn_2',	'guardian_name_first_2',	'guardian_name_last_2',	'guardian_relationship_2',	'guardian_relationship_other_2',	'guardian_email_2',	'guardian_country_2',	'guardian_street_2',	'guardian_street2_2',	'guardian_city_2',	'guardian_state_2',	'guardian_province_2',	'guardian_postal_code_2',	'guardian_addr_verification_2',	'guardian_phone_country_code_2',	'guardian_phone_2',	'guardian_phone_type_2',	'guardian_education_level_2',	'guardian_occupation_title_2',	'guardian_employed_university_2',	'guardian_university_employer_2',	'guardian_employer_2','guardian_birth_country_2',	'guardian_deceased_yn_3',	'guardian_name_first_3',	'guardian_name_last_3',	'guardian_relationship_3',	'guardian_relationship_other_3',	'guardian_email_3',	'guardian_country_3',	'guardian_street_3',	'guardian_street2_3',	'guardian_city_3',	'guardian_state_3',	'guardian_province_3',	'guardian_postal_code_3',	'guardian_addr_verification_3',	'guardian_phone_country_code_3',	'guardian_phone_3',	'guardian_phone_type_3',	'guardian_education_level_3',	'guardian_occupation_title_3',	'guardian_employed_university_3',	'guardian_university_employer_3',	'guardian_employer_3',	'guardian_birth_country_3',	'guardian_deceased_yn_4',	'guardian_name_first_4',	'guardian_name_last_4',	'guardian_relationship_4',	'guardian_relationship_other_4',	'guardian_email_4',	'guardian_country_4', 'guardian_street_4',	'guardian_street2_4',	'guardian_city_4',	'guardian_state_4',	'guardian_province_4',	'guardian_postal_code_4',	'guardian_addr_verification_4',	'guardian_phone_country_code_4',	'guardian_phone_4',	'guardian_phone_type_4',	'guardian_education_level_4','guardian_occupation_title_4',	'guardian_employed_university_4',	'guardian_university_employer_4',	'guardian_employer_4',	'guardian_birth_country_4',	'sibling_first_1',	'sibling_last_1',	'sibling_age_1',	'sibling_first_2',	'sibling_last_2',	'sibling_age_2',	'sibling_first_3',	'sibling_last_3',	'sibling_age_3',	'sibling_first_4',	'sibling_last_4',	'sibling_age_4',	'sibling_additional'] # Specify the column names to extract
        output_csv_path = 'compiled_output.csv'  # Define the output file path
        compile_csv_columns_to_rows(selected_files, columns_to_extract, output_csv_path)
    else:
        print("No files selected.")
