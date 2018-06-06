#coding: utf-8
from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)
POSTS = [
    {},
    {'title': 'first request', 'content': 'Request first interface'},
    {'title': 'second request', 'content': 'Request second interface'},
    {'title': 'third request', 'content': 'Request third interface'}
]

def abort_if_post_doesnt_exist(post_id):
    try:
        POSTS[post_id]
    except IndexError:
        abort(404, message="POSTS doesn't exist")
parser = reqparse.RequestParser()
parser.add_argument('requests', type=int)

class Post(Resource):
    #/requests/1 get
    def get(self, post_id):
            post_id = int(post_id)
            abort_if_post_doesnt_exist(post_id)
            return POSTS[post_id], 200

    #/requests/1 delete
    def delete(self, post_id):
        post_id = int(post_id)
        abort_if_post_doesnt_exist(post_id)
        del POSTS[post_id]
        return "", 204

    #/requests/ put
    def put(self, post_id):
        json_data = request.get_json(force=True)
        post_id = int(post_id)
        post = {'title': json_data['title'], 'content': json_data['content']}
        POSTS[post_id] = post
        return post, 201

class PostList(Resource):
    #/requests Get
    def get(self):
        posts = []
        for post in POSTS:
            if post:
                new_post = {}
                new_post['url'] = '/requests/' + str(POSTS.index(post))
                new_post['title'] = post['title']
                posts.append(new_post)
        return posts, 202

    # /requests POST
    def post(self):
        json_data = request.get_json(force=True)
        post_id = len(POSTS)
        POSTS.append({'title': json_data['title'], 'content': json_data['content']})
        return POSTS[post_id], 201

api.add_resource(PostList, '/requests')
api.add_resource(Post, '/requests/<post_id>')

if __name__ == '__main__':
    app.run(debug=True)

