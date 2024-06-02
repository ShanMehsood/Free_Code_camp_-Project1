# main.py

from mean_var_std import calculate

# Manual test
print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))

# Running unit tests
if __name__ == "__main__":
    import unittest
    import test_module
    unittest.main(module=test_module)
