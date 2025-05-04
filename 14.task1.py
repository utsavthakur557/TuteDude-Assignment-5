marks = {'alice': 65,'bob': 43,'mike': 97,'kunal': 87,'utsav':68}

name = input("Enter the student's name: " )
if name in marks:
    print(f'{name} marks is {marks[name]}')
else:
    print(f'{name} not found in the student records')

