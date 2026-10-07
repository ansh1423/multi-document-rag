from llm import generate_answer


query = "Where does Ansh currently work?"

context = """
Ansh Yadav is currently working at Ericsson Global India
as a Network Engineer in Noida, India.
"""


answer = generate_answer(query, context)


print("\nQuestion:")
print(query)

print("\nAnswer:")
print(answer)