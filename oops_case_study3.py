class Student:

    def __init__(self, roll, name, m_in_e, m_in_m, m_in_s):
        self.roll_no = roll
        self.name = name
        self.marks_english = m_in_e
        self.marks_math = m_in_m
        self.marks_science = m_in_s
        print("I am constructor!")

    def display(jb):
        print("Name of the student: ", jb.name)
        print("Roll no: ", jb.roll_no)
        print("Marks in English: ", jb.marks_english)
        print("Marks in Maths: ", jb.marks_math)
        print("Marks in Science: ", jb.marks_science)
        print()
        print("Overall Percentage is :", (jb.marks_english + jb.marks_math + jb.marks_science) * 100 / 300)


s = Student(1010, 'jb', 75, 80, 78)
s.display()

t = Student(100, 'rp', 75, 80, 78)
t.display()

u = Student(110, 'ac', 75, 80, 78)
u.display()

v = Student(101, 'ak', 75, 80, 78)
v.display()

w = Student(10, 'ks', 75, 80, 78)
w.display()

x = Student(111, 'Ginau', 75, 80, 78)
x.display()