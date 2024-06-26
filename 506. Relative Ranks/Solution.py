class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_sorted = sorted(score, reverse = True)
        meds = [
            "Gold Medal", 
            "Silver Medal",
            "Bronze Medal"
        ]
        medals = {}
        for ind, x in enumerate(score_sorted[:3]):
            medals[score_sorted[ind]] = meds[ind]
        for i in range(3,len(score)):
            medals[score_sorted[i]] = str(i+1)
        for i in range(len(score)):
            score[i] = medals[score[i]]
        return score
