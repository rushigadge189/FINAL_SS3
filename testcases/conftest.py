import time

import pytest
from selenium import webdriver

def pytest_addoption(parser) :
    parser.addoption("--browser") ;

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser") ;


@pytest.fixture
def setup(browser):

    if ( browser == 'chrome' ):

        driver=webdriver.Chrome();
        print("--------------------RUNNING IN CHROME BROWSER-------------------");

    elif ( browser == 'edge') :
        driver=webdriver.Edge();
        print("-----------------RUNNING IN EDGE BROWSER--------------------") ;

    else:
        chrome_options=webdriver.ChromeOptions();
        chrome_options.add_argument("headless") ;
        driver=webdriver.Chrome(options=chrome_options) ;
        print("---------------RUNNING IN HEADLESS MODE---------------") ;

    time.sleep(1) ;

    driver.maximize_window();
    time.sleep(1) ;

    driver.implicitly_wait(10) ;

    return driver ;


def pytest_metadata(metadata):
    metadata['CLASS'] = 'CREDENCE' ;
    metadata[ 'ENGINEER' ] = 'RUSHIKESH_GADGE_PATIL' ;
    metadata[ 'URL' ] = 'www.google.com' ;
    metadata[ 'CLIENT' ] = "M/S SHIVSADHANA FOUNDATIONS"
    metadata.pop('Platform', None);
    metadata.pop( 'Python', None ) ;

