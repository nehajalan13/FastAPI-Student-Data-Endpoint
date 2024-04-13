import json

#root function to display student details by GET request
async def root(student_id: int):
    print(student_id)
    with open("Data.json","r") as file:
        json_data = json.load(file)
        for row in json_data:
            if row["student_id"] == student_id:
                return row

    return "Data not found"

#function to add student details in Data.json file by POST request
async def add_student(student_data):
    with open("Data.json","r+") as file:
        data = json.load(file)
        data.append(student_data)
        file.seek(0)
        json.dump(data,file,indent=4)
