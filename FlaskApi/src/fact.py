from flask_restful import Resource
class Fact(Resource):

    def get(self, n):
        f = 1
        for i in range(1, n + 1):
            f = f * i
        return f