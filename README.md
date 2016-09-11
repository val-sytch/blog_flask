# blog_flask

##Blog on Flask

Simple blog on Flask. Supports posts with possibility to add audio and image(image
is resized and watermapk putted).

By default package includes database with two posts as example(with audio and image)
and default watermark picture. If you want to have empty database, you will need to
delete files:

1. blog_flask/blog/database/database.db
2. blog_flask/blog/static/audio/*
3. blog_flask/blog/static/images/*
(do not delete watermark file from watermark folder)

after "5.flask run" new database will be created automatically

**Instalation:**

1. Create virtualenv and activate it (recommended but not required)
2. Clone blog_flask repository inside
3. python setup.py install
4. export FLASK_APP=run.py
5. flask run

