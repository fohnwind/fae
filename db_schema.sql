DROP DATABASE if exsits fae;
CREATE DATABASE fae;

use fae;

drop table if exsits `user`;
create table `user` (
    `uid` int(10) unsigned NOT NULL AUTO_INCREMENT,
    `sina_uid` bigint(20) unsigned DEFAULT NULL,
    `username` varchar(32) NOT NULL,
    `password` varchar(128) DEFAULT NULL,
    `user_level` int(4) DEFAULT 0,
     PRIMARY KEY (`uid`)
) CHARSET=utf8;


drop table if exsits `user_app`;
create table `user_app` (
    `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
    `uid` int(10) unsigned NOT NULL,
    `aid` int(10) unsigned NOT NULL,
    `create_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
) CHARSET=utf8;