-- phpMyAdmin SQL Dump
-- version 4.6.6
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jun 09, 2022 at 11:57 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `danielhesp`
--

-- --------------------------------------------------------

--
-- Table structure for table `food_reviews`
--

CREATE TABLE `food_reviews` (
  `ID` int(11) NOT NULL,
  `Dish Name` varchar(100) NOT NULL,
  `Cuisine` varchar(50) NOT NULL,
  `Served For:` varchar(100) NOT NULL,
  `Rating` int(1) NOT NULL,
  `Review` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `food_reviews`
--

INSERT INTO `food_reviews` (`ID`, `Dish Name`, `Cuisine`, `Served For:`, `Rating`, `Review`) VALUES
(1, 'Nachos', 'Tex-Mex', 'Dinner', 5, 'One of my favourite dishes of all time, nachos is an amazing mix of tortilla chips, mince, cheese and vegetables. Nachos is a dish that is just fun to eat. Picking up wedges of mince, cheese and veggies with a tortilla chip is so satisfying. This dish goes to another level when accompanied by guacamole, sour cream or chile con queso (a fantastic cheesy dipping sauce). I rate nachos at a fantastic 5/5 stars.'),
(2, 'Lasagna', 'Italian', 'Dinner', 4, 'Lasagna is a delightful dish consisting of wonderful layers of meat, cheese and pasta. I love lasagna because of its delicious flavor combinations. The creamy cheese combined with the mouth-watering mince is simply splendid. This dish goes great with a light salad and a glass of lemonade. I rate lasagna a solid 4/5 stars.'),
(3, 'Fish & Chips', 'British', 'Lunch or Dinner', 4, 'Whether you\'re lounging at home or having fun at the beach, fish & chips can be enjoyed anywhere, anytime. A simple but fantastic dish, fish & chips is exactly what it says it is. Usually served with tartar sauce or tomato sauce, coleslaw, and a slice of lemon, fish & chips are simply delicious. Although a fabulous dish, the quality can be affected by the vendor. If you get soggy chips and sub-par fish, a great dish can be turned into a gross affair. I rate fish & chips at 4/5 stars.'),
(4, 'Teriyaki Chicken', 'Japanese', 'Lunch or Dinner', 3, 'Teriyaki chicken is a dish that\'s very hard to mess up. Usually served with rice and an assortment of vegetables, teriyaki chicken is great to eat for lunch or dinner. I usually enjoy teriyaki chicken, but if the sauce is overpowering, the dish is not as nice. I rate teriyaki chicken at 3/5 stars.'),
(5, 'Salmon Quiche', 'French', 'Dinner', 2, 'Salmon quiche is not a dish for me. While still fairly good tasting, I\'m not a fan of the textures in this dish. This dish goes well with some kind of salad. I rate this dish at 2/5 stars.'),
(6, 'Brownies', 'American', 'Dessert', 4, 'A splendid treat, brownies go fantastically with a dollop of cream. I love eating brownies at all times, but they\'re traditionally served for dessert. Filled with scrumptious chocolate, brownies are one of my favourite desserts. I rate brownies at 4/5 stars. '),
(7, 'English Breakfast', 'British', 'Breakfast', 3, 'A fairly tasty meal, an English Breakfast is great if you\'re looking for something more filling in the morning.\r\nIt usually features beans, toast, mushrooms, tomatoes, potatoes, bacon, eggs and black pudding.\r\nI like most of this meal, but sometimes I\'m not looking for such a large meal in the mornings.\r\nI rate this meal at 3/5 stars.');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `food_reviews`
--
ALTER TABLE `food_reviews`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `food_reviews`
--
ALTER TABLE `food_reviews`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
