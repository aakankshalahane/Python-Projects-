import os, shutil

folder = input("Enter folder path: ")
for f in os.listdir(folder):
    if os.path.isfile(os.path.join(folder, f)):
        ext = f.split('.')[-1]
        new_dir = os.path.join(folder, ext)
        os.makedirs(new_dir, exist_ok=True)
        shutil.move(os.path.join(folder, f), os.path.join(new_dir, f))
print("Files organized by extension.")
