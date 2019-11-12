
#-------------------------------------------------------------------------------

import sys
import inspect
import os

import file_utils as fu
reload (fu)

def main():
    test_funcs = get_test_functions()
    for test_func in test_funcs:
        test_func()

# Add import statement for the module under test as follows:
# import module_under_test as alias

# For example:
# import world_pop_explorer as wpe
# reload(wpe)



def test_get_file_content_file_exists():
    """Check the content of a file"""

    script_folder = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(script_folder, "data", "demo.txt")

    expected='Twas brillig, and the slithy toves.'
    actual = fu.get_file_content(file_name)
    print_test_results(test_get_file_content_file_exists, expected, actual)


def test_get_file_content_file_does_not_exist():
    """Check the content of a file"""
    script_folder = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(script_folder, "data", "missing_demo.txt")

    expected='{} does not exist'.format(file_name)
    actual = fu.get_file_content(file_name)
    print_test_results(test_get_file_content_file_does_not_exist, expected, actual)



def test_write_to_file():
    """"""
    script_folder = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(script_folder, "data", "TestFile.txt")



# Copy/paste/change the test template below to create new test functions, where:
#    - the test function name must begin with the word "test"
#    - Docstring contains description of the test being made
#    - expected = Expected result from calling the function
#    - actual = Actual result from calling the function
#    - func = Function being tested (the actual function, not the name)"""
#


#def template_for_test_functions():
    #"""Docstring"""
    #expected = ""
    #actual = ""
    #print_test_results(func, desc, expected, actual)



# ------------------------------------------------------------------------------

# Create test functions here using the template_for_test_functions above.
# The name of the test functions needs to begin with "test"


#def test_function():
    #"""Docstring"""
    #expected = "x"
    #actual = ""
    #print_test_results(test_function, expected, actual)



# ------------------------------------------------------------------------------
# Test template helper functions.  Code in this section should not need to
# modified.
#
def get_test_functions():
    """Returns a list of functions that begin with the word test in the order
       they appear in this file."""

    test_funcs = [obj for name,obj in inspect.getmembers(sys.modules[__name__])
                     if (inspect.isfunction(obj) and name.startswith('test'))]
    src = inspect.getsource(sys.modules[__name__])
    lines = src.split('\n')

    # Create a dictionary with key=function name and value is 0-based order
    # in the module
    ordered_func_names = dict()
    ordered_funcs = list()
    func_index = 0
    for line in lines:
        if line.find("def test") == 0:
            func_name = line.split("(")[0].split()[1]
            ordered_func_names[func_name] = func_index
            # Create an empty list with sampe number of elements as test
            # functions
            ordered_funcs.append('')
            func_index += 1
    for test_func in test_funcs:
        index = ordered_func_names[test_func.__name__]
        ordered_funcs[index] = test_func
    return ordered_funcs

def print_test_results(func_tested, expected, actual):
    """func_tested is the function being tested
       desc = Test description
       expected = Expected result of test
       actual = Actual result of test """

    if not callable(func_tested):
        raise Exception("{} is not a function".format(func_tested))

    func_name = func_tested.__name__
    desc = func_tested.__doc__

    if expected == actual:
        print "PASSED: {}".format(func_name)
    else:
        print "FAILED: {}".format(func_name)
        print "Expect: {}".format(expected)
        print "Actual: {}".format(actual)
        print "Desc:   {}".format(desc)
    print ""

if __name__ == '__main__':
    main()
