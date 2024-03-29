class Solution:
    def arrangeWords(self, text: str) -> str:
        dt = {}
        for text in text.lower().split(" "):
            dt[len(text)] = dt.get(len(text),[]) + [text]
        string = []
        for item in sorted(dt.keys()):
            string += dt[item]
        string[0] = string[0].capitalize()
        return " ".join(string)
