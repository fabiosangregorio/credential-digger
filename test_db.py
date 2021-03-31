from psycopg2 import connect

db = connect(dbname=os.getenv('POSTGRES_DB'),
             user=os.getenv('POSTGRES_USER'),
             password=os.getenv('POSTGRES_PASSWORD'),
             host=os.getenv('DBHOST'),
             port=os.getenv('DBPORT'))
cursor = db.cursor()
cursor.execute("INSERT INTO rules (regex, category, description) \
                    VALUES ('test', 'test', 'test') RETURNING id")
db.commit()
print(int(cursor.fetchone()[0]))
