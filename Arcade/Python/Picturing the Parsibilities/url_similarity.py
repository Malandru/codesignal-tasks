from urllib.parse import urlparse


def urlSimilarity(url1, url2):
    url1 = urlparse(url1)
    url2 = urlparse(url2)
    path1, query1 = rebase(url1)
    path2, query2 = rebase(url2)

    similarity = is_equal(url1.scheme, url2.scheme) * 5
    similarity += is_equal(url1.netloc, url2.netloc) * 10
    for p1, p2 in zip(path1, path2):
        if not is_equal(p1, p2): break
        similarity += 1
    same_vars = query1.keys() & query2.keys()
    similarity += len(same_vars)
    for var in same_vars:
        if is_equal(query1[var], query2[var]):
            similarity += 1
    return similarity


def rebase(parse_result):
    path = parse_result.path.split("/")
    path = path[1:] if len(path) > 1 else []
    query = dict()
    if len(parse_result.query) > 0:
        query = dict([q.split("=") for q in parse_result.query.split("&")])
    return path, query


def is_equal(a, b):
    return a == b and len(a) > 0


url1 = "https://codesignal.com/home/test?param1=42&param3=testing&login=admin"
url2 = "https://codesignal.com/home/secret/test?param3=fish&param1=42&password=admin"
# url1 = "https://www.google.com/search?q=codesignal"
# url2 = "http://www.google.com/search?q=codesignal"
# url1 = ""
# url2 = ""
print(urlSimilarity(url1, url2))

#  1. Initially their similarity is 0
#  2. Then, it is increased by the following rules:
#  --> +5, if the same protocol is used in both URLs.
#  --> +10, if url1 and url2 have the same address.
#  --> +k, if the first k components of path (delimited by /)
#      are exactly the same (and in the same order) between the two URLs.
#  --> +1 if for each varNames common between them. Additional +1 if the respective values are equal too.
