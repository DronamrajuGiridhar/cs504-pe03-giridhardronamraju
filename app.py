"""
PE03 Giridhar Dronamraju

The Modifications I have Made to the app.py based on the HOS Assignment

- I have modified the application to work with the to-do list application rather than an application working with students details.
- I have changed the name of the database to 'tasks' since I will be storing the data regarding the tasks.
- I have also the name of all the API endpoints in the code and instead used '/tasks' in place of them.
- I have changed the 'age' attribute of the student and now used 'status' attribute for each task.
- I have re-written the POST and PUT methods to create and update tasks respectively based on the name of the task and its status.
- I have also updated the GET method to retrieve information on tasks and the message to be returned by this method instead of retreiving the student details as in HOS.
- I have re-written the DELETE endpoint in such a way that it will delete tasks using the '/tasks/<Task_name>'.
- I have also modified the names of the functions, variables, and messages being returned accordingly that it matches the PE. """

from flask import Flask
from flask import request
import json

tasks = {}
app = Flask(__name__)

@app.route("/")
def index():
    return "To Do List"

#POST

@app.route('/tasks', methods=['POST'])
def post_tasks_details():
    try:
        data = request.json
        dict_json = json.loads(json.dumps(data))

        tasks[dict_json["name"]] = dict_json["status"]

        return "Success", 200

    except Exception as e:
        print("Error during saving object", e)
        return "Failed", 400

#PUT

@app.route('/tasks', methods=['PUT'])
def put_tasks_details():
    try:
        data = request.json
        dict_json = json.loads(json.dumps(data))

        tasks[dict_json["name"]] = dict_json["status"]

        return "Success", 200

    except Exception as e:
        print("Error during saving object", e)
        return "Failed", 400

#GET

@app.route('/tasks/<Task_name>', methods=['GET'])
def get_task_details(Task_name):
    try:
        name = tasks[Task_name]

        if name is None:
            return "Task Not Found", 404
        else:
            return "Task Found " + Task_name + " Status : " + str(name), 200

    except KeyError:
        return "Task Not Found", 404

#DELETE

@app.route('/tasks/<Task_name>', methods=['DELETE'])
def delete_task_details(Task_name):
    try:
        tasks.pop(Task_name)

        return "Task deleted successfully", 200

    except KeyError:
        return "Task Not Found", 404

    except Exception as e:
        print("Error while removing task", e)
        return "Error while removing task", 400

#Run flask operation
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)