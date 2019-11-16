-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 16, 2019 at 02:16 AM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.3.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `qlbaixe`
--

-- --------------------------------------------------------

--
-- Table structure for table `tblcamera`
--

CREATE TABLE `tblcamera` (
  `IdCam` tinyint(4) NOT NULL,
  `TenCam` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `MoTa` varchar(500) COLLATE utf8_unicode_ci NOT NULL,
  `NgayTao` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `tblcamera`
--

INSERT INTO `tblcamera` (`IdCam`, `TenCam`, `MoTa`, `NgayTao`) VALUES
(1, 'Camera lắp cổng vào', 'Camera lắp cổng vào, check xe vào ', '2019-10-25'),
(2, 'Camera lắp cổng ra', 'Camera lắp cổng vào, check xe ra', '2019-10-25');

-- --------------------------------------------------------

--
-- Table structure for table `tblcudan`
--

CREATE TABLE `tblcudan` (
  `IdCuDan` int(11) NOT NULL,
  `HoDem` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `Ten` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `Image` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `DienThoai1` varchar(12) COLLATE utf8_unicode_ci NOT NULL,
  `DienThoai2` varchar(12) COLLATE utf8_unicode_ci NOT NULL,
  `Email` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `DiaChi` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `TamNgung` bit(1) NOT NULL DEFAULT b'0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `tblcudan`
--

INSERT INTO `tblcudan` (`IdCuDan`, `HoDem`, `Ten`, `Image`, `DienThoai1`, `DienThoai2`, `Email`, `DiaChi`, `TamNgung`) VALUES
(1, 'Phan Trọng ', 'Tiến', '/images/Tien.jpg', '09812132132', '09812132133', 'phantien@gmail.com', 'Nhà 20, Lâm Viên, Đặng Xá', b'0');

-- --------------------------------------------------------

--
-- Table structure for table `tbllichsuguixe`
--

CREATE TABLE `tbllichsuguixe` (
  `IdGui` int(11) NOT NULL,
  `IdCam` tinyint(4) NOT NULL,
  `NgayTao` datetime NOT NULL,
  `BienSo` char(10) COLLATE utf8_unicode_ci NOT NULL,
  `HinhAnh` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `MaXacNhan` int(11) NOT NULL,
  `TrangThai` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `IdNguoiDung` char(20) COLLATE utf8_unicode_ci NOT NULL,
  `DoChinhXac` double(4,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tblloaixe`
--

CREATE TABLE `tblloaixe` (
  `IdLoaiXe` int(11) NOT NULL,
  `TenLoai` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `MoTa` varchar(100) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `tblloaixe`
--

INSERT INTO `tblloaixe` (`IdLoaiXe`, `TenLoai`, `MoTa`) VALUES
(1, 'Honda AirBlade', 'Xe màu vàng, đen và màu đan vàng'),
(2, 'Honda Vision', 'Xe màu xanh, màu bạc, màu ghi');

-- --------------------------------------------------------

--
-- Table structure for table `tblnguoidung`
--

CREATE TABLE `tblnguoidung` (
  `IdNguoiDung` char(15) COLLATE utf8_unicode_ci NOT NULL,
  `Pass` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `HoDem` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `Ten` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `DienThoai` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `Email` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `IdQuyen` tinyint(4) NOT NULL,
  `TamNgung` bit(1) NOT NULL DEFAULT b'0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `tblnguoidung`
--

INSERT INTO `tblnguoidung` (`IdNguoiDung`, `Pass`, `HoDem`, `Ten`, `DienThoai`, `Email`, `IdQuyen`, `TamNgung`) VALUES
('a', 'a', 'Họ đệm', 'Tên', '0868681297', 'aa@gmail.com', 3, b'0'),
('admin', 'admin', 'Nguyen van', 'bach', '0868681297', 'hack@gmail.com', 1, b'0'),
('nv1', 'nv1', 'duong', 'vu', '0123456789', 'bbb@gmail.com', 2, b'0');

-- --------------------------------------------------------

--
-- Table structure for table `tblquyen`
--

CREATE TABLE `tblquyen` (
  `IdQuyen` tinyint(4) NOT NULL,
  `TenQuyen` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `MoTa` varchar(100) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `tblquyen`
--

INSERT INTO `tblquyen` (`IdQuyen`, `TenQuyen`, `MoTa`) VALUES
(1, 'Quản trị hệ thống', 'Toàn quyền hệ thống'),
(2, 'Quản lý bãi xe', 'Cập nhật dữ liệu cư dân và các bảng không liên quan đến cấu hình, phân quyền'),
(3, 'Nhân viên', 'Chỉ thực hiện chức năng tiếp nhận xe và trả xe');

-- --------------------------------------------------------

--
-- Table structure for table `tblxecudan`
--

CREATE TABLE `tblxecudan` (
  `BienSo` char(10) COLLATE utf8_unicode_ci NOT NULL,
  `IdCuDan` int(11) NOT NULL,
  `IdLoaiXe` int(11) NOT NULL,
  `MauSac` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `TamNgung` bit(1) NOT NULL DEFAULT b'0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `tblxecudan`
--

INSERT INTO `tblxecudan` (`BienSo`, `IdCuDan`, `IdLoaiXe`, `MauSac`, `TamNgung`) VALUES
('29N14129', 1, 1, 'Vàng', b'0');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tblcamera`
--
ALTER TABLE `tblcamera`
  ADD PRIMARY KEY (`IdCam`);

--
-- Indexes for table `tblcudan`
--
ALTER TABLE `tblcudan`
  ADD PRIMARY KEY (`IdCuDan`);

--
-- Indexes for table `tbllichsuguixe`
--
ALTER TABLE `tbllichsuguixe`
  ADD PRIMARY KEY (`IdGui`),
  ADD UNIQUE KEY `IdCam` (`IdCam`),
  ADD UNIQUE KEY `IdNguoiDung` (`IdNguoiDung`),
  ADD UNIQUE KEY `BienSo` (`BienSo`);

--
-- Indexes for table `tblloaixe`
--
ALTER TABLE `tblloaixe`
  ADD PRIMARY KEY (`IdLoaiXe`);

--
-- Indexes for table `tblnguoidung`
--
ALTER TABLE `tblnguoidung`
  ADD PRIMARY KEY (`IdNguoiDung`),
  ADD KEY `tblnguoidung_ibfk_1` (`IdQuyen`);

--
-- Indexes for table `tblquyen`
--
ALTER TABLE `tblquyen`
  ADD PRIMARY KEY (`IdQuyen`);

--
-- Indexes for table `tblxecudan`
--
ALTER TABLE `tblxecudan`
  ADD PRIMARY KEY (`BienSo`) USING BTREE,
  ADD UNIQUE KEY `IdCuDan` (`IdCuDan`),
  ADD UNIQUE KEY `IdLoaiXe` (`IdLoaiXe`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tbllichsuguixe`
--
ALTER TABLE `tbllichsuguixe`
  MODIFY `IdGui` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `tbllichsuguixe`
--
ALTER TABLE `tbllichsuguixe`
  ADD CONSTRAINT `tbllichsuguixe_ibfk_1` FOREIGN KEY (`IdCam`) REFERENCES `tblcamera` (`IdCam`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `tbllichsuguixe_ibfk_2` FOREIGN KEY (`IdNguoiDung`) REFERENCES `tblnguoidung` (`IdNguoiDung`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `tbllichsuguixe_ibfk_3` FOREIGN KEY (`BienSo`) REFERENCES `tblxecudan` (`BienSo`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tblnguoidung`
--
ALTER TABLE `tblnguoidung`
  ADD CONSTRAINT `tblnguoidung_ibfk_1` FOREIGN KEY (`IdQuyen`) REFERENCES `tblquyen` (`IdQuyen`) ON UPDATE NO ACTION;

--
-- Constraints for table `tblxecudan`
--
ALTER TABLE `tblxecudan`
  ADD CONSTRAINT `tblxecudan_ibfk_1` FOREIGN KEY (`IdCuDan`) REFERENCES `tblcudan` (`IdCuDan`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `tblxecudan_ibfk_2` FOREIGN KEY (`IdLoaiXe`) REFERENCES `tblloaixe` (`IdLoaiXe`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
