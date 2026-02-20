import os, sys

full_path = os.path.abspath(__file__)

print(f"현재 작업 디렉토리: {os.getcwd()}")
print(f"Python 버전: {sys.version.split()[0]}")
print(f"운영체제: {os.name}")

print("\n실제 파일 경로 정보:")
print(f"- 디렉토리: {os.path.dirname(full_path)}")
print(f"- 파일명: {os.path.basename(full_path)}")
print(f"- 확장자: {os.path.splitext(full_path)[1]}")

print(f"파일 존재 여부: {os.path.exists(full_path)}")