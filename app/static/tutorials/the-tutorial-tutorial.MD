The Tutorial Tutorial
=====================
So my first tutorial is a bit meta. I will show you how I coded the file upload and Markdown display functionality that 
allowed me to easily add this very tutorial that I wrote in Markdown.

Let's Get Started
-----------------
###There are several things needed in order to be able to upload files securely.
* First, I needed some kind of login functionality. This will be taken care of by Flask-Login.
* Second, I needed an admin page that would give my login access to the upload features while not allowing any regular
  user to reach my admin page. This will be taken care of by Flask-Admin.