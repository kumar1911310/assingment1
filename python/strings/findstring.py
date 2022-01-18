def count_substring(string, sub_string):
    a=len(string)
    b=len(sub_string)
    m=0
    count=0
    for i in range(0,a):
        if (string[m:b]==sub_string):
            count+=1
        m+=1
        b+=1       
    return count
