from flask_app.config.mysqlconnection import connectToMySQL
# from .ninja import Ninjas
from flask_app.models.ninja import Ninjas
# from flask import flash
# import re
# EMAIL_REGEX= re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Dojos:
    db="dojos_and_ninjas_schema"
    def __init__(self, data):
        self.id = data['id']
        self.name=data['name']
        self.created_at= data['created_at']
        self.updated_at= data['updated_at']
        self.all_ninjas = []

# queries with CRUD and OOP
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"

        results= connectToMySQL(cls.db).query_db(query)
        dojos = []

        for all_dojos in results:
            dojos.append( cls(all_dojos) )
        return dojos

    # save a user to database
    @classmethod
    def save_dojo(cls, data):
        query= '''
                INSERT INTO dojos
                (name)
                VALUES
                (%(name)s);
        '''
        results= connectToMySQL(cls.db).query_db(query, data)
        
        # the results is returning the id of the record that was just created back to the route that called this method
        return results


    

    # # query for a user with all of their posts, return one User instance with a list of Post instances 
    @classmethod
    def dojo_with_ninjas(cls, data):
        query= '''
            SELECT * FROM dojos
            LEFT JOIN ninjas
            ON dojos.id = ninjas.dojo_id
            WHERE dojos.id = %(id)s;
        '''
        results= connectToMySQL(cls.db).query_db(query, data)
        print (results)
        # creating a User instance from the database info of the user
        one_dojo = cls(results[0])
        for row in results:

            # parsing out the database data for the post
            ninja_data={
                "id" : row['ninjas.id'],
                "dojo_id" : row['dojo_id'],
                "first_name": row['first_name'],
                "last_name":row['last_name'],
                "age": row['age'],
                "created_at": row['ninjas.created_at'],
                "updated_at": row['ninjas.updated_at']
            }

            # creating a post instance and appending it to the user's all_post attribute-which is an empty list.
            one_dojo.all_ninjas.append(Ninjas(ninja_data))

            # return this user to the route in the controller, to be used in the template
        return one_dojo
    

    # @staticmethod
    # def validate_user(form_data):
    #     is_valid= True
    #     if len(form_data['f_name']) < 2:
    #         flash("First Name must be atleast 2 characters", "register")
    #         is_valid= False
    #     if len(form_data['l_name']) < 2:
    #         flash("Last Name must be atleast 2 characters")
    #         is_valid= False
    #     if not EMAIL_REGEX.match(form_data['email']):
    #         flash("Invalid email address!")
    #         is_valid=False
    #     if len(form_data['password']) < 8:
    #         flash("Password needs to be atleast 8 characters")
    #         is_valid=False
    #     if form_data['conf_password'] != form_data['password']:
    #         flash("password and confirm password must match!")
    #         is_valid=False
    #     return is_valid


            

