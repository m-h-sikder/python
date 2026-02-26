"""
Strings Practice Module
Author: Mohammad Monir Hossen Sikder
Level: Beginner – Pattern-first, mini-tests included
"""

def demo_string_operations(name: str):
    """
    Demonstrates string methods:
    - upper, lower
    - find
    - replace
    - membership
    """
    print("Original string:", name)
    print("Uppercase:", name.upper())
    print("Lowercase:", name.lower())
    print("Find 'on':", name.find('on'))
    print("Replace 'on' with 'ON':", name.replace('on', 'ON'))
    print("Lower + Replace chaining:", name.lower().replace('on', 'ON'))
    print("'Monir' in string?", 'Monir' in name)


# ===== Mini-Tests =====

def test_normal_cases():
    """Normal cases for basic string operations"""
    assert 'Mohammad'.upper() == 'MOHAMMAD'
    assert 'on' in 'Monir' == False
    print("Normal cases passed ✅")


def test_edge_cases():
    """Edge cases like empty string"""
    assert ''.replace('a','b') == ''
    assert ''.upper() == ''
    assert 'x' in '' == False
    print("Edge cases passed ✅")


def test_broken_inputs():
    """Broken / unexpected inputs, handled safely"""
    try:
        'hello'.replace(5, 'x')  # wrong type
    except TypeError:
        pass

    try:
        'hello'.find(None)       # invalid argument
    except TypeError:
        pass

    print("Broken input tests passed ✅")


# ===== Main Execution =====
if __name__ == "__main__":
    my_name = 'Mohammad Monir Hossen Sikder'
    demo_string_operations(my_name)
    
    # Run mini-tests
    test_normal_cases()
    test_edge_cases()
    test_broken_inputs()