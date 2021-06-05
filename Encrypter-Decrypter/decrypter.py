###
### Author: Satvik Panchal
### Description: This program takes two user input, one of them being the content file,
###              the other being the index file of the content. This program decrypts the
###              content using the index and writes it another file called encrypted.txt
###

def main():
    """
    The main function takes two inputs from the user and calls the function that decrypts
    the content of the file.
    """

    encrypted_text = input("Enter the name of an encrypted text file: \n")
    encrypted_index = input("Enter the name of the encryption index file: \n")
    decryption(encrypted_text, encrypted_index)


def decryption(encrypted_text, encrypted_index):
    """
    This function takes the two input from the user, the encrypted content file and the
    encrypted index file. Using the correct indexes in the encrypted index file, it
    re-arranges the content of the file in such a way that it goes from index 1 to index
    length of the content list. After getting a list of the decrypted content, the correctly
    arranged content is written to decrypted.txt.
    """

    file = open('decrypted.txt', 'w')
    encrypted_text_file = open(encrypted_text, 'r')
    encrypted_index_file = open(encrypted_index, 'r')

    encrypted_text_list = []
    encrypted_index_list = []

    for i in encrypted_text_file:
        i = i.strip('\n')
        encrypted_text_list.append(i)

    for k in encrypted_index_file:
        k = k.strip('\n')
        encrypted_index_list.append(int(k))

    decrypted_list = []
    for index in range(0, len(encrypted_index_list)):
        index_text = encrypted_index_list.index(index+1)
        decrypted_list.append(encrypted_text_list[index_text])

    for file_write in decrypted_list:
        file.write(file_write + '\n')

    file.close()


main()