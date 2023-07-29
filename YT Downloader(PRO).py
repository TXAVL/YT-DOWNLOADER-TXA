#VUI LÒNG KHÔNG ĐƯỢC CHỈNH SỬA BẤT KÌ NỘI DUNG NÀO BÊN DƯỚI NHÉ!
#CHỈ ĐƯỢC THAM KHẢO THUI


#👉Mọi thắc mắc vui lòng ib qua fb: https://bom.so/FB_ADMIN

#©️NGUỒN: TXA VLOG!!
from tkinter import *
import requests, pyautogui
from pathlib import Path
import locale
from datetime import datetime
from gtts import gTTS
# import speedtest
import os
import playsound
from time import strftime, gmtime
from pytube import request
import pytube as pyt
from pytube import YouTube
from tkinter import filedialog, colorchooser
from tkinter import messagebox
from configparser import ConfigParser
import os,sys,clipboard
from win10toast import ToastNotifier
import _thread, re
from tkinter.ttk import Progressbar
from tkinter.ttk import Combobox
from datetime import datetime,date
from random import random
from random import randint
from random import seed
import time, getpass
from pystray import MenuItem as item
import pystray
from PIL import Image, ImageTk
# import pywin32
from tkinter import ttk
import subprocess, psutil
import urllib.request
import threading
from pySmartDL import SmartDL
from tqdm import tqdm
import re
from pytube.helpers import safe_filename
import urllib.request
import threading, json
import pyperclip
import clipboard
import base64
import socket, sys

#KTRA 
toaster = ToastNotifier()
# Tên file thực thi của ứng dụng
app_exe = "YT DOWNLOADER TXA PRO V3.7.5.exe"

# Lấy đường dẫn tuyệt đối đến thư mục chứa script hiện tại
script_dir = os.path.dirname(os.path.abspath(__file__))

# Lấy đường dẫn tuyệt đối đến file thực thi của ứng dụng
app_path = os.path.join(script_dir, app_exe)

# Kiểm tra tất cả các tiến trình đang chạy
for proc in psutil.process_iter(['pid', 'exe']):
    # Kiểm tra đường dẫn thực thi của tiến trình
    try:
        if proc.exe() == app_path:
            # Hiển thị thông báo và thoát khỏi ứng dụng
            messagebox.showinfo("Thông báo", "Ứng dụng đang chạy rồi mở nữa làm gì!")
            os._exit(0) # Thoát chương trình
    except psutil.AccessDenied:
        pass

    # Nếu không có tiến trình nào đang chạy với đường dẫn thực thi là app_path, tiếp tục chạy chương trình
print("Không có ứng dụng đang chạy")

log_file = 'download_log.txa'
download_count = 0

#LẤY TÊN NGƯỜI DÙNG
username = getpass.getuser()

# Khởi tạo biến lưu trữ nội dung clipboard trước đó
last_clipboard_content = ""

# BTHUC
url_regex = r"(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})"
url_short = r"(https?://)?(www\.)?(youtube\.com/shorts/|youtu\.be/)([a-zA-Z0-9_-]{11})"

# Hàm bắt sự kiện khi người dùng quay lại ứng dụng
def on_focus(event):
    global last_clipboard_content

    # Đọc nội dung trong clipboard
    clipboard_content = pyperclip.paste()

    # Kiểm tra nội dung có phải là link YouTube hay không
    if detect_link and ("https://youtube.com/watch" in clipboard_content or
            "https://youtu.be/" in clipboard_content or
            "http://youtube.com/watch" in clipboard_content or
            "http://youtu.be/" in clipboard_content or
            "https://www.youtube.com/watch" in clipboard_content):

        # Kiểm tra nội dung clipboard có thay đổi so với trước đó hay không
        if clipboard_content != last_clipboard_content:
            # Cập nhật nội dung clipboard trước đó
            last_clipboard_content = clipboard_content

            # Thông báo cho người dùng
            messagebox.showinfo("Clipboard Notification",
                                "Đã tìm thấy link YouTube trong clipboard.\nĐã dán link video đầu tiên vào ô nhập URL.")
            # Điền nội dung vào ô url
            url_entry.delete(0, END)
            url_entry.insert(0, clipboard_content)
    else:
        pass

# Khởi tạo biến Boolean để lưu trữ tùy chọn nhận diện link YouTube
detect_link = True

now = datetime.now()
hour = now.strftime("%H")
minute = now.strftime("%M")
second = now.strftime("%S")
day = now.strftime("%d")
month = now.strftime("%m")
year = now.strftime("%Y")
fr = strftime("%Y-%m-%d %H:%M:%S", gmtime())



# # create speedtest object
# st = speedtest.Speedtest()

# # test download speed
# download_speed = st.download()

# # convert download speed from bytes per second to megabits per second
# download_speed_mbps = download_speed / 1000000

# #NGÔN NGỮ ỨNG DỤNG:
# Lấy ngôn ngữ hệ thống
lang_sys = locale.getpreferredencoding()
print(lang_sys)

with open("LANG.txa", "w") as f:
    f.write('NGÔN NGỮ HỆ THỐNG LÀ: ')
    f.write(lang_sys)
    f.write('\n')
    f.close()


#DATE UPDATED
hour1 = time.strftime("%H")
minute1 = time.strftime("%M")
second1 = time.strftime("%S")
day1 = time.strftime("%d")
month1 = time.strftime("%m")
year1 = time.strftime("%Y")
#GET DATA WITH OTHER
na_dat = day1+'/'+month1+'/'+year1+' '+hour1+':'+minute1+':'+second1

t = ToastNotifier()
path_to_file = 'user_pro.ini'
path = Path(path_to_file)


if path.is_file():
   pass
else:
    if lang_sys == 'vi_VN' or lang_sys == "cp65001":
        messagebox.showwarning("ERROR VN","Không tìm thấy file cấu hình(user_pro.ini) để đọc dữ liệu!\nVui lòng thêm nó từ trang web https://github.com/TXAVL/YT-DOWNLOADER-TXA/blob/main/user_pro.ini nếu k có hoặc xem lại thư mục cài đặt ứng dụng!\nĐể chỉnh sửa lại tên file!\n Còn nếu không đươc nữa thì ib qua fb ở menu Help nhé!")
    else:
        messagebox.showwarning(f"ERROR ({lang_sys})","Can't find configuration file(user_pro.ini) to read data!\nPlease add it from website https://github.com/TXAVL/YT-DOWNLOADER-TXA/blob/main/user_pro.ini if ​​not available or check app installation directory! \nTo edit the filename!")
    raise SystemExit(0)

def check_internet_connection():
    try:
        # Kiểm tra kết nối bằng cách mở một URL
        urllib.request.urlopen('https://yt-txa.mw.lt', timeout=1)
        return True
    except urllib.request.URLError as err:
        return False

def check_network_connection():
    try:
        # Kiểm tra kết nối bằng cách tạo một socket
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False

def start_application():
    if check_internet_connection() and check_network_connection():
        # Ứng dụng của bạn bắt đầu ở đây
        messagebox.showinfo("Kết nối thành công✅✅✅", "☑️✔️Kết nối thành công tới server!")
    else:
        wifi_icon = "📶"
        messagebox.showerror("Kết nối thất bại tới server của chúng tôi❌❌", f"{wifi_icon} Bạn hiện không có kết nối mạng vì vậy sẽ không truy cập được vào ứng dụng!\nVui lòng kết nối mạng và thử lại!!! ❤️❤️")
        sys.exit()

# messagebox.showinfo(f"Xin chào {username}!", "Đang load thư viện trước khi vô app....! \n👉 ©️COPY BY TXA VLOG!")
# messagebox.showinfo(f"Cảnh cáo {username} nhé!", "Vui lòng đợi đi nào.......!")
# messagebox.showinfo(f"Cảnh cáo {username} nhé!", "Vui lòng đợi đi nào.......!")
# messagebox.showinfo(f"Cảnh cáo {username} nhé!", "Đã bảo là đợi đi mà.......!")
# messagebox.showinfo(f"Cảnh cáo {username} nhé!", "Vui lòng đợi đi nào.......!")
# messagebox.showinfo(f"Cảnh cáo {username} nhé!", "Vui lòng đợi đi nào.......!")
# messagebox.showinfo(f"Cảnh cáo {username} nhé!", "Sắp xong rồi.......!")
# messagebox.showinfo(f"Cảnh cáo {username} nhé!", "Vui lòng đợi đi nào.......!")
# messagebox.showinfo(f"Cảnh cáo {username} nhé!", "Vui lòng đợi đi nào.......!")
# messagebox.showinfo(f"Cảnh cáo {username} nhé!", "Vui lòng đợi đi nào.......!")
# messagebox.showinfo("LOAD DONE!", f"Cảm ơn vì đã đợi nhé {username}!")

txa = Tk()
txa.geometry('670x500')
txa.resizable(0,0)
txa.title(f"Trình tải xuống video Youtube V3.7.5 - Pro(USER: {username})")
# txa.title("Trình tải xuống video Youtube - DEMO")
txa.resizable(False, False)
# txa.iconbitmap('logo.ico')

#ĐỌC FILE CẤU HÌNH
parser = ConfigParser()
parser.read('user_pro.ini')
save_bgcolor = parser.get('setting', 'bg_color')
save_path = parser.get('setting', 'noiluu')
save_tttb = parser.get('setting', 'tbao')
save_migi = parser.get('setting', 'migi')
title_ban = parser.set('setting', 'phienban', 'PRO')
lay_ngay = parser.get('setting', 'ngayhientai')
save_exit = parser.get('setting', 'tbao_exit')
detect_link = parser.get('setting', 'detect_link')
na_dat = str(day)+'/'+str(month)+'/'+str(year)+' '+str(hour)+':'+str(minute)+':'+str(second)
set_ngay = parser.set('setting', 'ngayhientai', na_dat)
with open ('user_pro.ini', 'w') as f:
    parser.write(f)
