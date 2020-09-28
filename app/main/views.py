from flask import Flask
from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required,current_user
from .forms import BlogForm,UpdateProfile,CommentForm,SubscriberForm
from .. models import User,Blog,Comment,Subscriber
from ..email import mail_message
from ..import db,photos

@main.route('/')
def index():
    subscriber_form=SubscriberForm()
    blogs = Blog.query.all()
    title = "blog"
    return render_template('index.html',blogs=blogs,subscriber_form=subscriber_form, title = title)

@main.route('/new/blog', methods = ['GET','POST'])
@login_required
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        blog = Blog(category = form.category.data, content = form.blog.data)
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('main.index'))
     
    return render_template('blog.html',form = form ,blog=blog) 



@main.route('/', methods=['GET','POST'])
def subscriber():
    subscriber_form=SubscriberForm()
    if subscriber_form.validate_on_submit():
        subscriber= Subscriber(email=subscriber_form.email.data,title = subscriber_form.title.data)
        db.session.add(subscriber)
        db.session.commit()
        mail_message("Hey Welcome To My Personal Blog ","email/welcome_subscriber",subscriber.email,subscriber=subscriber)
    subscriber = Blog.query.all()
    beauty = Blog.query.all()
    return render_template('index.html',subscriber=subscriber,subscriber_form=subscriber_form,beauty=beauty) 

@main.route('/new/Beauty', methods = ['GET','POST'])
@login_required
def new_Beauty():
    form = BlogForm()
    if form.validate_on_submit():
        blog = Blog(category = form.category.data, content = form.content.data)
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('beauty.html',form =form)

@main.route('/new/fashion', methods = ['GET','POST'])
@login_required
def new_fashion():
    form = BlogForm()
    if form.validate_on_submit():
        blog = Blog(category = form.category.data, content = form.content.data)
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('fashion.html',form =form)    
@main.route('/new/lifestyle', methods = ['GET','POST'])
@login_required
def new_lifestyle():
    form = BlogForm()
    if form.validate_on_submit():
        blog = Blog(category = form.category.data, content = form.content.data)
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('lifestyle.html',form =form)    

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user =User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(admin)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        admin.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))    

@main.route('/comment/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):  
    comment = CommentForm()
    if comment.validate_on_submit():
        com = Comment(content=comment.comment.data,blog_id=id)
        db.session.add(com)
        db.session.commit()
        
    return render_template('comment.html',comment=comment)





  