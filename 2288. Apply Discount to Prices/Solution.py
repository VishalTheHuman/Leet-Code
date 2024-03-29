class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        sentence = sentence.split()
        discount = (100-discount)*0.01
        for i in range(len(sentence)):
            if sentence[i][0] == "$":
                try:
                    s = sentence[i][1:]  
                    if "e" in s:
                        continue
                    val = float(s)*discount
                    sentence[i] = f"${val:.2f}"
                except:
                    continue
        return " ".join(sentence)
