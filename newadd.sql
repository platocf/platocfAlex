/*
Navicat MySQL Data Transfer

Source Server         : 192.168.10.210_3306
Source Server Version : 50173
Source Host           : 192.168.10.210:3306
Source Database       : poi

Target Server Type    : MYSQL
Target Server Version : 50173
File Encoding         : 65001

Date: 2017-05-03 19:12:30
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `befen`
-- ----------------------------
DROP TABLE IF EXISTS `befen`;
CREATE TABLE `befen` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `matchinfoid` int(11) DEFAULT NULL,
  `companyid` int(11) DEFAULT NULL,
  `e_1_0h` double DEFAULT NULL,
  `e_1_0g` double DEFAULT NULL,
  `e_2_0h` double DEFAULT NULL,
  `e_2_0g` double DEFAULT NULL,
  `e_2_1h` double DEFAULT NULL,
  `e_2_1g` double DEFAULT NULL,
  `e_3_0h` double DEFAULT NULL,
  `e_3_0g` double DEFAULT NULL,
  `e_3_1h` double DEFAULT NULL,
  `e_3_1g` double DEFAULT NULL,
  `e_3_2h` double DEFAULT NULL,
  `e_3_2g` double DEFAULT NULL,
  `e_4_0h` double DEFAULT NULL,
  `e_4_0g` double DEFAULT NULL,
  `e_4_1h` double DEFAULT NULL,
  `e_4_1g` double DEFAULT NULL,
  `e_4_2h` double DEFAULT NULL,
  `e_4_2g` double DEFAULT NULL,
  `e_4_3h` double DEFAULT NULL,
  `e_4_3g` double DEFAULT NULL,
  `e_0_0` double DEFAULT NULL,
  `e_1_1` double DEFAULT NULL,
  `e_2_2` double DEFAULT NULL,
  `e_3_3` double DEFAULT NULL,
  `e_4_4` double DEFAULT NULL,
  PRIMARY KEY (`p_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of befen
-- ----------------------------

-- ----------------------------
-- Table structure for `bqc`
-- ----------------------------
DROP TABLE IF EXISTS `bqc`;
CREATE TABLE `bqc` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `matchinfoid` int(11) DEFAULT NULL,
  `e11` double DEFAULT NULL,
  `e10` double DEFAULT NULL,
  `e1-1` double DEFAULT NULL,
  `e01` double DEFAULT NULL,
  `e00` double DEFAULT NULL,
  `e0-1` double DEFAULT NULL,
  `e-11` double DEFAULT NULL,
  `e-10` double DEFAULT NULL,
  `e-1-1` double DEFAULT NULL,
  PRIMARY KEY (`p_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of bqc
-- ----------------------------

-- ----------------------------
-- Table structure for `company`
-- ----------------------------
DROP TABLE IF EXISTS `company`;
CREATE TABLE `company` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `company_name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`p_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of company
-- ----------------------------
INSERT INTO `company` VALUES ('2', '立博');
INSERT INTO `company` VALUES ('3', '威廉希尔');
INSERT INTO `company` VALUES ('4', 'Bet365');

-- ----------------------------
-- Table structure for `daxiao`
-- ----------------------------
DROP TABLE IF EXISTS `daxiao`;
CREATE TABLE `daxiao` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `matchinfoid` int(11) DEFAULT NULL,
  `companyid` int(11) DEFAULT NULL,
  `left` double DEFAULT NULL,
  `handline` varchar(20) DEFAULT NULL,
  `right` double DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`p_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of daxiao
-- ----------------------------

-- ----------------------------
-- Table structure for `dsjinqiu`
-- ----------------------------
DROP TABLE IF EXISTS `dsjinqiu`;
CREATE TABLE `dsjinqiu` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `matchinfoid` int(11) DEFAULT NULL,
  `single` double DEFAULT NULL,
  `double` double DEFAULT NULL,
  `ret` double DEFAULT NULL,
  `e01` double DEFAULT NULL,
  `e23` double DEFAULT NULL,
  `e47` double DEFAULT NULL,
  `e7plus` double DEFAULT NULL,
  PRIMARY KEY (`p_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of dsjinqiu
-- ----------------------------

-- ----------------------------
-- Table structure for `jinqiu`
-- ----------------------------
DROP TABLE IF EXISTS `jinqiu`;
CREATE TABLE `jinqiu` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `matchinfoid` int(11) DEFAULT NULL,
  `e_0` double DEFAULT NULL,
  `e_1` double DEFAULT NULL,
  `e_2` double DEFAULT NULL,
  `e_3` double DEFAULT NULL,
  `e_4` double DEFAULT NULL,
  `e_5` double DEFAULT NULL,
  `e_6` double DEFAULT NULL,
  `e_7plus` double DEFAULT NULL,
  PRIMARY KEY (`p_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of jinqiu
-- ----------------------------

-- ----------------------------
-- Table structure for `oupei`
-- ----------------------------
DROP TABLE IF EXISTS `oupei`;
CREATE TABLE `oupei` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `matchinfoid` int(11) DEFAULT NULL,
  `companyid` int(11) DEFAULT NULL,
  `op_s` double DEFAULT NULL,
  `op_p` double DEFAULT NULL,
  `op_f` double DEFAULT NULL,
  `ret` double DEFAULT NULL,
  `kl_s` double DEFAULT NULL,
  `kl_p` double DEFAULT NULL,
  `kl_f` double DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`p_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of oupei
-- ----------------------------
INSERT INTO `oupei` VALUES ('1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2017-05-03 18:56:05');

-- ----------------------------
-- Table structure for `playerstatistics`
-- ----------------------------
DROP TABLE IF EXISTS `playerstatistics`;
CREATE TABLE `playerstatistics` (
  `p_id` int(11) NOT NULL,
  `matchinfoid` int(11) DEFAULT NULL,
  `number` int(11) DEFAULT NULL,
  `name_c` varchar(40) DEFAULT NULL,
  `name_e` varchar(40) DEFAULT NULL,
  `position` varchar(10) DEFAULT NULL,
  `type` varchar(10) DEFAULT NULL,
  `time` int(11) DEFAULT NULL,
  `goal` int(11) DEFAULT NULL,
  `assists` int(11) DEFAULT NULL,
  `shoot` int(11) DEFAULT NULL,
  `shootz` int(11) DEFAULT NULL,
  `pass` int(11) DEFAULT NULL,
  `steals` int(11) DEFAULT NULL,
  `foul` int(11) DEFAULT NULL,
  `befoul` int(11) DEFAULT NULL,
  `offside` int(11) DEFAULT NULL,
  `rescue` int(11) DEFAULT NULL,
  `yelcrad` int(11) DEFAULT NULL,
  `redcrad` int(11) DEFAULT NULL,
  `saves` int(11) DEFAULT NULL,
  PRIMARY KEY (`p_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of playerstatistics
-- ----------------------------

-- ----------------------------
-- Table structure for `rangqiu`
-- ----------------------------
DROP TABLE IF EXISTS `rangqiu`;
CREATE TABLE `rangqiu` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `matchinfoid` int(11) DEFAULT NULL,
  `rangqiucount` int(11) DEFAULT NULL,
  `companyid` int(11) DEFAULT NULL,
  `rq_s` double DEFAULT NULL,
  `rq_p` double DEFAULT NULL,
  `rq_f` double DEFAULT NULL,
  `ret` double DEFAULT NULL,
  `kl_s` double DEFAULT NULL,
  `kl_p` double DEFAULT NULL,
  `kl_f` double DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`p_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of rangqiu
-- ----------------------------

-- ----------------------------
-- Table structure for `teamstatistics`
-- ----------------------------
DROP TABLE IF EXISTS `teamstatistics`;
CREATE TABLE `teamstatistics` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `matchinfoid` int(11) DEFAULT NULL,
  `static_attack` int(11) DEFAULT NULL,
  `static_dattack` int(11) DEFAULT NULL,
  `static_shoot` int(11) DEFAULT NULL,
  `static_shootz` int(11) DEFAULT NULL,
  `static_freekick` int(11) DEFAULT NULL,
  `static_corner` int(11) DEFAULT NULL,
  `static_offside` int(11) DEFAULT NULL,
  `static_foul` int(11) DEFAULT NULL,
  `static_yelcrad` int(11) DEFAULT NULL,
  `static_redcrad` int(11) DEFAULT NULL,
  `static_control` int(11) DEFAULT NULL,
  PRIMARY KEY (`p_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of teamstatistics
-- ----------------------------

-- ----------------------------
-- Table structure for `yazhi`
-- ----------------------------
DROP TABLE IF EXISTS `yazhi`;
CREATE TABLE `yazhi` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `matchinfoid` int(11) DEFAULT NULL,
  `companyid` int(11) DEFAULT NULL,
  `left` double DEFAULT NULL,
  `handline` varchar(20) DEFAULT NULL,
  `right` double DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`p_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of yazhi
-- ----------------------------
