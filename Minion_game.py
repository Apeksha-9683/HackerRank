'''def minion_game(string):
    # your code goes here
    s=string.lower()
    word=0
    count=0
    sum_count=0
    dict={}
    i=0
    while i<len(s):
        if s[i] in 'aeiou':
            word+=s[i]
            dict[word]=count
            if word in dict:
                count+=1
            else:
                count = 1
            sum_count+=count
        
        else:
            word+=s[i]
            dict[word]=count
            if word in dict:
                count+=1
            else:
                count = 1
            sum_count+=count
        i+=1
        print("Score of Stuart is ", sum_count)
        return sum_count
        
            
    
if __name__ == '__main__':
    s = input("Enter a string ")
    minion_game(s)'''

def minion_game(string):
    s=string.lower()
    word=""
    count=0
    kevin_score=0
    stuart_score=0
    dict={}
    i=0
    while i<len(s):
        word =s[i]

        if s[i] in 'aeiou':
            if word in dict:
                count=dict[word]+1
            else:
                count=1
            dict[word]=count
            kevin_score+=(len(s)-i)
        else:
            if word in dict:
                count=dict[word]+1
            else:
                count=1
            dict[word]=count
            stuart_score+=(len(s)-i)

        i+=1

    if kevin_score>stuart_score:
        print("Kelvin", kevin_score)
    else:
        print("Stuart", stuart_score)
        
    s=input("enetr the string")
    minion_game(s)

    def minion_game(s):
        vowels="AEIOU"
        kevin=0
        stuart=0
        n=len(s)

        for i in range(n):
            if s[i] in vowels:
                kevin+=n-i
            else:
                stuart+=n-i
        if kevin>stuart:
            print("Kevin", kevin)
        elif stuart>kevin:
            print("Stuart", stuart)
        else:
            print("Draw")
        return s
    s=input("Enter a string ")
    minion_game(s)