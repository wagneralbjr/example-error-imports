
# in the spark operator, after i add pyfiles i can import functions 
# like this
# https://github.com/kubeflow/spark-operator
# https://github.com/kubeflow/spark-operator/blob/master/docs/api-docs.md#dependencies:w


from utils import some_adding_function
from utils import another_utils_func

def a_function_same_file(x,y):

    return x * y

def main():

    a = 1
    b = 2
    print(some_adding_function(a,b))
    print(a_function_same_file(x,y))
    return 

if __name__ == "__main__":
    main()