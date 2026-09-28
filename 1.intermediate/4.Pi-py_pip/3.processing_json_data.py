"""
Our JSON data looks like that:
idTask
idUser
taskContent
completed


idTask when
completed == "true"

and save each occurrence/appearance/manifestation in format:

{
    1 : 11
    2 : 8
    3 : 5

    #and so on
}

"""

import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/todos")

try:
    data = json.loads(response.text)

except json.decoder.JSONDecodeError:
    print("The content is not json")
    
else:
    completedTaskFrequencyByUser = {}
    # print(type(completedTaskFrequencyByUser))
    for i in data:
        if i["completed"] is True:
            try:
                completedTaskFrequencyByUser[i['userId']] +=1
            except KeyError:
                completedTaskFrequencyByUser[i['userId']]= 1
    print(completedTaskFrequencyByUser)

    userIdWithMaximumCompletedTasks = []
    for userId, numberOfCompletedTasks in completedTaskFrequencyByUser.items():
        maxAmountOfCompletedTasks = max(completedTaskFrequencyByUser.values())
        if numberOfCompletedTasks == maxAmountOfCompletedTasks:
            userIdWithMaximumCompletedTasks.append(userId)
    print(userIdWithMaximumCompletedTasks)

        

