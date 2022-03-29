# Title: Employee Test Program
# Program created by William Schaeffer
# CPS 313
# P. 579, Exercise 4, Emp Test Program
# 03.15.22

# This program will test the employee class

# import for class

import emp

# Main Function

def main():
   
   employee_1 = emp.Employee('Susan Meyers', 47899, 'Accounting', 'Vice President')
   employee_2 = emp.Employee('Mark Jones', 39119, 'IT', 'Programmer')
   employee_3 = emp.Employee('Joy Rogers', 81774, 'Manufacturing', 'Engineer')

   employee_list = [employee_1, employee_2, employee_3]

   for employee in range(len(employee_list)):
       print(f'Employee {employee + 1}:')
       print(employee_list[employee])
       print()

if __name__ == '__main__':
    main()                                                      # call main function


