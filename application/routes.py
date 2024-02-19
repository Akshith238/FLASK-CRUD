from application import app,db
from flask import request,jsonify
from application.models import Post
from application import calculator

@app.before_request
def create_tables():
    db.create_all()

@app.route('/',methods=['GET','POST','PATCH','DELETE'])
def Home():
    if request.method=="GET":
        return jsonify({"hi":"hello"})
         
    elif request.method=="POST":
        data = request.json
        content = data.get('content')
        new_content={
            "content":content,
        }
        post=Post(**new_content)
        try:
            db.session.add(post)
            db.session.commit()
            return jsonify({"message":f"{post} added successfully"}),200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error":str(e)}),400
    elif request.method=="PATCH":
        data=request.json
        id=data.get('id')
        post=Post.query.filter_by(id=id).first()
        content=data.get("content")
        if content is not None:
            post.content=content
        try:
            db.session.commit()
            return jsonify({"message":"Data updated Successfully","data":content}),200
        except Exception as e:
            return jsonify({"error":str(e)}),400
    elif request.method=="DELETE":
        data=request.json
        id=data.get('id')
        post=Post.query.filter_by(id=id).delete()
        try:
            db.session.commit()
            return jsonify({"message":"Deleted Successfully"})
        except Exception as e:
            db.session.rollback()
            return jsonify({"error":str(e)})
      
@app.route("/calculate",methods=['POST'])
def calculate():
    data=request.json
    method_name=data.get('method')
    args=data.get('args',[])
    
    if hasattr(calculator,method_name):
        method=getattr(calculator,method_name)
        result=method(*args)
        if result:
            return jsonify({"result":result}),200
        else:
            return jsonify({"message":"no response"})
    
    
@app.route('/home/<int:id>')
def User(id):
    return jsonify({'user_id': id})

