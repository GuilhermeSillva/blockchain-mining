from app.main import data_base as db
class BaseModel:

    def __commit_changes(self):
        db.session.commit()


    def insert(self, data, return_public_id = False):
        db.session.add(data)
        self.__commit_changes()

        if return_public_id:
            return data.public_id
        return


    def update(self, data, class_object):
        for column in data:
            if data.get(column) is not None:
                if data.get(column) == 'status':
                    continue
                setattr(class_object, column, data.get(column))
        self.__commit_changes()
        return class_object.public_id


    def delete(self, class_object):
        class_object.status = 0
        self.__commit_changes()


    def select(self):
        return db.session
