#this will print out the value of a variable in binary and hexadecimal form
x =18
print (x, bin(x), hex(x))

#Now I will identify the error when setting an invalid input equal to x
#I changed it to 1.825 and the error I received was that it was a 'float' object and cannot be interpreted as an integer. In other words, 'float' is a fraction or decimal.

#I will assign two binary values to two variables
y=101101
x=11100101
print (y, x)

#This will add numbers as variables
x = 2
y = 4
z = 14
w = x + y + z
print ("The sum is" , w)

#This will calculate the percent of compression
original_size = 240
dictionary_size = 25
compressed_text_size = 148
percent_of_compression = 1-((compressed_text_size + dictionary_size)/original_size)
print("The percent of compression is", (percent_of_compression*100), "%")

#This is the extra credit portion. It is using two's complement of a decimal number with input from a user.
def to_twos_complement(n):
    if n < 0:
        n = (1 << 8) + n
    return format(n, '08b')
def main():
    num = int(input("Enter a non-decimal number between -128 and 127: "))
    if num < -128 or num > 127:
        print("Error: Please enter a number between -128 and 127.")
        return
    print("Two's complement:", to_twos_complement(num))
if __name__ == "__main__":
    main()