txa.configure(background=save_bgcolor)
print(na_dat+""+"\nTrạng thái giọng nói:" +save_migi)
print("MA EXIT: "+save_exit)
print(save_path)
print(save_bgcolor)
print("Thời gian mở lần cuối: ",lay_ngay, f'bởi {username}')
print("Trạng thái thông báo: ",save_tttb)
print("Nhận diện link video khi quay lại ứng dụng:", detect_link)
# Biến toàn cục để lưu tiêu đề
selected_title = ""

# Kiểm tra và tạo file lịch sử nếu không tồn tại
if not os.path.exists(log_file):
    with open(log_file, 'w') as f:
        f.write('')

# Load danh sách lịch sử từ file
with open(log_file, 'r') as f:
    history = f.read().splitlines()

# Cập nhật danh sách tải xuống (downloads) từ lịch sử
downloads = []
for entry in history:
    match = re.match(r"URL BẠN NHẬP: (.+) \(Vào lúc (.+)\)", entry)
    if match:
        url = match.group(1)
        download_time = match.group(2)
        downloads.append({"URL": url, "Thời gian": download_time.strip()})

def save_history():
    with open(log_file, 'w') as f:
        for download in downloads:
            f.write(f"URL BẠN NHẬP: {download['URL']} (Vào lúc {download['Thời gian']})\n")
# # def check_inter():
#     st = speedtest.Speedtest()
#     download_speed = st.download()
#     download_speed_vv = download_speed / 1e6  # Trả về tốc độ download tính bằng Mbps'

#     #KTRA MẠNG TRC KHI TRUY CẬP
#     download_speed_mbps = download_speed_vv

#     if download_speed_mbps <= 2:
#         if lang_sys == 'vi_VN':
#             mang.config(text="Tốc độ mạng của bạn quá chậm ({:.1f} Mbps), \n hãy kiểm tra lại đường truyền của bạn xem có ổn định hay không!\n Nếu không sẽ không thể tải video đc!".format(download_speed_mbps))
#         else:
#             mang.config(text="Network speed is too low: {:.1f} Mbps!. \n Please check your internet speed!\n If no, you don't download video!".format(download_speed_mbps))
#     else:
#         mang.config(text='', background='red', foreground='yellow')
#     with open("DATA TEST SPEED.txa", "w") as f:
#         f.write("TỐc độ mạng hiện tại của bạn là: "+ str(download_speed_mbps)+ " MBPS!\n")
#         f.write('©️COPY BY TXA VLOG!\n YOU ARE PRO VERSION APP!!!!🖖😇\n')
#         f.close()
#     print("Tốc độ mạng: "+str(download_speed_mbps))

def donglenh():
    print("©️Phần mềm : YT DOWNLOADER TXA!")
    print("©️Nguồn: TXA VLOG!")
    print("👉Công cụ chạy dòng lệnh: txa-build!")
    print("👉Ver: 1.0!")
    lenh = input("Nhập lệnh(txa --l hoặc là txa --help hoặc là txa -h): ")
    cmdArray = lenh.split(' ')
    while True:
        if len(cmdArray) == 2 and \
            cmdArray[0] == 'txa --l' and \
            cmdArray[1] == '--lol' or cmdArray[1] == '-l':
            lenh = "python . --lol" + cmdArray[1]
            subprocess.call(lenh, shell=True)
            ucc=True
        elif lenh == 'txa --help' or lenh == 'txa -h':
            ucc=False
            print("HELLO")
            break
        else:
            print("Sai lệnh r vui lòng nhập lại....")
          

def update(event=None):
    start_time_2 = time.time()  # Khởi tạo biến start_time
    def check_for_updates():
        # Disable the Check for Updates button to prevent multiple updates
        check_for_updates_button.config(state=DISABLED)

        # Define the update function to run in a separate thread
        def do_update():
            try:
                # Get the version data from the web
                # url = 'https://txaml.viwap.com/get-version.json'
                url = 'https://yt-txa.mw.lt/get-version.json'
                response = urllib.request.urlopen(url)
                data = json.loads(response.read())

                # Get the current version and compare it to the online version
                current_version = f"3.7.5"
                online_version = f"{data['pban_pro']}"
                if current_version == online_version:
                    if lang_sys == 'vi_VN' or lang_sys == "cp65001":
                        messagebox.showinfo("Không có bản cập nhật khả dụng", "App của bạn đã được cập nhật ở phiên bản mới nhất😂.")
                    else:
                        messagebox.showinfo("No update found", "YOU ARE LASTED VERSION😂.")
                    #update.destroy()
                    raise SystemExit(0)
                else:
                    # Prompt the user to download the update
                    if lang_sys == 'vi_VN' or lang_sys == "cp65001":
                        if messagebox.askyesno("Cập nhật khả dụng", f"Có 1 phiên bản mới: v{online_version} được tìm thấy trên trang web của chúng tôi vào ngày {data['day']}/{data['mon']}/{data['year']}.\n Bạn có muốn tải nó ngay bây giờ?"):
                            # Download the updated file
                            download_url = data["server_file_pro"]
                            pattern = r'"(https://download[^"]+)"'
                            response = requests.get(download_url)
                            matches = re.findall(pattern, response.text)
                            if not matches:
                                print("Lỗi không tìm thấy link!!")
                                return
                            download_link = matches[0]
                            filename = download_link.split("/")[-1]
                            download_and_install(download_link, filename)
                    else:
                        if messagebox.askyesno("Update available", f"There is a new version:{online_version} found on our website on {data['day']}/{data['mon' ]}/{data['year']}.\n Would you like to download it now?"):
                            # Download the updated file
                            download_url = data["server_file_pro"]
                            pattern = r'"(https://download[^"]+)"'
                            response = requests.get(download_url)
                            matches = re.findall(pattern, response.text)
                            if not matches:
                                print("Unable to find the download link.")
                                return
                            download_link = matches[0]
                            filename = download_link.split("/")[-1]
                            download_and_install(download_link, filename)
            except Exception as e:
                da = str(e)
                if 'server_file_pro' in da:
                    messagebox.showerror("Lỗi", "Không thể tìm thấy link trên Server của chúng tôi!!!❌")
                elif 'failed to respond' in da:
                    messagebox.showerror("ERROR❌","Không thể kết nối đến server của chúng tôi!Vui lòng thử lại sau giây lát!\nHoặc liên hệ qua FB: https://bom.so/FB_ADMIN!❌❎")
                
                else:
                    messagebox.showerror("Error❌", str(e))
                raise SystemExit(0)

            # Re-enable the Check for Updates button
            check_for_updates_button.config(state=NORMAL)

        # Start the update thread
        update_thread = threading.Thread(target=do_update)
        update_thread.start()

    def download_and_install(download_url, filename):
        response = requests.get(download_url, stream=True)
        if response.status_code != 200:
            print("Unable to download the file.")
            return

        # Save the file to the specified output path
        with open(filename, "wb") as f, tqdm(
            total=int(response.headers.get("content-length", 0)), unit="B", unit_scale=True, unit_divisor=1024, ncols=80
        ) as progress_bar:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    progress_bar.update(len(chunk))

                    # Update the progress label
                    downloaded_size = os.path.getsize(filename)
                    total_size = int(response.headers.get("content-length", 0))
                    progress_percentage = (downloaded_size / total_size) * 100

                    # Format progress percentage with leading zero if less than 10
                    formatted_percentage = f"{progress_percentage:.2f}"
                    if progress_percentage < 10:
                        formatted_percentage = f"0{formatted_percentage}"

                    # Calculate remaining time
                    elapsed_time = time.time() - start_time_2
                    remaining_size = total_size - downloaded_size
                    download_speed = downloaded_size / elapsed_time if elapsed_time > 0 else 0
                    remaining_time = remaining_size / download_speed if download_speed > 0 else 0
                    remaining_minutes = int(remaining_time / 60)
                    remaining_seconds = int(remaining_time % 60)

                    # Update the progress label
                    progress_label.config(
                        text=f"Đang tải xuống... {formatted_percentage}% - Thời gian còn lại: {remaining_minutes}m {remaining_seconds}s"
                    )

                    # Update the Tkinter window
                    update.update()

        # Prompt the user to install the update
        if messagebox.askyesno("Cập nhật thành công", "Tải xuống thành công, bạn có muốn cài đặt nó bây giờ không?"):
            subprocess.Popen([filename], shell=True)
            update.destroy()  # Quit the application without waiting for the installation process
        else:
            update.destroy()
    # Create the main window
    update = Toplevel(txa)
    update.geometry("350x150")
    update.grab_set() # Vô hiệu hóa cửa sổ cha
    update.resizable(0,0)
    def on_close_settings():
        if messagebox.askokcancel("Thoát ứng dụng", "Bạn có chắc muốn thoát?"):
            update.grab_release() # Kích hoạt lại cửa sổ cha
            update.destroy()
        else:
            pass
    if lang_sys == 'vi_VN' or lang_sys == "cp65001":
        update.title("Kiểm tra cập nhật ứng dụng")
    else:
        update.title("WINDOWS CHECK UPDATE APP")

    # Create the Check for Updates button
    check_for_updates_button = Button(update, text="Check for Updates", command=check_for_updates)
    check_for_updates_button.pack(pady=10)

    # Create the progress bar and label
    progress_bar = ttk.Progressbar(update, orient='horizontal', mode='determinate')
    progress_label = Label(update, text="")
    progress_bar.pack(pady=10)
    progress_label.pack(pady=5)
    update.protocol("WM_DELETE_WINDOW", on_close_settings)
    # Start the Tkinter event loop
    update.mainloop()

# txa.configure(background='black')

#HAM SETTING
def changebg(event=None):
    
    color2 = colorchooser.askcolor()[1]
    if color2:
        if color2 == '#0d0006' or color2 == '#020202' or color2 == '#121212' or color2 == '#070707':
            color2 = 'black'
        else:
            parser.set('setting','bg_color',color2)
        with open('user_pro.ini','w') as f:
            parser.write(f)
        txa.configure(background=color2)

def resetbg(event=None):
    color2 = 'black'
    parser.set('setting','bg_color',color2)
    with open('user_pro.ini','w') as f:
            parser.write(f)
    txa.configure(background=color2)

