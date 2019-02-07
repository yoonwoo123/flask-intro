CREATE TABLE classmates (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- 주의 AUTOINCREMENT 에는 INT가 아닌 INTEGER만 사용 가능!!
    name TEXT NOT NULL, -- NOT NULL : INSERT에는 반드시 값이 들어가야함.
    age INT NOT NULL,
    address TEXT NOT NULL
);
 