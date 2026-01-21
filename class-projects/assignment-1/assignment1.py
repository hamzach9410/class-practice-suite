def list_demo():
    fruits = ["apple", "banana", "cherry"]
    print(f"Fruits: {fruits}")
    fruits.append("orange")
    print(f"Updated List: {fruits}")

def dict_demo():
    student = {"name": "Ali", "age": 20, "course": "Computer Science"}
    print(f"Student Profile: {student}")
    print(f"Course: {student['course']}")

def main():
    print("Executing Assignment 1 Demo...")
    list_demo()
    dict_demo()
    print("Assignment 1 logic executed successfully.")

if __name__ == "__main__":
    main()
