from config import ZIP_FILE
import zipfile

with zipfile.ZipFile(ZIP_FILE, 'r') as zip_file:
    for entry in zip_file.namelist():
        print(entry)
        if entry.endswith('/'):
            print(f'Directory found: {entry}')
        else:
            print(f'File found: {entry}')

    
