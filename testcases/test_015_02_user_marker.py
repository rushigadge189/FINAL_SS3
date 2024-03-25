import pytest


class Test_015_02_user_defined_marker():

    @pytest.mark.customer

    def test_add_cust(self):
        print( "\nCustomer Added Successfully" ) ;

    @pytest.mark.customer
    def test_del_cust(self):
        print ( "\nCustomer Deleted Successfully" ) ;

    @pytest.mark.product
    def test_add_prod(self):
        print ( "\nProduct Added Successfully" ) ;

    @pytest.mark.product
    def test_del_prod(self):
        print ( "\nProduct Deleted Successfully" ) ;

    @pytest.mark.bill
    def test_add_bill(self):
        print ( "\nBill Added Successfully" ) ;

    @pytest.mark.bill
    @pytest.mark.regression
    def test_del_bill(self):
        print ( "\nBill Deleted Successfuly") ;

    @pytest.mark.patinet
    def test_add_patient(self):
        print ( "\nPatient Added Successfully" ) ;

    @pytest.mark.patient
    @pytest.mark.sanity
    @pytest.mark.re
    def test_del_patient(self):
        print ( "\nPatient Deleted Successfully" ) ;