-- MySQL dump 10.13  Distrib 5.7.19, for macos10.12 (x86_64)
--
-- Host: localhost    Database: actual16
-- ------------------------------------------------------
-- Server version	5.7.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `role` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=96 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (73,'testmd5','0efeb8d44cf7c30b40aa948a5a311989','testmd5@reboot.com','admin'),(74,'admin','e10adc3949ba59abbe56e057f20f883e','admin21@reboot.com','admin'),(75,'test133333','964c02612b2a1013ed26d46ba9a73e74','test1@reboot.com','common'),(76,'test2','ad0234829205b9033196ba818f7a872b','test2@reboot.com','common'),(77,'test3','8ad8757baa8564dc136c1e07507f4a98','test3@reboot.com','common'),(78,'test4','86985e105f79b95d6bc918fb45ec7727','test4','common'),(79,'test5','e3d704f3542b44a621ebed70dc0efe13','test5','common'),(80,'test6','4cfad7076129962ee70c36839a1e3e15','test6','common'),(81,'monkey','d0763edaa9d9bd2a9516280e9044d885','monkey','common'),(82,'monkey1','a41d81871cc00919542ac86f493b9b76','monkey1','common'),(83,'monkey2','e10adc3949ba59abbe56e057f20f883e','monkey2','common'),(86,'joe123456','e10adc3949ba59abbe56e057f20f883e','joe@gmail.com','admin'),(87,'joe1','96e79218965eb72c92a549dd5a330112','joe1@gmail.com','common'),(88,'test111','e10adc3949ba59abbe56e057f20f883e','test111@reboot.com','admin'),(89,'test111','e10adc3949ba59abbe56e057f20f883e','test111@reboot.com','admin'),(90,'aaaaaa','0b4e7a0e5fe84ad35fb5f95b9ceeac79','aaaaaa@reboot.com','common'),(91,'aaaaaa','0b4e7a0e5fe84ad35fb5f95b9ceeac79','aaaaaa@reboot.com','common'),(92,'bbbbbbbb','810247419084c82d03809fc886fedaad','bbbbbbbb','admin'),(93,'55555555','f638f4354ff089323d1a5f78fd8f63ca','55555555','admin'),(95,'','d41d8cd98f00b204e9800998ecf8427e','','---请选择角色---');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-12-07 11:03:55
