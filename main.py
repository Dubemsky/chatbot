import json
from difflib import get_close_matches


# Load the knowledge base from a specified file
def load_knowledge_base(file_path):
    # Open the file in read mode and load its contents as JSON
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data



# Save the knowledge base to a specified file
def save_knowledge_base(file_path, data):
    # Open the file in write mode and write the data in JSON format
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)


# Find the best-matched question based on user input
def find_best(user_question, questions):
    # Use difflib's get_close_matches to find the closest match
    matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None


# Retrieve the answer for a given question from the knowledge base
def get_answer_for_question(question, knowledge_base):
    # Iterate through the knowledge base and find the matching question
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]


# Main function for the chatbot
def chat_bot():
    # Load the knowledge base from 'knowledge_base.json'
    knowledge_base = load_knowledge_base('knowledge_base.json')

    # Main chat loop
    while True:
        # Get user input
        user_input = input("You: ")

        # Check if the user wants to quit
        if user_input.lower() == 'quit':
            print("Bye!")
            break

        # Find the best matching question in the knowledge base
        best_match = find_best(user_input, [q["question"] for q in knowledge_base["questions"]])

        # If a match is found, provide the answer
        if best_match:
            answer = get_answer_for_question(best_match, knowledge_base)
            print(f"Bot: {answer}")
        else:
            # If no match is found, ask the user to provide an answer
            print("Bot: I don't know the answer. Can you teach me?")
            new_answer = input('Type the answer or skip: ')

            # If the user provides an answer, add it to the knowledge base
            if new_answer.lower() != 'skip':
                knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                # Save the updated knowledge base to 'knowledge_base.json'
                save_knowledge_base('knowledge_base.json', knowledge_base)
                print("Thank you!")


# Execute the chat_bot function if this script is run
if __name__ == '__main__':
    chat_bot()




