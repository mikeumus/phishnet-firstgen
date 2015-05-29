#Scrapetank

A scrapy spider for getting all the offline valid scripts from PhishTank.com

Run the spider: `$ scrapy crawl offline_phishies -a target_id=7`
See Spider-Arugements-Key.md for `target_id`

![Creative Commons license image](http://creativecommons.org/images/public/somerights20.png)
All content from [PhishTank.com](https://www.phishtank.com/) is under a [Creative Commons Attribution-ShareAlike 2.5 License](http://creativecommons.org/licenses/by-sa/2.5/).

_ _ _


### Project Notes

###### Deleting Tables
In `./manage.py shell`
```
In [2]: from pishing.models import Phish                                                               
                                                                                                       
In [3]: Phish.objects.all().count()                                                                    
Out[3]: 4821                                                                                           
                                                                                                       
In [4]: Phish.objects.all().delete()                                                                   
                                                                                                       
In [5]: Phish.objects.all().count()                                                                    
Out[5]: 0   
```

to clear out an application is as simple as writing:
`./manage.py sqlclear app_name | ./manage.py dbshell`
then in order to rebuild your tables just type:
`./manage.py syncdb`

##### Notes

###### Saving Images in Scrapy
http://doc.scrapy.org/en/latest/topics/images.html

###### Don't forget to install service_indentity (for C9)!
https://service-identity.readthedocs.org/en/14.0.0/installation.html

###### Scrapy formrequest
http://stackoverflow.com/questions/11213467/cant-get-through-a-form-with-scrapy

###### Code modeled after 
- http://stackoverflow.com/questions/5851213/crawling-with-an-authenticated-session-in-scrapy?answertab=votes#tab-top

Other references
- https://scrapy.readthedocs.org/en/latest/topics/request-response.html?highlight=login#using-formrequest-from-response-to-simulate-a-user-login
-- http://stackoverflow.com/questions/5850755/using-scrapy-with-authenticated-logged-in-user-session
-- http://stackoverflow.com/questions/17403596/python-scrapy-cant-post-information-to-forms


_ _ _ 



### Cloud9 ReadMe 

     ,-----.,--.                  ,--. ,---.   ,--.,------.  ,------.
    '  .--./|  | ,---. ,--.,--. ,-|  || o   \  |  ||  .-.  \ |  .---'
    |  |    |  || .-. ||  ||  |' .-. |`..'  |  |  ||  |  \  :|  `--, 
    '  '--'\|  |' '-' ''  ''  '\ `-' | .'  /   |  ||  '--'  /|  `---.
     `-----'`--' `---'  `----'  `---'  `--'    `--'`-------' `------'
    ----------------------------------------------------------------- 


Welcome to your Django project on Cloud9 IDE!

Your Django project is already fully setup. Just click the "Run" button to start
the application. On first run you will be asked to create an admin user. You can
access your application from 'https://scrapy-phishtank-mikeumus.c9.io/' and the admin page from 
'https://scrapy-phishtank-mikeumus.c9.io/admin'.

## Starting from the Terminal

In case you want to run your Django application from the terminal just run:

1) Run syncdb command to sync models to database and create Django's default superuser and auth system

    $ python manage.py syncdb

2) Run Django

    $ python manage.py runserver $IP:$PORT
    
## Support & Documentation

Django docs can be found at https://www.djangoproject.com/

You may also want to follow the Django tutorial to create your first application:
https://docs.djangoproject.com/en/1.7/intro/tutorial01/

Visit http://docs.c9.io for support, or to learn more about using Cloud9 IDE.
To watch some training videos, visit http://www.youtube.com/user/c9ide