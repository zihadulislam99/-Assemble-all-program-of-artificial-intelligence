import os
from Body.Speak import Say

def FilesAndFolders(command):
    FilesAndFolders = [["movie folder", "F:\ALL\MOVIE"]
        ]
    for FileAndFolder in FilesAndFolders:
        if f"open {FileAndFolder[0]}" in command:
            Say(f"Opening {FileAndFolder[0]}")
            os.startfile(FileAndFolder[1])
