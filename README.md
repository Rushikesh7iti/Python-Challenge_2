Student Registration System (Python)
Project analysis
It takes details from a student and checks whether all the information is in proper format . If all conditions are correct , the registration is approved; orit is rejected.
The program asks the user to enter:

Student ID

Email ID

Password

Referral Code
Validation Rules 
1.Student ID
2.Must start with CSE
3.Must contain a hyphen (-) after CSE
4.Must end with exactly 3 digits

🔹 Email ID

Must contain @ and .

@ should not be the first or last character

Must end with .edu.


🔹 Password

Must be at least 8 characters long

First letter must be uppercase

Must contain at least one number


🔹 Referral Code

Must start with REF

Must have 2 digits after REF

Must end with @

Program flow:

The user gives required inputs.

The program checks each input using string slicing and built-in functions.

If all conditions are satisfied, it prints:

APPROVED


If any one condition fails, it prints:

REJECTED
