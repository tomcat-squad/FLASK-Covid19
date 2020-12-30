-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 30 Des 2020 pada 08.39
-- Versi server: 10.4.14-MariaDB
-- Versi PHP: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tomcat_covid19`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `bekasi_barat`
--

CREATE TABLE `bekasi_barat` (
  `id` date NOT NULL,
  `daily_konfirmasi` int(11) NOT NULL,
  `Tanggal` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `bekasi_barat`
--

INSERT INTO `bekasi_barat` (`id`, `daily_konfirmasi`, `Tanggal`) VALUES
('2020-12-29', 25, '29 Dec'),
('2020-12-30', 11, '30 Dec');

-- --------------------------------------------------------

--
-- Struktur dari tabel `bekasi_selatan`
--

CREATE TABLE `bekasi_selatan` (
  `id` date NOT NULL,
  `daily_konfirmasi` int(11) NOT NULL,
  `Tanggal` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `bekasi_selatan`
--

INSERT INTO `bekasi_selatan` (`id`, `daily_konfirmasi`, `Tanggal`) VALUES
('2020-12-29', 25, '29 Dec'),
('2020-12-30', 20, '30 Dec');

-- --------------------------------------------------------

--
-- Struktur dari tabel `bekasi_timur`
--

CREATE TABLE `bekasi_timur` (
  `id` date NOT NULL,
  `daily_konfirmasi` int(11) NOT NULL,
  `Tanggal` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `bekasi_timur`
--

INSERT INTO `bekasi_timur` (`id`, `daily_konfirmasi`, `Tanggal`) VALUES
('2020-12-29', 42, '29 Dec'),
('2020-12-30', 7, '30 Dec');

-- --------------------------------------------------------

--
-- Struktur dari tabel `bekasi_utara`
--

CREATE TABLE `bekasi_utara` (
  `id` date NOT NULL,
  `daily_konfirmasi` int(11) NOT NULL,
  `Tanggal` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `bekasi_utara`
--

INSERT INTO `bekasi_utara` (`id`, `daily_konfirmasi`, `Tanggal`) VALUES
('2020-12-29', 53, '29 Dec'),
('2020-12-30', 5, '30 Dec');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `bekasi_barat`
--
ALTER TABLE `bekasi_barat`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `bekasi_selatan`
--
ALTER TABLE `bekasi_selatan`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `bekasi_timur`
--
ALTER TABLE `bekasi_timur`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `bekasi_utara`
--
ALTER TABLE `bekasi_utara`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
