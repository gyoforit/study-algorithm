-- 서브쿼리 이용 (등록 장소가 2개 이상인 호스트 id 목록)
SELECT *
FROM PLACES
WHERE HOST_ID IN (SELECT HOST_ID FROM PLACES GROUP BY HOST_ID HAVING COUNT(ID) >= 2)
ORDER BY ID;