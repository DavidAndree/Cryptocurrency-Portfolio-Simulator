# Assignment 5 - Extra Credit - Creating an AdminLTE2 Site

## Author

David Alvarado

## Description

Create a Django Web Application that uses the django-adminlte2-pdq package.

There is no specific problem to solve for this assignment. In short, I want you create some sort of web application using all the knowledge you have gained thus far this semester coupled with the django-adminlte2-pdq package. It can not be the same as any of the projects that we have done for in-class work or assignments. It needs to be an original idea.

There is no specific requirement for models aside from the following. Users should be included and attached to at least one of your models as a foreign key. Non-user models can be anything you want so long as they are not models from any of the in-classes or assignments that we have done this semester. If you have a really good idea, but it requires a similar model to what we have used in the past, talk to me. I may be flexible so long as the entire thing is a good original idea.

Users should be able to sign up / login / out and do password resetting. Many of the templates for this are already done for you. However, the functionality should still work correctly. So, you may need to verify / implement the parts that are not already done for you.

Users should not be able to do anything in the site unless they are logged in. (Aside from signup / login / password reset)

Users that have Staff or Superuser status should be able to see the admin page links in the sidebar regardless of which page they are on once logged in.

Tests for the site should be similar to the ones we have written in-class thus far. At this point you should know what is a sufficient amount of testing. I am expecting that all views and models will be properly tested. And in case you aren't sure, there is no need to test any admin views.

Ensure that you have a `requirements.txt` file with your required packages. I will not grade the assignment if I can't restore the packages easily!

In general, the program should allow the following functionality:

1.  At least 2 models in addition to the User model.
2.  Users must be connected to at least one of the other models as a Foreign Key.
3.  All models, including the User model, must be utilized in the site somehow.
4.  CRUD pages for at least one of the non-user models.
5.  Sidebar menu entries that make sense for your application and its models.
6.  Users must be logged in to do anything in the site.
7.  Users with staff or superuser status can see admin links in the sidebar regardless of what page they are on.
8.  Automated Tests to verify everything.
9. Ensure `requirements.txt` is included in your project.

Documentation should include the following for this, and all future assignments:
* Comments at the top of each source code file that you add or edit with:
  * Your Name
  * Class
  * Date
* A comment after the definition of each method describing what it does. Use the """ (triple quote) doc string method for the comment.
* Comments in the rest of the code where it isn't obvious what is going on. (I prefer above the line comments vs at the end of the line because who likes to horizontally scroll, but either will work)

### Database Requirements
There is no specific requirement for models aside from the following. Users should be included and attached to at least one of your models as a foreign key. Other models can be anything you want so long as they are not models from any of the in-classes or assignments that we have done this semester. If you have a really good idea, but it requires a similar model to what we have used in the past, talk to me. I may be flexible so long as the entire thing is an original idea.

### Screenshots
Obviously I can't provide any screenshots as the entire concept for this application is left up to you.

### Notes
Once you have added any additional packages that you need to your project. Be sure to run pip freeze to dump the package information to requirements.txt

  pip freeze > requirements.txt

Remember that you can see all of the documentation for the django-adminlte2-pdq package here:

https://django-adminlte2-pdq.readthedocs.io/en/latest/

You can also view general adminlte2 CSS documentation here:

https://adminlte.io/themes/AdminLTE/documentation/index.html

1.  At least 2 models in addition to the User model.
2.  Users must be connected to at least one of the other models as a Foreign Key.
3.  All models, including the User model, must be utilized in the site somehow.
4.  CRUD pages for at least one of the non-user models.
5.  Sidebar menu entries that make sense for your application and its models.
6.  Users must be logged in to do anything in the site.
7.  Users with staff or superuser status can see admin links in the sidebar regardless of what page they are on.
8.  Automated Tests to verify everything.

## Grading
| Feature                                     | Points |
|---------------------------------------------|--------|
| User model and at least 2 more models       |  5     |
| User connected to one other model a FK      |  5     |
| All models are used in the application      |  5     |
| CRUD pages for at least one non-user model  |  5     |
| Sidebar menu entries for you application    |  5     |
| Users must be logged into use the site      |  5     |
| Staff / Superuser users can see admin links |  5     |
| Automated Tests                             |  5     |
| Documentation                               |  5     |
| Readme                                      |  5     |
| **Total**                                   | **50** |

## Outside Resources Used

This is the website where I got Coingecko's api    (Its' very well documented)
  https://docs.coingecko.com/reference/simple-price
 
## Known Problems, Issues, And/Or Errors in the Program

I'm not aware of any problems with this program.