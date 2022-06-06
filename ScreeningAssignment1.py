#1. Create a function in python to read the text file and replace specific content
#of the file.

import os
def updateTextFile(fileName,originalString,replaceString):
    """
    This function modified the original string in the
     given file with the other string passed
    :param fileName: Name of the file which is to be modified
    :param originalString: The string which exists in the file provided and to be modified
    :param replaceString: The string which replaces the existing string in the file
    :return: None
    """
    try:
        _,ext=os.path.splitext(fileName)
        if ext==".txt":
            with open(fileName,mode="a+") as file:
                file.seek(0)
                content=file.read()
                content=content.replace(originalString,replaceString)
                file.seek(0)
                file.truncate()
                file.write(content)
        else:
            raise Exception("Not as Text File")
    except Exception as e:
        print(f"Unable to update the file:{fileName}",e)


if __name__=="__main__":
    updateTextFile("F:\WorkSpace\Bicycles.txt","Bike","Bicycle")
