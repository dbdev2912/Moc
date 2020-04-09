DROP VIEW IF EXISTS CONG_NHAN, NHAN_VIEN_DAC_THU,
					XUONG_TOM_1, XUONG_TOM_2, XUONG_TOM_3, XUONG_TOM_4, XUONG_TOM_5, XUONG_TOM_6,
					XUONG_CA_PHI_LE_1, XUONG_CA_PHI_LE_2, XUONG_CA_PHI_LE_3, XUONG_CA_PHI_LE_4,
                    NHAN_VIEN_TOA_HANH_CHINH;
                               
DROP PROCEDURE IF EXISTS TIM_XUONG;
DROP PROCEDURE IF EXISTS THEM_CN;
DROP PROCEDURE IF EXISTS THEM_NVDT;
DROP PROCEDURE IF EXISTS THEM_NHAN_VIEN_TOA_HANH_CHINH;

CREATE VIEW CONG_NHAN AS 
	SELECT C.MACN, HOTEN, DATE_FORMAT(NGAYSINH, '%d/%m/%Y') AS NGAYSINH, TENTINH AS DIACHI, GIOITINH, LUONG, CASE WHEN GHICHU='NULL' THEN '--' ELSE GHICHU END AS GHICHU
	FROM CONGNHAN AS C 
		INNER JOIN TINH AS T ON T.MATINH=C.MATINH 
			INNER JOIN PHANCONG AS P ON P.MACN = C.MACN 
				INNER JOIN CONGVIEC AS V ON MID(P.MACN, 4, 3)=V.LOAISP AND V.MACV=P.MACV
	ORDER BY C.MACN;

CREATE VIEW NHAN_VIEN_DAC_THU AS
	SELECT MANV, HOTEN, DATE_FORMAT(NGAYSINH, '%d/%m/%Y') AS NGAYSINH, GIOITINH, CONGVIEC, TENTINH, LUONG
    FROM NHANVIENDACTHU AS N 
		INNER JOIN TINH AS T ON T.MATINH=N.MATINH
	ORDER BY N.MANV;

CREATE VIEW XUONG_TOM_1 AS
	SELECT C.MACN, HOTEN, DATE_FORMAT(NGAYSINH, '%d/%m/%Y') AS NGAYSINH, TENTINH AS DIACHI, GIOITINH, LUONG, CASE WHEN GHICHU='NULL' THEN '--' ELSE GHICHU END AS GHICHU
	FROM CONGNHAN AS C 
		INNER JOIN TINH AS T ON T.MATINH=C.MATINH 
			INNER JOIN PHANCONG AS P ON P.MACN = C.MACN 
				INNER JOIN CONGVIEC AS V ON MID(P.MACN, 4, 3)=V.LOAISP AND V.MACV=P.MACV
	WHERE MID(C.MACN, 4, 4) = 'CBT1'
	ORDER BY C.MACN;
    
CREATE VIEW XUONG_TOM_2 AS
	SELECT C.MACN, HOTEN, DATE_FORMAT(NGAYSINH, '%d/%m/%Y') AS NGAYSINH, TENTINH AS DIACHI, GIOITINH, LUONG, CASE WHEN GHICHU='NULL' THEN '--' ELSE GHICHU END AS GHICHU
	FROM CONGNHAN AS C 
		INNER JOIN TINH AS T ON T.MATINH=C.MATINH 
			INNER JOIN PHANCONG AS P ON P.MACN = C.MACN 
				INNER JOIN CONGVIEC AS V ON MID(P.MACN, 4, 3)=V.LOAISP AND V.MACV=P.MACV
	WHERE MID(C.MACN, 4, 4) = 'CBT2'
	ORDER BY C.MACN;

CREATE VIEW XUONG_TOM_3 AS
	SELECT C.MACN, HOTEN, DATE_FORMAT(NGAYSINH, '%d/%m/%Y') AS NGAYSINH, TENTINH AS DIACHI, GIOITINH, LUONG, CASE WHEN GHICHU='NULL' THEN '--' ELSE GHICHU END AS GHICHU
	FROM CONGNHAN AS C 
		INNER JOIN TINH AS T ON T.MATINH=C.MATINH 
			INNER JOIN PHANCONG AS P ON P.MACN = C.MACN 
				INNER JOIN CONGVIEC AS V ON MID(P.MACN, 4, 3)=V.LOAISP AND V.MACV=P.MACV
	WHERE MID(C.MACN, 4, 4) = 'CBT3'
	ORDER BY C.MACN;
    