#IN VỊ TRÍ CON TRỎ CHUỘT
def print_mouse_position(event):
    x, y = pyautogui.position()
    print("Mouse position - x: {}, y: {}".format(x, y))

def setting(event=None):
    uk = Toplevel(txa)
    uk.title("Cài đặt")
    uk.geometry('400x400')
    uk.resizable(False, False)
    uk.grab_set()
    save_tttb = parser.get('setting', 'tbao')
    save_migi = parser.get('setting', 'migi')
    save_exit = parser.get('setting', 'tbao_exit')
    detect_link = parser.get('setting', 'detect_link')
    check_duration = parser.get('setting', 'duration')
    var = IntVar()
    bar = IntVar()
    den = IntVar()
    time_entry_var = StringVar()

    if lang_sys == 'vi_VN' or lang_sys == "cp65001":
        anh = Label(uk, text='Thông báo khi tải xong: ',borderwidth=3, relief="raised", font=("Verdana italic", 13), background='red')
        anh.place(x=10, y=5)
        ban = Label(uk, text='Thông báo bằng giọng nói: ',borderwidth=3, relief="raised", highlightcolor="white", font=("Digital-7", 13), background='green')
        ban.place(x=10, y=30)
        can = Label(uk, text='Thông báo khi thoát ứng dụng: ', borderwidth=2, relief='raised', highlightcolor='green', font=("Helvetica bold", 12), background='yellow')
        can.place(x=10, y=55)
    # Tạo checkbox để cho phép/tắt chức năng nhận diện link
        detect_link_label = Label(uk, text="Nhận diện link YouTube:",borderwidth=2, relief="raised", font=("Arial italic", 13), background='blue')
        detect_link_label.place(x=10, y=85)
        detect_link_checkbox_var = IntVar()
        detect_link_checkbox = Checkbutton(uk, variable=detect_link_checkbox_var,
                                        onvalue=True, offvalue=False)
        detect_link_checkbox.place(x=230, y=85)
        # Tạo label để hiển thị trạng thái của checkbox
        detect_link_status_label = Label(uk, text="Bật" if detect_link else "Tắt")
        detect_link_status_label.place(x=250, y=85)

        check_path_status_var = IntVar()
        detect_link = parser.get('setting', 'detect_link')
            
        # Thêm chức năng nhập thời gian
        time_label = Label(uk, text='Nhập thời gian (đơn vị miligiây):', borderwidth=2, relief="raised", font=("Arial", 13), background='#C0F0CC')
        time_label.place(x=10, y=110)
        time_entry = Entry(uk, textvariable=time_entry_var, font=("Arial", 13), width=10)
        time_entry.place(x=260, y=110)
        # Thiết lập giá trị ban đầu và trạng thái của checkbox
        if detect_link == 'True':
            detect_link_checkbox_var.set(True)
            detect_link_status_label.config(text="Bật")
        else:
            detect_link_checkbox_var.set(False)
            detect_link_status_label.config(text="Tắt")
        
            
        # Thiết lập hàm callback cho checkbox để cập nhật trạng thái label
        def on_checkbox_changed():
            detect_link_status_label.config(text="Bật" if detect_link_checkbox_var.get() else "Tắt")
        detect_link_checkbox_var.trace("w", lambda name, index, mode, sv=detect_link_checkbox_var: on_checkbox_changed())

    else:
        anh = Label(uk, text='Notice when loading is done: ',borderwidth=3, relief="raised", font=("Verdana italic", 13), background='red')
        anh.place(x=10, y=5)
        ban = Label(uk, text='Voice notice: ',borderwidth=3, relief="raised", highlightcolor="white", font=("Digital-7", 13), background='green' )
        ban.place(x=10, y=30)
        can = Label(uk, text='App exit message: ', borderwidth=2, relief='raised', highlightcolor='green', font=("Helvetica bold", 12), background='yellow' )
        can.place(x=10, y=55)
        # Create checkbox to enable/disable link recognition
        detect_link_label = Label(uk, text="Detect YouTube links:",borderwidth=2, relief="raised", font=("Arial italic", 13), background='blue')
        detect_link_label.place(x=10, y=85)
        detect_link_checkbox_var = IntVar()
        detect_link_checkbox = Checkbutton(uk, variable=detect_link_checkbox_var)
        detect_link_checkbox.place(x=230, y=85)
        # Set initial state of checkbox
        detect_link_checkbox_var.set(int(detect_link))
        # Create a label to show the status of the checkbox
        detect_link_status_label = Label(uk, text="On" if detect_link else "Off")
        detect_link_status_label.place(x=250, y=85)

        # Add time input function
        time_label = Label(uk, text='Enter time (in milliseconds):', borderwidth=2, relief="raised", font=("Arial", 13), background='#C0F0CC')
        time_label.place(x=10, y=110)
        time_entry = Entry(uk, textvariable=time_entry_var, font=("Arial", 13), width=10)
        time_entry.place(x=260, y=110)

        if detect_link == 'True':
            detect_link_checkbox_var.set(True)
            detect_link_status_label.config(text="Enable")
        else:
            detect_link_checkbox_var.set(False)
            detect_link_status_label.config(text="Off")
        # Set callback function for checkbox to update label status
        def on_checkbox_changed():
            detect_link_status_label.config(text="On" if detect_link_checkbox_var.get() else "Off")
        detect_link_checkbox_var.trace("w", lambda name, index, mode, sv=detect_link_checkbox_var: on_checkbox_changed())
        
    if save_tttb == "1":
        var.set('1')
    elif save_tttb == "2":
        var.set('2')
    else:
            print("LOI")
    if save_migi == "1":
            bar.set('1')
    elif save_migi == "2":
            bar.set('2')
    else:
            print("ERROR")
    if save_exit == "1":
        den.set('1')
    elif save_exit == '2':
        den.set('2')
    else:
        print("LOL")

    if check_duration == '' or check_duration is None:
        time_entry_var.set('1000')  # Đặt giá trị mặc định là '1000'
    else:
        if int(check_duration) > 60000:
            time_entry_var.set('59000')
        elif int(check_duration) < 1000:
            random_duration = randint(1000, 2000)  # Sinh số ngẫu nhiên từ 1000 đến 2000
            time_entry_var.set(str(random_duration))
        elif check_duration.isnumeric():
            time_entry_var.set(check_duration)  # Giữ nguyên giá trị ban đầu của time_entry_var
        else:
            time_entry_var.set('1000')  # Nếu giá trị không phải là số, đặt giá trị mặc định là '1000'

#SAVE SETTING IN CONFIG FILE
    def save():
        lol = str(var.get())
        bol = str(bar.get())
        dol = str(den.get())
        dlo = time_entry_var.get()
        global detect_link
        if detect_link_checkbox_var.get() == 1:
            detect_link = True
        else:
            detect_link = False

        print(lol)
        print(bar)
        # if lol == save_tttb:
        #     messagebox.showinfo("ERROR","Bạn đã cài đặt thành như thế r thi!")

        print(bar.get())
        print(var.get())
        print(f"HELO THOIWG IA: {dlo}")
        if lol == "0":
            lol = "1"
        parser.set('setting','tbao', lol)
        parser.set('setting', 'migi', bol)
        parser.set('setting','tbao_exit', dol)
        parser.set('setting', 'detect_link', str(detect_link))
        parser.set('setting', 'duration', dlo)  # Lưu giá trị nhân 1000 (dạng chuỗi) vào file cấu hình
        with open("user_pro.ini", 'w')as f:
            parser.write(f)
        print("Đã lưu!")
        if lang_sys == 'vi_VN' or lang_sys == "cp65001":
            messagebox.showinfo("THÔNG BÁO", "Vui lòng khởi động lại ứng dụng để cập nhật cài đặt!")
        else:
            messagebox.showinfo("NOTICE", "Please restart the app to update settings!")
        uk.destroy()
        return "break"
#RADIO STATUS

    r1 = Radiobutton(uk, text="Bật", variable=var, value=1)
    r1.place(x=230, y=5)
    r2 = Radiobutton(uk, text="Tắt", variable=var, value=2)
    r2.place(x=275, y=5)


    r3 = Radiobutton(uk, text='ON', variable=bar, value=1)
    r3.place(x=230, y=30)
    r4 = Radiobutton(uk, text='OFF', variable=bar, value=2)
    r4.place(x=270, y=30)
    # arc = Label(uk, text="Cái này hiện đang lỗi nha!!!!!", fg="black")
    # arc.place(x=230, y=30)

    #GET EXIT NOTIFICATION

    r5 = Radiobutton(uk, text='Có', variable=den, value=1)
    r5.place(x=230, y=55)
    r6 = Radiobutton(uk, text='K', variable=den, value=2)
    r6.place(x=270, y=55)

#SAVE BUTTON
    if lang_sys == 'vi_VN' or lang_sys == "cp65001":
        button = Button(uk, text="Lưu cài đặt", command=save, background='blue')
        button.place(x=15, y=370)
    else:
        button = Button(uk, text="Save settting", command=save, background='blue')
        button.place(x=15, y=370)
    uk.bind("<Motion>", print_mouse_position)

def speak(text):
    read = gTTS(text, lang="vi")
    file = "TAO_GHET_MAY_NHAT_DO("+hour1+'-'+second1+").mp3"
    read.save(file)
    playsound.playsound(file)
    os.remove(file)

for i in range(1,5):
    with open("user_account.txa", 'w+', encoding="UTF-8") as f:
        f.write("TIME: "+ str(hour1)+':'+str(minute1)+':'+str(second1)+'\n')
        f.write(str(i))
        f.write('\n')
        f.write("DATE: "+str(day)+'\n')
        f.write("MONTH: "+str(month)+'\n')
        f.write("YEARS: "+str(year)+'\n')
        f.close()
#LAYGIO
def get_date():
    hour1 = time.strftime("%H")
    minute1 = time.strftime("%M")
    second1 = time.strftime("%S")
    day1 = time.strftime("%d")
    month1 = time.strftime("%m")
    year1 = time.strftime("%Y")
    na_dat = day1+'/'+month1+'/'+year1+' '+hour1+':'+minute1+':'+second1
    phot.config(text=na_dat)
    phot.after(1000, get_date)

