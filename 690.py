"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees, id):

        importance = {e.id: e.importance for e in employees}        
        subordinates = {e.id: e.subordinates for e in employees} 

        def get_subordinates(id):           
            all_staff = []                      
            queue = [id]                           
            while queue:                     
                staff = queue.pop(0)           
                all_staff.append(staff)         
                queue.extend(subordinates[staff]) 
            return all_staff                    

        return sum([importance[staff] for staff in get_subordinates(id)])