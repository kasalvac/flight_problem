import os
directory = r"C:\Users\kasal\Desktop\KaV_CIP_procedury"

# Loop through all files in the directory
for filename in os.listdir(directory):
    # Get the full file path
    old_name = os.path.join(directory, filename)

    # Only rename files (skip directories)
    if os.path.isfile(old_name):
        # Replace spaces with underscores
        new_name = os.path.join(directory, filename.replace(" ", "_"))

        # Rename the file
        os.rename(old_name, new_name)

        print(f'Renamed: {filename} -> {new_name.split(os.sep)[-1]}')

print("Renaming completed.")
