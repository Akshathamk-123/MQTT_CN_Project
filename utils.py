import sys

def handleForceExit(ClassName):
    object = ClassName()
    try:
        object.execute()
    except KeyboardInterrupt:
        object.closeConnection()
        sys.exit(1)

def parseInt(stringToParse):
    try:
        if not stringToParse: return None
        return int(stringToParse)
    except:
        print('Cannot convert string to integer')
        return None