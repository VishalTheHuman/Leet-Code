class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        ate = 0
        l = len(students)
        s_ind = 0
        while sandwiches:
            remain = []
            i = 0
            count = 0
            while i < len(students) and s_ind < len(sandwiches):
                if students[i] == sandwiches[s_ind]:
                    count += 1
                    s_ind += 1
                else:
                    remain.append(students[i])
                i += 1
            if count == 0:
                break
            students = remain
            ate += count
        return l - ate
