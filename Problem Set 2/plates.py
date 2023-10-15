# Defining a function to check if the plate number has atleast 2 letters
def two_letters(a:str):
    count=0
    for char in a:
        if char.isalpha():
            count+=1
    return count >=2
#Defining a function to check if numbers remain at end
def numbers_at_end(a:str):
    if a[-1].isdigit() and not a[0].isdigit() and a[0]!=0 and not a[-2].isalpha():
        return True
    elif a [-1].isalpha() and not a[-2].isdigit() and not a[-3].isdigit() and not a[-4].isdigit():
        return True
    else:
        return False
def number_starts_with_zero(a:str):
    digits=any(char.isdigit() for char in a)
    if digits:
        numbers=''.join(char for char in a if char.isdigit())
        if numbers.startswith('0') and numbers !='0':
            return False
    return True
def check_punc(a:str):
    if all(char.isalnum() for char in a):
        return True
def is_valid(s):
    if 2<=len(s)<=6 and two_letters(s) and numbers_at_end(s) and number_starts_with_zero(s) and check_punc(s):
        return True
    else:
        return False
def main():
    plate =input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
main()