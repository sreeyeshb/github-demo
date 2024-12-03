def check_pal(word):
    if word == word[::-1]:
        return True
    else:
        return False    
    
def main():
    word = input("Enter the word: ")
    if check_pal(word):
        print("It is a palindrome")
    else:
        print("It is not a palindrome")

if __name__ == "__main__":
    main()