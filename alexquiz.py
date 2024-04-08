# Quiz App - Tutorial for Learn IT

# Questions and possible answers as well as the define for which answer is correct. Make note of the formatting and placement of symbols
questions = [
    {
  "question": "What is my middle name?",
  "options": ["A: Isak", "B: Robert", "C: Ringo", "D: Stig"],
  "answer": "C"
},

{
  "question": "What is my Favorite color?",
  "options": ["A: Blue", "B: Red", "C: Black", "D: Yellow", "E: Green"],
  "answer": "A"
},

{
  "question": "What is my favorite subject in school?",
  "options": ["A: Web development", "B: English", "C: Programming", "D: Math"],
  "answer": "B"
},

{
  "question": "What year was I born?",
  "options": ["A: 2003", "B: 2002", "C: 2005", "D: 2004"],
  "answer": "A"
},

{
  "question": "What soda do I like the most?",
  "options": ["A: Coca Cola", "B: Pepsi max", "C: Sprite", "D: Fanta"],
  "answer": "D"
},

{
  "question": "What is my most played video game?",
  "options": ["A: Overwatch", "B: Fortnite", "C: Destiny 2", "D: League of Legends"],
  "answer": "C"
},

{
  "question": "Which of these movies is my favorite?",
  "options": ["A: Inception", "B: Interstellar", "C: Dune", "D: The Maze Runner"],
  "answer": "B"
},

{
  "question": "How many siblings do I have?",
  "options": ["A: 1", "B: 2", "C: 3", "D: 4"],
  "answer": "A"
},

{
  "question": "What swedish political party do I support the most?",
  "options": ["A: Moderaterna", "B: Socialdemokraterna", "C: Sverigedemokraterna", "D: Liberalerna"],
  "answer": "B"
},

{
  "question": "What snacks do I enjoy the most?",
  "options": ["A: Chips", "B: Candy", "C: Protein bars", "D: Popcorn"],
  "answer": "A"
},
    # You can remove this comment or move it down and add more questions. You should enclose each question in their own {} brackets.
]

# This function will define the quiz code on launch
def run_quiz(questions):
    score = 0  # Initialize score to 0 and create a variable "score" to store the value of correct answers

    # Loop through all the questions. This will follow all the questions above until finished
    for question in questions:
        print("\n" + question["question"])  # Print the question
        for option in question["options"]:
            print(option)  # Print all the answer options

        # Get the user's answer
        user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()

        # Check if the user's answer is correct
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1  # Increment score if correct
        else:
            print("Wrong answer.")

    # Print the final score from the stored variable
    print(f"\nYou got {score} out of {len(questions)} questions correct!")

# Run the quiz
run_quiz(questions)