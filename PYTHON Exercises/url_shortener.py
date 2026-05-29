import hashlib

class URLShortener:
    def __init__(self):
        self.db = {}

    def shorten(self, url):
        short = hashlib.md5(url.encode()).hexdigest()[:6]
        self.db[short] = url
        return short

    def retrieve(self, short):
        return self.db.get(short, "Not found")


u = URLShortener()
code = u.shorten("https://google.com")
print("Short URL:", code)
print("Original:", u.retrieve(code))