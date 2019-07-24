import pymongo

#client = MongoClient('mongodb://localhost:27017/')
client = pymongo.MongoClient(host='localhost',port=27017) #define a objection MongoClinet
#1连接MongoDB数据库

#指定数据库
db = client.test
#db.client['test']

#指定集合
collection = db.students
#collection = db['students']     #声明一个对象

#插入数据
student1 = {
	'id' : '20170102',
	'name' : 'Mike',
	'age' : 20,
	'gender' : 'male'
}

student2 = {
	'id' : '20170103',
	'name' : 'Tom',
	'age' : 21,
	'gender' : 'male'
}
result = collection.insert([student1,student2])      #insert_one and insert_many()
print(result)

	
#find_one()
# find() generator object

#发现数据
result = collection.find_one({'name':'Mike'}) 
print(result)
print(type(result))





