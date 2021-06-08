-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 08, 2021 at 10:58 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sblog`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(11) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone_num` varchar(12) NOT NULL,
  `message` text NOT NULL,
  `date` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `name`, `email`, `phone_num`, `message`, `date`) VALUES
(1, 'Default_NAME', 'default@email.com', '1234567890', 'DEFAULT_MESSAGE', '2021-01-05 22:36:28');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(11) NOT NULL,
  `Title` text NOT NULL,
  `slug` varchar(50) NOT NULL,
  `image_file` varchar(30) NOT NULL,
  `Content` text NOT NULL,
  `Date` date NOT NULL DEFAULT current_timestamp(),
  `html_file` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `Title`, `slug`, `image_file`, `Content`, `Date`, `html_file`) VALUES
(1, 'Background Remover', 'background_remover', 'background_remover_3.png', 'Removal of unwanted outer areas from a graphic or illustrated image; this process usually consists of removing some of the peripheral regions of an image to remove extraneous trash from the picture, improving its framing, and accentuating or isolating the subject matter from its background.\r\n\r\nHere, we have a web application that uses artificial intelligence to remove the background of any image or photo. It works 100% automatically, so you don\'t need to select the background/foreground layers to separate them manually - choose or select your image and instantly download the output image with the background removed.', '2021-01-06', 'posts.html'),
(2, 'Predictive Analysis of GRACE Satellite Data', 'pyGrace', 'pyGrace_CNN2.jpg', 'Global hydrological models are increasingly being used to evaluate water availability and sea-level rise. However, deficiencies in the conceptualization and parameterization in these models may introduce significant uncertainty in model predictions. A study by Alexander Y. Sun and Bridget R. Scanlon applied Deep Learning to study the Spatial and Temporal Patterns of mismatch or residual between model simulation and GRACE observations. Through three different types of convolution neural network-based deep learning models, we show that deep learning is a viable approach for improving model-GRACE match. ', '2021-06-08', 'pyGrace.html'),
(3, 'AI ChatBot: Olivia', 'olivia', 't4.jpg', 'An AI chatbot is a program within a website or app that simulates human conversations using NLP (natural language processing). They are programmed to address users\' requirements autonomously of a human operator. Standard functions of chatbots include answering frequently asked questions and assisting users in navigating the website or app. ', '2021-06-08', 'olivia.html');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
