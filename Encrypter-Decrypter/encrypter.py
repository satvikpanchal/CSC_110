###
### Author: Satvik Panchal
### Description: This program takes one input from the user, a file with content,
###              strings or integers and encrypts the content. The encrypted content
###              and the encrypted index is added to a file.
###

import random


def main():
    """
    This is the main function which defines the random seed for the program. This function
    also takes an input from the user, the content that encryption(file, stripped, num_list)
    encrypts. This also has two lists which are used in encryption(file, stripped, num_list)
    later on.
    """
    random.seed(125)
    file = str(input("Enter a name of a text file to encrypt:\n"))
    file_stripped = []
    num_list = []
    encryption(file, file_stripped, num_list)


def encryption(file, file_stripped, num_list):
    """
    This function takes an input file and encrypts the content so that no one else can read it
    without a decrypter. Using the index of the file content, it takes two random numbers(two
    numbers from the index of the file content) and swaps them and repeats range(0, (length * 5))
    times. The random index corresponds to the index of the content of the file and encrypts the
    data in the file respectively. That encrypted data is added to a file and cannot be decrypted
    without decrypted.py.
    """
    index_file = open('index.txt', 'w')

    file1_read = open(file, 'r')

    file1_list = file1_read.readlines()

    for strip in file1_list:
        strip = strip.rstrip("\n")
        file_stripped.append(strip)

    length = len(file_stripped)

    inc_var = 1
    for k in range(0, length):
        num_list.append(inc_var)
        inc_var += 1

    for i in range(0, (length * 5)):

        num1 = random.randint(0, length - 1)
        num2 = random.randint(0, length - 1)

        file_stripped[num1], file_stripped[num2] = file_stripped[num2], file_stripped[num1]
        num_list[num1], num_list[num2] = num_list[num2], num_list[num1]

    for jumbled in num_list:
        index_file.write(str(jumbled) + '\n')

    file1_write = open('encrypted.txt', 'w')

    for jumbled in file_stripped:
        file1_write.write(str(jumbled) + '\n')

    file1_write.close()
    index_file.close()


main()