def about_window(event=None):
    
    tt=Toplevel(txa)
    tt.title("THÔNG TIN Phiên bản⏬: ")
    tt.transient(txa)
    tt.resizable(False, False)
    tt.geometry('600x300')
    tt.configure(bg='blue')
    tt.grab_set()
    def on_cll():
        tt.grab_release() # Kích hoạt lại cửa sổ cha
        tt.destroy()
    tt.protocol("WM_DELETE_WINDOW", on_cll)

    def contact():
        os.startfile("https://bom.so/FB_ADMIN")

    def dow():
        os.startfile("https://bom.so/YouTube-Downloader")

    if lang_sys == 'vi_VN' or lang_sys == "cp65001":

        a1 = Label(tt, text="💖APP ĐƯỢC VIẾT BỞI TXA VLOG!💖", font=("Courier New", 12), background='red')
        a1.place(x=12, y=30)
        a2 = Label(tt, text="©️COPYRIGHT BY TXA VLOG! ❌DO NOT REUP❌", font=("Courier New", 12), background='red')
        a2.place(x=12, y=50)
        a3 = Label(tt, text="👉Đây là bản PRO!\n 👉Đã được mua và kích hoạt bản quyền!\n 👉Bạn hãy tận hưởng đầy đủ tính năng mới nhất nhé!!!😍😍", font=("Digital-7", 13), background='green')
        #a3 = Label(tt, text="👉Đây là bản DEMO!\n 👉Chỉ có trên Github(Test các tính năng mới trc khi phát hành chính thức tại trang web)!\n 👉Bạn hãy tận hưởng đầy đủ tính năng mới nhất nhé!!!😍😍", font=("Digital-7", 13), background='green')
        a3.place(x=12, y=70)
        a4 = Button(tt, text="CONTACT ME", font=("Times New Roman", 12), background='red', foreground='yellow', command=contact)
        a4.place(x=12, y=150)
        a5 = Label(tt, text="Bấm vào đây để quay lại☝️", font=("Arial", 12))
        a5.place(x=400, y=5)
        a6 = Button(tt, text="▶️GO TO DOWNLOAD APP", font=("Verdana italic", 12), background='brown', foreground='red', command=dow)
        a6.place(x=130, y=150)
        # a7 = Button(tt, text="👉Tải trên Github", font=("Digital-7 italic", 13), background='yellow', foreground='green', command=github)
        # a7.place(x=378, y=150)
    else:
        a1 = Label(tt, text="💖APP WRITTEN BY TXA VLOG!💖", font=("Courier New", 12), background='red')
        a1.place(x=12, y=30)
        a2 = Label(tt, text="©️COPYRIGHT BY TXA VLOG! ❌DO NOT REUP❌", font=("Courier New", 12), background='red')
        a2.place(x=12, y=50)
        a3 = Label(tt, text=" 👉This is the PRO version!\n 👉The license has been purchased and activated!\n 👉Please enjoy the latest features fully!!!😍😍", font= ("Digital-7", 13), background='green')
        #a3 = Label(cont, text=" 👉This is a DEMO!\n 👉Only on Github(Test new features before official release at website)!\n 👉Enjoy the feature fully. latest feature!!!😍😍", font=("Digital-7", 13), background='green')
        a3.place(x=12, y=70)
        a4 = Button(tt, text="CONTACT ME", font=("Times New Roman", 12), background='red', foreground='yellow', command=contact)
        a4.place(x=12, y=150)
        a5 = Label(tt, text="Click here to go back☝️", font=("Arial", 12))
        a5.place(x=400, y=5)
        a6 = Button(tt, text="▶️GO TO DOWNLOAD APP", font=("Verdana italic", 12), background='brown', foreground='red', command=dow)
        a6.place(x=130, y=150)

def github():
    os.startfile("https://github.com/TXAVL/TXAVL/releases")

def txa_popup(e):
    txa_menu.tk_popup(e.x_root, e.y_root)

def contact():
    os.startfile("https://bom.so/FB_ADMIN")

def exi(a):
    save_exit = parser.get('setting', 'tbao_exit')
    save_migi = parser.get('setting', 'migi')
    if save_exit=="1":
        if lang_sys == 'vi_VN'  or lang_sys == "cp65001": 
            a = messagebox.askyesno("🖐Dừng lại🖐", "❌Bạn có đang tải gì k đấy????❌")
            if a==True:
                pass
            elif a==False:
                if save_migi == "1":
                    speak("Hẹn gặp lại bạn sau nhé!")
                elif save_migi == "2":
                    pass
            else:
                    print("LOI FILE CAU HINH!")

        else:
            a = messagebox.askyesno("🖐STOP🖐", "❌DO YOU DOWNLOAD ANYTHING????❌")
            if a==True:
                pass
            elif a==False:
                if save_migi == "1":
                    speak("GOODBYE AND SEE YOU AGAIN!")
                elif save_migi == "2":
                    pass
            else:
                    print("ERROR FILE CONFIG!")
    elif save_exit=="2":
        pass
    raise SystemExit(0)

def di():
    urls = str(url.get())
    clipboard.copy(urls)
    clipboard.paste()

fl = ''
def get_path():
    global fl
    fl = filedialog.askdirectory(title="👇CHỌN NƠI LƯU FILE TẢI XUỐNG CỦA BẠN👇 - ©COPY BY TXA VLOG")
    path.set(fl)
    if len(fl) == 0:
        msb_path = messagebox.showwarning("warning", "❌Vui lòng chọn đường dẫn❌")
    else:
        pass

def shortcut():
    st=Toplevel(txa)
    
    
    st.title("THÔNG TIN Phím tắt⏬: ")
    st.transient(txa)
    st.resizable(False, False)
    st.geometry('550x500')
    st.configure(bg='blue')
    st.grab_set()
    def on_cll():
        st.grab_release() # Kích hoạt lại cửa sổ cha
        st.destroy()
    st.protocol("WM_DELETE_WINDOW", on_cll)
# take the data
    class Table:
     
        def __init__(self,root):
    # t = Table(txa)
            for i in range(total_rows):
                    for j in range(total_columns):
                        
                        self.e = Entry(st, width=20, fg='blue',
                                    font=('Arial',10,'bold'), bd=6, highlightcolor='red', cursor="cross")
                        
                        self.e.grid(row=i, column=j)
                        self.e.insert(END, lst[i][j])
    lst = [
        ('STT', "Phím tắt", "Chức năng"),
        (1,'Ctrl+W','Hthị bản quyền'),
        (2,'Alt+Q','Exit'),
        (3,'Alt+D','Ktra cập nhật app'),
        (4, "Ctrl+K", "Hthị thông tin"),
        (4, "Ctrl+R", "RESET MÀU NỀN VỀ MẶC ĐỊNH"),
        (5, "Ctrl+Shift+I", "Đổi màu nền app"),
        (6, "Ctrl+I", "Mở cài đặt"),
        (7, "Alt+Ctrl+D", "Check cập nhật phiên bản 2"),
        (8, "Đg cập nhật thêm", "UPDATING....")
        # (4,'Rachna','Mumbai'),
        # (5,'Shubham','Delhi')
        ]
    
    # find total number of rows and
    # columns in list
    total_rows = len(lst)
    total_columns = len(lst[0])
    t = Table(st)

def handle_c31_click(event):
    global sort_by_time_desc
    sort_by_time_desc = not sort_by_time_desc  # Đảo ngược trạng thái sắp xếp

    sort_table_by_time()  # Sắp xếp bảng theo thời gian tải

    # Cập nhật hiển thị của bảng
    update_table_display()

def sort_table_by_time():
    # Sắp xếp bảng theo thời gian tải
    url_table.delete(*url_table.get_children())  # Xóa dữ liệu hiện tại của bảng

    # Sắp xếp danh sách downloads theo thời gian tải
    sorted_downloads = sorted(downloads, key=lambda x: datetime.strptime(x["Thời gian"], "%d/%m/%Y %H:%M:%S"), reverse=sort_by_time_desc)

    # Thêm lại dữ liệu đã sắp xếp vào bảng
    for idx, download_info in enumerate(sorted_downloads):
        url = download_info["URL"]
        download_time = download_info["Thời gian"]
        url_table.insert("", "end", values=[idx+1, url, download_time])

def update_table_display():
    # Cập nhật hiển thị của bảng
    url_table.update()
    url_table.update_idletasks()

def show(ul, chunk, byte_remaining):
    prig = int(((ul.filesize - byte_remaining)/ul.filesize) * 100)
    mb_downloaded = round((ul.filesize - byte_remaining) / (1024 * 1024), 2)
    percent = round((mb_downloaded / (ul.filesize / (1024 * 1024))) * 100, 2)
    filesize_gb = ul.filesize / (1024 * 1024 * 1024)
    filesize_mb = ul.filesize / (1024 * 1024)
    # check_download_path()

    if filesize_gb >= 1:
        if mb_downloaded < 1024:
            status.config(text="Đang tải xuống... {:.2f}MB/{:.2f}GB ({:.2f}%)".format(mb_downloaded, filesize_gb, percent))
        elif mb_downloaded >= 1024:
            gb_downloaded = mb_downloaded / 1024
            status.config(text="Đang tải xuống... {:.2f}GB/{:.2f}GB ({:.2f}%)".format(gb_downloaded, filesize_gb, percent))
    else:
        if mb_downloaded < 1024:
            status.config(text="Đang tải xuống... {:.2f}MB/{:.2f}MB ({:.2f}%)".format(mb_downloaded, filesize_mb, percent))
        elif mb_downloaded >= 1024:
            gb_downloaded = mb_downloaded / 1024
            status.config(text="Đang tải xuống... {:.2f}GB/{:.2f}MB ({:.2f}%)".format(gb_downloaded, filesize_mb, percent))
    # # phantram = int(((ul.filesize - byte_remaining/ul.filesize)) * 100)
    # # sotram = phantram//100%10
    # # sochuc = phantram//10%10
    # # sodvi = phantram%10
    # # tong = sotram+sochuc+sodvi
    # r = prig//100%10
    # pt = prig//10%10
    # dvi = prig%10
    # # if r >= "1":
    #     r = 1
   # status.configure(text = "DOWNLOADING..." + str(r) + str(pt) + str(dvi) + "%")
    # print("PT DOWNLOADED: " + str(pt) + str(dvi) + "%")
    # print("{} %".format(gt))

    # # Tính thời gian còn lại
    # if ul.streams:
    #     remaining_bytes_per_second = ul.streams[0].downloaded_bytes_per_second()
    # else:
    #     remaining_bytes_per_second = 0
    # remaining_time_seconds = byte_remaining / remaining_bytes_per_second if remaining_bytes_per_second else 0
    # remaining_time = str(datetime.timedelta(seconds=round(remaining_time_seconds)))
    
    # # Tính thời gian đã trôi qua
    # time_elapsed_seconds = time.time() - start_time
    # time_elapsed = str(datetime.timedelta(seconds=round(time_elapsed_seconds)))

    # status.config(text="Đang tải xuống... {:.2f}/{:.2f}MB ({:.2f}%) - Thời gian còn lại: {} - Thời gian đã trôi qua: {}".format(mb_downloaded, mb_total, percent, remaining_time, time_elapsed))
    
    # pt_download['value'] = percent

    
    pt_download['value'] = prig


