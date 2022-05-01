from flask_sqlalchemy import SQLAlchemy
import pandas as pd
app: Flask = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///credentials.db'
db: SQLAlchemy = SQLAlchemy(app)



df = pd.read_sql_table(table_name='credentials', con=db.engine)

print(df)

df.to_excel('credentials.xlsx') # run this to move it to excel