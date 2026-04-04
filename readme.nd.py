"""
Final Project: Automated Data Reporter
Author: ccyeo
Description: Professional script that processes user input and saves results to a file.
"""

import os
import sys


def process_data(data_list):
    """
    Core Logic: Processes a list of strings into numeric values and calculates stats.
    """
    try:
        # Convert strings to numbers, ignoring non-numeric junk
        numbers = [float(x) for x in data_list if x.replace('.', '', 1).isdigit()]

        if not numbers:
            return None

        return {
            "count": len(numbers),
            "sum": sum(numbers),
            "average": sum(numbers) / len(numbers),
            "max": max(numbers)
        }
    except Exception as e:
        print(f"Error in processing: {e}")
        return None


def save_report(results):
    """
    File I/O: Saves the processed data to the 'output/' directory.
    """
    # Ensure the output directory exists as per README
    if not os.path.exists('output'):
        os.makedirs('output')

    report_path = "output/results.txt"

    with open(report_path, "w") as f:
        f.write("--- FINAL PROJECT REPORT ---\n")
        for key, value in results.items():
            f.write(f"{key.capitalize()}: {value}\n")

    return os.path.abspath(report_path)


def main():
    print("=== Welcome to the Automated Reporter ===")
    print("Enter a list of numbers (separated by spaces).")

    try:
        # 1. Get User Input
        user_input = input("> ").split()

        if not user_input:
            print("No data entered. Exiting.")
            return

        # 2. Process
        stats = process_data(user_input)

        if stats:
            # 3. Save to File
            file_loc = save_report(stats)

            # 4. Print Results to Console
            print("\n--- RESULTS ---")
            print(f"Items Processed: {stats['count']}")
            print(f"Average Value:   {stats['average']:.2f}")
            print(f"Maximum Value:   {stats['max']}")
            print(f"\n[SUCCESS] Report saved at: {file_loc}")
        else:
            print("[ERROR] No valid numeric data found to process.")

    except KeyboardInterrupt:
        print("\nProgram closed by user.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")


if __name__ == "__main__":
    main()