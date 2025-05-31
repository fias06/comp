from classss import Person

class Group:
    def __init__(self, name, members = []):
        self.name = name
        self.members = members
        
    def add_member(self, person):
        self.members.append(person)
        
    def list_members(self):
        print("Members of the "+ str(self.name))
        
        for i in self.members:
            print(i.name)
            
    def average_age(self):
        avg = 0
        if self.members == []:
            return None
        else:
            for i in self.members:
                avg += i.age
        
        return(avg/len(self.members))    
        
group  = Group("Study group")
person1 = Person("Shraddha",19,"shraddha06@gmail.com")
person2 = Person("Saif",18,"saifmshaikh06@gmail.com")

group.add_member(person1)
group.add_member(person2)

group.list_members()

print(group.average_age())