-- 테이블 만들기
CREATE TABLE tb_test (
	name varchar,
	age INT,
	birth timestamp
);

/*
조회(read R)
select 컬럼명, 컬럼명
from 테이블명
*/
SELECT NAME, AGE, birth FROM tb_test;
SELECT * FROM tb_test;
SELECT NAME FROM tb_test;

/*
삽입(create C)
insert into 테이블명 (컬럼명, 컬럼명)
values (값, 값)
*/
INSERT INTO tb_test (NAME, AGE, birth)
VALUES 
('이름1', 20, '2025-12-01'),
('이름2', 21, '2025-12-02')

SELECT * FROM tb_test
WHERE NAME = '이름2'

SELECT * FROM tb_test
WHERE AGE = 20

/*
수정 (update U)
update 테이블명
set 컬럼명 = 값, 컬럼명 = 값
where 조건 꼭 쓰기
*/
UPDATE tb_test
SET AGE = 30
WHERE NAME='이름2'

SELECT * FROM tb_test

/*
삭제 (delete D)
delete from 테이블명
where 조건 꼭 쓰기
*/
DELETE FROM tb_test
WHERE AGE = 30

SELECT * FROM tb_test

SELECT NOW()


SELECT * FROM emp
OFFSET 5
LIMIT 4;

SELECT * FROM dept;

-- 문제: emp에서 deptno가 10인 사람만 선택
SELECT * FROM emp
WHERE deptno = 10

SELECT * FROM emp
-- 문제 1 
-- 월급이 2000 이상인 사람
SELECT * FROM emp
WHERE sal >= 2000
-- 문제 2
-- 월급이 2000 초과 3000 이하인 사람
SELECT * FROM emp
WHERE sal > 2000 AND sal <= 3000
-- 문제 3
-- 사원번호로 SMITH만 조회
SELECT * FROM emp
WHERE empno = 7369

SELECT ename, sal FROM emp


SELECT * FROM emp
WHERE comm < 400

SELECT * FROM emp
WHERE comm IS null

SELECT * FROM emp
WHERE comm IS NULL OR comm < 400

SELECT * FROM emp
WHERE
	job = 'CLERK' OR job = 'SALESMAN'
	
SELECT * FROM emp
WHERE job IN ('CLERK', 'SALESMAN')

SELECT * FROM emp
WHERE job not IN ('CLERK', 'SALESMAN')

SELECT * FROM emp
WHERE ename LIKE '%a%'

SELECT ename FROM emp
SELECT upper('Allen')

SELECT * FROM emp
WHERE LOWER(ename) LIKE LOWER('%aM%')

SELECT * FROM emp
ORDER BY sal DESC, ename ASC, empno


SELECT job FROM emp
GROUP BY job

SELECT job, deptno FROM emp
GROUP BY job, deptno

SELECT COUNT(*) FROM emp

SELECT job, COUNT(*), MAX(sal) FROM emp
GROUP BY job

/* 4 */  select job, COUNT(*) AS cnt
/* 1 */  from emp
/* 2 */  where sal > 1000
/* 3 */  group by job
/* 5 */  order by cnt

SELECT comm FROM emp

SELECT 'N/A' FROM emp
WHERE comm IS null

SELECT
	sal,
	CASE 
		WHEN sal > 3000 THEN '고액'
		WHEN sal <= 3000 AND sal > 1000 THEN '적당'
		ELSE '소액'
	end
FROM emp


SELECT * FROM emp
WHERE deptno = 10
UNION all
SELECT * FROM emp
WHERE sal >= 2000

SELECT * FROM emp
SELECT * FROM dept

SELECT *
FROM emp, dept
WHERE emp.deptno = dept.deptno

SELECT *
FROM emp e, dept d
WHERE e.deptno = d.deptno

SELECT e.ename, d.dname, loc, e.deptno
FROM emp e, dept d
WHERE e.deptno = d.deptno
AND e.ename = 'SMITH'

SELECT * 
FROM emp e1, emp e2
WHERE e1.mgr = e2.empno

-- join, outer join, left outer join
-- LEFT OUTER JOIN : 조건이 null 이어도 모두 출력됨
-- 즉, 왼쪽 테이블의 모든 값을 출력
SELECT *
FROM emp e1
LEFT OUTER JOIN emp e2 ON e1.mgr = e2.empno

SELECT *
FROM emp e
LEFT OUTER JOIN dept d ON e.deptno = d.deptno

SELECT *
FROM emp e
LEFT OUTER JOIN dept d USING (deptno)


SELECT ROW_NUMBER() over(), e.* 
FROM emp e


SELECT ROW_NUMBER() over(), e.* 
FROM emp e
ORDER BY sal

SELECT ROW_NUMBER() over(), a.*  
FROM (
	SELECT * FROM emp
	ORDER BY sal
) a

SELECT ROW_NUMBER() over(order by sal), e.* 
FROM emp e

/*
	insert, update, delete 이후에
	commit : 확정
	rollback : 취소(즉, 이전 commit으로 돌아감)
*/
