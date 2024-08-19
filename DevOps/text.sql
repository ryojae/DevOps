
drop table if exists usertbl;
create table usertbl
(
    userid                          char(20)        not null ,
    name                            varchar(50)  not null ,
    birthyear                      int not null   ,
    constraint primary key PK_usertbl_userid (userid)
)default character set utf8;


drop table if exists buytbl;
create table buytbl
(
  num                    INT AUTO_INCREMENT not null PRIMARY KEY,
  userid                 char(8) not null,
  prodName         char(8)  null,
  groupname       char(8)   null,
  price                   int null,
  amount              smallint  null,
   foreign key(userid) references usertbl(userid)
)default character set utf8;

drop table if exists prodtbl;
create table prodtbl
( prodCode char(3) not null,
pordID char(4) not null,
prodDate DATETIME not null,
prodCar char(10) null,
constraint PK_pordTbl_prodCode_prodID
primary key (prodCode,prodID)
)default character set utf8;
