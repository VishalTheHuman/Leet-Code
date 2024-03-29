class Solution:
    def bestClosingTime(self, customers: str) -> int:
        no_count = 0
        yes_count = customers.count("Y")
        penalties =[yes_count+no_count]
        for i in range(len(customers)):
            if customers[i] == "N":
                no_count += 1
            else:
                yes_count -= 1
            val = yes_count + no_count
            penalties.append(val)
        min_val = min(penalties)
        return penalties.index(min_val)
