import numpy as np

def input_matrix(rows, cols, name):
    print(f"\nEnter elements of Matrix {name}:")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        matrix.append(row)
    return np.array(matrix)

def main():
    print("=== Matrix Operations Tool ===")

    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    A = input_matrix(rows, cols, "A")
    B = input_matrix(rows, cols, "B")

    while True:
        print("""
Choose Operation:
1. Addition
2. Subtraction
3. Multiplication
4. Transpose
5. Determinant
6. Exit
""")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            print("Result (A + B):")
            print(A + B)

        elif choice == '2':
            print("Result (A - B):")
            print(A - B)

        elif choice == '3':
            if cols == rows:
                print("Result (A x B):")
                print(np.dot(A, B))
            else:
                print("Matrix multiplication not possible.")

        elif choice == '4':
            print("Transpose of Matrix A:")
            print(A.T)

        elif choice == '5':
            if rows == cols:
                print("Determinant of Matrix A:")
                print(np.linalg.det(A))
            else:
                print("Determinant only possible for square matrix.")

        elif choice == '6':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

