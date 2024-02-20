import pytest


class Test_015_markers():

    @pytest.mark.skip
    def test_001_add(self):
        a=20 ;
        b=10 ;
        add=a+b ;
        if ( add==30 )  :
            print ('\n----------------ADDITION IS SUCCESSFUL------------------') ;
            print ( '\nRESULT=' ,add ) ;
            assert True ;
        else:
            print ( '\n--------------SORRY, INVALID OPEARTION--------------' ) ;
            assert False ;

    @pytest.mark.xfail
    def test_002_sub(self):
        a=20 ;
        b=10 ;
        sub=a-b ;
        if ( sub==10 ) :
            print ( '\n---------------SUBSTRACTION IS SUCCESSFUL-------------' ) ;
            print ( '\nRESULT=', sub ) ;
            assert True ;
        else:
            print( '\n----------------SORRY, INVALID OPERATION--------------' ) ;
            assert False ;

    def test_003_mul(self):
        a=20 ;
        b=10 ;
        mul=a*b;
        if ( mul==200 ) :
            print ( '\n--------------MULTIPLICATION IS SUCCESSFUL--------------' ) ;
            print ( '\nRESULT=', mul ) ;
            assert True ;
        else:
            print( '\n--------------SORRY, INVALID OPERATION--------------' )
            assert False ;

    @pytest.mark.skipif
    def test_004_div(self):
        a=20 ;
        b=10 ;
        div=a//b ;
        if ( div==2 ) :
            print ( '\n---------------DIVISION IS SUCCESSFUL------------' ) ;
            print ( '\n RESULT=', div ) ;
            assert True ;
        else:
            print ( '\n--------------SORRY, INVALID OPERATION-------------' ) ;
            assert False ;
