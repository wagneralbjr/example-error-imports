# i know that this is not the right syntax, but i would like to replicate
# something like this.


#from main1 import a_function_same_file

# i know that if this was a module i would import like this
from pipelines.pipeline1.etls.somezone.main1 import a_function_same_file


def  test_a_function():

    assert a_function_same_file(3,2) == 6