type = None
download_path_exists = True
def check_download_path():
    global download_path_exists
    check_duration = parser.get('setting', 'duration')
    if not check_duration:
        check_duration = '1000'
        # Lưu giá trị 'check_duration' vào file cấu hình
        parser.set('setting', 'duration', check_duration)
        with open('config.ini', 'w') as configfile:
            parser.write(configfile)
    save_path = fl
    if not os.path.exists(save_path):
        if download_path_exists:
            messagebox.showerror("Lỗi khi tải video!!🤶", "Đường dẫn bạn chọn hiện không tồn tại, vui lòng thử kiểm tra lại đường dẫn và bấm lại nút Download để không bị mất file tải xuống🥰")
            pt_download.stop()
            download_path_exists = False
            print(f"Đường dẫn của bạn là {save_path} với trạng thái là {download_path_exists}!")
    else:
        download_path_exists = True
        print(f"Đường dẫn của bạn là {save_path} với trạng thái là {download_path_exists}!")
    with open("log.txaweb", 'w') as f:
        f.write(f"Đường dẫn của bạn là {save_path} với trạng thái là {download_path_exists}!")
        f.write('\n')
        f.write('👉Nguồn: ©️TXA VLOG!!\n')
        f.close()
    txa.after(int(check_duration), check_download_path)


