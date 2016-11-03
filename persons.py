persons ={}
class Person(object):
    def __ini__(self,name):
        self.name = name

    def __hash__(self):
        return hash(self.name)

persons[Person("kenan")]
print(Person("kenan") in persons)
