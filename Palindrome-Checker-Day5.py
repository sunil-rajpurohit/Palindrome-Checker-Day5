import re

def isPalindrome():
  word = input("Enter a word: ")
  clean_word = word.replace(" ", "").replace(",", "").lower()
  clean_word = re.sub(r'[^a-z0-9]', '', word.lower()) #Thanks to GFG
  
  if clean_word == clean_word[::-1]:
    print("It's a palindrome!")
  else:
    print("Not a palindrome.")
  re_check = input("Wanna Check Again?(y/n): ").lower()
  if re_check == "y":
    return isPalindrome()
  else:
    print("Thank you !!")
    
if __name__ == "__main__":
  isPalindrome()