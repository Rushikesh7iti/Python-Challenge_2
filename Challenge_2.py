student_id = input("ID:")
email = input("Email:")
passcode = input("Password:")
referral = input("Referral:")
if student_id[0:3] == "CSE" and student_id[3] == "-" and student_id[-3:].isdigit() == True and "@" in email and "." in email and  "@" != email[0] and "@"!= email[-1] and email[-4:] == ".edu" and len(passcode) >= 8 and passcode[0].isupper() == True and ('0'in passcode or '1'in passcode or '2'in passcode or '3'in passcode or '4' in passcode or '5' in passcode or '6' in passcode or '7' in passcode or '8' in passcode or '9' in passcode) and referral[0:3] == "REF" and referral[3:5].isdigit() == True and referral[-1] == "@":
    print("APPROVED")
else:
    print("REJECTED")

