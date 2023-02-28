#time spent: 40 min
#time complexity: O(n)
#space complexity: O(n)
#method used: incresing/decreasing sliding window method


def BackspaceStringCompare(str1, str2):
    cou1 = 0
    cou2 = 0
    
    if "#" in str1:
        for i in str1:
            if i == '#':
                cou1 +=1
                
    if "#" in str2:
        for i in str2:
            if i == '#':
                cou2 +=1
            
    slider1 = cou1+1
    slider2 = cou2+1
    #print(slider1*"#")
    main1 = ''
    main2 = ''
    
    for i in range(len(str1)):
        if "#" not in str1[i:slider1:]:
            if str1[i] != "#":
                main1= main1 + str1[i]
            slider1 +=1
            if  i >0 and str1[i-1] == "#":
                slider1+=1
        
            
            
    for i in range(len(str2)):
        if "#" not in str2[i:slider2:]:
            if str2[i] != "#":
                main2= main2 + str2[i]
            slider2 +=1
            if  i >0 and str2[i-1] == "#":
                slider2+=1
        
        #slider2 +=1
    
    #print(main1)
    #print(main2)
    
    return main1 == main2
            
        
    
    

#print(BackspaceStringCompare("abcde", "abcde"))
#print(BackspaceStringCompare("U e##r", "u#U ee###r"))
#print(BackspaceStringCompare("abcdef###xyz", "abcw#xyz"))
#print(BackspaceStringCompare("abcdef###xyz", "abcdefxyz###"))

##Given two strings representing series of keystrokes,
#determine whether the resulting text is the same.
#Backspaces are represented by the '#' character so "x#" results in the empty string ("").

#Examples:
#eInput Strings: "abcde", "abcde"
#Output: True

#Input Strings: "Uber Career Prep", "u#Uber Careee#r Prep"
#Output: True

#Input Strings: "abcdef###xyz", "abcw#xyz"
#Output: True

#Input Strings: "abcdef###xyz", "abcdefxyz###"
#Output: False




