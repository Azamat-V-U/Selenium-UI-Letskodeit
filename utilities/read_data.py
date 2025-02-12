# import os
import csv
# from dotenv import load_dotenv

# load_dotenv()


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


# def get_csv_data():
#     csv_file_path = os.getenv("CSV_FILE_PATH")
#
#     if not csv_file_path:
#         raise FileNotFoundError("CSV file path not found in .env file")
#
#     data = []
#     try:
#         # Open the CSV file using 'with' to ensure it is properly closed after reading
#         with open(csv_file_path, newline="", encoding="utf-8") as data_file:
#             # Create a CSV Reader from the CSV file
#             reader = csv.reader(data_file)
#             # Skip the headers
#             next(reader)
#             # Add rows from reader to list
#             for row in reader:
#                 data.append(row)
#     # except FileNotFoundError:
#     #     print(f"Error: The file '{file_name}' doesn't exist.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#     return data