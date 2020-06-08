import json


def json_walk(tree):
    for k, v in tree.items():
        _type = type(v)
        if _type is list: tree[k] = []
        elif _type is str: tree[k] = ""
        elif _type is dict: json_walk(tree[k])
        else: tree[k] = 0


def build_command(json_file):
    x = json.loads(json_file)
    json_walk(x)
    return json.dumps(x)


json_file = "{\"version\": \"0.1.0\",\"command\": \"c:python\",\"args\": [\"app.py\"],\"problemMatcher\": {\"fileLocation\": [\"relative\", \"${workspaceRoot}\"],\"pattern\": {\"regexp\": \"^(.*)+s$\", \"message\": 1}}}"
print(build_command(json_file))
