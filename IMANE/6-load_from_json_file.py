import json:
    def load_from_json_file(filename):
        with open(filename, "r") as f:
            data = f.read()
            return json.load(data)
