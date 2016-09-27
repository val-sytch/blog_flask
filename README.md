# blog_flask

## Blog on Flask

Simple blog on Flask. Supports posts with possibility to add audio and image(image
is resized and watermapk putted).  Fields title and text are required, image and audio
optional.  SQLite database is used.

By default package includes watermark picture. Afterr installation you could change
watermark on your own image .png.

When you will first launch an app , database will be created automatically

### **To launch app on localhost:**

1. Create virtualenv and activate it (recommended but not required)
2. Clone blog_flask repository inside
3. python setup.py install
4. python run.py

App was tested. Tests included and could be launched with fabric tool.
Also you could  launch coverage and pylint reports.
Look into fabfile.py for details.

To make a source distribution: 'python setup.py sdist'  or  with fabric 'fab make_targz'
