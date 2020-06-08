def checkPassword(attempts, password):
    def check():
        while True:
            received = yield  # This will be none, so the next() function is also necessary
            print(f"received: {received}")
            yield received == password  # This is the response

    checker = check()
    for i, attempt in enumerate(attempts):
        print("next: {}".format(next(checker)))  # It is totally necessary
        response = checker.send(attempt)
        print(f"response: {response}")
        if response:
            return i + 1

    return -1


attempts = ["hello", "world", "I", "like", "coding"]
password = "like"
print(checkPassword(attempts, password))