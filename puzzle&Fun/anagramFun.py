'''
The point of this excercise is to solve a simple anagram problem.
A anagram is to my understanding, given two words, one word is the other word rearranged
for this program we will asssume the following

word1- "ABCD"
word2-"DCBA" these are anagrams

we will assume equal length for both words and lowercase characters
just having some fun
'''

def anagramOrNot(word1,word2):
    list1=list(word1)  #put both words into a sep list
    list2=list(word2)

    list1.sort()   #sort each of them
    list2.sort()

    doesItMatch = True #this will tell me if each position like 'p' in word1(python) is equal to 'p' in word2(typhon), sorted
    position = 0 #simple counter to keep track of the ith position

    while position < len(word1) and doesItMatch:
        if list1[position] == list2[position]:#check if theyre equal if true, check next i
            position=position+1#i++
        else:
            doesItMatch = False #else return doesItMatch with False
    return doesItMatch



print(anagramOrNot('python','typhon')) #true
print(anagramOrNot('abcde','blaha')) #false
