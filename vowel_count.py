string_input=input('enter the string : ')
vowel="aeiouAEIOU"
vowel_count=0
c_count=0
for char in string_input:
    if char in vowel:
        vowel_count+=1
    else:
        c_count+=1
print(f"Number of vowel ={vowel_count}\nNumber of consonant ={c_count}")