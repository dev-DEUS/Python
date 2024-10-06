name1 = input("Your name: ")
name2 = input("Their name: ")
combined_string = name1.lower() + name2.lower()

t = combined_string.count('t')
r = combined_string.count('r')
u = combined_string.count('u')
e = combined_string.count('e')
first_digit = t + r + u + e

l = combined_string.count('l')
o = combined_string.count('o')
v = combined_string.count('v')
e = combined_string.count('e')
second_digit = l + o + v + e

love_score = first_digit + second_digit

if love_score < 10 or love_score > 90:
    print("you go together like coke and mentos")
elif love_score >= 40 and love_score <= 50:
    print("you are mid together")
elif love_score == 69:
    print("you are like ying and yang")
else:
    print("you are like bonnie and clyde")