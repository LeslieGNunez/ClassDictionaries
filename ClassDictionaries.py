Python 3.13.2 (v3.13.2:4f8bb3947cf, Feb  4 2025, 11:51:10) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Class Dictionaries
>>> #Classroom Number Directory
>>> room_numbers = {
...     "MKT505": "5151",
...     "CSC502": "4024",
...     "STATS404": "3011",
...     "ECON321": "3289",
...     "MKT508": "5022",
...     "CSC505": "4020"
...     }
>>> #Class Instructors
>>> instructors = {
...     "MKT505": "Veliz",
...     "CSC502": "4024",
...     "STATS404": "3011",
...     "ECON321": "3289",
...     "MKT508": "5022",
...     "CSC505": "4020"
...     }
>>> #Class Meeting Times
>>> meeting_times = {
...     "MKT505": "9:00 am",
...     "CSC502": "10:00 am",
...     "STATS404": "8:00 am",
...     "ECON321": "9:00 am",
...     "MKT508": "10:00 am",
...     "CSC505": "8:00 am"
...     }
>>> #Get User Input
>>> course = input("Enter your course number (e.g.,ECON321): ").upper()
Enter your course number (e.g.,ECON321): 
>>> #Display Course Info
...     
>>> if course in room_numbers:
...     print(f"Course: {course}")
...     print(f"Room Number: {room_numbers[course]}")
...     print(f"Instructor: {instructors[course]}")
...     print(f"Meeting Time: {meeting_times[course]}")
... else:
