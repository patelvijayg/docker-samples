#_id INT(6) PRIMARY KEY,name VARCHAR(100) NOT NULL,salary DECIMAL(10,2),birthdate DATE
import json

class testing:
  def __init__(self,_id,name,salary,birthdate):
   self._id=_id
   self.name=name
   self.salary=salary
   self.birthdate=birthdate

  @classmethod
  def from_json(cls, json_str):
    #Since Dictionary contains single quote which creates problem hence
    #we need to transform real JSON.
    json_data=json.dumps(json_str)
    json_dict = json.loads(json_data)
    return cls(**json_dict)

  def getTuple(self):
    return (self._id,self.name,self.salary,self.birthdate)
  def getJson(self):
    return {"_id":self._id,"name":self.name,"salary":self.salary,"birthdate":self.birthdate}
  def __str__(self):
    return '({0},"{1}",{2},"{3}")'.format(self._id,self.name,self.salary,self.birthdate)
  def __repr__(self):
    return '({0},"{1}",{2},"{3}")'.format(self._id,self.name,self.salary,self.birthdate)