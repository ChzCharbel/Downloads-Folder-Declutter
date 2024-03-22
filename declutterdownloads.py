import os
from pathlib import Path

# file types

folderNames = {
    "Audio": {'mp3','mpa','ogg','wav','wma'},
    "Compressed":{'7z', 'rar', 'zip'},
    'Documents':{'ppt','pptx','pdf','xls', 'xlsx','doc','docx','txt', 'tex', 'epub', 'csv'},
    'Images':{'bmp','jpeg','jpg','png','jfif','svg'},
    'Softwares':{'apk','bat','bin', 'exe','jar','msi','py'},
    'Videos':{'h264','mov','mp4','mpg','mpeg','wmv'},
    'Others': {'NONE'}
}

# get the list of files/folders

dpath = r"C:\Users\charb\Downloads"

ofiles = [os.path.join(dpath, file) 
        for file in os.listdir(dpath) 
            if os.path.isfile(os.path.join(dpath, file))]

ofolders = [os.path.join(dpath, file) 
        for file in os.listdir(dpath) 
            if not os.path.isfile(os.path.join(dpath, file))]

extensions_map = {extension: fileType 
        for fileType, extensions in folderNames.items() 
                for extension in extensions }

# create folders

folder_paths = [os.path.join(dpath, folder_name) 
        for folder_name in folderNames.keys()]

[os.mkdir(folderPath) 
        for folderPath in folder_paths if not os.path.exists(folderPath)]

# move files
def newPath(oldPath):
    extension = str(oldPath).split('.')[-1]
    amplified_folder = extensions_map[extension] if extension in extensions_map.keys() else 'Others'
    final_path = os.path.join(dpath,amplified_folder, str(oldPath).split('\\')[-1])
    return final_path
    

[Path(eachfile).rename(newPath(eachfile)) for eachfile in ofiles]

# move other folders
[Path(onlyfolder).rename(os.path.join(dpath,'Others', str(onlyfolder).split('\\')[-1])) 
        for onlyfolder in ofolders 
                if str(onlyfolder).split('\\')[-1] not in folderNames.keys()]