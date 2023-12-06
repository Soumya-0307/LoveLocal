easy:

    Given an integer numRows, return the first numRows of Pascal's triangle.
    In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
        Example 1:
        Input: numRows = 5
        Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

medium:

    Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
    Example 1:
    Input: nums = [3,2,3]
    Output: [3]

hard:

    Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
    Output: [3,3,5,5,6,7]
    Explanation: 
    Window position                Max
    ---------------               -----
    [1  3  -1] -3  5  3  6  7       3
    1 [3  -1  -3] 5  3  6  7       3
    1  3 [-1  -3  5] 3  6  7       5
    1  3  -1 [-3  5  3] 6  7       5
    1  3  -1  -3 [5  3  6] 7       6
    1  3  -1  -3  5 [3  6  7]      7