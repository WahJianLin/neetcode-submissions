class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        rem = len(students)
        count = 0
        while count < rem:
            target = students.pop(0)
            
            if target == sandwiches[0]:
                sandwiches.pop(0)
                count = 0 
                rem -=1
            else:
                students.append(target)
                count+=1
            

        return rem
