import app

def test_app_output():
    # This checks if the main function returns True
    assert app.main() == True
    print("Test Passed: App returned True.")

if __name__ == "__main__":
    test_app_output()
