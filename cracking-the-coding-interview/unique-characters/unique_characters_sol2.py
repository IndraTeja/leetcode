# ASCII Set solution(8bit) 
import time
start_time = time.time()

def unique_characters(string):
    if len(string) > 256 : return False

    chars = [False] * 256

    for i in range(len(string)):
        index = ord(string[i]) # returns the unicode(int) for characters
        
        if chars[index] == True : 
            return False
        
        chars[index] = True
    return True

if __name__ == '__main__':
    string = "hello world"
    if unique_characters(string):
        print("The string has unique characters")
    else :
        print("The string has duplicate characters")

print("--- %s seconds ---" % (time.time() - start_time))