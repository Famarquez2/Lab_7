def edit_distance(val1, val2):
    val = []  # where to store the strings
    for i in range(val1 + 1):
        val.append([0 for i in range(val2 + 1)])

    # Create a table for edit distance
    for x in range(val1 + 1):
        for y in range(val2 + 1):

            if x == 0 or y == 0:  # Checks if first string or second string is empty
                val[x][y] = x
                val[x][y] = y

            elif s1[x - 1] == s2[y - 1]:  # Determines if characters are equal
                val[x][y] = val[x - 1][y - 1]

            else:  # If chars are not equal then find Min resources and take the min value
                val[x][y] = 1 + min(val[x][y - 1], val[x - 1][y], val[x - 1][y - 1])

    return val[val1][val2]  # Returns edit distance of string if any distance is there


def are_strings_distant(s1, s2):
    # Length of current string
    curr1 = len(s1)
    curr2 = len(s2)

    if (curr1 - curr2) > 1:  # Edit distance cannot be more than 1
        return "No"

    count = 0  # Start count at 0

    # Set variables to 0
    str1 = 0  # s1
    str2 = 0  # s2

    while str1 < curr1 and str2 < curr2:

        if s1[str1] != s2[str2]:
            if count == 1:
                return "No"  # return false if s1 does not equal to s2

            if curr1 > curr2 or curr1 < curr2:   # adds 1 to length of string 1 if its greater
                str1 += 1                        # adds 1 to length of string 2 if its less
                str2 += 1

            else:  # If s1 and s2 are the same strings
                str1 += 1
                str2 += 1

            count += 1  # add 1 to count

        else:  # Updates both strings if they are the same
            str1 += 1
            str2 += 1

    if str1 < curr1 or str2 < curr2:
        count += 1  # increment if strings are either or both less then current

    return "Yes"  # Return True if strings are distant


# Test if strings are distant and how much edit distance is:
s1, s2 = "Miners", "Miners"  # Team Spirit
print("Strings given: -------------->", s1, s2)
print("Are strings distant: -------->", are_strings_distant(s1, s2))
print("Edit distance of the strings: ", edit_distance(len(s1), len(s2)))
