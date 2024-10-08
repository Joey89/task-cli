import sys, json

taskList = {
    "id"            : 0,
    "description"   : "",
    "status"        : "todo / inprogress / done",
    "createdAt"     : "date and time",
    "updatedAt"     : "date and time last updated"
}


#need to have json file and looped over to see what next id will be.

def todoList(args):
    commandArg = args[1]

    if commandArg == 'add':
        task = args[1]
        print('add')

    elif commandArg == 'update':
        if len(args) > 3:
            taskID = args[2]
            task =  args[3]
            # task-cli update 1 "Buy groceries and cook dinner"
            print('update')
        else:
            print('Requires 3 Arguments, ex: task-cli.py update 1 "todo"')
            
    elif commandArg == 'delete':
        if len(args) > 2:
            taskID = args[2] 
            print('delete')
        else:
            print('Requires 2 Arguments, ex: task-cli.py delete 1')

    elif commandArg == 'list':
        if len(args) > 2:
            listCommand = args[2]
            print('Display list where listCommand is true')
        else:
            print('Display list')


# Convert the dictionary to a JSON string
##json_string = json.dumps(taskList)

#print(json_string)

if len( sys.argv ) > 1 :
    todoList(sys.argv)