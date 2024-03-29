class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed)==1 and flowerbed[0]==0:
            return True
        i = 0
        while i < len(flowerbed) and n:
            if flowerbed[i] == 0:
                if i-1 >=0 and i+1 <len(flowerbed):
                    if flowerbed[i-1] == flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        n-=1
                elif (i-1) < 0:
                    if flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        n-=1
                elif (i+1)==len(flowerbed):
                    if flowerbed[i-1] == 0:
                        flowerbed[i] = 1
                        n-=1 
            i+=1
        return n==0
