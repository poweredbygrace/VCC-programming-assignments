# Define the function to encrypt a single word using the Caesar Cipher
def encryptWord(word, key):
    # Convert word to lowercase
    word = word.lower()
    # Initialize an empty result string
    result = ""
    # Encrypt each character in the word
    for ch in word:
        # Convert character to Caesar cipher number using the given formula
        num = (ord(ch) + key - 97) % 26 + 97
        # Append encrypted character to the result string
        result += chr(num)
    return result

# Define the function to encrypt the entire text using Caesar Cipher
def encrypt(text, key):
    # Split text into words
    words = text.split()
    # Initialize an empty result string for the final output
    result = ""
    # Encrypt each word and concatenate with spaces
    for word in words:
        # Encrypt the word using encryptWord and append to result
        encrypted_word = encryptWord(word, key)
        result += encrypted_word + " "
    # Return the final encrypted text (strip the trailing space)
    return result.strip()

# Define the main function to read, encrypt, and write output
def main():
    # Part 1: Read the input file content
    with open("message.txt", "r") as infile:
        message = infile.read().strip()
    
    # Part 2: Encrypt the message using the Caesar Cipher
    encrypted_message = encrypt(message, 10)
    
    # Part 3: Write the encrypted message to an output file
    with open("../../3. Introduction to Programming/Assignments/encryptedMessage.txt", "w") as outfile:
        outfile.write(encrypted_message)

# Call the main function to execute the encryption
if __name__ == "__main__":
    main()
