from basic_function import read_back

def test_read_back(): 
    formatted_name = read_back("Austin", "Andrews")
    assert formatted_name == "Austin Andrews"

def test_failing():
    formatted_name = read_back("Austin", "Samuel", "Andrews")
    assert formatted_name == "Austin Samuel Andrews"