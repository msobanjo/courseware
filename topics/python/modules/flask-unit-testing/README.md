# Flask Unit Testing 

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Testing Layout](#testing-layout)
- [Creating, Setting up and Tearing down environments](#creating-setting-up-and-tearing-down-environments)
- [Adding the First Test](#adding-the-first-test)

<!--TOC_END-->
## Overview
In this tutorial we will set up a flask application for unit testing and then add one unit test.
We will also save a unique report for each time we carry out the test.

## Tutorial

### Prerequisites
You will need the example flask blog app you have created in your lessons.
It must be working with a database. 

### Testing Layout
For Pytest to work we need an `__init__.py` file inside a `tests` directory along with out testing files.
Also add a `test_results` directory for later:
```text
.
├──application
├──tests
|  ├──__init__.py
|  └──test_back_end.py
├──app.py
└──test_results
```

You will also have to do the appropriate install for pytest.
While also recording this in your `requirements.txt`
```bash
pip3 install pytest
pip3 install pytest-cov
```

### Creating, Setting up and Tearing down environments
To run tests for a flask app we need to change the configurations of the app to not interfer with the app in production by using a test database.
You will need to edit this configuration, to interact with your database,when writing the functions.

We also need to set up an environment for the app to run in to perform tests on. This environment will need to be set up and torn down for every tests.

We group these functions together in a class so they can be called upon for every test in another class.

Write these functions in your test_back_end.py
```python
import unittest

from flask import abort, url_for
from flask_testing import TestCase

from application import app, db
from application.models import Users, Posts
class TestBase(TestCase):

    def create_app(self):

        # pass in test configurations
        config_name = 'testing'
        app.config.update(
            SQLALCHEMY_DATABASE_URI='mysql+pymysql://(YOUR TEST DB INFO)'        )
        return app

    def setUp(self):
        """
        Will be called before every test
        """

        db.session.commit()
        db.drop_all()
        db.create_all()

        # create test admin user
        admin = Users(first_name="admin", last_name="admin", email="admin@admin.com", password="admin2016")

        # create test non-admin user
        employee = Users(first_name="test", last_name="user", email="test@user.com", password="test2016")

        # save users to database
        db.session.add(admin)
        db.session.add(employee)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()
```

### Adding the First Test
Now we can add our first unit test. It will be a simple test of the status code of the home page. 

We will add a new class that will contain all our tests. This class be passed our TestBase class that contains our Create_App, SetUp and TearDown functions so these will be ran for every test.

```python
class TestViews(TestBase):

    def test_homepage_view(self):
        """
        Test that homepage is accessible without login
        """
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
```
Now if we run this command in the root of your project, the test will run
```bash
pytest
```
We need to keep track of our tests and how well they cover every eventuality with our app.

We will do this using pytest coverage.

Instead of using the pytest command above we will use
```bash
pytest --cov .
```
This will print a report with your coverage.

We will then make pytest save this report in a html file
```bash
pytest --cov . --cov-report html
```
This will create a directory with lots of files.
```text
.
├──application
├──app.py
├──tests
|  ├──__init__.py
|  └──test_back_end.py
└──htmlcov
   ├──index.html
   ├──jquery.isonscreen.js 
   ├──keybd_closed.png           
   ├──status.json
   └──...
```
We are only interested in the `index.html` file. 

Copy and paste this html file into a local text editor and save as a html file. 

Then open the file and you will see its contents.

To save space after many tests, we will move the index.html and rename it so that each set of test results has a unique name.

Then we will delete the htmlcov directory
```
mkdir test_results
mv ./htmlcov/index.html ./test_results/test-at-$(date "+%h-%m")-on-$(date "+%y-%H:%M").html
rm -rf htmlcov
```

Now set up your project for unit testing and prepare your app to be tested several times with reports.
