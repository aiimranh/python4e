# madlib using f string & for this project it the best realible.
name = input("Enter Your Name: ").capitalize()
varsity_name = input("Enter University Name :").upper()
subject_name = input("Enter Subject Name :").upper()
programming_language = input("Enter a Programming Language :").capitalize()
adjective = input("Enter a Adjective :").lower()

madlib1  = f"I am {name}. I am a student. I am studying in {varsity_name}. My subject name is {subject_name}. Currently, I work in {programming_language}. \
Now, I am creating some {adjective} projects for practise."
print(madlib1)
