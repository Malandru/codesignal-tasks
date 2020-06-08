from html.parser import HTMLParser


class Parser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.depth = 0
        self.tree = dict()

    def handle_starttag(self, tag, attrs):
        print(self.depth, tag)
        if self.depth not in self.tree.keys():
            self.tree[self.depth] = set()
        self.tree[self.depth].add(tag)
        self.depth += 1

    def handle_endtag(self, tag):
        self.depth -= 1


def pageComplexity(document):
    parser = Parser()
    parser.feed(document)
    max_depth = max(parser.tree.keys())
    return list(sorted(parser.tree[max_depth]))


document = "<!DOCTYPE html> <html lang=\"en\" dir=\"ltr\"> <head> <meta name=\"description\" content=\"application/xhtml+xml\"/> <meta charset=\"UTF-8\"/> <title>Get an object</title> </head> <body> <section>This is a section</section> </body> </html>"
print(pageComplexity(document))