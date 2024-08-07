class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        points = 0
        enemyEnergies.sort()
        while enemyEnergies:
            if currentEnergy >= enemyEnergies[0]:
                to_add = currentEnergy // enemyEnergies[0]
                points += to_add
                currentEnergy -= to_add*enemyEnergies[0]
            elif points >=1:
                currentEnergy += enemyEnergies.pop()
            else:
                break
        return points
        
