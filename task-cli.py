import sys, json

taskList = {
    "id"            : 0,
    "description"   : "",
    "status"        : "todo / inprogress / done",
    "createdAt"     : "date and time",
    "updatedAt"     : "date and time last updated"
}

if len( sys.argv ) > 1 :
    for arg in sys.argv:
        if arg == 'add':
            #create todo
        elif arg == 'update':
            pass
        elif arg == 'delete':
            pass
        elif arg == 'list':
            #seperate lists done, todo, in-progress
            pass
        
# Convert the dictionary to a JSON string
json_string = json.dumps(taskList)

print(json_string)