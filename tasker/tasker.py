#An exercise in using doctests and building functions with built
#in python types
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
    """
    # Pop the first dict off the list, return it and the remaining list
    todo = todos.pop(0)
    todos = todos
    return (todo, todos)

def sum_points(todo1, todo2):
    """
    sum_points takes two todo dicts and returns the sum of their point values
    >>> todos = [{'name': 'Example 1', 'body': 'Test task', 'points': '3'},
    ... {'name': 'Task 2', 'body': 'Another example task', 'points': '2'}]
    >>> sum_points(todos[0], todos[1])
    5
    """
    #Since both dicts are passed in directly, we can reference their
    #points values, cast to ints, and sum them

    return int(todo1['points']) + int(todo2['points'])
