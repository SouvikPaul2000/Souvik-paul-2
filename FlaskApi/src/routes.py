from flask_restful import Resource, Api
from src import app
api = Api(app)
from src.hello import HelloWorld
from src.pal import palindrome
from src.fact import Fact

class HelloWorld(Resource):
    def get(self):
        return {'Data': 'Helloworld'}

      
api.add_resource(HelloWorld,'/')
api.add_resource(palindrome, '/<n>',)
api.add_resource(Fact, '/f/<int:n>',)