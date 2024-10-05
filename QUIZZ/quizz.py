# import random
# import time

# class Quiz:
#     def __init__(self):
#         self.questions = {
#             "1. தமிழ்நாட்டின் தலைநகரம் எது?": {
#                 "options": ["A) சென்னை", "B) மதுரை", "C) கோயம்புத்தூர்", "D) திருச்சி"],
#                 "correct": "A"
#             },
#             "2. பைதாகரஸ் தேற்றம் எந்த வடிவத்திற்கு பொருந்தும்?": {
#                 "options": ["A) வட்டம்", "B) முக்கோணம்", "C) செவ்வக முக்கோணம்", "D) சதுரம்"],
#                 "correct": "C"
#             },
#             "3. HTML-ன் முழு வடிவம் என்ன?": {
#                 "options": ["A) High Text Markup Language", "B) Hyper Text Markup Language", 
#                            "C) Hyper Transfer Markup Language", "D) High Transfer Markup Language"],
#                 "correct": "B"
#             },
#             "4. Python-ல் list-ஐ உருவாக்க எந்த அடைப்புக்குறி பயன்படுகிறது?": {
#                 "options": ["A) ()", "B) {}", "C) []", "D) <>"],
#                 "correct": "C"
#             },
#             "5. தமிழ் மொழியின் தொன்மையான இலக்கிய நூல் எது?": {
#                 "options": ["A) சிலப்பதிகாரம்", "B) திருக்குறள்", "C) தொல்காப்பியம்", "D) புறநானூறு"],
#                 "correct": "C"
#             }
#         }
#         self.score = 0
#         self.total_questions = len(self.questions)

#     def welcome(self):
#         print("\n" + "="*50)
#         print("\tவணக்கம்! Quiz-க்கு வரவேற்கிறோம்")
#         print("="*50)
#         print("\nவிதிமுறைகள்:")
#         print("1. ஒவ்வொரு கேள்விக்கும் 4 விருப்பங்கள் உள்ளன")
#         print("2. சரியான பதிலுக்கு 1 மதிப்பெண்")
#         print("3. தவறான பதிலுக்கு 0 மதிப்பெண்")
#         input("\nதொடங்க Enter அழுத்தவும்...")

#     def ask_question(self, question, options, correct):
#         print("\n" + "-"*50)
#         print(question)
#         for option in options:
#             print(option)
        
#         while True:
#             answer = input("\nஉங்கள் பதில் (A/B/C/D): ").upper()
#             if answer in ['A', 'B', 'C', 'D']:
#                 break
#             print("தயவுசெய்து A, B, C, அல்லது D-ஐ மட்டும் தேர்வு செய்யவும்")
        
#         if answer == correct:
#             print("\n✅ சரியான பதில்!")
#             self.score += 1
#         else:
#             print(f"\n❌ தவறான பதில். சரியான பதில் {correct}")
        
#         time.sleep(1)

#     def display_final_score(self):
#         print("\n" + "="*50)
#         print(f"\tஉங்கள் மதிப்பெண்: {self.score}/{self.total_questions}")
#         percentage = (self.score / self.total_questions) * 100
#         print(f"\tசதவீதம்: {percentage:.2f}%")
        
#         if percentage == 100:
#             print("\tஅருமை! எல்லா கேள்விகளுக்கும் சரியான பதில்!")
#         elif percentage >= 80:
#             print("\tமிக நன்று!")
#         elif percentage >= 60:
#             print("\tநன்று!")
#         else:
#             print("\tமேலும் முயற்சி செய்யுங்கள்!")
#         print("="*50)

#     def run_quiz(self):
#         self.welcome()
#         questions_list = list(self.questions.items())
#         random.shuffle(questions_list)
        
#         for question, data in questions_list:
#             self.ask_question(question, data["options"], data["correct"])
        
#         self.display_final_score()

# # Quiz ஐ இயக்க
# if __name__ == "__main__":
#     quiz = Quiz()
#     quiz.run_quiz()

import random
import time

class Quiz:
    def __init__(self):
        self.questions = {
            "1. Which planet is known as the Red Planet?": {
                "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
                "correct": "B"
            },
            "2. What is the capital of France?": {
                "options": ["A) London", "B) Berlin", "C) Paris", "D) Rome"],
                "correct": "C"
            },
            "3. What does CPU stand for?": {
                "options": ["A) Central Process Unit", "B) Computer Personal Unit", 
                           "C) Central Processor Unit", "D) Central Processing Unit"],
                "correct": "D"
            },
            "4. Which of these is not a programming language?": {
                "options": ["A) Java", "B) Python", "C) Cobra", "D) HTML"],
                "correct": "C"
            },
            "5. What is the largest mammal in the world?": {
                "options": ["A) African Elephant", "B) Blue Whale", "C) Giraffe", "D) Polar Bear"],
                "correct": "B"
            }
        }
        self.score = 0
        self.total_questions = len(self.questions)

    def welcome(self):
        print("\n" + "="*50)
        print("\tWelcome to the Quiz Game!")
        print("="*50)
        print("\nRules:")
        print("1. There are multiple choice questions")
        print("2. Each correct answer gets 1 point")
        print("3. There's no negative marking")
        input("\nPress Enter to start the quiz...")

    def ask_question(self, question, options, correct):
        print("\n" + "-"*50)
        print(question)
        for option in options:
            print(option)
        
        while True:
            answer = input("\nYour answer (A/B/C/D): ").upper()
            if answer in ['A', 'B', 'C', 'D']:
                break
            print("Please choose A, B, C, or D only")
        
        if answer == correct:
            print("\n✅ Correct!")
            self.score += 1
        else:
            print(f"\n❌ Wrong! The correct answer is {correct}")
        
        time.sleep(1)

    def display_final_score(self):
        print("\n" + "="*50)
        print(f"\tYour Score: {self.score}/{self.total_questions}")
        percentage = (self.score / self.total_questions) * 100
        print(f"\tPercentage: {percentage:.2f}%")
        
        if percentage == 100:
            print("\tPerfect! You got all questions right!")
        elif percentage >= 80:
            print("\tExcellent performance!")
        elif percentage >= 60:
            print("\tGood job!")
        else:
            print("\tKeep practicing!")
        print("="*50)

    def run_quiz(self):
        self.welcome()
        questions_list = list(self.questions.items())
        random.shuffle(questions_list)
        
        for question, data in questions_list:
            self.ask_question(question, data["options"], data["correct"])
        
        self.display_final_score()

# To run the Quiz
if __name__ == "__main__":
    quiz = Quiz()
    quiz.run_quiz()