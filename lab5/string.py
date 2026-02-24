student = {}
#to insert an element
student['name'] = 'Aviral'
student['roll'] = 43
student['age'] = 23

print(student)

student["english"] = 89
student["roll"] = 1024

print(student)

for key in student:
    print("key",key,"value",student[key])
    
    
'''#output
{'name': 'Aviral', 'roll': 43, 'age': 23}
{'name': 'Aviral', 'roll': 1024, 'age': 23, 'english': 89}
key name value Aviral
key roll value 1024
key age value 23
key english value 89
'''





sentence="Hello world"
print(sentence.isalnum())

str3='hello 123'
print(str3.isalnum())

str4="123"
print(str4.isalnum())


'''#output
False
False
True'''




#to count number of alphabets in a sentence
sentence=input("Enter a sentence: ")
#to count number of  alphabets in the sentence
count=0
for x in sentence:
    if x.isalpha():
        count += 1
#output the number of alphabets in the sentence
print("Number of alphabets:", count)

'''#output
Enter a sentence: Hello world 123
Number of alphabets: 10
'''