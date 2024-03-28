from pymongo import MongoClient
from dotenv import load_dotenv
import os

# .env 파일에서 환경 변수 로드
load_dotenv()

# 환경 변수에서 MongoDB 연결 정보 가져오기
mongo_uri = os.getenv('MONGO_URI')
mongo_db = os.getenv('MONGO_DB')
mongo_collection = os.getenv('MONGO_COLLECTION')

client = MongoClient(mongo_uri)
db = client[mongo_db]
collection = db[mongo_collection]


# # 기존 데이터가 있다면 삭제 (새로운 실습을 위해)
# collection.delete_many({})

# # 샘플 데이터 삽입
# sample_users = [
#     {"name": "Alice", "team":"lion", "age": 25, "status": "active"},
#     {"name": "Bob", "age": 30, "status": "inactive","team":"tiger"},
#     {"name": "Charlie", "age": 35, "status": "active","team":"tiger"},
#     {"name": "David", "age": 40, "status": "active","team":"lion"},
#     {"name": "Eve", "age": 25, "status": "active","team":"king"},
#     {"name": "Frank", "age": 30, "status": "active","team":"lion"}
# ]

# collection.insert_many(sample_users)


# 파이프 라인 
pipeline = [
    {"$match": {"status": "active"}},
    {"$group": {"_id": "$team", "count": {"$sum": 1}}}
]
results = collection.aggregate(pipeline)

for result in results:
    print(result)