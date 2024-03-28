from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

# .env 파일에서 환경 변수 로드
from dotenv import load_dotenv
import os
load_dotenv()

# 환경 변수에서 MongoDB 연결 정보 가져오기
MONGO_URI = os.getenv('MONGO_URI')
MONGO_DB = os.getenv('MONGO_DB')
COLLECTION_NAME = os.getenv('COLLECTION_NAME')

# MongoDB에 연결
client = MongoClient(MONGO_URI)
db = client[MONGO_DB]
users = db[COLLECTION_NAME]

# # 'email' 필드에 대한 인덱스 생성
# users.create_index([('email', 1)], unique=True)


# # insert_many 사용 예제
# try:
#     users.insert_many([
#         {"name": "John Doe", "email": "john@example.com"},
#         {"name": "Jane Doe", "email": "jane@example.com"},
#         {"name": "Park sungjoon", "email" : "psj@example.com"}
#     ])
#     print("Documents inserted successfully.")
# except Exception as e:
#     print("An error occurred:", e)


# # update_many 사용예제
# try:
#     result = users.update_many(
#         {"name": {"$regex": "^J"}},  # 이름이 J로 시작하는 모든 문서
#         {"$set": {"status": "verified"}}
#     )
#     print(f"{result.matched_count} documents matched, {result.modified_count} documents updated.")
# except Exception as e:
#     print("An error occurred:", e)

# # update_mnay 사용예제2
# try:
#     result = users.update_many(
#         {"name": {"$regex": "^P"}},  # 이름이 J로 시작하는 모든 문서
#         {"$set": {"status": "verified"}}
#     )
#     print(f"{result.matched_count} documents matched, {result.modified_count} documents updated.")
# except Exception as e:
#     print("An error occurred:", e)


# # delete_many 사용예제
# try:
#     result = users.delete_many({"status": "verified"})
#     print(f"{result.deleted_count} documents deleted.")
# except Exception as e:
#     print("An error occurred:", e)


# # 예외 처리
# try:
#     users.insert_one({"email": "john@example.com"})  # 이미 존재하는 이메일
# except DuplicateKeyError as e:
#     print("Duplicate key error:", e)
# except Exception as e:
#     print("An error occurred:", e)



# 모든 문서 조회
for doc in users.find():
    print(doc)
