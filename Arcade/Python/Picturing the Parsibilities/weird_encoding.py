import base64

def weirdEncoding(encoding, message):
    return base64.b64decode(message, encoding).decode()


encoding = "-_"
message = "Q29kZVNpZ25hbA=="
print(weirdEncoding(encoding, message))