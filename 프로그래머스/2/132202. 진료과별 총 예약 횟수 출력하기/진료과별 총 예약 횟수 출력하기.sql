SELECT MCDP_CD AS "진료과코드",
       COUNT(*) AS "5월예약건수"
FROM APPOINTMENT
-- 날짜 비교는 대소비교로
WHERE APNT_YMD >= '2022-05-01'
  AND APNT_YMD < '2022-06-01'
  -- 취소하지 않은 환자수라는 말 없었다
GROUP BY MCDP_CD
-- ORDER BY 별칭 쓰지마
ORDER BY COUNT(*) ASC, MCDP_CD ASC;