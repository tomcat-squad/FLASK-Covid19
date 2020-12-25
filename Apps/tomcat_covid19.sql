-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 25 Des 2020 pada 09.03
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
-- Struktur dari tabel `dki_jakarta`
--

CREATE TABLE `dki_jakarta` (
  `id` date NOT NULL,
  `kasus_positif` int(11) NOT NULL,
  `kasus_sembuh` int(11) NOT NULL,
  `kasus_meninggal` int(11) NOT NULL,
  `Tanggal` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `dki_jakarta`
--

INSERT INTO `dki_jakarta` (`id`, `kasus_positif`, `kasus_sembuh`, `kasus_meninggal`, `Tanggal`) VALUES
('2020-12-25', 169775, 152413, 3132, '25 Dec');

-- --------------------------------------------------------

--
-- Struktur dari tabel `jawa_barat`
--

CREATE TABLE `jawa_barat` (
  `id` date NOT NULL,
  `kasus_positif` int(11) NOT NULL,
  `kasus_sembuh` int(11) NOT NULL,
  `kasus_meninggal` int(11) NOT NULL,
  `Tanggal` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `jawa_barat`
--

INSERT INTO `jawa_barat` (`id`, `kasus_positif`, `kasus_sembuh`, `kasus_meninggal`, `Tanggal`) VALUES
('2020-12-25', 77194, 63788, 1114, '25 Dec');

-- --------------------------------------------------------

--
-- Struktur dari tabel `jawa_tengah`
--

CREATE TABLE `jawa_tengah` (
  `id` date NOT NULL,
  `kasus_positif` int(11) NOT NULL,
  `kasus_sembuh` int(11) NOT NULL,
  `kasus_meninggal` int(11) NOT NULL,
  `Tanggal` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `jawa_tengah`
--

INSERT INTO `jawa_tengah` (`id`, `kasus_positif`, `kasus_sembuh`, `kasus_meninggal`, `Tanggal`) VALUES
('2020-12-25', 75226, 49953, 3056, '25 Dec');

-- --------------------------------------------------------

--
-- Struktur dari tabel `jawa_timur`
--

CREATE TABLE `jawa_timur` (
  `id` date NOT NULL,
  `kasus_positif` int(11) NOT NULL,
  `kasus_sembuh` int(11) NOT NULL,
  `kasus_meninggal` int(11) NOT NULL,
  `Tanggal` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `jawa_timur`
--

INSERT INTO `jawa_timur` (`id`, `kasus_positif`, `kasus_sembuh`, `kasus_meninggal`, `Tanggal`) VALUES
('2020-12-25', 78385, 67208, 5399, '25 Dec');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `dki_jakarta`
--
ALTER TABLE `dki_jakarta`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `jawa_barat`
--
ALTER TABLE `jawa_barat`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `jawa_tengah`
--
ALTER TABLE `jawa_tengah`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `jawa_timur`
--
ALTER TABLE `jawa_timur`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
