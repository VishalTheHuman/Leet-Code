class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        def add(folders, node):
            if not folders:
                node["*"] = None
                return 
            
            if folders[0] not in node:
                node[folders[0]] = {}

            add(folders, node[folders.pop(0)])

        def getFolder(node, prev = ""):
            if not node:
                return [prev]
            result = []
            if "*" in node:
                return [prev]
            for n in node:
                result += getFolder(node[n], prev + f"/{n}")
            return result

        struct = {}
        for fold in folder:
            fold = fold.split("/")[1:]
            add(fold,struct)
        return getFolder(struct)
