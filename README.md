# CS517_Approx_Derivative
This program calculates the approximate derivative of f(x) (sin(x)) using the finite difference formula, the actual derivative (cos(x)), and the absolute error between the two for x = 1 and h: 2^-1 -> 2^-30.

- Run `python3 approx_derivative.py`

The graph of h vs absolute error values can be found in h_vs_abs_error.png, or can be created by uncommenting `plotResults(xValues, yValues)`.

The end result will be in the form:
|  h   |     x      | Approx. f’(x) | Known f’(x) | Abs. Error |
|:----:|:----------:|:-------------:|:-----------:|:----------:|
|2^-01 | 1.00000000 |    0.31204800 |  0.54030231 | 0.22825430 |
|2^-02 | 1.00000000 |    0.43005454 |  0.54030231 | 0.11024777 |
|2^-03 | 1.00000000 |    0.48637287 |  0.54030231 | 0.05392943 |
|2^-04 | 1.00000000 |    0.51366321 |  0.54030231 | 0.02663910 |
The minimum value for the magnitude of the error is 1.850815717229236e-09, √eps is 1.4901161193847656e-08, the difference between them is 1.305034547661842e-08.