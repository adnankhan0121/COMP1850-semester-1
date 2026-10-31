from datetime import date
from person import Person

p = Person("Alan John Smith", date(2000, 10, 31))
print(p.initials())
print(p.is_birthday())