def can_make_str(s1, s2):
    count = {s1[i] : 0 for i in range(len(s1))}
    
    for i in range(len(s1)):
        count[s1[i]] += 1

    for i in range(len(s2)):
        if count[s2[i]] ==0:
            return False
        count[s2[i]] -= 1
    return True

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

if can_make_str(s1, s2):
    print("Yes")
else:
    print("No")