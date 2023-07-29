@echo off
cls
title SETUP PIP

REM Kiểm tra sự tồn tại của Python trên máy người dùng
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Bạn chưa cài đặt Python. Vui lòng tải và cài đặt Python tại trang web https://python.org/download!
    timeout 12 /nobreak
    exit
)

REM Tiếp tục với các hành động khác nếu Python đã được cài đặt
goto :SETUP

:SETUP
echo.
echo Đang kiểm tra cập nhật thư viện...
python.exe -m pip install --upgrade pip >nul 2>&1
if %errorlevel% equ 0 (
    echo Đã cập nhật phiên bản mới nhất của pip installer.
    timeout /t 2 /nobreak
    cls
) else (
    echo Không có phiên bản pip installer mới.
    timeout /t 3 /nobreak
    cls
)
echo.

REM Kiểm tra và cài đặt các thư viện cần thiết nếu chưa có
echo Đang kiểm tra và cài đặt các thư viện cần thiết...

pip install --upgrade wheel > nul

REM Danh sách thư viện cần kiểm tra và cài đặt
set "libraries=playsound psutil tk pygame mutagen tabulate openpyxl speedtest  pyqt5 wikipedia youtube_search pyttsx3 pyautogui pyinstaller pytube win10toast clipboard requests opencv-python playsound speechrecognition pyaudio gTTS qrcode pyzbar pystray selenium webdriver_manager youtube-search-python pysmartdl"

REM Lặp qua danh sách thư viện và kiểm tra cài đặt
set "required_libraries="
set "installed_libraries=0"

for %%i in (%libraries%) do (
    pip show %%i >nul 2>&1
    if !errorlevel! neq 0 (
        echo Đang cài đặt thư viện %%i...
        call :install_library %%i
    ) else (
        echo Đã cài đặt sẵn thư viện %%i.
        set /a installed_libraries+=1
    )
)

echo.
echo Đã cài đặt các thư viện cần thiết.
echo.

echo 1. Các thư viện yêu cầu:%required_libraries%
echo 2. Thư viện đã được cài thêm: %installed_libraries%/%libraries%

echo.
echo Bấm phím bất kỳ để thoát...
pause >nul
exit

:install_library
@REM pip install "%~1" >nul 2>&1
pip install "%~1"
exit /b