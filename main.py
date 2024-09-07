def multiply_single_iteration(N, M):
    """Multiply N and M using a single iteration."""
    return N * M

def multiply_n_iterations(N, M):
    """Multiply N and M using N iterations (addition)."""
    result = 0
    for _ in range(N):
        result += M
        return result
    
# Codingal usage
if __name__ == "__main__":
    # Input values for N and M
    N = int(input("Enter the value of N: "))
    M = int(input("Enter the value of M: "))

    # Multiply using single iteration
    result_single = multiply_single_iteration(N, M)
    print(f"Result using single iteration: {result_single}")

    # Multiply using N iterations
    result_n_iterations = multiply_n_iterations(N, M)
    print(f"Result using N iterations: {result_n_iterations}")