from more_itertools import last


results = ['BMW', 'Mercedes', 'Opel', 'Mazda']
print(len(results))

#ilk eleman
first_element= results[0]

#son eleman
last_element=results[-1]

print("ilk eleman:",first_element)
print("son eleman:",last_element)

results[-1]= 'Toyota'
print(results)