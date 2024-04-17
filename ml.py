from sklearn import tree

from database import Database


class ML:
    clf = tree.DecisionTreeClassifier()

    def learn(self):
        db = Database()
        db.connect_to_database()

        x = []
        y = []

        query = f"SELECT* FROM {Database.TABLE_NAME}"
        db.execute_query(query)

        for ID, name, price, mileage in db.cursor:
            x.append([name, mileage])
            y.append(price)

        db.close()
        self.clf = self.clf.fit(x, y)

    def predict(self, data):
        return self.clf.predict(data)
