from sampleinsert import SamInsert
from datetime import datetime
Obj = SamInsert()
#print(Obj.getBook())
now = datetime.now()
te = now.strftime('%Y-%m-%d %H:%M:%S')
print(te)
Obj.insertUser("Suneeth1","21guns")
Obj.insertBook("HarryPotter","JK Rowling",te)
Obj.insertBook("Lord of the Rings","LJ Tolkien",te)
print(Obj.getPeople())