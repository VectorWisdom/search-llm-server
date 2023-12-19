import json

def load_json(fileName):
    return json.load(open(fileName))

def save_json(fileName,data):
    jfile = open(fileName, "w")
    jfile.write(json.dumps(data, indent=4))
    jfile.close()
    print(f"{len(data)} entries saved in {fileName}")
    return

