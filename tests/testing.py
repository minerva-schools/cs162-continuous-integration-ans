import requests

# post  valid expression
r = requests.post('http://192.168.99.100:5000/add', data = {'expression': '1+2+3'})

'''First check post'''
# check the correct response #was received
if r.status_code != 200:
	raise Exception('failed to post')

'''Second check answer'''
# check you would see the answer
if '6.00 = 1+2+3' not in r.text: #if answer isn't the correct one
	raise Exception('did not get and present a correct answer')

import psycopg2 #for postgres
from sqlalchemy import create_engine, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base #lol


#connection string from stack overflow + details form Docker Compose file
con_string = 'postgres+psycopg2://cs162_user:cs162_password@192.168.99.100:5432/cs162'
engine = create_engine(con_string) #connecting
engine.connect()

Base = declarative_base() #base model for ta ble inheritance

class Expr(Base):
    __table__ = Table('expression', Base.metadata,
                    autoload=True, autoload_with=engine)

# This class is pretty much pulling a table form the database (querying the database:
# "Tell me about this table" instead of creating another table locally because it will
# erase whatever data was in the initial table + we'll have to update the database schema
# whenever we modify something on this table. Check class again to see prof's "not to do")

Session = sessionmaker(bind=engine)
s = Session()

#get latest item inserted
latest = s.query(Expr).order_by(Expr.now.desc()).first() #last item
if latest.text != '1+2+3' or latest.value != 6: #checking = to our calc
	raise Exception('Latest query not saved in the db')

# post faulty query
r2 = requests.post('http://192.168.99.100:5000/add', data = {'expression': '1///2+3'})

'''Check error'''
if r2.status_code != 500: #should be an error
	raise Exception('This query dont be right)

latest = s.query(Expr).order_by(Expr.now.desc()).first() #checking last item
if latest.text != '1+2+3' or latest.value != 6: #if it isn't the same (if something was added from faulty calc)
	raise Exception('Something was change in db')

print ('All tests have passed')
