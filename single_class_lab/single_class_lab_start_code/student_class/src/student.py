class Student():
    def __init__(self, name, cohort):
        self.name = name
        self.cohort = cohort
    def talk(self):
        return "I can talk!"
    def say_favourite_language(self, fav_language):
        if fav_language == "Python":
            return "I love Python"
        else:
            return "Wrong answer"

