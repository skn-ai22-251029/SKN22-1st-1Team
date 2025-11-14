# SKN22-1st-1Team
Repository for SKN22-1st-1Team


🚗 교통사고 통합 데이터 분석 시스템

사고 · 운전자 · 지역 데이터를 MySQL 기반으로 정규화하여
조회·분석·시각화에 활용하기 위한 데이터베이스 구축 프로젝트입니다.

✅ Dev Environment

Python 3.13.9

Conda env: project_1_env

Packages: pyyaml, requests

Database: MySQL 8.0+

Schema: /repository/schema.sql

🔍 주요 기능 요약

1. 사고 데이터 조회

지역·발생월·사고유형·주야·기상/노면 조건 필터링

인덱스 기반 빠른 검색 지원

2. 지역 기반 통계

시군구별 사고 건수

사고 유형 분포 및 심각도(사망/중상/경상) 분석

3. 운전자 정보 분석

가해/피해 구분

연령대·성별·차종별 사고 특성

상해 정도 기반 사고 심각도 분류

# ERD
![ERD](Varchar.jpg)