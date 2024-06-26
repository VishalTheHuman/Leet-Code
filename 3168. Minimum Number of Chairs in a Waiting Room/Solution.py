class Solution:
    def minimumChairs(self, s: str) -> int:
        people = max_people = 0
        for x in s:
            if x == "E":
                people += 1
            else:
                people -= 1
            if people > max_people:
                max_people = people
        return max_people
