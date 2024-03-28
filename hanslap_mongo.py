from pymongo import MongoClient
import os
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv()

# 환경 변수에서 MongoDB 연결 정보 가져오기
MONGO_URI = os.getenv('MONGO_URI')

# MongoDB에 연결
client = MongoClient(MONGO_URI)

# 데이터베이스 선택 (없으면 새로 생성됨)
MONGO_DB = os.getenv('MONGO_DB')
db = client[MONGO_DB]

# 컬렉션 선택 (없으면 새로 생성됨) (여기서 컬렉션은 테이블)
COLLECTION_NAME = os.getenv('COLLECTION_NAME')
collection = db[COLLECTION_NAME]

# # 새 문서 생성 및 삽입
# document = {"name": "John Doe", "age": 30, "city": "New York"}
# collection.insert_one(document)

# document = {"name": "OpenAI", "age": 100, "country": "America", }
# collection.insert_one(document)

# document = {"name": "Park sungjoon", "age": 26, "city": "Seoul", }
# collection.insert_one(document)

## 문서 삭제
# result = collection.delete_one({"name": "Park sungjoon"})
## 콜렉션 삭제 : 
# 콜렉션.drop()
# 데이터베이스 삭제 : 
# client.drop_database('데이터베이스명')

# # 문서 업데이트
# collection.update_one(
#     {"name": "John Doe"},  # 조건
#     {"$set": {"age": 31}}  # 변경할 내용
# )


# 모든 문서 조회
for doc in collection.find():
    print(doc)

# #특정 조건에 맞는 문서 조회
# query = {"city": "Seoul"}
# documents = collection.find(query)
# for doc in documents:
#     print(doc)
    
