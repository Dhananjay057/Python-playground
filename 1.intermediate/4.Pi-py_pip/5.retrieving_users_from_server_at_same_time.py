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

def get_usernames_from_use_ids(list):
# sol1:
    # user_data = requests.get("https://jsonplaceholder.typicode.com/users")
    # users = json.loads(user_data.text)
    # # userNames = []
    # # for userId in list:
    # #     for j in range(len(users)):
    # #         if userId == users[j]["id"]:
    # #             userNames.append(users[j]["name"])
    # # return userNames
    # # return [users[j]["name"] for userId in list for j in range(len(users)) if userId == users[j]["id"]]
    # return [user["name"] for user in users if user["id"] in list]
  
# -- Sol2
    return [(json.loads((requests.get(f"https://jsonplaceholder.typicode.com/users/{i}")).text))["name"] for i in list]


try:
    data = json.loads(response.text)

except json.decoder.JSONDecodeError:
    print("The content is not json")
    
else:
    completedTasksFrequencybyUsers = count_completed_task_frequency(data)
    # userIdWithMaximumCompletedTasks = get_user_with_top_completed_tasks(completedTasksFrequencybyUsers)
    # print("cookies for:", userIdWithMaximumCompletedTasks)

    id_list = get_keys_with_top_values(completedTasksFrequencybyUsers)

    print(get_usernames_from_use_ids(id_list))