
def PatternCount(Text, Pattern):

    count = 0

    for i in range(len(Text)-len(Pattern)+1):

        if Text[i:i+len(Pattern)] == Pattern:

            count =count+1

    return count

file = open("dataset_30272_6.txt", "r")
content = file.readlines()

Text = content[0]
Pattern = content[1]
Pattern = Pattern.rstrip()

print(PatternCount(Text, Pattern))


