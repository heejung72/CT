SELECT 
    -- 1. 분화된 연도 추출하기
    YEAR(DIFFERENTIATION_DATE) AS YEAR,
    -- 2. 연도별 최대 크기에서 현재 대장균의 크기(SIZE_OF_COLONY) 빼기
    ( MAX_SIZE - SIZE_OF_COLONY ) AS YEAR_DEV,
    -- 3. 대장균 ID 출력하기
    ID
    
FROM ECOLI_DATA AS E

-- 4. 연도별 최대 크기를 구하는 서브쿼리와 JOIN 하기
JOIN (
    SELECT 
        -- 연도 추출
        YEAR(DIFFERENTIATION_DATE) AS YEAR,
        -- 연도별 가장 큰 대장균의 크기 구하기
        MAX(SIZE_OF_COLONY) AS MAX_SIZE
    FROM ECOLI_DATA
    GROUP BY YEAR(DIFFERENTIATION_DATE)
) AS M 
  ON YEAR(E.DIFFERENTIATION_DATE) = M.YEAR -- 연도를 기준으로 조인

-- 5. 정렬 조건 작성하기 (연도 오름차순, 편차 오름차순)
ORDER BY 
    YEAR ASC, 
    YEAR_DEV ASC;