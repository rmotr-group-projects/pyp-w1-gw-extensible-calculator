# -*- coding: utf-8 -*-
import unittest

from calculator.operations import *
from calculator.exceptions import *


class TestCalculatorOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1), 1)
        self.assertEqual(add(1, 2, 3, 4), 10)
        self.assertEqual(add(1, 2, 3, 4, 5), 15)
        self.assertEqual(add(10, -2), 8)
        self.assertEqual(add(10, 2.5), 12.5)

    def test_subtract(self):
        self.assertEqual(subtract(1), 1)
        self.assertEqual(subtract(10, 1, 3, 3), 3)
        self.assertEqual(subtract(10, 5.5), 4.5)
        self.assertEqual(subtract(10, -2), 12)
        self.assertEqual(subtract(10, 2.5), 7.5)

    def test_multiply(self):
        self.assertEqual(multiply(1), 1)
        self.assertEqual(multiply(2, 3, 5), 30)
        self.assertEqual(multiply(10, 2.5), 25.0)
        self.assertEqual(multiply(10, -2), -20)

    def test_divide(self):
        self.assertEqual(divide(1), 1)
        self.assertEqual(divide(4, 2), 2)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(10, -2), -5)
        self.assertEqual(divide(12, 2, 3), 2)

    # def test_plot(self):
    #     x = symbols('x')
    #     plot_test = (plot(-x**2, -2, 2))
    #     self.assertEqual(plot_test, 
    #     """
    #     -0.0013 |                       .....  ......                    
    #             |                    ...             ..                  
    #             |                  ..                  ..                
    #             |                ..                      ..              
    #             |              ..                          ..            
    #             |             /                              \           
    #             |            /                                \          
    #             |           /                                  \         
    #     -2.0006 | ---------/------------------------------------\--------
    #             |        ..                                      ..      
    #             |                                                  .     
    #             |       .                                                
    #             |      /                                            .    
    #             |     /                                              \   
    #             |    /                                                \  
    #             |   /                                                  \ 
    #             |  /                                                    \
    #          -4 | /                                                      
    #               -2                     0                          2
    #     """)
    # attempted plot test using textplot and the README example
    # unknown variables: output width, height, etc.
    
    
    
    
    # x=5
    # (plot(-x**2, -2, 2))
    
    # x=2
    # plot(-2**2, -2, 2)
    # plot(-4, -2, 2)
    
    #    -0 |             ... ...
        #   |           ..       ..
        #   |          /           \
        #   |         /             \
        #   |        /               \
        #   |       /                 \
        #   |      .                   .
    #    -2 | ------------------------------
        #   |     .                     .
        #   |    .                       .
        #   |
        #   |   .                         .
        #   |
        #   |  .                           .
       # -4 | /
        #      -2         0              2
