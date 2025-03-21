# Construct a program to read cities.csv dataset, remove last column and save it in
# an array. Save the last column to another array. Plot the first two columns.

import numpy as np  # Import NumPy for array operations
import matplotlib.pyplot as plt  # Import Matplotlib for plotting
import csv  # Import CSV module

def process_csv(file_path):
    """Reads a CSV file, removes the last column, and saves data in separate arrays."""
    
    data = []  # List to store the main data (excluding last column)
    last_column = []  # List to store the last column separately
    
    try:
        # Open the CSV file
        with open(file_path, 'r') as file:
            reader = csv.reader(file)  # Create a CSV reader object
            header = next(reader)  # Read the header (first row)

            for row in reader:
                if len(row) < 2:  # Skip empty or invalid rows
                    continue

                data.append(row[:-1])  # Add all columns except last to `data`
                last_column.append(row[-1])  # Add last column separately

        # Convert lists to NumPy arrays
        data_array = np.array(data, dtype=float)  # Convert main data to NumPy array
        last_column_array = np.array(last_column)  # Convert last column to NumPy array

        return data_array, last_column_array

    except FileNotFoundError:
        print("Error: The file does not exist!")
        return None, None
    except ValueError:
        print("Error: Ensure all numeric columns contain valid numbers.")
        return None, None

def plot_columns(data):
    """Plots the first two columns of the dataset."""
    if data is None or len(data) == 0:
        print("No data available for plotting.")
        return

    plt.figure(figsize=(8, 6))  # Set figure size
    plt.scatter(data[:, 0], data[:, 1], color='blue', alpha=0.6)  # Scatter plot (x: col1, y: col2)

    plt.xlabel("Column 1")  # Label for X-axis
    plt.ylabel("Column 2")  # Label for Y-axis
    plt.title("Scatter Plot of First Two Columns")  # Title
    plt.grid(True)  # Show grid

    plt.show()  # Display the plot

# Example Usage
file_name = "cities.csv"  # Replace with your actual file name
data_array, last_column_array = process_csv(file_name)  # Read and process CSV

if data_array is not None:
    print("Data (excluding last column):\n", data_array)
    print("Last Column Data:\n", last_column_array)
    plot_columns(data_array)  # Plot the first two columns
