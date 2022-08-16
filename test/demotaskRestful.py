
from flask import Flask
from flask_restful import Resource, Api



app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'Data': 'Helloworld'}

        
class palindrome(Resource):
    
    def get(self,n):
        l=n[::-1]
        if n==l:
           return "Yes its a palindrome"
        else:
           return "No its not a palindrome"

class Fact(Resource):
    def get(self, n):
        f = 1
        for i in range(1, n + 1):
            f = f * i
        return f
        


api.add_resource(HelloWorld,'/')
api.add_resource(palindrome, '/<int:n>',)
api.add_resource(Fact, '/<int:n>',)


if __name__ == '__main__':
    app.run(debug=True)