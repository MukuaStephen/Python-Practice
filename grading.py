score = input("Enter your marks")
score = int(score)
if score >= 70 and score <100:
    print("Grade A")
elif score >=60 and score <70:
    print("Grade B")
elif score >= 50 and score < 60:
    print("Grade C")
elif score >= 40 and score < 50:
    print("Grade D")
elif score >= 0 and score < 40:
    print("Grade Fail")
else:
    print("Invalid score")