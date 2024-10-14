
todos=[]
while True:
    user_action=input("Type add ,edit, show or exit : ")
    user_action=user_action.strip()
    if user_action=='add':
        todo=input("Enter a todo:")
        todos.append(todo.capitalize())
    elif user_action=='show'or user_action=='display':
        for item in todos:
            print(item.title())
    elif user_action=='exit':
        break
    elif user_action=='edit':
        number=int(input("Number of the todo to edit : "))
        new_todo=input("Enter edited todo : ")
        todos[number-1]=new_todo
        print("Editing completed")
    else:
        print("You enter the wrong command, type add,edit,show or exit")

