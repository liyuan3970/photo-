# photo-
## 这是一个基于django mysql jquery 的项目

## 所需要的库
pip install django==1.11.8
pip install pymysql
pip install pillow

## 所需要的软件
1. mysql
2. python （版本3以上，本人的是3.7）
3. pycharm(不想用也可以)


## 创建数据库

1. mysql -uroot -p  
2. create databases photo default charset=utf8;

## 数据库实体类
**总共有4个实体数据表，分别是landscpe、life、happniess、food**
### 四个数据表结构相似，如下：

| Field | Type         | Null | Key | Default | Extra          |
|-------|--------------|------|-----|---------|----------------|
| id    | int(11)      | NO   | PRI | NULL    | auto_increment |
| img   | varchar(100) | NO   |     | NULL    |                |
| time  | date         | NO   |     | NULL    |                |
| title | varchar(50)  | NO   |     | NULL    |                |



## 将项目跑起来

1. python manage.py makemigrations
2. python manage.py migrate
3. python manage.py createsuperuser
4. python manager.py runserver
5. ctul + C 结束项目

## 首页展示
![index.picture](index.png)