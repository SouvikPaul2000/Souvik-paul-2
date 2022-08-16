from flask_restful import Resource
class palindrome(Resource):
    
    def get(self,n):
        l=n[::-1]
        if n==l:
           return "Yes its a palindrome"
        else:
           return "No its not a palindrome"