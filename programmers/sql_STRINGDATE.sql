-- 루시와 엘라 찾기
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
ORDER BY ANIMAL_ID;

-- 이름에 el이 들어가는 동물 찾기
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE ANIMAL_TYPE = 'Dog' AND NAME LIKE '%el%'
ORDER BY NAME;
-- LIKE는 대소문자 구분 X
-- 구분하려면 BINARY(컬럼명) LIKE '~~' 라고 쓰면 됨

-- 중성화 여부 파악하기
SELECT ANIMAL_ID, NAME,
CASE WHEN SEX_UPON_INTAKE LIKE '%Neutered%' OR SEX_UPON_INTAKE LIKE '%Spayed%'
THEN 'O'
ELSE 'X' END AS 중성화
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;

-- 오랜 기간 보호한 동물(2)
SELECT i.animal_id, i.name
from animal_ins i
inner join animal_outs o on i.animal_id = o.animal_id
order by datediff(o.datetime,i.datetime) desc
limit 2;

-- DATETIME에서 DATE로 형 변환
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, '%Y-%m-%d') AS 날짜
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;