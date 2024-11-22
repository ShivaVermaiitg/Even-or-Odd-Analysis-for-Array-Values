def even_odd(N, A):
    result = []
    
    for i in range(N):
        Value1 = 0
        Value2 = 0
        
        # Calculate Value1 and Value2 for the current index i
        for j in range(i):
            if A[j] < A[i]:
                Value1 += A[j]
            elif A[j] > A[i]:
                Value2 += 1
        
        # Calculate sum for the current index i
        sum_i = Value1 + (Value2 * A[i])
        
        # Check if sum_i is even or odd
        if sum_i % 2 == 0:
            result.append(1)
        else:
            result.append(0)
    
    return result

# Example usage
T = int(input("Enter number of test cases: "))
for _ in range(T):
    N = int(input("Enter size of array: "))
    A = list(map(int, input("Enter array elements: ").split()))
    print(even_odd(N, A))
