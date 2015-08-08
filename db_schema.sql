DROP DATABASE if exists fae;
CREATE DATABASE fae;

use fae;

drop table if exists `user`;
create table `user` (
    `uid` int(10) unsigned NOT NULL AUTO_INCREMENT,
    `sina_uid` bigint(20) unsigned DEFAULT NULL,
    `username` varchar(32) NOT NULL,
    `password` varchar(128) DEFAULT NULL,
    `user_level` int(4) DEFAULT 0,
    `project_count` int(4) DEFAULT 0,
     PRIMARY KEY (`uid`)
) CHARSET=utf8;


drop table if exists `project`;
create table `project` (
    `pid` int(10) unsigned NOT NULL AUTO_INCREMENT,
    `pname` varchar(32) NOT NULL,
    `create_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `intro` text,
    `url` varchar(128),
    `owner` int(10) unsigned NOT NULL,
    PRIMARY KEY (`pid`)
) CHARSET=utf8;


drop table if exists `container`;
create table `container` (
    `cid` int(10) unsigned NOT NULL AUTO_INCREMENT,
    `cname` varchar(32) NOT NULL,
    `ip` varchar(32) NOT NULL DEFAULT "172.17.0.0",
    `image` varchar(32) NOT NULL,
    `relation` int(10) unsigned NOT NULL,
    PRIMARY KEY (`cid`)
) CHARSET=utf8;



drop table if exists `level`;
create table `level` (
    `code` int(4) unsigned,
    `rank` varchar(10)
) CHARSET=utf8;


drop table if exists `version`;
create table `version` (
    `pid` int(10) unsigned NOT NULL,
    `version` int(4) unsigned NOT NULL DEFAULT 1,
    `v_name` varchar(32) DEFAULT "",
    `path` text NOT NULL,
    `info` varchar(128)
) CHARSET=utf8;


drop table if exists `container_logs`;
create table `container_logs` (
    `clog_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
    `pid` int(10) unsigned NOT NULL,
    `info` varchar(128) NOT NULL DEFAULT "",
    `act_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`clog_id`)
) CHARSET=utf8;


drop table if exists `project_logs`;
create table `project_logs` (
    `plog_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
    `pid` int(10) unsigned NOT NULL,
    `info` varchar(128) NOT NULL DEFAULT "",
    `actor` varchar(32) NOT NULL,
    `act_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`plog_id`)
) CHARSET=utf8;

