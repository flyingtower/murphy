create database murphy;

CREATE TABLE `base_user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `create_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '记录创建时间',
  `modify_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '记录修改时间',
  `user_name` varchar(16) NOT NULL COMMENT '用户名',
  `depart` varchar(16) NOT NULL COMMENT '部门',
  `token` varchar(64) NOT NULL COMMENT '当前的用户token',
  `password` varchar(64) NOT NULL COMMENT '用户密码',
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_token` (`token`),
  UNIQUE KEY `idx_user_name` (`user_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

insert into base_user(user_name,password,token,depart) values('廖宸一','lcy','','推广中心');
insert into base_user(user_name,password,token,depart) values('贾唯','jw','','推广中心');
insert into base_user(user_name,password,token,depart) values('钟彬礼','zbl','','推广中心');
insert into base_user(user_name,password,token,depart) values('张蕾','','zl','推广中心');
insert into base_user(user_name,password,token,depart) values('周昕毅','zxy','','推广中心');
insert into base_user(user_name,password,token,depart) values('周幸','zx','','推广中心');
insert into base_user(user_name,password,token,depart) values('黄柏豪','zbh','','推广中心');
insert into base_user(user_name,password,token,depart) values('闫俊','yj','','推广中心');
insert into base_user(user_name,password,token,depart) values('杨晶','yj','','推广中心');
insert into base_user(user_name,password,token,depart) values('梁伟乐','lwl','','推广中心');

CREATE TABLE `daily_report` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `create_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '记录创建时间',
  `modify_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '记录修改时间',
  `daily_date` datetime NOT NULL COMMENT '日报时间',
  `user_id` varchar(16) NOT NULL COMMENT '用户id',
  `content` text COMMENT '一句话总结',
  `extra` text COMMENT '备注遇到的问题',
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_date_user_id` (`daily_date`,`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;