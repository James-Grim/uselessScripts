import csv
import tkinter as tk
from tkinter import filedialog

def convert_pipe_delimited_to_csv(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r') as infile, open(output_file_path, 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            for line in infile:
                writer.writerow(line.strip().split('|'))
        print(f"File converted successfully and saved as {output_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Initialize the tkinter GUI
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Ask the user to select the input file
    input_file_path = filedialog.askopenfilename(
        title="Select the pipe-delimited file you want to convert",
        filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
    )
    
    if not input_file_path:
        print("No file selected. Exiting...")
        return
    
    # Ask the user to select the location and name for the output file
    output_file_path = filedialog.asksaveasfilename(
        title="Save the output CSV file as",
        filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
    )
    
    if not output_file_path:
        print("No output file specified. Exiting...")
        return

    # Add a .csv extension if not already present
    if not output_file_path.endswith('.csv'):
        output_file_path += '.csv'

    # Convert the file
    convert_pipe_delimited_to_csv(input_file_path, output_file_path)

if __name__ == "__main__":
    main()
