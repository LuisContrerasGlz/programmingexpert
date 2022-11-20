"""

  Write a function that accepts a list of lists that contain the name, age and
  salary of specific employees and also accepts a string representing the key to
  sort employees by. Your function should return a new list that contains the
  lists representing each employee sorted in ascending order by the given key.



"""

def sort_employees(employees, sort_by):

    # Know what index we will be sorting by
    sort_indices = ["name", "age", "salary"]
    sort_index = sort_indices.index(sort_by)

    # Using sorted to create/return a new list sorted, then using a lambda function we get x by sort_index
    sorted_employees = sorted(employees, key=lambda x: x[sort_index])

    return sorted_employees