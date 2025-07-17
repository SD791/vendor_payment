class DatabaseRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'vendorpay':
            return 'vendorpay'
        elif model._meta.app_label == 'merchant':
            return 'merchant'
        return 'default'  # 'amazon' and others go to default

    def db_for_write(self, model, **hints):
        return self.db_for_read(model, **hints)

    def allow_relation(self, obj1, obj2, **hints):
        return True  # Allow relations across databases (optional but useful)

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'vendorpay':
            return db == 'vendorpay'
        elif app_label == 'merchant':
            return db == 'merchant'
        elif app_label == 'amazon':
            return db == 'default'
        return None  # Prevent migrating unknown apps
