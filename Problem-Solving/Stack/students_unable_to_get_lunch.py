class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        while students and sandwiches and sandwiches[0] in students :
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                n-=1
            else:
                students.append(students.pop(0))
        return n