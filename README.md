# Cryptocurrency Portfolio & Alerts Simulator

## Author

David Alvarado

## Description

A Django Web Application that uses the django-adminlte2-pdq package to track real-time cryptocurrencies prices and setup alerts.

Using adminlte2-pdq package web application coupled with the django-adminlte2-pdq package. The original idea was created by me: I always wanted to see the revenue potential with a specific cryptocurrency-- without using real money.

# Details 

Users should not be able to do anything in the site unless they are logged in. (Aside from signup / login / password reset)

Users that have Staff or Superuser status should be able to see the admin page links in the sidebar regardless of which page they are on once logged in.

All views and models are properly tested.

Ensure that you have `requirements.txt` downloaded to run the app.

In general, the program allows the following functionality's:

1.  Models in addition to the User model.
2.  Users are connected to at least one of the other models as a Foreign Key.
3.  All models, including the User model, are utilizing the site.
4.  CRUD pages for at least one of the non-user models.
5.  Sidebar menu entries.
6.  Users must be logged in to do anything in the site.
7.  Users with staff or superuser status can see admin links in the sidebar regardless of what page they are on.
8.  Automated Tests to verify everything.


### Database 
Users are included and attached to the models as a foreign key.


### Notes
Once you have added any additional packages that you need to your project. Be sure to run pip freeze to dump the package information to requirements.txt

  pip freeze > requirements.txt

Remember that you can see all of the documentation for the django-adminlte2-pdq package here:

https://django-adminlte2-pdq.readthedocs.io/en/latest/

You can also view general adminlte2 CSS documentation here:

https://adminlte.io/themes/AdminLTE/documentation/index.html


## Features Recap
Features 
---------------------------------------------
 User model and 3 more models      
 User connected to one other model a FK      
 All models are used in the application      
 CRUD pages for non-user model  
 Sidebar menu entries for the application    
 Users must be logged into use the site      
 Staff / Superuser users can see admin links 
 Automated Tests                             
 Well-Documented                                                                     

## Outside Resources Used

Website link for Coingecko's api.  
  https://docs.coingecko.com/reference/simple-price