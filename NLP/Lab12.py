from nltk.tokenize import word_tokenize

print("Welcome to AIMMIT Admission Chatbot!")
print("Type 'exit' to end the conversation.")

responses = {
    "Courses": "AIMMIT offers courses in Data Science, Artificial Intelligence, and Machine Learning.",
    "eligibility": "For MCA admission, candidtes must have a bachelor's degree in any discipline with at least 50% marks.",
    "fees": "The total fees for the MCA program at AIMMIT is approximately $10,000 per year.",
    "admission": "To apply for admission, please visit our website and fill out the application form. The admission process includes an entrance exam and an interview.",
    "contact": "You can contact AIMIT at +123-456-7890 or email us at admission@aimmit.edu",
    "location": "AIMIT is located at 123 Main Street, Anytown, USA.",
    "hostel": "AIMMIT provides hostel facilities for students. The hostel is equipped with modern amenities and is located within the campus."
}

while True:
    user_input = input("You: ").lower()
    if user_input == "exit":
        print("Chatbot: Thank you for your interest in AIMMIT. Have a great day!")
        break
    tokens = word_tokenize(user_input)

    if "courses" in tokens or "program" in tokens:
        print("Chatbot:", responses["Courses"])
    elif "eligibility" in tokens or "criteria" in tokens:
        print("Chatbot:", responses["eligibility"])
    elif "fees" in tokens or "cost" in tokens:
        print("Chatbot:", responses["fees"])
    elif "admission" in tokens or "apply" in tokens:
        print("Chatbot:", responses["admission"])
    elif "contact" in tokens or "phone" in tokens or "email" in tokens:
        print("Chatbot:", responses["contact"])
    elif "location" in tokens or "address" in tokens:
        print("Chatbot:", responses["location"])
    elif "hostel" in tokens or "accommodation" in tokens:
        print("Chatbot:", responses["hostel"])
    else:
        print("Chatbot: Sorry, no match found.")

