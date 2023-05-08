import os
import time

### NOTE that this works for Date Modified, not "Date" for Windows.


# Specify the path to the folder
folder_path = "path/to/file"

# Get the current time as a Unix timestamp
current_time = time.time()

# Iterate over each file in the folder
for file_name in os.listdir(folder_path):
    # Construct the full path to the file
    file_path = os.path.join(folder_path, file_name)

    # Set the modification time of the file to the current time
    os.utime(file_path, (current_time, current_time))