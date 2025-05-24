# PRODIGY_CS_03
Password Strength Checker
Yo, What's This?
This is a chill little Python tool that checks if your password is tough enough. It looks at stuff like how long it is, if you’ve got uppercase and lowercase letters, numbers, and those funky special characters. Then it gives you a score and some tips to make your password beefier.
What’s It Do?

Checks if your password’s long enough (8 or more characters is the vibe)
Spots uppercase letters, lowercase letters, numbers, and special characters
Gives you a score from 0 to 5
Says if your password’s Weak, Moderate, or Strong
Drops some quick tips to make it better

What You Need

Just Python 3, nothing fancy

How to Use It

Grab the password_checker.py file and toss it somewhere on your computer.
Open your terminal and hit:

python password_checker.py


Type in a password to test out.
Check out the score and tips it spits out.
Wanna try another? Go for it. Done? Just type 'q' to bounce.

Example Run
Password Strength Checker
-----------------------
Enter a password (or 'q' to quit): Pass123!
Results:
Strength: Moderate
Score: 4/5
Tips:
- Decent length (8-11 chars).
- Has uppercase: Nice!
- Has lowercase: Good job!
- Numbers included: Sweet!
- Add special chars like !@#$%.

Enter a password (or 'q' to quit): q
See ya!

How It Scores

Length: Less than 8 chars? 0. Between 8-11? 1 point. 12 or more? 2 points.
Uppercase letters? +1 if you’ve got ‘em.
Lowercase letters? +1 if they’re there.
Numbers? +1 if you used any.
Special characters? +1 for those weird symbols.

Strength Vibes

0-2 points: Weak (ouch, gotta step it up)
3-4 points: Moderate (not bad, but could be tougher)
5 points: Strong (you’re killing it!)


