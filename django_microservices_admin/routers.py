class AuthRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """

    @staticmethod
    def db_for_read(model, **hints):
        """
        Attempts to read auth and contenttypes models go to auth_db.
        """
        return getattr(model, '_meta').app_label

    @staticmethod
    def db_for_write(model, **hints):
        """
        Attempts to write auth and contenttypes models go to auth_db.
        """
        return getattr(model, '_meta').app_label

    @staticmethod
    def allow_relation(obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        return None

    @staticmethod
    def allow_migrate(db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'auth_db' database.
        """
        return None
