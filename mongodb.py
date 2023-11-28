# import marshmallow_mongoengine as ma
# import mongoengine as me
# from pymongo import MongoClient
#
# # Connecting to MongoDB
# client = MongoClient('mongodb://localhost:27017')
#
# # Chose DataBase
# db = client['database']
#
# # Settings about mongoengine
# me.connect('database', host='mongodb://localhost:27017')
#
#
# # creating Task
# class Task(me.EmbeddedDocument):
#     content = me.StringField(required=True)
#     priority = me.IntField(default=1)
#
#
# # Creating User
# class User(me.Document):
#     name = me.StringField()
#     password = me.StringField(required=True)
#     email = me.StringField()
#     tasks = me.ListField(me.EmbeddedDocumentField(Task))
#
#
# # Creating Schema from User
# class UserSchema(ma.ModelSchema):
#     class Meta:
#         model = User
#
#
# # Creating object from user to UserSchema
# user_schema = UserSchema()
# u = user_schema.load({"name": "John Doe", "email": "jdoe@example.com", "password": "123456",
#                       "tasks": [{"content": "Find a proper password"}]})
#
# # Save information in DataBase
# if u.save():
#     print("ok")
#
#
# # Show the saves results from DataBase
# user = User.objects(name="John Doe").first()
# if user:
#     print("نام:", user.name)
#     print("ایمیل:", user.email)
#     print("تسک‌ها:")
#     for task in user.tasks:
#         print("- محتوا:", task.content)
#         print("- اولویت:", task.priority)
# else:
#     print("کاربر یافت نشد.")
