-- 실행시키는 방법 .read insert.sql

INSERT INTO classmates(name, age, address) -- (id, name, age, address) -- 모든 값을 넣을 때는 column을 명시할 필요 없이 순서만 지키면 된다.
VALUES('홍길동', 30, '서울'); -- id는 PRIMARY 이므로 같은 id를 넣으면 UINQUE 오류가 뜬다.
-- INSERT INTO classmates('윤영우', 20)
-- VALUES(2, '홍길동', 30, '서울');
INSERT INTO classmates(name, age, address)
VALUES('이재찬', 30, '대전');
INSERT INTO classmates(name, age, address)
VALUES('박성민', 15, '대전');
INSERT INTO classmates(name, age, address)
VALUES('윤영우', 26, '수원');
INSERT INTO classmates(name, age, address)
VALUES('정태현', 18, '부산');
