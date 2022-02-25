#An exercise in using doctests and building functions with built
#in python types.
#Some tests have been modified to break!
# We can use if statements and loops to fix them.
def print_todo(todo):
    """
    print_todo takes in a todo dictionary and prints it out
    with by separating the 'name' from the 'body' using a colon(:).

    >>> todo = {'name': 'Example 1', 'body': 'Test task', 'points': '3' }
    >>> print_todo(todo)
    Example 1: Test task
    >>>
    """
    #All we need to do here is call print with string interpolation
    #Make sure to reference the keys in the todo dict
    print(f"{todo['name']}: {todo['body']}")

def take_first(todos):
    """
    take_first recieves a list of todos and removes the take_first
    then returns that todo and the remaining ones in a tuple

    >>> todos = [{'name': 'Example 1', 'body': 'Test task', 'points': '3'},
    ... {'name': 'Task 2', 'body': 'Another test task', 'points': '2'}]
    >>> todo, todos = take_first(todos)
    >>> todo
    {'name': 'Example 1', 'body': 'Test task', 'points': '3'}
    >>> todos
    [{'name': 'Task 2', 'body': 'Another test task', 'points': '2'}]
    >>> todos = []
    >>> take_first(todos)
    (None, [])
    """
    # Pop the first dict off the list, return it and the remaining list
    # UNLESS todos is an empty list, then return None
    if todos: #if todos is truthy, do what you normally do
        todo = todos.pop(0)
        return (todo, todos)
    else:
        return(None, []) #otherwise, return none

def sum_points(todos):
    """
    sum_points takes two todo dicts and returns the sum of their point values
    >>> todos = [{'name': 'Example 1', 'body': 'Test task', 'points': '3'},
    ... {'name': 'Task 2', 'body': 'Another example task', 'points': '2'},
    ... {'name': 'Task 3', 'body': 'Third task', 'points': '5'}]
    >>> sum_points(todos)
    10
    """
    #The function signature was changed in the test to only take 1 argument
    #Thus we need to change how we find values in the list
    total_points = 0
    for todo in todos:
        total_points += int(todo['points'])
    return total_points
