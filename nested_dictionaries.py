x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#A
x[1][0] = 15
print(x)

#B
students[0]['last_name'] = 'Bryant'
print(students)

#C
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

#D
z[0]['y'] = 30
print(z)



students = [
        {'first_name' :  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

#2
def iterate_dictionary(students):
    for i in range(len(students)):
        for key,value in students[i].items():
            if key == "last_name":
                print(f"{key} - {value}")
            else:
                print(f"{key} - {value},", end=" ")
iterate_dictionary(students)


#3
def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        for key,value in some_list[i].items():
            if key == key_name:
                print(value)

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)


#4
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dictionary):
    for key, value in dictionary.items():
        print(len(value), key.upper())
        for value in value:
            print(value)

printInfo(dojo)