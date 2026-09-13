def print_matrix(A, b):
    """Display the augmented matrix."""

    for i in range(len(A)):
        row = ""

        for value in A[i]:
            row += f"{value:8.2f} "

        row += f"| {b[i]:8.2f}"

        print(row)

    print()


def gaussian_elimination(A, b):
    n = len(A)

    print("\nInitial matrix:")
    print_matrix(A, b)

    for i in range(n):

        max_row = i

        for k in range(i + 1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k

        if max_row != i:

            print(
                f"Operation: R{i + 1} <-> R{max_row + 1}"
            )

            A[i], A[max_row] = A[max_row], A[i]
            b[i], b[max_row] = b[max_row], b[i]

            print_matrix(A, b)

        if abs(A[i][i]) < 1e-12:
            raise ValueError(
                "The system cannot be solved with a unique solution."
            )

        pivot = A[i][i]

        if abs(pivot - 1) > 1e-12:

            print(
                f"Operation: R{i + 1} <- "
                f"R{i + 1} / {pivot:.2f}"
            )

            for j in range(n):
                A[i][j] /= pivot

            b[i] /= pivot

            print_matrix(A, b)

        for k in range(n):

            if k == i:
                continue

            factor = A[k][i]

            if abs(factor) < 1e-12:
                continue

            if factor >= 0:
                print(
                    f"Operation: R{k + 1} <- "
                    f"R{k + 1} - {factor:.2f}R{i + 1}"
                )
            else:
                print(
                    f"Operation: R{k + 1} <- "
                    f"R{k + 1} + {abs(factor):.2f}R{i + 1}"
                )

            for j in range(n):
                A[k][j] -= factor * A[i][j]

            b[k] -= factor * b[i]

            # Avoid -0.00
            for j in range(n):
                if abs(A[k][j]) < 1e-12:
                    A[k][j] = 0

            if abs(b[k]) < 1e-12:
                b[k] = 0

            print_matrix(A, b)

    return b


# ==================================
# INPUT
# ==================================

while True:

    try:
        n = int(input("Number of unknowns: "))

        if n <= 0:
            print("Error: enter a positive integer.")
            continue

        break

    except ValueError:
        print("Error: enter an integer.")


A = []
b = []

print("\nEnter the coefficients of each equation.")

for i in range(n):

    while True:

        try:

            values = input(
                f"Equation {i + 1} ({n} coefficients): "
            ).split()

            if len(values) != n:
                print(
                    f"Error: enter exactly {n} coefficients."
                )
                continue

            row = list(map(float, values))

            A.append(row)

            break

        except ValueError:
            print("Error: coefficients must be numbers.")


print("\nEnter the right-hand side values.")

for i in range(n):

    while True:

        try:

            value = float(input(f"b[{i + 1}] = "))

            b.append(value)

            break

        except ValueError:
            print("Error: enter a valid number.")


# ==================================
# SOLVE
# ==================================

try:

    solution = gaussian_elimination(A, b)

    print("\nFinal matrix:")
    print_matrix(A, solution)

    print("Solution:")

    for i, value in enumerate(solution):
        print(f"x{i + 1} = {value:.4f}")

except ValueError as error:

    print("\nError:", error)