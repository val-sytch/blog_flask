import os
from flask import request, flash
from blog_flask.blog.database.db import WorkWithDatabase
from blog_flask.blog.configurations.config import (STATIC_AUDIO_PATH, STATIC_IMAGES_PATH,
                                                   IMG_HEIGHT_REQUIR, IMG_WIDTH_REQUIR,
                                                   WATERMARK_OPACITY,WATERMARK_FILE,
                                                   SQL_QUERIES_PATH)
from blog_flask.blog.servises.img_resizer_and_watermark_add import img_resizer_and_watermark_add
from datetime import datetime
from werkzeug.utils import secure_filename


class AddEntryViewModel():

    def __init__(self,db = WorkWithDatabase):
        self.db = db()

    def add_entry_to_database(self):
        audiofile = request.files['audiofile']
        imagefile = request.files['imagefile']
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        audiofilename = 'empty'
        new_audiofilename = 'empty'
        new_imagefilename = 'empty'
        if audiofile:
            audiofilename = secure_filename(audiofile.filename)
            new_audiofilename = 'audio' + timestamp + '.' + audiofilename.rsplit('.',1)[1]
            audiofile.save(os.path.join(STATIC_AUDIO_PATH,new_audiofilename))
        if imagefile:
            imagefile_edited = img_resizer_and_watermark_add(imagefile, IMG_WIDTH_REQUIR, IMG_HEIGHT_REQUIR,
                                                             WATERMARK_FILE, WATERMARK_OPACITY)
            new_imagefilename = 'image' + timestamp + '.png'
            imagefile_edited.save(os.path.join(STATIC_IMAGES_PATH,new_imagefilename),'PNG')
        query_path = os.path.join(SQL_QUERIES_PATH, 'add_entry_to_database_query.sql')
        query = open(query_path, mode='r').read()
        self.db.execute_post_query(query,[request.form['title'], request.form['content'], audiofilename,
                                          new_audiofilename, new_imagefilename])
        self.db.close_connection()
        return flash('New post was successfully posted')
