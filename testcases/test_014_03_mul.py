class Test_014_03():

    def test_014_03_multiplication(self):

        a=10;
        b=5;
        mul=a*b;
        if (mul==50) :
            print ('\n------------------MULTIPLICATION IS SUCCESSFUL-----------------'  ) ;
            print ( '\nRESULT=', mul ) ;
            assert True ;
        else:
            print( '\n--------------SORRY, INVALID OPERAION--------------' ) ;
            assert False ;
            