# Workshop

**1)**

```sql
sqlite> CREATE TABLE countries (
   ...> room_num TEXT,
   ...> check_in TEXT,
   ...> check_out TEXT,
   ...> grade TEXT,
   ...> price INTEGER);
```

**2)**

```sql
sqlite> INSERT INTO countries VALUES
   ...> ('B203', '2019-12-31', '2020-01-03', 'suite', 900),
   ...> ('1102', '2020-01-04', '2020-01-08', 'suite', 850),
   ...> ('303', '2020-01-01', '2020-01-03', 'deluxe', 500),
   ...> ('807', '2020-01-04', '2020-01-07', 'superior', 300);
```

**3)**

```sql
sqlite> ALTER TABLE countries
   ...> RENAME TO hotels;
```

**4)**

```sql
sqlite> SELECT room_num, price
   ...> FROM hotels
   ...> ORDER BY price DESC;
```

**5)**

```sql
sqlite> SELECT grade, COUNT(grade)
   ...> FROM hotels
   ...> GROUP BY grade
   ...> ORDER BY COUNT(grade) DESC;
```

**6)**

```sql
sqlite> SELECT *
   ...> FROM hotels
   ...> WHERE room_num LIKE 'B%' OR grade = 'deluxe';
```

**7)**

```sql
sqlite> SELECT *
   ...> FROM hotels
   ...> WHERE room_num NOT LIKE 'B%' AND check_in = '2020-01-04'
   ...> ORDER BY price;
```



# Homework

### 1

1) 스키마

2) 테이블

3) 컬럼

4) 레코드

5) 기본키

### 2

(1) CREATE - DDL이다.

### 3

관계형 모델을 기반으로 데이터베이스를 관리하는 시스템이다.

![image-20210325214137587](django_11_homework.assets/image-20210325214137587.png)

2021년 3월 기준 DB-Engine 랭킹이다.

출처 : https://db-engines.com/en/ranking/relational+dbms

### 4

(3)이 틀렸다.

positional argument로 주어야 한다.

### 5

_ : _의 개수만큼 글자가 있어야 한다.

% : 1개 이상의 글자가 있어도 되고 없어도 된다.