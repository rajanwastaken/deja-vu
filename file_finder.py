import os

def get_largest_files(start_path, top_n=10):
    # List to hold files and their sizes
    files_with_sizes = []

    # Walk through all directories and files in the start path
    for root, dirs, files in os.walk(start_path):
        for file in files:
            # Get the full path of the file
            filepath = os.path.join(root, file)
            try:
                # Get the size of the file and add it to the list
                size = os.path.getsize(filepath)
                files_with_sizes.append((filepath, size))  # Store the full path instead of just the file name
            except OSError:
                # Handle error if file is inaccessible
                print(f"Error accessing file: {filepath}")
                continue

    # Sort the list of files by size in descending order
    sorted_files = sorted(files_with_sizes, key=lambda x: x[1], reverse=True)

    # Print the top N largest files
    print(f"Top {top_n} largest files:")
    for filepath, size in sorted_files[:top_n]:
        print(f"{filepath}: {size} bytes")

# Specify the path to search and number of files to display
directory_path = os.getcwd()  # Can replace with any directory path
get_largest_files(directory_path)
