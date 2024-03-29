class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        tokens.sort()
        i , j = 0, len(tokens) - 1
        max_score = 0
        while i <= j:
            if power >= tokens[i]:
                power -= tokens[i]
                score += 1
                i += 1
            elif score:
                power += tokens[j]
                j -= 1
                score -= 1
            else:
                break
            if score > max_score:
                max_score = score
        return max_score
