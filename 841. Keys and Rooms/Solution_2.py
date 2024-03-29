class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque([0])
        visited = set([0])
        while q:
            for i in range(len(q)):
                ind = q.popleft()
                for x in rooms[ind]:
                    if x not in visited:
                        q.append(x)
                        visited.add(x)
        return len(visited) == len(rooms)
