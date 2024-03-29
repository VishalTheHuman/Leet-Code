class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content = defaultdict(list)
        for path in paths:
            path = path.split()
            for file in path[1:]:
                file = file.split("(")
                content[file[1][:-1]].append(f"{path[0]}/{file[0]}")
        result = []
        for x in content.values():
            if len(x) > 1:
                result.append(x)
        return result
