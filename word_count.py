def count_words(sen):
   
    Count the number of words in a given text.
    
    Args:
        sen (str): The input text to count words in.
    
    Returns:
        int: The number of words in the text.
    
    # Split the text into words based on whitespace and return the length of the list
    return len(sen.split())

def main():
    
    Main function to run the word counting program.
    
    # Prompt the user to enter a sentence or paragraph
    user_input = input("Please enter a sentence or paragraph: ").strip()

    # Check if the input is empty
    if not user_input:
        print("Error: You must enter a sentence or paragraph.")
    else:
        # Count the words using the count_words function
        word_count = count_words(user_input)
        # Display the word count to the user
        print(f"The number of words in your input is: {word_count}")

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
