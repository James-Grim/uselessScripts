# Converter file for USNews Grad data transforms
# The inconsistency in the data and the differences in the seperate colleges

import pandas as pd
import pycountry
from tkinter import Tk, filedialog, Label, Button, StringVar, ttk, messagebox
import traceback

def select_source_college_and_file():
    """
    Opens a dialog to select the college and a file dialog to select a CSV file.
    """
    try:
        root = Tk()
        root.title("Data Transformer")
        root.geometry('400x300')

        # Variables to store selections
        college_var = StringVar(root)
        file_var = StringVar(root)

        # Set default value for college
        college_var.set("ENG")

        # Styling
        style = ttk.Style()
        style.configure('TLabel', font=('Helvetica', 12))
        style.configure('TButton', font=('Helvetica', 12))
        style.configure('TOptionMenu', font=('Helvetica', 12))

        # Dropdown menu for college selection
        Label(root, text="Please select the college:", font=('Helvetica', 12)).pack(pady=10)
        college_options = ['ENG', 'AS', 'BU', 'EDU']
        college_menu = ttk.OptionMenu(root, college_var, *college_options)
        college_menu.pack(pady=10)

        def on_file_select():
            filename = filedialog.askopenfilename(title="Select a CSV file", filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
            if filename:
                file_var.set(filename)  # Store the filename
                root.quit()  # Stop the main loop

        # Button to confirm selections and proceed to file selection
        ttk.Button(root, text="Select File", command=on_file_select).pack(pady=20)

        root.mainloop()  # Start the GUI event loop
        root.destroy()  # Destroy the root window after exiting the main loop

        # Return the selections
        return college_var.get(), file_var.get()
    
    except Exception as e:
        # Show an error message box
        messagebox.showerror("Error", f"An error occurred while selecting the file: {e}")
        log_error(e)  # Log the error to a file

def convert_csv_data(input_file, output_file, college):
    """
    Performs data transformations on the selected CSV file based on the college selection
    and saves the result to a new file.
    """
    try:
        # Load the CSV file into a DataFrame
        df = pd.read_csv(input_file)

        # Add 'college' column with the selected college
        df.insert(0, 'college', college)

        # Insert a new column 'level' at the beginning with all values set to 'GR'
        df.insert(1, 'level', 'GR')

        df.insert(2, 'ERx_Import__Source__c', 'Grad - USNews')

        # Trim datetime data in 'student_connect_action_date'
        df['student_connect_action_date'] = df['student_connect_action_date'].str.split('.').str[0]

        # Date conversion
        date_column = 'date_of_birth'
        df[date_column] = df[date_column].str.split(' ').str[0]  # Strip time component if present
        df[date_column] = pd.to_datetime(df[date_column], errors='coerce').dt.strftime('%m/%d/%Y')

        # Student type transformation
        type_column = 'student_type'
        df[type_column] = df[type_column].map({
            'first-year': 'F',
            'transfer': 'T'
        }).fillna(df[type_column])

        # Name cleanup
        name_columns = ['first_name', 'last_name']
        for column in name_columns:
            df[column] = df[column].replace(regex=r'[^a-zA-Z\s]', value='')
            if column == 'first_name':
                df[column] = df[column].replace('', 'FNU')
            elif column == 'last_name':
                df[column] = df[column].replace('', 'LNU')

        # Gender transformation
        df['gender'] = df['gender'].map({
            'male': 'M',
            'female': 'F'
        }).fillna('Prefer Not to Answer')

        # Country code to name transformation
        countries = {country.alpha_2: country.name for country in pycountry.countries}
        df['country'] = df['country'].map(lambda code: 'United States of America' if code == 'US' else countries.get(code, None))

        # Change every value in 'student_connect_source' to 'usnews'
        df['student_connect_source'] = 'usnews'

        # Save the modified DataFrame back to a CSV file
        df.to_csv(output_file, index=False)

        print(f"Converted and modified CSV file saved to '{output_file}'.")

    except Exception as e:
        # Show an error message box
        messagebox.showerror("Error", f"An error occurred while converting the CSV: {e}")
        log_error(e)  # Log the error to a file

def log_error(error):
    """
    Logs the error details to a file for debugging purposes.
    """
    with open("error_log.txt", "a") as f:
        f.write("Error occurred:\n")
        f.write(traceback.format_exc())
        f.write("\n")

def main():
    try:
        college, input_file = select_source_college_and_file()
        if input_file:
            output_file = input_file.rsplit('.', 1)[0] + '_modified.csv'
            convert_csv_data(input_file, output_file, college)
        else:
            print("No file selected. Exiting...")
    except Exception as e:
        # Catch any unexpected error and display it
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")
        log_error(e)  # Log the error to a file

if __name__ == "__main__":
    main()
