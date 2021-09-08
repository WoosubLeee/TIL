# MySQL

## 비밀번호 변경 방법

```mysql
ALTER user 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '변경할비밀번호';
Query OK, 0 rows affected (0.07 sec)
```

변경 후 저장

```mysql
mysql> flush privileges;
Query OK, 0 rows affected (0.01 sec)
```



## References

https://to-dy.tistory.com/58 (MySQL 8.0 비밀번호 변경하기! (MySQL 5.7버전 이상)