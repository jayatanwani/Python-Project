Create table User1 
(UserId  int auto_increment key,
UserName 		varchar(200),
UserClass       varchar(50),
UserYear        varchar(50),
UserRollNo      bigint(50),
UserAttendance  bigint(50)
)
Insert into User1(UserName,UserClass,UserYear,UserRollNo,UserAttendance)
Values('jaya','D7A','SE',67,68)
SELECT * from User1;
