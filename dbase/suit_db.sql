-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 13, 2023 at 06:49 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `suit_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `tbl_admin`
--

CREATE TABLE `tbl_admin` (
  `id` int(11) NOT NULL,
  `username` text NOT NULL,
  `password` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_admin`
--

INSERT INTO `tbl_admin` (`id`, `username`, `password`) VALUES
(1, 'admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_detect_log`
--

CREATE TABLE `tbl_detect_log` (
  `id` int(11) NOT NULL,
  `date_log` date DEFAULT NULL,
  `time_log` time DEFAULT NULL,
  `department` varchar(50) NOT NULL,
  `course` varchar(50) NOT NULL,
  `unif_detect_result` varchar(50) NOT NULL DEFAULT '"IMPROPER"'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_detect_log`
--

INSERT INTO `tbl_detect_log` (`id`, `date_log`, `time_log`, `department`, `course`, `unif_detect_result`) VALUES
(23, '2023-07-13', '12:47:52', 'CONAHS', 'BS in Nutrition and Dietetics', 'PROPER');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_logs`
--

CREATE TABLE `tbl_logs` (
  `student_id` int(11) NOT NULL,
  `date_log` date NOT NULL DEFAULT current_timestamp(),
  `time_log` time NOT NULL DEFAULT current_timestamp(),
  `department` varchar(50) NOT NULL,
  `course` varchar(100) NOT NULL,
  `unif_detect_result` int(11) NOT NULL DEFAULT 0,
  `improper` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_logs`
--

INSERT INTO `tbl_logs` (`student_id`, `date_log`, `time_log`, `department`, `course`, `unif_detect_result`, `improper`) VALUES
(16, '2023-07-10', '00:00:00', '', '', 1, 0),
(17, '2023-07-10', '00:00:00', '', '', 1, 0),
(18, '2023-07-13', '11:58:27', 'CABEIHM', 'BS in Tourism Management', 0, 0),
(19, '2023-07-13', '11:59:18', 'CET', 'BS in Computer Engineering', 0, 0),
(20, '2023-07-13', '11:59:22', 'CABEIHM', 'BS in Accountancy', 0, 0),
(21, '2023-07-13', '11:59:24', 'CET', 'BS in Industrial Technology', 0, 0),
(22, '2023-07-13', '12:01:21', 'CONAHS', 'BS in Nutrition and Dietetics', 1, 0),
(23, '2023-07-13', '12:01:27', 'CET', 'BS in Computer Engineering', 1, 0);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_student`
--

CREATE TABLE `tbl_student` (
  `id` int(11) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `middle_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) NOT NULL,
  `course` varchar(100) NOT NULL,
  `sr_code` text NOT NULL,
  `gender` text NOT NULL,
  `department` text NOT NULL,
  `image` text NOT NULL,
  `status` text NOT NULL DEFAULT 'Active',
  `date_created` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_student`
--

INSERT INTO `tbl_student` (`id`, `first_name`, `middle_name`, `last_name`, `course`, `sr_code`, `gender`, `department`, `image`, `status`, `date_created`) VALUES
(16, 'asd', 'asd', 'asd', 'BS In Information Technology', '123', 'Male', 'CICS', 'asd-asd-16.jpg', 'Active', '2023-06-17 23:10:49'),
(17, 'Pau', 'Floi', 'Delfin', 'Bachelor of Science in Computer Science', '12312333', 'Female', 'CICS', '', 'Active', '2023-06-28 10:57:17'),
(18, 'sss', 'sss', '', '', '', '', '', '', 'Active', '2023-06-28 11:33:22'),
(20, 'asd', 'asd', 'asd', 'BS In Information Technology', '123', 'Male', 'CICS', 'asd-asd-20.jpg', 'Active', '2023-07-01 11:52:23');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tbl_admin`
--
ALTER TABLE `tbl_admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tbl_detect_log`
--
ALTER TABLE `tbl_detect_log`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tbl_logs`
--
ALTER TABLE `tbl_logs`
  ADD PRIMARY KEY (`student_id`);

--
-- Indexes for table `tbl_student`
--
ALTER TABLE `tbl_student`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tbl_admin`
--
ALTER TABLE `tbl_admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tbl_detect_log`
--
ALTER TABLE `tbl_detect_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `tbl_logs`
--
ALTER TABLE `tbl_logs`
  MODIFY `student_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `tbl_student`
--
ALTER TABLE `tbl_student`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
