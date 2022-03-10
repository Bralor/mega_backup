from mega import Mega

mega_instance = Mega()
session = mega_instance.login()

# find a folder non-empty object (dictionary) or NoneType
session.find()

# .. if there is none, create one (in the root folder)
session.create_folder()

# .. if there is finally particular folder, upload the backup. 
file = session.upload("backup.file")