def extract_log_info(file_log, url):
    with open(file_log, "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            line = lines[i]
            if url in line:
                if line.startswith("Tiêu đề video là:"):
                    next_line = lines[i + 1].strip() if i + 1 < len(lines) else ""
                    if next_line.startswith("URL BẠN NHẬP:"):
                        title = line.split("Tiêu đề video là: ")[1].strip()
                        return title
                    else:
                        # Đọc định dạng tiêu đề từ lịch sử
                        title_line = next_line.split("có tiêu đề là ")[1].strip()
                        title = title_line[:-1]  # Xóa ký tự đóng ngoặc đơn cuối cùng ")"
                        return title
    print(f"Không tìm thấy tiêu đề cho URL '{url}' trong file log.")
    return None

def download():
    global type, save_migi, selected_title
    urls = str(url_entry.get())
    mk = cbb.get()
    global fl
    if not re.match(url_regex, urls):
        if lang_sys == 'vi_VN' or lang_sys == "cp65001":
            messagebox.showerror("Lỗi", "URL video không đúng định dạng!\n Vui lòng viêt theo định dạng: https://(http://)youtube.com(youtu.be)/watch?v=id(id)!")
        else:
            messagebox.showerror("Error{lang_sys}", "Invalid video URL!\n Please write in the following format: https://(http://)youtube.com(youtu.be)/watch?v=id( id)")
        return

    ul = YouTube(str(url_entry.get()), on_progress_callback=show)
    if not fl:
        if lang_sys == 'vi_VN' or lang_sys == "cp65001":
            msb_path = messagebox.showwarning("CẢNH BÁO", "❌Vui lòng chọn đường dẫn❌")
        else:
            messagebox.showwarning("WARNING", "PATH IS REQUIRED!")

        if save_migi == "1":
                speak("Hãy chọn đường dẫn để tải xuống đi nào")
        elif save_migi == "2":
                    pass
        else:
                    print("LOI FILE CAU HINH VUI LONG XEM LAI!")
                    speak("LỖI FILE CẤU HÌNH DIU SƠ PỜ RỒ CHẤM I NỜ I RỒI nhé!Vui lòng xem lại")
    if not cbb:
        if lang_sys == 'vi_VN' or lang_sys == "cp65001":
            messagebox.showwarning("CẢNH BÁO","❌Vui lòng chọn chất lượng để tải xuống❌")
        else:
            messagebox.showwarning("WARNING({lang_sys})","❌Please select quality to download❌")
    print("DOWNLOADING>>>>>>", urls)

    hour1 = time.strftime("%H")
    minute1 = time.strftime("%M")
    second1 = time.strftime("%S")
    day1 = time.strftime("%d")
    month1 = time.strftime("%m")
    year1 = time.strftime("%Y")
    
    save_migi = parser.get('setting', 'migi')
    if save_migi == "1":
        speak("Đang lấy dữ liệu nhé!")
    elif save_migi == "2":
        pass
    else:
        print("LOI FILE CAU HINH VUI LONG XEM LAI!")
        # toaster.showtoast("Bị lỗi❌", f"File cấu hình {file_path} bị lỗi rồi kìa mau xem xem đi nào!!", duration=4)
        speak(f"File cấu hình {file_path} bị lỗi rồi kìa mau xem xem đi nào!!")
        # URL VIDEO DÀI: https://www.youtube.com/watch?v=51aCi69Dw9o
    if "youtube.com" in urls or "youtu.be" in urls:
        status.config(text="✨GETTING DATA FROM YOUTUBE.")
        time.sleep(0.1)
        status.config(text="✨✨GETTING DATA FROM YOUTUBE..")
        time.sleep(0.3)
        status.config(text="✨✨✨GETTING DATA FROM YOUTUBE...")
        status.config(text="✨GETTING DATA FROM YOUTUBE.")
        time.sleep(0.1)
        status.config(text="✨✨GETTING DATA FROM YOUTUBE..")
        time.sleep(0.3)
        status.config(text="✨✨✨GETTING DATA FROM YOUTUBE...")
        global download_count
        download_count += 1
        log_msg = f"{download_count}- URL BẠN NHẬP: {urls} (Vào lúc {day1}/{month1}/{year1} {hour1}:{minute1}:{second1})\n👉COPY BY ©️TXAVLOG\n"
        with open(log_file, 'a') as f:
            f.write(log_msg)
        start_time = time.time()
        try:
            if any(download['URL'] == urls for download in downloads):
                confirm = messagebox.askyesno("Xác nhận", "Video này đã tồn tại trong lịch sử. Bạn có muốn tải lại?")
                if not confirm:
                    return 
            type = 'Video'
            check_download_path()
            if(mk == ''):
                if lang_sys == 'vi_VN' or lang_sys == "cp65001":
                    messagebox.showwarning("CẢNH BÁO","❌Vui lòng chọn chất lượng để tải xuống")
                else:
                    messagebox.showwarning("WARNING","❌Please select quality to download")
                if save_migi == "1":
                    speak("Chưa chọn chất lượng kìa!")
                elif save_migi == "2":
                    pass
                else:
                    print("LOI FILE CAU HINH VUI LONG XEM LAI!")
            elif(mk == qua[0]):
                a = ul.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
                b = a.download(fl, filename='TXA VLOG - ' + safe_filename(ul.title) + ' - 720p.mp4')
                az = "720p"
                file_extension = '.mp4'
                chatluong = "video: 720p"
            elif(mk == qua[1]):
                a = ul.streams.filter(progressive=True, file_extension='mp4').get_by_resolution('360p')
                b = a.download(fl, filename='TXA VLOG - ' + safe_filename(ul.title) + ' - 360p.mp4')
                file_extension = '.mp4'
                chatluong = "video: 360p"
                az = "360p"
            elif(mk == qua[2]):
                a = ul.streams.filter(progressive=True, file_extension='mp4').get_lowest_resolution()
                b = a.download(fl, filename='TXA VLOG - ' + safe_filename(ul.title) + ' - 144p.mp4')
                file_extension = '.mp4'
                chatluong = "video: 144p"
                az = "144p"
            elif(mk == qua[3]):
                a = ul.streams.filter(only_audio=True).first()
                b = a.download(fl, filename='TXA VLOG - ' + safe_filename(ul.title) + ' - 128kps.mp3')
                file_extension = '.mp3'
                chatluong = "nhạc: 128kps"
                az = "128kps"
                type = 'Nhạc'
            else:
                messagebox.showwarning("ERROR", "Không có chất lượng này!")
            size = round(a.filesize/1024/1024, 2)
                # thoigian = b.length
            thoigian = ul.length
            gio = thoigian // 3600
            phut = (thoigian // 60) % 60
            giay = thoigian % 60
            thoi_gian_str = "{:02d}g:{:02d}p:{:02d}s".format(gio, phut, giay)
            luot_Xem_htai = ul.views
            kenh = ul.channel_url
            key = ul.keywords
            mta = ul.description
            meta = ul.age_restricted
            s = ul.metadata
            response = requests.get(urls)
            selected_title = {safe_filename(ul.title)}  # Gán giá trị tiêu đề cho biến toàn cục
            if os.path.isfile(os.path.join(fl, f"{safe_filename(ul.title)}."+file_extension)):
                messagebox.showwarning("Warning", "Video đã tồn tại ở thư mục đã chọn.")
            #     toaster.show_toast("CẢNH BÁO🔔", "VIDEO ĐÃ TỒN TẠI Ở THƯ MỤC BẠN CHỌN!")
            # toaster.show_toast("🛟INFOMATION", f"Bắt đầu tải {safe_filename(ul.title)}....")
            if response.status_code == 200:
                # tbao = ToastNotifier()
                # tbao.show_toast("DOWNLOADED VIDEO", "ĐÃ TẢI XONG VIDEO. \n Kích thước ước lượng: " + str(size)+"MB! \n Hãy kiểm tra nó đi nào!!!!\n APP BY TXA VLOG:))")
                if save_migi == "1":
                    speak("Đã tải xong video "+ safe_filename(ul.title)+'Tại thư mục đã chỉ định\nBây giờ hãy quay lại app này để dán link mới hoặc là thoát ra nhé!')
                elif save_migi == "2":
                    pass
                else:
                    print("LOI FILE user_pro.ini> VUI LONG XEM LAI!")
                elapsed_time = time.time() - start_time
                print(f"Tải video thành công! Thời gian tải: {elapsed_time:.2f} giây")
                if size >= 1024:
                    size_str = f"{size / 1024:.2f} GB"
                else:
                    size_str = f"{size} MB"
                if elapsed_time >= 3600:
                    elapsed_time_str = f"{int(elapsed_time // 3600):02d}h:{int((elapsed_time % 3600) // 60):02d}p:{int(elapsed_time % 60):02d}s"
                else:
                    elapsed_time_str = f"{int(elapsed_time // 60):02d}:{int(elapsed_time % 60):02d}"
                # toaster.show_toast(f"{type} đã tải xog rồi kìa em ơi với thời gian tải {type} là {elapsed_time:.2f}s!", f"Tên {type} là {safe_filename(ul.title)} nhé!\n©️COPY BY TXA VLOG!", duration=3)
                # toaster.show_toast(f"{type} của bạn đã tải xong!", f"Vui lòng vô thư mục {fl} và kiểm tra đi!©️COPYRIGHT BY TXA VLOG!")
                messagebox.showinfo("Thông báo", f"Tải xuống thành công.\nVui lòng kiểm tra thư mục {fl}\nVới tên: {safe_filename(ul.title)}{file_extension}\nKích thước: {size_str}\nThời gian: {thoi_gian_str}\nChất lượng: {chatluong}")
                messagebox.showinfo("Thông tin trên YT về video từ link của bạn", "Số lượt xem video ở thời điểm htại: " + str(luot_Xem_htai) + " views! \n URL kênh: " + kenh + "\n Từ khóa video: " + str(key))
                # status = Label(txa, text="DOWNLOADED!", font=("Arial bold", 15), background='#ff0fff').place(x=50, y=160)
                status.config(text="Đã tải xong")
                txa.title("VideoDownloaded tại thư mục: " + fl + "!Chất lượng: "+ az)
                lang_tt = f'Tiêu đề video là: {safe_filename(ul.title)}'
                        # Thêm URL và trạng thái vào bảng
                downloads.append({"URL": urls, "Thời gian": ""})
                update_table()
                print(lang_tt)
                idx = len(downloads) - 1
                # downloads[idx][1] = "Finished"
                current_time = time.strftime("%d/%m/%Y %H:%M:%S")
                downloads[idx]["Thời gian"] = current_time
                update_table()

                # Lưu URL vào danh sách lịch sử
                history.append(f"URL BẠN NHẬP: {urls} (Vào lúc {current_time}) có tiêu đề là {safe_filename(ul.title)}")
                save_history()
                with open(log_file, 'a') as f:
                    f.write('\n'+ lang_tt+'\n')

                with open(f"Mô tả về video - {safe_filename(ul.title)}.data", "w") as file:
                    file.write(f"I. MÔ TẢ VIDEO: \n{mta}\n\n")
                    file.write("II. THÔNG TIN VỀ VIDEO:\n")
                    file.write(f"1. Độ phân giải: {az}\n")
                    file.write(f"2. Kích thước file: {a.filesize / (1024 * 1024):.2f} MB\n")
                    file.write(f"3. Đường dẫn đến file: {fl}/{safe_filename(ul.title)}{file_extension}\nURL VIDEO Ở TRONG FILE LOG NHÉ KHÔNG PHẢI Ở TRÊN FILE NÀY!\n")
                    # file.write(f"4. URL VIDEO: " + {urls}+ '\n')
                    file.write(f"III. THỜI GIAN TẢI:\n")
                    file.write(f"1. Ngày tải: {day1}/{month1}/{year1}\n")
                    file.write(f"2. Giờ tải: {hour1:02}:{minute1:02}:{second1:02}\n")
                    file.write(f"IV. TỔNG THỜI GIAN TẢI VIDEO:\n")
                    file.write(f"Thời gian tải: {int(elapsed_time // 3600):02d}h:{int((elapsed_time % 3600) // 60):02d}p:{elapsed_time % 60:04.1f}s!\n")
                    file.write("V. CHÚ THÍCH:\n")
                    file.write(f"1. Tài khoản lưu trữ: {username}\n")
                    file.write("2. Liên hệ: https://bom.so/FB_ADMIN\n")
                    file.write("3. 👉©️COPY BY TXA VLOG!")
                    file.close()
                print(na_dat)
                print(meta) 
                print(str(s))
            else:
                if lang_sys == 'vi_VN' or lang_sys == "cp65001":
                    messagebox.showerror("Lỗi", "Lỗi kết nối đến server!")
                else:
                    messagebox.showerror("Error", "Connection error to server!")
        except pyt.exceptions.VideoUnavailable:
            messagebox.showerror("Lỗi khi load video!!🤶","Video này không khả dụng trên YouTube.\nHãy kiểm tra lại link của bạn xem có đúng định dạng hoặc có đúng với link trên Youtube hay không\nHãy copy link này và dán nó vào trình duyệt để ktra nhé!")
            pt_download.stop()
        except pyt.exceptions.ExtractError as e:
            messagebox.showerror("Lỗi khi load video!!🤶","Không thể trích xuất thông tin video.")
            print(str(e))
            pt_download.stop()
        except pyt.exceptions.VideoPrivate:
            messagebox.showerror("Lỗi khi load video!!🤶","Video này là video riêng tư, bạn không thể tải về.")
            pt_download.stop()
        except pyt.exceptions.VideoRegionBlocked:
            messagebox.showerror("Lỗi khi load video!!🤶","Video này bị chặn tại khu vực của bạn.")
            pt_download.stop()
        except Exception as e:
            print("Lỗi khi tải video!!🤶")
            print("Có lỗi xảy ra khi tải video.")
            print("Thông báo lỗi:", str(e))
            d = str(e)
            if "local variable 'a' referenced before assignment" in d:
                e = "Chưa chọn biến chất lượng!"
            elif 'streamingData' in d:
                messagebox.showerror("Lỗi!","Gặp vấn đề nghiêm trọng khi kết nối đến server.\n Rất có thể server đã chặn tải xuống từ ứng dụng này rồi!\nVì vậy hãy thử lại sau ít phút nhé hoặc là dùng ứng dụng khác!")
            elif 'Invalid argument' in d or 'invalid argument' in d:
                pass
            elif 'Permission denied' in d or 'permission denied' in d:
                e = "Vì bạn 🚫 không có đủ quyền truy cập vô thư mục đã chọn vui lòng bấm Download lại đi nào!"
            else:
                messagebox.showerror("Lỗi khi tải video!!🤶","Có lỗi xảy ra khi tải video.\n("+str(e)+")!")
            pt_download.stop()

        except requests.exceptions.RequestException as e:
            if lang_sys == 'vi_VN' or lang_sys == "cp65001":
                messagebox.showerror("Lỗi", "Lỗi kết nối mạng!")
                speak("Lỗi rồi mạng đang bị lỗi!")
            else:
                messagebox.showerror("Error", "Network connection error!")
            pt_download.stop()

    if len(urls) == '' or len(urls) <= 6:
        messagebox.showwarning("warning", "Vui lòng nhập đúng định dạng") 
def info(event=None):
    if lang_sys == 'vi_VN' or lang_sys == "cp65001":
        messagebox.showinfo("INFO", "💖APP ĐƯỢC VIẾT BỞI TXA VLOG!💖")
        messagebox.showinfo("INFO", "✝Chức năng: TẢI XUỐNG VIDEO YOUTUBE")
        messagebox.showinfo("INFO", "✔VERSION 3.7.5\n Nếu có thắc mắc ib fb: https://bom.so/FB_ADMIN")
    else:
        messagebox.showinfo("INFO", "💖APP WRITE BY TXA VLOG!💖")
        messagebox.showinfo("INFO", "✝Function: DOWNLOAD YOUTUBE VIDEO")
        messagebox.showinfo("INFO", "✔VERSION 3.7.5\n If you have any questions ib fb: https://bom.so/FB_ADMIN")
def check(e):
    ht ="3.7.5"
    # htt = ht.split(',')
    print("ĐANG KIỂM TRA PHIÊN BẢN VÀ SẼ TBÁO NẾU CÓ PHIÊN BẢN MỚI VÌ VẬY HÃY ĐỢI!!")
    for d in range(2):
        messagebox.showwarning("Cảnh báo", "CHECKING UPDATE😎")
        print("CHECKING.")
        print("CHECKING..")
        print("CHECKING...")
        time.sleep(1)
    version = requests.get('https://yt-txa.mw.lt/get-version.json')
    # version = version.encoding("utf-8")

    up = version.json()
    d1 = f'{up["day"]}'
    m1 = f'{up["mon"]}'
    y1 = f'{up["year"]}'
    getdl = f'{up["pban_pro"]}'

    for i in range(3):
        with open('CHECKING UPDATE_'+ str(year)+str(month)+str(day)+'-'+str(hour)+str(minute)+str(second)+'.txa', "+w") as f:
            f.write('CHECK UPDATE....')
            f.write('\n')
            f.write('Phiên bản hiện tại của bạn là: '+str(ht)+'\n')
            f.write("Phiên bản trên trang web của chúng tôi: "+str(getdl)+'\n')
            f.write("DATE: "+ str(year)+'/'+str(month)+'/'+str(day)+'-'+str(hour)+':'+str(minute)+':'+str(second)+'('+str(fr)+')'+'\n')
            f.write("INDEX OF "+str(i)+'\n')
            f.write("DATE UPDATE: "+str(d1)+'/'+str(m1)+'/'+str(y1)+'\n')
            f.write("©️Copy by TXA VLOG!!®️")
            f.close()
    # htai = f'{up["hta"]}'
    if getdl > str(ht):
        messagebox.showinfo("The update is available v" +getdl, "ĐÃ CÓ BẢN CẬP NHẬT MỚI VÀO NGÀY "+day+'/'+month+'/'+year+"!\n HÃY TRUY CẬP TRANG WEB https://bom.so/YouTube-Downloader để lấy phiên bản mới nhất!!🙌")
    elif getdl < str(ht):
        messagebox.showerror("There is no update", "CHX CÓ BẢN CẬP NHẬT KHẢ DỤNG😂("+ht+")")

    else:
        messagebox.showwarning("THIS IS A UPDATE LASTED VERSION!!" + str(ht), "BẠN ĐANG Ở PBẢN MS NHẤT R CÒN GÌ😒😒😒!")
    print("DONE!!")

def update_table():
    url_table.delete(*url_table.get_children())
    for idx, download_info in enumerate(downloads):
        url = download_info["URL"]
        download_time = download_info["Thời gian"]
        url_table.insert("", "end", values=[idx+1, url, download_time])

def handle_row_selection(event):
    selected_row = url_table.focus()  # Lấy dòng được chọn
    if selected_row != "" and url_table.identify_column(event.x) == "#2":  # Kiểm tra xem có dòng nào được chọn và double-click trên cột thứ 2 không
        column_value = url_table.item(selected_row)["values"][1]  # Lấy giá trị trong cột Link tải
        url_entry.delete(0, END)  # Xóa nội dung trong ô nhập URL
        url_entry.insert(0, column_value)  # Đưa giá trị của dòng được chọn vào ô nhập URL
        url_entry.select_range(0, END)  # Bôi đen toàn bộ văn bản trong ô nhập URL
        url_entry.icursor(END)  # Di chuyển con trỏ đến cuối văn bản trong ô nhập 
        # messagebox.showinfo("Thông tin", f"Tên video của url đang chọn là: {title_ent}")
        if os.path.exists(log_file):
            log_file_path = os.path.abspath(log_file)
            print("Đường dẫn đến file log:", log_file_path)
            
        title = extract_log_info(log_file, column_value)
        if title is not None:
            messagebox.showinfo("Thông báo", f"Tiêu đề video của URL '{column_value}' là '{title}'")
        else:
            messagebox.showinfo("Thông báo", f"Không tìm thấy tiêu đề cho URL '{column_value}' trong file log.") 


# Create a label
title_window = Label(txa, text="YouTube Downloader", font=("Arial bold", 20), background='#f5f5f5').place(x=190, y=10)

#INSERT URL
url = StringVar()
url_label = Label(txa, text="URL:", font=("Arial bold", 15), background='#ff0f0f').place(x=70, y=70)
url_entry = Entry(txa, width=30,textvariable = url, font=("Arial bold", 15), background='#00cf0f')
url_entry.place(x=150, y=70)

def reset():
    messagebox.showinfo("NO NAME","👉TÍNH NĂNG ĐANG ĐƯỢC PHÁT TRIỂN, VUI LÒNG ĐỢI Ở CÁC BẢN CẬP NHẬT TIẾP THEO NHA!\n🔔©️COPY BY TXAVLOG!!")

#RIGHTMENU
txa_menu = Menu(txa, tearoff=False)
txa_menu.add_command(label="Copy url", command=di)
txa_menu.add_separator()
txa_menu.add_command(label="CONTACT ME", command=contact)

sm = Menu(txa, tearoff=False)
sm.add_command(label='Open Setting', command=setting)
sm.add_separator()
sm.add_command(label='Đổi màu nền', command=changebg)
sm.add_separator()
sm.add_command(label='RESET Cài đặt', command=reset, font=("Verdana italic", 18))
txa_menu.add_cascade(label="OPTION", menu=sm)
txa.bind("<Button-3>", txa_popup)

#INSERT PATH
path = StringVar()
path_label = Label(txa, text="PATH:", font=("Arial bold", 15), background='#ff0fce').place(x=70, y=100)
path_e = Entry(txa, width=30, font=("Arial bold", 15), background='brown', textvariable=path, state='readonly').place(x=150, y=100)
path_button = Button(txa,height=-50, text="Browse", font=("Arial bold", 15), background='#00cfff', command=get_path).place(x=500, y=100)

#INSERT COMBOBOX
combo_label = Label(txa, text="Quality:", font=("Arial bold", 15), background='#f00f0f').place(x=70, y=130)
qua = ["Cao(720p)", "360p", "144p", "MP3 Audio File"]
cbb = Combobox(txa, width=30, font=("Arial bold", 15),state='readonly', values=qua, background='red')
cbb.grid(column=0, row=0, sticky=(W, E))
cbb.place(x=150, y=130)

#PT_DOWNLOAD
pt_download = Progressbar(txa, orient='horizontal', length=300, mode='determinate')
pt_download.place(x=90, y=190)

#BUTTON
btn_download = Button(txa, text="Download", font=("Arial bold", 15), background='#00cfff', command=lambda:_thread.start_new_thread(download, ())).place(x=220, y=230)
#STATUS
status = Label(txa, font=("Arial bold", 15), background='#ff0fff')
status.place(x=90, y=160)

phot = Label(txa, text='rrr', font=("Digital-7", 12), background='#a074cd')
phot.place(x=0, y=310)

#URL HISTORY TABLE
# Create a frame for the URL table
table_frame = ttk.Frame(txa)
table_frame.place(x=13, y=350)

# Create a scrollbar for the table
scrollbar = ttk.Scrollbar(table_frame)
scrollbar.pack(side='right', fill='y')

# Create the URL table
url_table = ttk.Treeview(table_frame, columns=(1, 2, 3), show="headings", yscrollcommand=scrollbar.set)
url_table.pack()
# Set the maximum height of the table to display 7 rows
url_table.configure(height=7)
# Định nghĩa biến sort_by_time_desc ở phạm vi toàn cục
sort_by_time_desc = False

# Configure the scrollbar for the table
scrollbar.config(command=url_table.yview)
url_table.column(1, width=40, anchor='center')
url_table.column(2, width=300)
url_table.column(3, width=150, anchor='center')
url_table.heading(1, text="STT")
url_table.heading(2, text="Link tải")
url_table.heading(3, text="Thời gian tải")

# Populate the URL table with data from history
for idx, download_info in enumerate(downloads):
    url = download_info["URL"]
    download_time = download_info["Thời gian"]
    url_table.insert("", "end", values=[idx+1, url, download_time])

# Bind double-click on a row to select URL
url_table.bind("<Double-Button-1>", handle_row_selection)

# Bind double-click on a column to select URL
url_table.bind("<Double-Button-1>", handle_row_selection, "+")

# Cập nhật hiển thị của bảng
update_table_display()

# Gán sự kiện click vào dòng C31 cho bảng
url_table.heading(3, text="Thời gian tải", command=lambda: handle_c31_click(None))

#TEXT_INFO
text_info = Label(txa, width=50, height=10, font=("Arial bold", 15), background='#00cfff')

#pt mạng
mang = Label(txa, text='👉©COPY BY TXA VLOG!', font=("Verdana italic", 9))
mang.place(relx=1, rely=1, anchor='se')

#OPTION LEFT
menubadr = Menu(txa, selectcolor='#fff0cc')
fme = Menu(menubadr,tearoff=0)
sub = Menu(fme, tearoff=0)

# Hàm hiển thị thông tin về bản cập nhật
def show_update_info():
    # Tạo cửa sổ hiển thị thông tin
    update_info_window = Toplevel(txa)
    update_info_window.title("Thông tin cập nhật")

    # Tạo label hiển thị thông tin phiên bản
    version_label = Label(update_info_window, text="Phiên bản: YT DOWNLOADER PRO TXA V3.7.5", font=("Arial", 14, "bold"), fg="blue")
    version_label.pack()

    # Tạo label hiển thị thông tin tác giả
    author_label = Label(update_info_window, text="Tác giả: ©TXA VLOG", font=("Arial", 12))
    author_label.pack()

    # Tạo label hiển thị thông tin về tính năng mới
    feature_label = Label(update_info_window, text="👉Có gì mới:", font=("Arial", 12, "underline"))
    feature_label.pack()

    # Tạo listbox hiển thị các tính năng mới
    feature_listbox = Listbox(update_info_window, width=170, height=7, font=("Arial", 12))
    feature_listbox.pack()

    # Thêm tính năng mới vào listbox
    feature_listbox.insert(END, "1. Thêm tính năng tự động nhận diện link youtube đầu tiên trong clipboard khi quay lại ứng dụng (có cả cài đặt xem nên bật hay tắt tính năng này).")
    feature_listbox.insert(END, "2. Sửa đổi lại ở tính năng lưu file log khi tải video xong là thêm mục thời gian tải video vô file và tên người thực hiện.")
    feature_listbox.insert(END, "3. Thêm tiếp tính năng tải trực tiếp file cập nhật của app ngay trong ứng dụng để khỏi phải vô trình duyệt (có thể bấm phím tắt Alt+Ctrl+D).")
    feature_listbox.insert(END, "4. Sửa đổi lại tiêu đề của cửa sổ và thêm cả cửa sổ check thông tin cập nhật.")
    feature_listbox.insert(END, "5. Đã sửa lỗi bị 'StreamingData' khi tải khiến video hông thể tại được!")
    feature_listbox.insert(END, "6. Đã sửa lỗi không thể kiểm tra và cập nhật ứng dụng!")           
    feature_listbox.insert(END, "7. Sửa đổi lỗi bị 'Không thể trích xuất thông tin video'!")
    feature_listbox.insert(END, "8. Sửa đổi lại tính năng thông báo bằng giọng nói và nếu trong quá trình tải có bị vấn đề gì về tính năng này thì cứ bỏ qua nó nhé!")
    feature_listbox.insert(END, "9. Thêm tính năng kiểm tra kết nối mạng trước khi vô ứng dụng!")
    feature_listbox.insert(END, "10. Thay đổi logo app thành logo mới kỉ niệm 1 năm ra mắt app!!!")
    feature_listbox.insert(END, "👉Hết rồi đó.")

    # Tạo label hiển thị thông tin liên hệ
    contact_label = Label(update_info_window, text="⛔Mọi thắc mắc vui lòng liên hệ qua Facebook: https://bom.so/FB_ADMIN!", font=("Times New Roman bold", 14))
    contact_label.pack()


# fme.add_cascade(label='FUNCTION', menu=sub)
# fme.add_separator()
# sub.add_command(label="LOL", command=te)
fme.add_command(label='Exit', command=lambda: exi(True), accelerator= "Alt+Q")
fme.add_separator()
if lang_sys == 'vi_VN' or lang_sys == "cp65001":
    fme.add_command(label='Các phím tắt trong app', command=shortcut)
    fme.add_separator()
    fme.add_command(label='Setting', command=lambda: setting(True), accelerator='Ctrl+I')

    #HELP
    hep = Menu(menubadr, tearoff=False, font=("Arial bold", 12))
    hep_sup = Menu(hep, tearoff=0, font=("Arial bold", 11))

    #OPTION HELP
    hep.add_cascade(label='Thông tin', command=lambda: info(True), accelerator='Ctrl+K')
    hep.add_separator()
    hep.add_cascade(label='Check cập nhật', accelerator='Alt+D', command=lambda: check(True), font=("Arial italic", 10))
    hep.add_separator()
    hep.add_cascade(label='Check cập nhật phiên bản 2(...)',accelerator='Alt+Ctrl+D', command= lambda:update(True),compound='left', font=("Arial italic", 8))
    hep.add_separator()
    hep.add_command(label='Bản quyền', accelerator='Ctrl+W', command=lambda: about_window(True), compound='left', underline=0, font=("Arial", 10))
    hep.add_separator()
    hep.add_command(label="Thông tin cập nhật", command=show_update_info)

    #MENU OPTION
    opt = Menu(menubadr, tearoff=False)
    opt_s = Menu(opt, tearoff=0)

    opt.add_command(label='Đổi màu nền(background) app', accelerator='Ctrl+Shift+I', command=lambda: changebg(True), compound='left', font=("Verdana bold", 12))
    opt.add_separator()
    opt.add_command(label='Reset màu về mặc định', accelerator='Ctrl+R', command=lambda: resetbg(True), compound='left',font=("Times New Roman italic", 11))


    #txa.bind("<Button-3>", show)
    def show_window(icon, item):
        icon.stop()
        txa.after(0,txa.deiconify())

    def quit_window(icon, item):
        icon.stop()
        txa.destroy()

    # Hide the window and show on the system taskbar
    def hide_window():
        messagebox.showinfo("🥇🥇ĐÃ THU NHỎ","🙌🙌ỨNG DỤNG ĐÃ ĐC THU NHỎ XUỐNG KHAY HỆ THỐNG!!")
        messagebox.showinfo("👉👉👉👉THÔNG TIN🍀🍀", "🔽🔽🔽VUI LÒNG CLICK CHUỘT PHẢI VÀO ICON Ở KHAY HỆ THỐNG VÀ CHỌN CHỨC NĂNG CẦN THIẾT!!🔽🔽")
        #t.show_toast("🥇🥇ĐÃ THU NHỎ", "🙌🙌ỨNG DỤNG ĐÃ ĐC THU NHỎ XUỐNG KHAY HỆ THỐNG!!📍 📍", icon_path="logo.ico")
        #t.show_toast("👉👉👉👉THÔNG TIN🍀🍀", "🔽🔽🔽VUI LÒNG CLICK CHUỘT PHẢI VÀO ICON Ở KHAY HỆ THỐNG VÀ CHỌN CHỨC NĂNG CẦN THIẾT!!🔽🔽", icon_path="logo.ico")
        txa.withdraw()
        image=Image.open("logo-app.ico")
        menu=(item('Hiển thị app', show_window), item('Thoát', quit_window), item('Check cập nhật', check), item('Trang web', contact))
        icon=pystray.Icon("name", image, "YT DOWNLOADER TXA - PRO (VN) V3.7.5", menu)
        icon.run()

else:
    # Function to display information about updates
    def show_update_info2():
        # Create information display window
        update_info_window = Toplevel(txa)
        update_info_window.title("Update Info")

        # Create a label that displays version information
        version_label = Label(update_info_window, text="Version: YT DOWNLOADER PRO TXA V3.7.5", font=("Arial", 14, "bold"), fg="blue")
        version_label.pack()

        # Create a label to display author information
        author_label = Label(update_info_window, text="Author: ©TXA VLOG", font=("Arial", 12))
        author_label.pack()

        # Create a label that displays information about the new feature
        feature_label = Label(update_info_window, text=" 👉What's New:", font=("Arial", 12, "underline"))
        feature_label.pack()

        # Create a listbox showing new features
        feature_listbox = Listbox(update_info_window, width=180, height=5, font=("Arial", 12))
        feature_listbox.pack()

        # Add new feature to listbox
        feature_listbox.insert(END, "1. Added the feature to automatically detect the first youtube link in the clipboard when returning to the application (including setting whether to enable or disable this feature))")
        feature_listbox.insert(END, "2. Modifying the feature to save the log file when the video is finished downloading is to add the video download time to the file and the name of the performer.")
        feature_listbox.insert(END, "3. Add the feature to directly download the app's update file right in the application to avoid having to go to the browser (can press the shortcut Alt+Ctrl+D))")
        feature_listbox.insert(END, "4. Modify the title of the window and add a window that checks for updates.")
        feature_listbox.insert(END, "5. Fixed a bug where 'StreamingData' was loading causing the video to be unplayable!")
        feature_listbox.insert(END, "6. App could not be checked and updated!")
        feature_listbox.insert(END, "7. Fix error with 'Can't extract video info'!")
        feature_listbox.insert(END, "8. Revised voice notification feature and if there is any problem with this feature during download, just ignore it!")
        feature_listbox.insert(END, "9. Add a feature to check network connectivity before entering the application!")
        feature_listbox.insert(END, "10. Change the app logo to celebrate the app's 1 year anniversary!!!")
        feature_listbox.insert(END, "👉It's over.")
        # Create a label that displays contact information
        contact_label = Label(update_info_window, text="⛔Any questions please contact via Facebook: https://bom.so/FB_ADMIN!", font=("Times New Roman bold", 14))
        contact_label.pack()
    fme.add_command(label='App shortcuts', command=shortcut)
    fme.add_separator()
    fme.add_command(label='Setting', command=lambda: setting(True), accelerator='Ctrl+I')

    #HELP
    hep = Menu(menubadr, tearoff=False, font=("Arial bold", 12))
    hep_sup = Menu(hep, tearoff=0, font=("Arial bold", 11))

    #OPTION HELP
    hep.add_cascade(label='Info', command=lambda: info(True), accelerator='Ctrl+K')
    hep.add_separator()
    hep.add_cascade(label='Check for updates', accelerator='Alt+D', command=lambda: check(True), font=("Arial italic", 10))
    hep.add_separator()
    hep.add_cascade(label='Check update version 2(...)',accelerator='Alt+Ctrl+D', command= lambda:update(True),compound='left', font=("Arial italic", 8))
    hep.add_separator()
    hep.add_command(label='Copyright©', accelerator='Ctrl+W', command=lambda: about_window(True), compound='left', underline=0, font=("Arial", 10))
    hep.add_separator()
    hep.add_command(label="Update Info", command=show_update_info2)

    #MENU OPTION
    opt = Menu(menubadr, tearoff=False)
    opt_s = Menu(opt, tearoff=0)

    opt.add_command(label='Change background color(background) app', accelerator='Ctrl+Shift+I', command=lambda: changebg(True), compound='left', font=("Verdana bold", 12 ))
    opt.add_separator()
    opt.add_command(label='Reset color to default', accelerator='Ctrl+R', command=lambda: resetbg(True), compound='left',font=("Times New Roman italic", 11))

    #txa.bind("<Button-3>", show)
    def show_window(icon, item):
        icon.stop()
        txa.after(0,txa.deiconify())

    def quit_window(icon, item):
        icon.stop()
        txa.destroy()

    # Hide the window and show on the system taskbar
    def hide_window():
        messagebox.showinfo("🥇🥇SYSTEM TRAY UCI","🙌🙌DOWNLOAD APP TO SYSTEM Tray!!")
        messagebox.showinfo("👉👉👉👉 INFORMATION 🍀🍀", "🔽🔽🔽 PLEASE CLICK ON THE SYSTEM Tray ICON AND CHOOSE THE NECESSARY FUNCTION!!🔽🔽")
        txa.withdraw()
        image=Image.open("logo-app.ico")
        menu=(item('Show app', show_window), item('Quit', quit_window), item('Check for updates', check), item('Website', contact))
        icon=pystray.Icon("name", image, "YT DOWNLOADER TXA - PRO({lang_sys}) V3.7.5", menu)
        icon.run()

menubadr.add_cascade(label='File', menu=fme, font=("Arial bold", 9))
menubadr.add_cascade(label='Help', menu=hep, font=("Arial bold", 9))
menubadr.add_cascade(label='Option', menu=opt, font=("Verdana italic", 9))

txa.config(menu=menubadr)
start_application()
get_date()
# check_inter()
txa.bind_all("<Alt-q>", exi)
txa.bind("<Control-W>", about_window)
txa.bind("<Control-w>", about_window)
txa.bind("<Alt-d>", check)
txa.bind("<Control-K>", info)
txa.bind("<Control-k>", info)
# Gán sự kiện Motion cho cửa sổ giao diện
txa.bind("<Motion>", print_mouse_position)
txa.protocol('WM_DELETE_WINDOW', hide_window)
if detect_link == 'True':
    txa.bind("<FocusIn>", on_focus)
else:
    pass
txa.bind("<Control-r>", resetbg)
txa.bind("<Control-I>", changebg)
txa.bind("<Control-i>", setting)
txa.bind("<Alt-Control-d>", update)
txa.mainloop()