CREATE VIEW XUONG_TOM_4 AS
	SELECT C.MACN, HOTEN, DATE_FORMAT(NGAYSINH, '%d/%m/%Y') AS NGAYSINH, TENTINH AS DIACHI, GIOITINH, LUONG, CASE WHEN GHICHU='NULL' THEN '--' ELSE GHICHU END AS GHICHU
	FROM CONGNHAN AS C 
		INNER JOIN TINH AS T ON T.MATINH=C.MATINH 
			INNER JOIN PHANCONG AS P ON P.MACN = C.MACN 
				INNER JOIN CONGVIEC AS V ON MID(P.MACN, 4, 3)=V.LOAISP AND V.MACV=P.MACV
	WHERE MID(C.MACN, 4, 4) = 'CBT4'
	ORDER BY C.MACN;

CREATE VIEW XUONG_TOM_5 AS
	SELECT C.MACN, HOTEN, DATE_FORMAT(NGAYSINH, '%d/%m/%Y') AS NGAYSINH, TENTINH AS DIACHI, GIOITINH, LUONG, CASE WHEN GHICHU='NULL' THEN '--' ELSE GHICHU END AS GHICHU
	FROM CONGNHAN AS C 
		INNER JOIN TINH AS T ON T.MATINH=C.MATINH 
			INNER JOIN PHANCONG AS P ON P.MACN = C.MACN 
				INNER JOIN CONGVIEC AS V ON MID(P.MACN, 4, 3)=V.LOAISP AND V.MACV=P.MACV
	WHERE MID(C.MACN, 4, 4) = 'CBT5'
	ORDER BY C.MACN;

CREATE VIEW XUONG_TOM_6 AS
	SELECT C.MACN, HOTEN, DATE_FORMAT(NGAYSINH, '%d/%m/%Y') AS NGAYSINH, TENTINH AS DIACHI, GIOITINH, LUONG, CASE WHEN GHICHU='NULL' THEN '--' ELSE GHICHU END AS GHICHU
	FROM CONGNHAN AS C 
		INNER JOIN TINH AS T ON T.MATINH=C.MATINH 
			INNER JOIN PHANCONG AS P ON P.MACN = C.MACN 
				INNER JOIN CONGVIEC AS V ON MID(P.MACN, 4, 3)=V.LOAISP AND V.MACV=P.MACV
	WHERE MID(C.MACN, 4, 4) = 'CBT6'
	ORDER BY C.MACN;

CREATE VIEW XUONG_CA_PHI_LE_1 AS
	SELECT C.MACN, HOTEN, DATE_FORMAT(NGAYSINH, '%d/%m/%Y') AS NGAYSINH, TENTINH AS DIACHI, GIOITINH, LUONG, CASE WHEN GHICHU='NULL' THEN '--' ELSE GHICHU END AS GHICHU
	FROM CONGNHAN AS C 
		INNER JOIN TINH AS T ON T.MATINH=C.MATINH 
			INNER JOIN PHANCONG AS P ON P.MACN = C.MACN 
				INNER JOIN CONGVIEC AS V ON MID(P.MACN, 4, 3)=V.LOAISP AND V.MACV=P.MACV
	WHERE MID(C.MACN, 4, 4) = 'CPL1'
	ORDER BY C.MACN;

CREATE VIEW XUONG_CA_PHI_LE_2 AS
	SELECT C.MACN, HOTEN, DATE_FORMAT(NGAYSINH, '%d/%m/%Y') AS NGAYSINH, TENTINH AS DIACHI, GIOITINH, LUONG, CASE WHEN GHICHU='NULL' THEN '--' ELSE GHICHU END AS GHICHU
	FROM CONGNHAN AS C 
		INNER JOIN TINH AS T ON T.MATINH=C.MATINH 
			INNER JOIN PHANCONG AS P ON P.MACN = C.MACN 
				INNER JOIN CONGVIEC AS V ON MID(P.MACN, 4, 3)=V.LOAISP AND V.MACV=P.MACV
	WHERE MID(C.MACN, 4, 4) = 'CPL2'
	ORDER BY C.MACN;

CREATE VIEW XUONG_CA_PHI_LE_3 AS
	SELECT C.MACN, HOTEN, DATE_FORMAT(NGAYSINH, '%d/%m/%Y') AS NGAYSINH, TENTINH AS DIACHI, GIOITINH, LUONG, CASE WHEN GHICHU='NULL' THEN '--' ELSE GHICHU END AS GHICHU
	FROM CONGNHAN AS C 
		INNER JOIN TINH AS T ON T.MATINH=C.MATINH 
			INNER JOIN PHANCONG AS P ON P.MACN = C.MACN 
				INNER JOIN CONGVIEC AS V ON MID(P.MACN, 4, 3)=V.LOAISP AND V.MACV=P.MACV
	WHERE MID(C.MACN, 4, 4) = 'CPL3'
	ORDER BY C.MACN;

