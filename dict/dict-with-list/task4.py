def get_older_than(users,age):
    older_users=[]
    for user in users:
        if user["age"]>age:
            older_users.append(user["name"])
            
    return older_users
    
users=[
    {"name" : "Aitaj" , "age": 20 },
    {"name" : "Tural" , "age" : 22 },
    {"name": "Nigar" , "age" : 25 }
]
    
result=get_older_than(users,24)
print(result)
