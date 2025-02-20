"""
CMPS 2200  Recitation 3.
See recitation-03.md for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y

def quadratic_multiply(x, y):
    # this just converts the result from a BinaryNumber to a regular int
    return _quadratic_multiply(x,y).decimal_val

def _quadratic_multiply(x, y):
    # Step One of Lab, Obtaining xvec and yvec which are the binary_vec values of x and y
    xvec = x.binary_vec
    yvec = y.binary_vec

    # Step Two of Lab, Pad xvec and yvec so they're the same length
    xvec, yvec = pad(xvec, yvec)
    
    # Step Three of Lab, Base Case
    if x.decimal_val <= 1 and y.decimal_val <= 1:
        return BinaryNumber(x.decimal_val * y.decimal_val)
    
    # Step Four of lab, splitting xvec and yvec into xleft, xright, yleft
    else:
        x_left, x_right = split_number(xvec)
        y_left, y_right = split_number(yvec)
        
        # Steps Five and Six of the Lab, applying the formula 2^n(Xl * Yl) + 2^(n/2)(Xl*YR + XR * YL) + (XR * YR)
        # Using quadratic multiply and bit shift respectively, also applying .decimal_val and BinaryNumber where applicable
        left_value = bit_shift(_quadratic_multiply(x_left, y_left), len(xvec)).decimal_val
        middle_value = bit_shift(BinaryNumber(_quadratic_multiply(x_left, y_right).decimal_val + _quadratic_multiply(x_right, y_left).decimal_val), len(xvec)//2).decimal_val
        right_value = _quadratic_multiply(x_right, y_right).decimal_val

        # Step Seven of the Lab, adding three the values to get the answer
        return BinaryNumber(left_value + middle_value + right_value)


    
# Step Eight of the Lab, implementing this function to obtain the running time
def test_quadratic_multiply(x, y, f):
    start = time.time()
    f(x, y)
    return (time.time() - start)*1000
    

