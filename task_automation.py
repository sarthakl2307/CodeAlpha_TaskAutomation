
import os
import shutil

base_folder = os.path.dirname(os.path.abspath(__file__))
source_folder = os.path.join(base_folder, "Source_Images")
destination_folder = os.path.join(base_folder, "Sorted_Images")

if not os.path.isdir(source_folder):
    print("Error: Source_Images folder does not exist.")
else:
    os.makedirs(destination_folder, exist_ok=True)
    count = 0

    for filename in os.listdir(source_folder):
        if filename.lower().endswith(".jpg"):
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(
                destination_folder, filename
            )

            if not os.path.isfile(source_path):
                continue

            if os.path.exists(destination_path):
                print(f"Skipped: {filename} already exists.")
                continue

            try:
                shutil.move(source_path, destination_path)
                print(f"Moved: {filename}")
                count += 1
            except OSError as error:
                print(f"Could not move {filename}: {error}")

    print(f"\nTask completed! Total files moved: {count}")
