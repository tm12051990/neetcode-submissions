class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        hungry = 0

        while students:

            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                hungry = 0
            else:
                students.append(students.pop(0))
                hungry += 1
            
            if hungry == len(students):
                break

        return len(students)

        