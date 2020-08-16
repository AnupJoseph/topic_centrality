import os
import zipfile
from pydrive.drive import GoogleDrive 
from pydrive.auth import GoogleAuth 

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


def up_load():
    gauth = GoogleAuth() 
    gauth.LocalWebserverAuth()        
    drive = GoogleDrive(gauth)
    path = r"/Zipped_file.zip"      
    f = drive.CreateFile({'title': 'Political_data.zip'}) 
    f.SetContentFile(os.path.join(path, 'Political_data.zip')) 
    f.Upload() 

zipf = zipfile.ZipFile('Zipped_file.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir('/data', zipf)
zipf.close()