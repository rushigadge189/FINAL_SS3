class Test_014_02() :

    def test_014_02_substraction(self):
        a=10 ;
        b=5 ;
        sub=a-b ;
        if (sub==5) :
            print( '\n------------------SUBSTRACTION IS SUCCESSFULL---------------' ) ;
            print('\nRESULT=',sub) ;
            assert True ;
        else :
            print ('\n---------------SORRY, INAVLID OPERATION--------------') ;
            assert False ;
