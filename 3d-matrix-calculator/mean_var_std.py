import numpy as np

def calculate(inputArray):
    """Reshapes a one dimensional NumPy array of size 9 into a 3x3 2D array and calculates the column-wise, row-wise and flattened: mean, variance, stanadard deviation, max, min and sum.
    Args:
        inputArray (np.array): 1D Numpy array of size 9
        
    Raises:
        ValueError: A ValueError is raised if the input array is not the size required

    Returns:
        Dictionary: An dictionary with the measure as the key and an array for each of the measures calculated as the value.
    """
    if inputArray.size != 9:
        raise ValueError("Input array must be of length 9")
    else:
        reshape_array = np.reshape(inputArray, (3, 3))
        return {
            'mean': [reshape_array.mean(axis=0).tolist(),
                     reshape_array.mean(axis=1).tolist(),
                     inputArray.mean(axis=0).tolist()],
            'variance': [reshape_array.var(axis=0).tolist(),
                         reshape_array.var(axis=1).tolist(),
                         inputArray.var().tolist()],
            'standard deviation': [reshape_array.std(axis=0).tolist(),
                                   reshape_array.std(axis=1).tolist(),
                                   inputArray.std().tolist()],
            'max': [reshape_array.max(axis=0).tolist(),
                    reshape_array.max(axis=1).tolist(),
                    inputArray.max().tolist()],
            'min': [reshape_array.min(axis=0).tolist(),
                    reshape_array.min(axis=1).tolist(),
                    inputArray.min().tolist()],
            'sum': [reshape_array.sum(axis=0).tolist(),
                    reshape_array.sum(axis=1).tolist(),
                    inputArray.sum().tolist()]
        }
    
inputArray = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
print(inputArray.size)
print(calculate(inputArray=inputArray))