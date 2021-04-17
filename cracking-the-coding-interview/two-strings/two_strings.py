import time
start_time = time.time()

def two_strings_permutation(string1, string2):
    chars1 = [False] * 256
    chars2 = [False] * 256
    if len(string1) == len(string2):
        for i in range(len(string1)):
            
            chars1[ord(string1[i])] = True
            
            chars2[ord(string2[i])] = True

        if chars1 == chars2 :
            return True
        else : 
            return False
    else : 
        return False


if __name__ == '__main__':
    string1 = "hello world"
    string2 = "world hello"
    if two_strings_permutation(string1, string2):
        print("The two strings are permutations of each other")
    else :
        print("The two strings are not permutations of each other")

print("--- %s seconds ---" % (time.time() - start_time))
