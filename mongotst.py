from models import Testing
import mongoservice

mongoservice.delete_one(1)
employee=Testing(1,'vijay',11.0,'2010-03-20')
mongoservice.insert_one(employee)
t=mongoservice.find_one(1)
print(t)