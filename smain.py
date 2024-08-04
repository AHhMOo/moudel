import text_utils as tu

def main():
    test_string = "python programming"
    
    reversed_str = tu.reverse_string(test_string)
    capitalized_str = tu.capitalize_string(test_string)
    
    print(f"Original: {test_string}")
    print(f"Reversed: {reversed_str}")
    print(f"Capitalized: {capitalized_str}")

main()
