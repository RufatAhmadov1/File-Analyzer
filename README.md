# Project Description:
The File Analyzer is a Python program that analyzes a text file and provides
various statistics related to the content of the file. It helps users understand the composition of
the text and extract useful insights.
# Features:
Word Count: The program counts the total number of words present in the text file. It splits the
content based on whitespace and punctuation to identify individual words and calculates their
count.

Character Count: The program calculates the total number of characters in the text file. It
includes all characters, including spaces, punctuation marks, and special symbols.

Frequency of Each Word: The program determines the frequency of each unique word present
in the text file. It counts how many times each word appears and generates a report with the
word and its corresponding count.
# Functionality:
Input: The program prompts the user to provide the path to the text file they want to analyze. It
validates the path and checks if the file exists.

Text Parsing: The program reads the contents of the text file and cleans it by removing any
unwanted characters or symbols, such as punctuation marks, special characters, or line breaks.
It ensures that only meaningful words are considered for analysis.

Word Count Calculation: The program counts the number of words in the cleaned text. It ignores
case sensitivity, treating "word" and "Word" as the same word.

Character Count Calculation: The program calculates the total number of characters in the text,
including letters, numbers, spaces, and symbols.

Word Frequency Calculation: The program creates a dictionary to store the frequency of each
unique word. It iterates over the words in the text, increments the count for each word
encountered, and generates a report with the word and its corresponding count.

Output: The program displays the calculated statistics to the user. It provides the word count,
character count, and a report showing the frequency of each word in the text.
