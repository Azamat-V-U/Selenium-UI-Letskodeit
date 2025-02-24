import os
import csv
from dotenv import load_dotenv

load_dotenv()


def get_csv_data(file_name):
    # csv_file_path = os.getenv("CSV_FILE_PATH")
    # csv_file_path = os.getenv(file_name)
    csv_file_path = file_name

    if not csv_file_path or not os.path.exists(csv_file_path):
        raise FileNotFoundError(f"CSV file path not found in {file_name} file")

    data = []
    try:
        # Open the CSV file using 'with' to ensure it is properly closed after reading
        with open(csv_file_path, newline="", encoding="utf-8") as data_file:
            # Create a CSV Reader from the CSV file
            reader = csv.reader(data_file)
            # Skip the headers
            next(reader)
            # Add rows from reader to list
            for row in reader:
                data.append(row)
    except Exception as e:
        print(f"An error occurred: {e}")
    # print(data)
    return data
