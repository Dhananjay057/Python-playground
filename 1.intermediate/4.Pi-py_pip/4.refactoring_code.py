"""
Refactoring code - chnaging your code so it doesnt chnage its behaviour
(the things it does)

Do it so easier to maintain

"""

import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/todos")

def count_completed_task_frequency(data):
    completedTaskFrequencyByUser = {}
    for i in data:
        if i["completed"] is True:
            try:
                completedTaskFrequencyByUser[i['userId']] +=1
            except KeyError:
                completedTaskFrequencyByUser[i['userId']]= 1
    return completedTaskFrequencyByUser

def get_user_with_top_completed_tasks(completedTaskFrequencyByUser):
    userIdWithMaximumCompletedTasks = []
    for userId, numberOfCompletedTasks in completedTaskFrequencyByUser.items():
        maxAmountOfCompletedTasks = max(completedTaskFrequencyByUser.values())
        if numberOfCompletedTasks == maxAmountOfCompletedTasks:
            userIdWithMaximumCompletedTasks.append(userId)
    return userIdWithMaximumCompletedTasks

def get_keys_with_top_values(dict):
    return [key for key, values in dict.items() if values == max(dict.values())]


try:
    data = json.loads(response.text)

except json.decoder.JSONDecodeError:
    print("The content is not json")
    
else:
    completedTasksFrequencybyUsers = count_completed_task_frequency(data)
    userIdWithMaximumCompletedTasks = get_user_with_top_completed_tasks(completedTasksFrequencybyUsers)
    print("cookies for:", userIdWithMaximumCompletedTasks)

    print(get_keys_with_top_values(completedTasksFrequencybyUsers))