Customizing the Django Authentication for Email
I encountered this in one of my projects where I needed the user to login via Email ID rather than Username. I thought I can use the Username field as Email ID by just changing the Label, but that was not enough.
So I found another solution customizing the django authentication to suite my needs. 

For this , I only needed to create a custom user model.
This was introduced in Django 1.5

Creating a new Custom User Model

The best way of creating a custom Django user model is to inherit from the AbstractBaseUser. AbstractBaseUser provides the core implementation of a User model, including hashed passwords and tokenized password resets.

The Default Django authentication used Username Field as a unique identifier.
We want Email ID for the same. 

Here we use USERNAME_FIELD="" .