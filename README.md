# djangoEcommerce
A django ecommerce app



# problem 1
I have an error I don't know how to fix.  When I try to load the project I get this message.
`  File "c:\users\g\appdata\local\programs\python\python36-32\Lib\nturl2path.py", line 48, in pathname2url
    if not ':' in p:
TypeError: a bytes-like object is required, not 'str'`
![screenshot_3](https://user-images.githubusercontent.com/21030885/44830128-25bdd780-ac5b-11e8-98f1-89b86db83833.jpg)


# problem 2
It has one problem in that when you register and click Place Order it does not render the success page located in myshop\orders\templates\orders\order.

#steps to start the app
1. In the folder myshop use the command `python manage.py makemigrations`.
2. Then use the command `python manage.py migrate`
3. Finally `python manage.py runserver`.

If you do not have Django 1.8 you might need to create a virtual environment that so you can download the necessary packages.

![screenshot_9](https://user-images.githubusercontent.com/21030885/44479964-046a5380-a67d-11e8-97ad-e32dcdc33324.jpg)
