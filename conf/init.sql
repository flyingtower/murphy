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

INSERT INTO base_user(create_at,modify_at,user_name,password,token,depart) VALUES (now(),now(),'ft','123','','工商局');

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