CREATE VIEW XUONG_CA_PHI_LE_4 AS
	SELECT C.MACN, HOTEN, DATE_FORMAT(NGAYSINH, '%d/%m/%Y') AS NGAYSINH, TENTINH AS DIACHI, GIOITINH, LUONG, CASE WHEN GHICHU='NULL' THEN '--' ELSE GHICHU END AS GHICHU
	FROM CONGNHAN AS C 
		INNER JOIN TINH AS T ON T.MATINH=C.MATINH 
			INNER JOIN PHANCONG AS P ON P.MACN = C.MACN 
				INNER JOIN CONGVIEC AS V ON MID(P.MACN, 4, 3)=V.LOAISP AND V.MACV=P.MACV
	WHERE MID(C.MACN, 4, 4) = 'CPL4'
	ORDER BY C.MACN;

DELIMITER $$
CREATE PROCEDURE TIM_XUONG
(
	IN MAXUONG VARCHAR(4)
)
BEGIN
	SELECT C.MACN, HOTEN, DATE_FORMAT(NGAYSINH, '%d/%m/%Y') AS NGAYSINH, TENTINH AS DIACHI, GIOITINH, LUONG, CASE WHEN GHICHU='NULL' THEN '--' ELSE GHICHU END AS GHICHU
	FROM CONGNHAN AS C 
		INNER JOIN TINH AS T ON T.MATINH=C.MATINH 
			INNER JOIN PHANCONG AS P ON P.MACN = C.MACN 
				INNER JOIN CONGVIEC AS V ON MID(P.MACN, 4, 3)=V.LOAISP AND V.MACV=P.MACV
	WHERE MID(C.MACN, 4, 4) = MAXUONG
	ORDER BY C.MACN;
END $$

DELIMITER $$
CREATE PROCEDURE THEM_CN
(
	IN MACN CHAR(11), 
    IN HOTEN NVARCHAR(100),
    IN NGAY_SINH TINYINT,
    IN THANG_SINH TINYINT,
    IN NAM_SINH SMALLINT,
    IN MATINH TINYINT,
    IN GIOITINH NVARCHAR(3),
    IN GHICHU NVARCHAR(255)
)
BEGIN
	INSERT INTO CONGNHAN VALUES(MANC, HOTEN, CONCAT(NAM_SINH, '-', THANG_SINH,'-', NGAY_SINH), MATINH, GIOITINH, GHICHU);
END $$

DELIMITER $$
CREATE PROCEDURE THEM_NVDT
(
	IN MANV CHAR(11), 
    IN HOTEN NVARCHAR(100),
    IN NGAY_SINH TINYINT,
    IN THANG_SINH TINYINT,
    IN NAM_SINH SMALLINT,
    IN CONGVIEC NVARCHAR(255),
    IN MATINH TINYINT, 
    IN GIOITINH NVARCHAR(3),
    IN LUONG INT
)
BEGIN
	INSERT INTO CONGNHAN VALUES(MANV, HOTEN, CONCAT(NAM_SINH, '-', THANG_SINH,'-', NGAY_SINH), CONGVIEC, MATINH, GIOITINH, LUONG);
END $$

DELIMITER $$
CREATE PROCEDURE THEM_NHAN_VIEN_TOA_HANH_CHINH
(
	IN MANV VARCHAR(5), 
    IN MAPB VARCHAR(2), 
    IN HOTEN NVARCHAR(100),
    IN NGAY_SINH TINYINT,
    IN THANG_SINH TINYINT,
    IN NAM_SINH SMALLINT,
    IN GIOITINH NVARCHAR(5),
    IN MATINH TINYINT, 
    IN CONGVIEC NVARCHAR(100),
    IN LUONG INT
)
BEGIN 
	INSERT INTO NHANVIEN VALUES(MANV, MAPB, HOTEN, CONCAT(NAM_SINH, '-', THANG_SINH,'-', NGAY_SINH), GIOITINH, MATINH, CONGVIEC, LUONG);
END $$

CREATE VIEW NHAN_VIEN_TOA_HANH_CHINH AS
	SELECT HOTEN, MANV, TENPB, CONGVIEC, DATE_FORMAT(NGAYSINH, '%d/%m/%Y') AS NGAYSINH, GIOITINH, LUONG, TENTINH
    FROM NHANVIEN AS N 
		INNER JOIN TINH AS T ON T.MATINH=N.MATINH
			INNER JOIN PHONGBAN AS P ON P.MAPB = N.MAPB
	ORDER BY P.MAPB;












		