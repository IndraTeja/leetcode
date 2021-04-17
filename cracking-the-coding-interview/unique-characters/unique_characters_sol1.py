# brute force solution
import time
start_time = time.time()

def unique_characters(string):
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                return False

if __name__ == '__main__':
    string = "hello world"
    if unique_characters(string):
        print("The string has unique characters")
    else :
        print("The string has duplicate characters")

print("--- %s seconds ---" % (time.time() - start_time))