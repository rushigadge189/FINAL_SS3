class Test_014_04() :

    def test_014_04_division(self):

        a=10;
        b=5;
        div=a/b ;
        if (div==2) :
            print ( '\n-------------DIVISION IS SUCCESSFUL-------------' ) ;
            print ( '\nRESULT=', div) ;
            assert True ;
        else:
            print ( '\n--------------SORRY, INVALID PERATION--------------' ) ;
            assert False ;


