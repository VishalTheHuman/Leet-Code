class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for ast in asteroids:
            if stk:
                if ast<0 and stk[-1]>0:
                    if (ast+stk[-1]) == 0:
                        stk.pop()
                    elif (ast+stk[-1]) < 0:
                        val = 1
                        while stk and (stk[-1] +ast) <=0 and stk[-1]>0 and val:
                            val = stk[-1] +ast
                            stk.pop()
                        if (not stk or stk[-1]<0) and val:
                            stk.append(ast)
                else:
                    stk.append(ast)
            else:
                stk.append(ast)
        return stk
