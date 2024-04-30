import numpy as np

def read(file: str):
    with open(file, "r") as f:
        data = f.read()

    return data

def mscrToPy(fileName: str):
    file = read(fileName)

    mprint = file.replace("println(", "print(")
    mprint2 = mprint.replace('")', '\\n")')

    python = mprint2.replace("func", "def").replace("&", "and").replace("|", "or").replace("switch", "match").replace("enum", "enumerate")

    with open(f"{file}.py", "w") as i:
        i.write(str(python))

    return file