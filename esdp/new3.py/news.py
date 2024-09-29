class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.voted = False

    def update_details(self, name):
        self.name = name

    def vote(self):
        if not self.voted:
            self.voted = True
            return True
        else:
            return False


class Admin:
    def __init__(self, admin_id, password):
        self.admin_id = admin_id
        self.password = password

    def login(self, admin_id, password):
        return admin_id == self.admin_id and password == self.password


class VotingSystem:
    def __init__(self):
        self.students = []
        self.admin = None
        self.president_nominee = None
        self.voting_details = {}

    def student_registration(self, student_id, name):
        student = Student(student_id, name)
        self.students.append(student)
        return student

    def student_login(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def admin_login(self, admin_id, password):
        if self.admin and self.admin.login(admin_id, password):
            return True
        return False

    def nominate_president(self, student_id):
        nominee = self.student_login(student_id)
        if nominee:
            self.president_nominee = nominee
            return True
        return False

    def update_nominee(self, student_id):
        if self.president_nominee:
            nominee = self.student_login(student_id)
            if nominee:
                self.president_nominee = nominee
                return True
        return False

    def remove_nominee(self):
        self.president_nominee = None

    def view_voting_details(self):
        return self.voting_details

    def vote_for_president(self, student_id):
        student = self.student_login(student_id)
        if student and student.vote():
            if student_id not in self.voting_details:
                self.voting_details[student_id] = "President"
            return True
        return False



voting_system = VotingSystem()


admin = Admin("admin123", "adminpassword")
voting_system.admin = admin


student1 = voting_system.student_registration("1001", "Alice")
student2 = voting_system.student_registration("1002", "Bob")


student1 = voting_system.student_login("1001")
student1.update_details("Alicia")


voting_system.nominate_president("1001")


voting_system.vote_for_president("1001")


voting_system.update_nominee("1002")

voting_system.remove_nominee()

voting_details = voting_system.view_voting_details()

print(student1.name, "voted for", voting_details[student1.student_id])

