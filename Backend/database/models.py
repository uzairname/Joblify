import mongoengine as me



class User(me.Document):

    name = me.StringField(required=True)
    meta = {'collection': 'users'}


class Resume(me.Document):

    content = me.StringField()
    user = me.ReferenceField(User, reverse_delete_rule=me.CASCADE)

    meta = {'collection': 'resumes'}


class JobListing(me.Document):

    description = me.StringField(required=True)
    user = me.ReferenceField(User, reverse_delete_rule=me.CASCADE)

    meta = {'collection': 'job_listings'}







class DbSettings(me.Document):
    database_version = me.IntField()

    meta = {
        'collection': 'db_settings',
        'max_documents': 1,
    }



__all__ = [
    'DbSettings',
    'User',
    'Resume',
]