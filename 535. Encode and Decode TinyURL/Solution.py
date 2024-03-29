class Codec:
    def __init__(self):
        self.hash = {}
        self.counter = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.hash[self.counter] = longUrl
        self.counter+=1
        return self.counter-1

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        self.counter-=1
        return self.hash[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
