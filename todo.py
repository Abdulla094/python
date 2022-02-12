todo=[]

def doSomething(tasks):
    todo.append(tasks)
    print("Added tasks "+tasks)

def printTodo(todo):
    print("todo list: ")
    i=1
    for task in todo:
        print(i,task)
        i+=1
        
doSomething("buy milk")
printTodo(todo)