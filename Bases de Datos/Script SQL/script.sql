USE [master]
GO
/****** Object:  Database [estacionamiento]    Script Date: 14/04/2024 01:39:37 p. m. ******/
CREATE DATABASE [estacionamiento]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'estacionamiento', FILENAME = N'D:\AQL server express\MSSQL16.SQLEXPRESS01\MSSQL\DATA\estacionamiento.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'estacionamiento_log', FILENAME = N'D:\AQL server express\MSSQL16.SQLEXPRESS01\MSSQL\DATA\estacionamiento_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT, LEDGER = OFF
GO
ALTER DATABASE [estacionamiento] SET COMPATIBILITY_LEVEL = 160
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [estacionamiento].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [estacionamiento] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [estacionamiento] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [estacionamiento] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [estacionamiento] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [estacionamiento] SET ARITHABORT OFF 
GO
ALTER DATABASE [estacionamiento] SET AUTO_CLOSE ON 
GO
ALTER DATABASE [estacionamiento] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [estacionamiento] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [estacionamiento] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [estacionamiento] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [estacionamiento] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [estacionamiento] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [estacionamiento] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [estacionamiento] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [estacionamiento] SET  ENABLE_BROKER 
GO
ALTER DATABASE [estacionamiento] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [estacionamiento] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [estacionamiento] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [estacionamiento] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [estacionamiento] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [estacionamiento] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [estacionamiento] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [estacionamiento] SET RECOVERY SIMPLE 
GO
ALTER DATABASE [estacionamiento] SET  MULTI_USER 
GO
ALTER DATABASE [estacionamiento] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [estacionamiento] SET DB_CHAINING OFF 
GO
ALTER DATABASE [estacionamiento] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [estacionamiento] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [estacionamiento] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [estacionamiento] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
ALTER DATABASE [estacionamiento] SET QUERY_STORE = ON
GO
ALTER DATABASE [estacionamiento] SET QUERY_STORE (OPERATION_MODE = READ_WRITE, CLEANUP_POLICY = (STALE_QUERY_THRESHOLD_DAYS = 30), DATA_FLUSH_INTERVAL_SECONDS = 900, INTERVAL_LENGTH_MINUTES = 60, MAX_STORAGE_SIZE_MB = 1000, QUERY_CAPTURE_MODE = AUTO, SIZE_BASED_CLEANUP_MODE = AUTO, MAX_PLANS_PER_QUERY = 200, WAIT_STATS_CAPTURE_MODE = ON)
GO
USE [estacionamiento]
GO
/****** Object:  Table [dbo].[Administrador]    Script Date: 14/04/2024 01:39:37 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Administrador](
	[ID_administrador] [int] NOT NULL,
	[Nombre] [varchar](100) NOT NULL,
	[Usuario] [varchar](16) NOT NULL,
	[Contraseña] [varchar](16) NOT NULL,
 CONSTRAINT [PK_Administrador] PRIMARY KEY CLUSTERED 
(
	[ID_administrador] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Propietario]    Script Date: 14/04/2024 01:39:38 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Propietario](
	[ID_Propietario] [int] NOT NULL,
	[Nombre] [varchar](100) NOT NULL,
	[ApellidoP] [varchar](50) NOT NULL,
	[ApellidoM] [varchar](50) NOT NULL,
	[Matricula] [varchar](10) NOT NULL,
 CONSTRAINT [PK_Propietario] PRIMARY KEY CLUSTERED 
(
	[ID_Propietario] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Registro]    Script Date: 14/04/2024 01:39:38 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Registro](
	[ID_Registro] [int] NOT NULL,
	[ID_Administrador] [int] NOT NULL,
	[ID_Propietario] [int] NOT NULL,
 CONSTRAINT [PK_Registro] PRIMARY KEY CLUSTERED 
(
	[ID_Registro] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Vehiculo]    Script Date: 14/04/2024 01:39:38 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Vehiculo](
	[ID_Vehiculo] [int] NOT NULL,
	[Placa] [varchar](20) NOT NULL,
	[ID_Propietario] [int] NOT NULL,
 CONSTRAINT [PK_Vehiculo] PRIMARY KEY CLUSTERED 
(
	[ID_Vehiculo] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Registro]  WITH CHECK ADD  CONSTRAINT [FK_Registro_Administrador] FOREIGN KEY([ID_Administrador])
REFERENCES [dbo].[Administrador] ([ID_administrador])
GO
ALTER TABLE [dbo].[Registro] CHECK CONSTRAINT [FK_Registro_Administrador]
GO
ALTER TABLE [dbo].[Registro]  WITH CHECK ADD  CONSTRAINT [FK_Registro_Propietario] FOREIGN KEY([ID_Propietario])
REFERENCES [dbo].[Propietario] ([ID_Propietario])
GO
ALTER TABLE [dbo].[Registro] CHECK CONSTRAINT [FK_Registro_Propietario]
GO
ALTER TABLE [dbo].[Vehiculo]  WITH CHECK ADD  CONSTRAINT [FK_Vehiculo_Propietario] FOREIGN KEY([ID_Propietario])
REFERENCES [dbo].[Propietario] ([ID_Propietario])
GO
ALTER TABLE [dbo].[Vehiculo] CHECK CONSTRAINT [FK_Vehiculo_Propietario]
GO
USE [master]
GO
ALTER DATABASE [estacionamiento] SET  READ_WRITE 
GO
