#_id INT(6) PRIMARY KEY,name VARCHAR(100) NOT NULL,salary DECIMAL(10,2),birthdate DATE
class testing:
  def __init__(self,_id,name,salary,birthdate):
   self._id=_id
   self.name=name
   self.salary=salary
   self.birthdate=birthdate
  def getTuple(self):
   return (self._id,self.name,self.salary,self.birthdate)
  def getJson(self):
   return {"_id":self._id,"name":self.name,"salary":self.salary,"birthdate":self.birthdate}
  def __str__(self):
   return '({0},"{1}",{2},"{3}")'.format(self._id,self.name,self.salary,self.birthdate)
  def __repr__(self):
   return '({0},"{1}",{2},"{3}")'.format(self._id,self.name,self.salary,self.birthdate)