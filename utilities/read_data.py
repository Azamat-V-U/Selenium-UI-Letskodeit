import csv


def get_csv_data(file_name):
    # Create an empty list to store rows
    rows = []
    try:
        # Open the CSV file using 'with' to ensure it is properly closed after reading
        with open(file_name, mode="r", newline="", encoding="utf-8") as data_file:
            # Create a CSV Reader from the CSV file
            reader = csv.reader(data_file)
            # Skip the headers
            next(reader)
            # Add rows from reader to list
            for row in reader:
                rows.append(row)
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' doesn't exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return rows
