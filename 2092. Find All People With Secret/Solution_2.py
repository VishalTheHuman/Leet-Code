class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        known = set([0, firstPerson])
        dt = defaultdict(list)

        for meeting in meetings:
            dt[meeting[2]].append((meeting[0], meeting[1]))
        
        for x in sorted(dt.keys()):
            while True and dt[x]:
                flag = 0
                i = 0
                while i < len(dt[x]):
                    if dt[x][i][0] in known or dt[x][i][1] in known:
                        known.add(dt[x][i][0])
                        known.add(dt[x][i][1])
                        dt[x].pop(i)
                        flag += 1
                    else:
                        i+=1
                if not flag:
                    break
        return list(known)
