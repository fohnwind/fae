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


drop table if exsits `project`;
create table `project` (
    `pid` int(10) unsigned NOT NULL AUTO_INCREMENT,
    `pname` varchar(32) NOT NULL,
    `create_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `type` varchar(10) NOT NULL,
    `intro` text DEFAULT "",
    `owner` int(10) unsigned NOT NULL
) CHARSET=utf8;


drop table if exsits `level`;
create table `level` (
    `code` int(4) unsigned,
    `rank` varchar(10)
) CHARSET=utf8;


drop table if exsits `version`;
create table `version` (
    `pid` int(10) unsigned NOT NULL,
    `version` int(4) unsigned NOT NULL DEFAULT 1,
    `path` text NOT NULL,
    `info` varchar(128)
) CHARSET=utf8;


drop table if exsits `container_logs`;
create table `container_logs` (
    `clog_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
    `pid` int(10) unsigned NOT NULL,
    `info` varchar(128) NOT NULL DEFAULT "",
    `act_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`clog_id`)
) CHARSET=utf8;


drop table if exsits `project_logs`;
create table `project_logs` (
    `plog_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
    `pid` int(10) unsigned NOT NULL,
    `info` varchar(128) NOT NULL DEFAULT "",
    `actor` varchar(32) NOT NULL,
    `act_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
    PRIMARY KEY (`plog_id`)
) CHARSET=utf8;
