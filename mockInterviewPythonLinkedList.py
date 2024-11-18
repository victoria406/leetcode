# todolist = TodoList()

# todolist.topPriority('Water the dogs')
# todolist.lowPriority('Write in journal')
# todolist.after(0, 'Walk the dogs')
# todolist.print()
# 1. Water the dogs
# 2. Walk the dogs
# 3. Write in journal

#will need four methods in our Todo class


class ToDoList:
    def __init__(self):
        self.tasks = []

    def topPriority(self, task):
        self.tasks.insert(0, task)
    
    def lowPriority(self, task):
        self.tasks.append(task)
    
    def after(self, current_task, new_task):
        if current_task in self.tasks:
            #add debug
            index = self.tasks.index(current_task)
            self.tasks.insert(index + 1, new_task)
        else:
            #add debug
            self.tasks.append(new_task)
    
    def print(self):
        # i is the index, printing the item would print the value
        for (idx, item) in enumerate(self.tasks):
            idx = idx + 1
            print(idx, item)
    
todoList = ToDoList()

todoList.topPriority("Water the plants")
todoList.after(0, "Walk the dogs")

todoList.print()

#start with the framework before hand, talk a bit more 
