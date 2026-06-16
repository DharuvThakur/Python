from flask import Flask,render_template,request
import os
web=Flask(__name__)
picfolder= os.path.join('static')
web.config['Uploded_folder']=picfolder
@web.route('/')

def first():
    pic=os.path.join(web.config['Uploded_folder'],'waterfall.jpg')
    return render_template('index.html',user_image=pic)

@web.route('/second')

def second():
    return render_template('second.html')




if __name__ =='__main__':
  web.run(debug=True)
