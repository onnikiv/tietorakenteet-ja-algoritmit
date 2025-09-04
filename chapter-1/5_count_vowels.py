
vowels_list = ["a","e","i","o","u","y"]

def vowels(string):
    count = 0
    
    for char in string:
        if char in vowels_list:
            count += 1
    
    print(f"Number of vowels: {count}")

vowels(input().lower())