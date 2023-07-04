# Import regular expressions modula
import re


def wordChecker():
    txtFile = input('Enter your file path: ')
    strWord = input('Specify the string to search: ')
    """Takes in a text file and a string root of a word.
    It searches for words related to that string using regular
    expressions and returns the words and the lines where they are."""

    # Declare a variable to hold the pattern to seach using re.compile function
    wordPattern = re.compile(r"\b\w*" + strWord + r"\w*\b", re.IGNORECASE)

    # Open the input and output files
    print("Opening origin.txt")
    with open(txtFile, "r") as inStream:
        print(f"Opening {strWord}.txt")
        with open(f"{strWord}.txt", "w") as outStream:

            # Iterate over each line in the input file, keeping track of
            # lineNum as index, line as item using enumerate built-in function
            for lineNum, line in enumerate(inStream, start=1):

                # Use re.search function to look for the pattern inline
                match = re.search(wordPattern, line)

                # Write word match to output file when a word is found
                if match:
                    outStream.write("{}\t{}\n".format(lineNum, match.group(0)))

    print("Done!")
    print(f"{txtFile} is closed?", inStream.closed)
    print(f"{strWord}.txt is closed?", outStream.closed)


if __name__ == "__main__":
    wordChecker()
