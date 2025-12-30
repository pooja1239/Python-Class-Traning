emp={
    'eid':101,
    'name':'RG',
    'esal':45000,
    'loc':'bangalore',
    'gender':'Male',
    'avail':True
}
print(emp.keys())

for key in emp.keys():
    print(key, ":", emp.get(key))