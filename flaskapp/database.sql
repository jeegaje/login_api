-- MySQL dump 10.13  Distrib 8.0.26, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: monggaweb
-- ------------------------------------------------------
-- Server version	8.0.26-0ubuntu0.20.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `akun`
--

DROP TABLE IF EXISTS `akun`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `akun` (
  `akun_id` varchar(255) NOT NULL,
  `nama_depan` varchar(100) NOT NULL,
  `nama_akhir` varchar(100) NOT NULL,
  `email` varchar(255) NOT NULL,
  `sandi` varchar(255) NOT NULL,
  `tipe_akun` varchar(255) NOT NULL,
  `create_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`akun_id`),
  UNIQUE KEY `akun_id` (`akun_id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `akun`
--

LOCK TABLES `akun` WRITE;
/*!40000 ALTER TABLE `akun` DISABLE KEYS */;
INSERT INTO `akun` VALUES ('054c423c83304622922f3698b22bda3f','admin','mongga','admin@gmail.com','admin123','admin','2021-08-31 12:18:09'),('42f2041a68724d66ac508887b4d5fc47','user','duaa','user2@gmail.com','user123','user','2021-08-31 13:37:44'),('61cd5935900641f1af51396a50220d6a','user','','','','user','2021-09-01 18:07:48'),('99410835469762560','user','satu','user1@gmail.com','user123','user','2021-08-31 11:05:19'),('99410835469762561','mentor','satu','mentor1@gmail.com','mentor123','mentor','2021-08-31 20:06:50'),('9cc614f9b19c40f3bc569e852faf16d9','mentor','tiga','angga@gmail.com','angga123','mentor','2021-08-31 20:14:46'),('d7978563ff5f4ca4a8a6f6773440b4dc','user','tiga','user3@gmail.com','user123','user','2021-09-01 14:46:40');
/*!40000 ALTER TABLE `akun` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contact_us`
--

DROP TABLE IF EXISTS `contact_us`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contact_us` (
  `id` varchar(255) NOT NULL,
  `perihal` varchar(100) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `subjek` varchar(255) NOT NULL,
  `pesan` varchar(255) NOT NULL,
  `create_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contact_us`
--

LOCK TABLES `contact_us` WRITE;
/*!40000 ALTER TABLE `contact_us` DISABLE KEYS */;
INSERT INTO `contact_us` VALUES ('3e2855f28258455f881bd6f110edfd34','Pertanyaan atau Bantuan','test1','test@gmail.com','coba','ini adalah uji coba pertama','2021-09-06 00:29:58');
/*!40000 ALTER TABLE `contact_us` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `data_diri`
--

DROP TABLE IF EXISTS `data_diri`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `data_diri` (
  `data_diri_id` varchar(255) NOT NULL,
  `jenis_kelamin` varchar(100) DEFAULT NULL,
  `tempat_lahir` varchar(100) DEFAULT NULL,
  `tanggal_lahir` date DEFAULT NULL,
  `agama` varchar(100) DEFAULT NULL,
  `alamat` varchar(255) DEFAULT NULL,
  `nomor_hp` varchar(255) DEFAULT NULL,
  `update_date` datetime DEFAULT NULL,
  `akun_id` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`data_diri_id`),
  UNIQUE KEY `data_diri_id` (`data_diri_id`),
  UNIQUE KEY `akun_id` (`akun_id`),
  CONSTRAINT `data_diri_ibfk_1` FOREIGN KEY (`akun_id`) REFERENCES `coba_akun` (`akun_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data_diri`
--

LOCK TABLES `data_diri` WRITE;
/*!40000 ALTER TABLE `data_diri` DISABLE KEYS */;
/*!40000 ALTER TABLE `data_diri` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-09-06  1:00:10
