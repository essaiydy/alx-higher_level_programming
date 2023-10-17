import json:

def save_to_json_file(my_obj, filename):
    jsonfile = json.dumps(my_obj)
    with open(filename, "w", encoding = "utf-8") as f:
        return f.write(jsonfile)
