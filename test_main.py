from main import *


# Step Nine of lab inputting more test cases
## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3*3
    assert quadratic_multiply(BinaryNumber(8), BinaryNumber(4)) == 8*4
    assert quadratic_multiply(BinaryNumber(1), BinaryNumber(1)) == 1
    assert quadratic_multiply(BinaryNumber(1), BinaryNumber(0)) == 0
    assert quadratic_multiply(BinaryNumber(1000), BinaryNumber(1500)) == 1000*1500

    # Step Eight Testing
    print(test_quadratic_multiply(BinaryNumber(1), BinaryNumber(1), quadratic_multiply))
    print(test_quadratic_multiply(BinaryNumber(10), BinaryNumber(10), quadratic_multiply))
    print(test_quadratic_multiply(BinaryNumber(100), BinaryNumber(100), quadratic_multiply))
    print(test_quadratic_multiply(BinaryNumber(1000), BinaryNumber(1000), quadratic_multiply))

    # 0.0
    #  0.029802322387695312
    # 0.06103515625
    # 0.18405914306640625
    # These are the results from those tests above!