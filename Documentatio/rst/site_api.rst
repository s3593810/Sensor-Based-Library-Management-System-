site\_api module
================
This site_api class inegrates the api with the site view
and helps geeting, posting and delating functions through api calls wiythin in 
the cloud thus acts as the client for the site.

Methods
-------

index()
    it srats up based on the index template.
    It starts as landing site with basic functional
    features in the site.

do_admin_login()
    Admin login functionalities through api get and post requests
    as user types in user name and password thus it posts the request to 
    the api for login and the api checks the user name and password with the 
    existing database thus it gets api results.
    
dashboard()
    This method opens app the dashbord site view based on rendering template
    dashboard.html.
report()
    This method helps getting the response ass all the books in the database 
    as rendered site as report.html.
addmenu()
    Allows user to type in book information through the site to add a book
    through the api calls to the cloud database.
delete()
    Using restful api calls this method allows user to delate 
    a book from cloud database based on users action on the site. 
    
.. automodule:: site_api
   :members:
   :undoc-members:
   :show-inheritance:
