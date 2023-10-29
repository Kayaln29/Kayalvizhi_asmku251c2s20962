class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  #sort the list of students in descending order of CGPA
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  # Syntax - lambda arg:exp
  return sorted_students


# Example usage:
students = [
     Student("Hari", "A123", 7.8),
     Student("Srikanth", "A124", "8.9"),
     Student("Sowmya", "A125", "9.1"),
     Student("Madhumitha", "A126", "9.9"),
]
