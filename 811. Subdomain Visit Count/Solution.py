class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dt = defaultdict(int)
        for domain in cpdomains:
            count, domain = domain.split(" ")
            count = int(count)
            while True:
                dt[domain] += count
                try:
                    ind = domain.index(".")
                    domain = domain[ind+1:]
                except:
                    break
        ls = []
        for k,v in dt.items():
            s = str(v) + " " + k
            ls.append(s)
        return ls
