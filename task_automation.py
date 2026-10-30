# Task 3: Task Automation - move all .jpg files to a new folder
import os
import shutil
source = input("Enter the folder path (example: C:/Users/Me/Pictures): ")
new_folder = os.path.join(source, "jpg_files")
# make the new folder if it does not exist
if not os.path.exists(new_folder):
    os.mkdir(new_folder)
count = 0
for file in os.listdir(source):
    if file.lower().endswith(".jpg"):
        shutil.move(os.path.join(source, file), os.path.join(new_folder, file))
        print("Moved:", file)
        count = count + 1
print("Done!", count, "file(s) moved.")
