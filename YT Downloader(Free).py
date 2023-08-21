import subprocess
from pathlib import Path
import threading
from tkinter import *
import urllib.request
from tkinter import colorchooser
import requests
from configparser import ConfigParser
from time import strftime, gmtime
from pytube import request
from pytube import YouTube
from tkinter import filedialog
from tkinter import messagebox
import os,sys,clipboard
import json
from win10toast import ToastNotifier
import _thread
from tkinter.ttk import Progressbar
from tkinter.ttk import Combobox
from datetime import datetime,date
from datetime import timedelta
from random import random
from random import randint
from random import seed
import time
import winreg
from pystray import MenuItem as item
import pystray
from PIL import Image, ImageTk
# import pywin32
import _thread
import socket, sys
from tkinter import ttk
from pytube.helpers import safe_filename
import urllib.request
import threading
from pySmartDL import SmartDL
from tqdm import tqdm
import re
now = datetime.now()
hour = now.strftime("%H")
minute = now.strftime("%M")
second = now.strftime("%S")
day = now.strftime("%d")
month = now.strftime("%m")
year = now.strftime("%Y")
fr = strftime("%Y-%m-%d %H:%M:%S", gmtime())
t = ToastNotifier()
i="0"
#BTHUC
url_regex = r"(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})"

path_to_file = 'user.ini'
path = Path(path_to_file)

if path.is_file():
   pass
else:
    messagebox.showwarning("ERROR","Không tìm thấy file cấu hình để đọc dữ liệu!\nVui lòng thêm nó từ trang web http://txaml.viwap.com/user.ini nếu k có hoặc xem lại thư mục cài đặt ứng dụng!\n Còn nếu không đươc nữa thì ib qua fb ở menu Help nhé!")
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
        socket.create_connection(("yt-txa.mw.lt", 80))
        return True
    except OSError:
        return False

def start_application():
    if check_internet_connection() and check_network_connection():
        # Ứng dụng của bạn bắt đầu ở đây
        messagebox.showinfo("Kết nối thành công✅✅✅", "☑️✔️Kết nối thành công tới server!")
    else:
        wifi_icon = "📶"
        messagebox.showerror("Kết nối thất bại tới server❌❌", f"{wifi_icon} Bạn hiện không có kết nối mạng vì vậy sẽ không truy cập được vào ứng dụng!\nVui lòng kết nối mạng và thử lại!!! ❤️❤️")
        sys.exit()


def show_update_notification():
    # Tạo đối tượng ToastNotifier
    toaster = ToastNotifier()

    try:
        # Get the version data from the web
        url = 'https://yt-txa.mw.lt/get-version.json'
        response = requests.get(url)
        data = response.json()

        # Get the current version and compare it to the online version
        current_version = "3.7"
        online_version = data["pban"]
        if current_version < online_version:
            toaster.show_toast("Cập nhật", f"Đang có phiên bản mới nhất là v{online_version}! Hãy vào thanh menu chọn 1 trong 2 chức năng cập nhật bản 1 và bản 2 để cập nhật nó đi nào!!!!\n©️COPY BY TXAVLOG!!", duration=10)
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Lỗi kết nối mạng", str(e))
    except (KeyError, json.JSONDecodeError) as e:
        messagebox.showerror("Lỗi dữ liệu", str(e))
    except Exception as e:
        messagebox.showerror("Lỗi không xác định", str(e))

def nen_i():
    # Tạo một luồng (thread) riêng biệt để hiển thị thông báo
    notification_thread = threading.Thread(target=show_update_notification)
    notification_thread.start()

    txa.after(15000, nen_i)

#UPDATE
def update():
    start_time_2 = time.time()  # Khởi tạo biến start_time
    def check_for_updates():
        # Disable the Check for Updates button to prevent multiple updates
        check_for_updates_button.config(state="disabled")

        # Define the update function to run in a separate thread
        def do_update():
            try:
                # Get the version data from the web
                url = 'https://yt-txa.mw.lt/get-version.json'
                response = urllib.request.urlopen(url)
                data = json.loads(response.read())

                # Get the current version and compare it to the online version
                current_version = "3.7"
                online_version = data["pban"]
                if current_version == online_version:
                    messagebox.showinfo("Không có bản cập nhật khả dụng", "App của bạn đã được cập nhật ở phiên bản mới nhất😂.")
                else:
                    # Prompt the user to download the update
                    if messagebox.askyesno("Cập nhật khả dụng",
                                        f"Có 1 phiên bản mới: v{online_version} được tìm thấy trên trang web của chúng tôi vào ngày {data['day']}/{data['mon']}/{data['year']}.\n Bạn có muốn tải nó ngay bây giờ?"):
                        
                        # Download the updated file
                        download_url = data["server_file"]
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
                messagebox.showerror("Error", str(e))

            # Re-enable the Check for Updates button
            check_for_updates_button.config(state="normal")

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

    def on_closing():
        if messagebox.askokcancel("Thoát ứng dụng", "Đang trong quá trình tải xuống. Bạn có chắc muốn thoát?"):
            update.destroy()

    # Create the main window
    update = Tk()
    update.title("Kiểm tra cập nhật ứng dụng")

    # Create the Check for Updates button
    check_for_updates_button = Button(update, text="Check for Updates", command=check_for_updates)
    check_for_updates_button.pack(pady=10)

    # Create the progress bar and label
    progress_bar = ttk.Progressbar(update, orient="horizontal", mode="determinate")
    progress_label = Label(update, text="")
    progress_bar.pack(pady=10)
    progress_label.pack(pady=5)

    # Add the on_closing function to handle closing event
    update.protocol("WM_DELETE_WINDOW", on_closing)

    # Start the Tkinter event loop
    update.mainloop()


#Số lần tải xuống video:
# Hàm để lấy giá trị "downloads_left" từ registry key "SOFTWARE\\Button_DOWNLOAD"
def get_downloads_left():
    try:
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, "SOFTWARE\\Classes\\Applications\\YT Downloader(Free).exe\\Button_DOWNLOAD")
        downloads_left = winreg.QueryValueEx(key, "downloads_left")[0]
        winreg.CloseKey(key)
    except WindowsError:
        # Trường hợp key không tồn tại, tạo mới key với giá trị mặc định là 50
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, "SOFTWARE\\Classes\\Applications\\YT Downloader(Free).exe\\Button_DOWNLOAD")
        downloads_left = 50
        winreg.SetValueEx(key, "downloads_left", 0, winreg.REG_DWORD, downloads_left)
        winreg.CloseKey(key)
    return downloads_left

# Cập nhật label "Số lần tải xuống còn lại" và kiểm tra số lần tải xuống sau mỗi khoảng thời gian nhất định
def update_downloads_left_label():
    downloads_left = get_downloads_left()
    downloads_left_label.config(text="Số lần tải xuống còn lại: {}".format(downloads_left))
    if downloads_left == 0:
        messagebox.showinfo("Hết lượt tải xuống", "Bạn đã hết lượt tải xuống video vui lòng mua bản PRO để không bị giới hạn.")
        txa.destroy()
    else:
        txa.after(1000, update_downloads_left_label)

# Create a window
# msb_welcome = messagebox.showinfo("Welcome", "Chào mừng bạn đến với YouTube Downloader")
# msb_read = messagebox.showinfo("READ", "Khi sử dụng ứng dụng là bạn đã đồng ý với các điều khoản của chúng tôi. Đọc thêm tại: https://bom.so/README")
# # msb_info = messagebox.showinfo("INFO", "APP ĐƯỢC VIẾT BỞI TXA VLOG!")
txa = Tk()
txa.geometry('670x330')
txa.resizable(0,0)
txa.title("Trình tải xuống video Youtube v3.7 - Free")
txa.resizable(False, False)
# txa.iconbitmap('logo.ico')
parser = ConfigParser()
parser.read('user.ini')
save_bgcolor = parser.get('setting', 'bg_color')
# new_bgcolor = parser.set('setting', 'bg_color', 'black')
save_path = parser.get('setting', 'noiluu')
save_tttb = parser.get('setting', 'tbao')
title_ban = parser.set('setting', 'phienban', 'Free')
lay_ngay = parser.get('setting', 'ngayhientai')
na_dat = str(day)+'/'+str(month)+'/'+str(year)+' '+str(hour)+':'+str(minute)+':'+str(second)
set_ngay = parser.set('setting', 'ngayhientai', na_dat)
check_duration = parser.get('setting', 'duration')
check_ne = parser.get('APP', 'check_start')
# Tạo đường dẫn đến khóa registry
key_path = "Software\\Classes\\Applications\\YT Downloader(Free).exe\\Time Trial"

# Lấy thời gian khởi động ứng dụng từ registry
def get_start_time():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path)
        value, regtype = winreg.QueryValueEx(key, "Time_Trial")
        return datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
    except WindowsError:
        return None

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
    with open("log.txaweb2", 'w') as f:
        f.write(f"Đường dẫn của bạn là {save_path} với trạng thái là {download_path_exists}!Đây là bản 🆓")
        f.write('\n')
        f.write('👉Nguồn: ©️TXA VLOG!!\n')
        f.close()
    txa.after(int(check_duration), check_download_path)


# Lưu thời gian khởi động ứng dụng vào registry
def save_start_time():
    value = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)
    winreg.SetValueEx(key, "Time_Trial", 0, winreg.REG_SZ, value)

# Tính số ngày còn lại trong thời gian dùng thử
def get_remaining_days():
    start_time = get_start_time()
    if start_time is None:
        save_start_time()
        start_time = get_start_time()
    days = (datetime.now() - start_time).days
    remaining_days = 30 - days
    return remaining_days if remaining_days > 0 else 0
    
    #return remaining_time if remaining_time > 0 else 0

# Kiểm tra thời gian dùng thử
def check_trial():
    remaining_days = get_remaining_days()
    # # remaining_time = remaining_days()
    # remaining_time_seconds = int(remaining_time.total_seconds())
    # time = str(datetime.timedelta(seconds=remaining_time_seconds))
    # remaining_time_str = str(remaining_days)[:-7]
    if remaining_days == 0:
        messagebox.showinfo("Thông báo", "Bạn đã hết thời gian dùng thử. Vui lòng mua bản PRO hoặc cài lại app để khôi phục lại thời gian.")
        remain.config(text="Đã hết hạn dùng thử")
        txa.destroy()
    else:
        remain.config(text="Bạn còn " + str(remaining_days) + " ngày dùng thử!")

# Cập nhật thời gian dùng thử mỗi 1 giây
def update_time():
    check_trial()
    txa.after(1000, update_time)


with open ('user.ini', 'w') as f:
    parser.write(f)
txa.configure(background=save_bgcolor)
print(na_dat)
print(save_path)
print(save_bgcolor)
print(lay_ngay)
print("Trạng thái thông báo: ",save_tttb)
print(time)



def donglenh():
    lenh = input()
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
            
for i in range(1,5):
    with open("user_account.txa", 'w+', encoding="UTF-8") as f:
        f.write("TIME: "+ str(hour)+':'+str(minute)+':'+str(second)+'\n')
        f.write(str(i))
        f.write('\n')
        f.write("DATE: "+str(day)+'\n')
        f.write("MONTH: "+str(month)+'\n')
        f.write("YEARS: "+str(year)+'\n')
        f.close()

def changebg(event=None):
    
    color2 = colorchooser.askcolor()[1]
    if color2:
        if color2 == '#0d0006' or color2 == '#020202' or color2 == '#121212' or color2 == '#070707':
            color2 = 'black'
        else:
            parser.set('setting','bg_color',color2)
        with open('user.ini','w') as f:
            parser.write(f)
        txa.configure(background=color2)

def resetbg(event=None):
    color2 = 'black'
    parser.set('setting','bg_color',color2)
    with open('user.ini','w') as f:
            parser.write(f)
    txa.configure(background=color2)

def setting(event=None):
    uk = Toplevel(txa)
    check_ne = parser.get('APP', 'check_start')
    uk.grab_set()
    uk.title("Cài đặt")
    uk.geometry('400x400')
    check_duration = parser.get('setting', 'duration')
    uk.resizable(False, False)
    anh = Label(uk, text='Thông báo khi tải xong: ', font=("Verdana italic", 13), background='red')
    anh.place(x=10, y=5)
    time_entry_var = StringVar()

#SAVE SETTING IN CONFIG FILE
    def save():
        lol = str(var.get())
        dlo = time_entry_var.get()
        clo = str(car.get())
        print(lol)
        print(f"CM{clo}")
        print(f"THời gian kiểm tra là: {dlo}ms")
        if lol == save_tttb and dlo == check_duration:
            messagebox.showinfo("ERROR","Bạn đã cài đặt thành như thế r thi!")
        if clo == "1":
            check_status_net = "True"
        elif clo == "2":
            check_status_net = "False"
        else:
            check_status_net = "None"
        # if lol == 1:
        #     lol = "True"
        # else:
        #     lol = "False"
        # # i+=1
        # if save_tttb == 1:
        #     lol = 1
        # else: 
        #     lol = 2
        parser.set('setting','tbao', lol)
        parser.set('setting', 'duration', dlo)  # Lưu giá trị nhân 1000 (dạng chuỗi) vào file cấu hình
        parser.set('APP', 'check_start', check_status_net)
        with open("user.ini", 'w')as f:
            parser.write(f)
        print("Đã lưu!")
        
        messagebox.showinfo("THÔNG BÁO", "Vui lòng khởi động lại ứng dụng để cập nhật cài đặt!")
        uk.destroy()
        return "break"
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
#RADIO STATUS
    var = IntVar()
    r1 = Radiobutton(uk, text="Bật", variable=var, value=1)
    r1.place(x=230, y=5)
    r2 = Radiobutton(uk, text="Tắt", variable=var, value=2)
    r2.place(x=275, y=5)
    check_path_status_var = IntVar()
            
        # Thêm chức năng nhập thời gian
    time_label = Label(uk, text='Nhập thời gian (đơn vị miligiây):', borderwidth=2, relief="raised", font=("Arial", 13), background='#C0F0CC')
    time_label.place(x=10, y=30)
    time_entry = Entry(uk, textvariable=time_entry_var, font=("Arial", 13), width=10)
    time_entry.place(x=260, y=30)
    check_net = Label(uk, text="Kiểm tra kết nối tới server mỗi khi khởi động: ", borderwidth=4, relief="raised", font=("Verdana", 7), background='#0fc0ff')
    check_net.place(x=10, y=55)
    car = IntVar()
    check_net_bt_1 = Radiobutton(uk,text="Có", variable=car, value=1)
    check_net_bt_1.place(x=240, y=55)    
    check_net_bt_2 = Radiobutton(uk,text="Không", variable=car, value=2)
    check_net_bt_2.place(x=285, y=55)
    if save_tttb == "1":
            var.set('1')
    elif save_tttb == "2":
            var.set('2')
    else:
            print("LOI")
    if check_ne == "True":
        car.set('1')
    elif check_ne == "False":
        car.set('2')
    else:
        print("K tồn tại")
    ani = Label(uk, text='Đg update....', font=("Digital-7", 30))
    ani.place(x=10, y=210)
# if day == "23" and month == "06" and year == "2022":
#         t = ToastNotifier()
#         t.show_toast("The update is available", "ĐÃ CÓ BẢN CẬP NHẬT MỚI!")
#SAVE BUTTON
    button = Button(uk, text="Lưu cài đặt", command=save, background='blue')
    button.place(x=15, y=370)

def about_window(event=None):
    tt=Toplevel(txa)
    tt.title("THÔNG TIN Phiên bản⏬: ")
    tt.transient(txa)
    tt.resizable(False, False)
    tt.geometry('600x500')
    tt.configure(bg='blue')
    def close():
        tt.destroy()
        tt.protocol('WM_DELETE_WINDOW', close)
        return "break"

    def contact():
        os.startfile("https://bom.so/FB_ADMIN")

    def dow():
        os.startfile("https://yt-txa.mw.lt")

    def buypro():
        # os.startfile("http://txaml.viwap.com/buy.html")
        os.startfile("https://yt-txa.mw.lt/buy.html")

    a1 = Label(tt, text="💖APP ĐƯỢC VIẾT BỞI TXA VLOG!💖", font=("Courier New", 12), background='red')
    a1.place(x=12, y=30)
    a2 = Label(tt, text="©️COPYRIGHT BY TXA VLOG! ❌DO NOT REUP❌", font=("Courier New", 12), background='red')
    a2.place(x=12, y=50)
    a3 = Label(tt, text="👉Đây là bản Free!\n 👉Khuyên bạn hãy mua bản Pro ở trang web của chúng tôi!\n 👉Để tận hưởng đc đầy đủ tính năng nhé!!!😍😍", font=("Digital-7", 13), background='green')
    a3.place(x=12, y=70)
    a4 = Button(tt, text="CONTACT ME", font=("Times New Roman", 12), background='red', foreground='yellow', command=contact)
    a4.place(x=12, y=150)
    a5 = Label(tt, text="Bấm vào đây để quay lại☝️", font=("Arial", 12))
    a5.place(x=400, y=5)
    a6 = Button(tt, text="▶️GO TO DOWNLOAD APP", font=("Verdana italic", 12), background='brown', foreground='red', command=dow)
    a6.place(x=130, y=150)
    a7 = Button(tt, text="📲Mua bản PRO", font=("Arial underline", 13), bg='red', fg='yellow', command=buypro, cursor='plus')
    a7.place(x=380, y=150)




def txa_popup(e):
    txa_menu.tk_popup(e.x_root, e.y_root)

def contact():
    os.startfile("https://bom.so/FB_ADMIN")

def exi():
    # a = messagebox.askyesno("🖐Dừng lại🖐", "❌Bạn có đang tải gì k đấy????❌")
    # if a==True:
    #     pass
    # elif a==False:
        raise SystemExit(0)

def error():
    messagebox.showwarning("❌Không khả dụng❌","👉Phím tắt này chỉ có sẵn trg phiên bản Pro!\nVui lòng mua nó để dùng phím tắt này☝️")

def error1():
    messagebox.showwarning("❌Không khả dụng❌","👉Phím tắt này hiện chỉ có sẵn trg phiên bản Pro!\nVui lòng mua nó để dùng phím tắt này☝️")

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
    st.geometry('750x250')
    st.configure(bg='blue')

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
        (2, "Ctrl+K", "Hthị thông tin"),
        (3, "Ctrl+R", "RESET MÀU NỀN VỀ MẶC ĐỊNH"),
        (4, "Ctrl+I", "Đổi màu nền app"),
        (5, "Ctrl+Shift+I", "Mở cài đặt"),
        (6, "Đg cập nhật thêm ", "cho bản Free.")
        # (4,'Rachna','Mumbai'),
        # (5,'Shubham','Delhi')
        ]
    
    # find total number of rows and
    # columns in list
    total_rows = len(lst)
    total_columns = len(lst[0])
    t = Table(st)

current_percentage = 0  # Biến toàn cục để lưu giá trị phần trăm hiện tại

def show(ul, chunk, byte_remaining):
    global current_percentage

    downloaded = ul.filesize - byte_remaining
    total_size = ul.filesize
    new_percentage = int((downloaded / total_size) * 100)

    if new_percentage > current_percentage:
        for percentage in range(current_percentage + 1, new_percentage + 1):
            current_percentage = percentage
            pt_download['value'] = current_percentage
            status.configure(text="DOWNLOADING...{:02d}%".format(current_percentage))
            txa.after(100, lambda: None)  # Cần có một tác vụ nhỏ để tránh đóng băng ứng dụng

    if new_percentage == 100:
        status.configure(text="Tải xuống thành công! 🎉")
    else:
        txa.after(100, lambda: show(ul, chunk, byte_remaining))

def download():
    urls = str(url.get())
    mk = cbb.get()
    global fl
    downloads_left = get_downloads_left()
    if downloads_left > 0:
        downloads_left -= 1
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, "SOFTWARE\\Classes\\Applications\\YT Downloader(Free).exe\\Button_DOWNLOAD")
        winreg.SetValueEx(key, "downloads_left", 0, winreg.REG_DWORD, downloads_left)
        winreg.CloseKey(key)
        downloads_left_label.config(text="Số lần tải xuống còn lại: {}".format(downloads_left))
    else:
        messagebox.showinfo("Hết lượt tải xuống", "Bạn đã hết lượt tải xuống video.")
        txa.destroy()
    # yt = YouTube(urls)
    # status = Label(txa, font=("Arial bold", 15), background='#ff0fff')
    # status.place(x=50, y=160)
    # status.configure(text = "DOWNLOADING...")
    # stream = ul.length
    
    if not re.match(url_regex, urls):
        messagebox.showerror("Lỗi", "URL video không đúng định dạng!\n Vui lòng viêt theo định dạng: https://(http://)youtube.com(youtu.be)/watch?v=id(id)")
        return
    ul = YouTube(str(url.get()), on_progress_callback=show, use_oauth=False, allow_oauth_cache=True)
    if not fl:
        msb_path = messagebox.showwarning("CẢNH BÁO", "❌Vui lòng chọn đường dẫn❌")
    if not cbb:
        messagebox.showwarning("CẢNH BÁO","❌Vui lòng chọn chất lượng để tải xuống❌")

    print("DOWNLOADING>>>>>>", urls)
    status.config(text="✨GETTING DATA FROM YOUTUBE.")
    time.sleep(0.1)
    status.config(text="✨✨GETTING DATA FROM YOUTUBE..")
    time.sleep(0.3)
    status.config(text="✨✨✨GETTING DATA FROM YOUTUBE...")
    status.config(text="✨GETTING DATA FROM YOUTUBE.")
    time.sleep(0.3)
    status.config(text="✨✨GETTING DATA FROM YOUTUBE..")
    time.sleep(0.5)
    status.config(text="✨✨✨GETTING DATA FROM YOUTUBE...")
    check_download_path()
    if(mk == ''):
        messagebox.showerror("CẢNH BÁO", "❌Vui lòng chọn chất lượng để tải xuống!")
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
        # a = ul.streams.filter(progressive=True, file_extension='mp4').get_by_resolution('240p')
        # b = a.download(fl, filename='TXA VLOG - ' + safe_filename(ul.title) + ' - 240p.mp4')
        # print(b)
        # file_extension = '.mp4'
        # chatluong = "video: 240p"
        a = ul.streams.filter(only_audio=True).first()
        b = a.download(fl, filename='TXA VLOG - ' + safe_filename(ul.title) + ' - 128kps.mp3')
        file_extension = '.mp3'
        chatluong = "nhạc: 128kps"
        az = "128kps"
    #     a = ul.streams.filter(progressive=True, only_audio=True).first().download(fl)
        # file_name = b.title
        # # ten_vd2 = ten_vd.replace("|", " ")
    size = round(a.filesize/1024/1024, 2)
        # thoigian = b.length
    thoigian = ul.length
    duration_str = f"{thoigian // 3600}:{(thoigian // 60) % 60}:{thoigian % 60}"
    luot_Xem_htai = ul.views
    kenh = ul.channel_url
    key = ul.keywords
    mta = ul.description
    meta = ul.age_restricted
    s = ul.metadata
    parser.set('setting', 'noiluu', fl)
    with open('user.ini','w') as f:
        parser.write(f)
        # file_size = round(a.filesize/1024/1024, 2)
        # text_info.insert("Kích thước: " + str(file_size) + "MB" + "\n" + "Địa chỉ: " + str(file_name) + "\n")
    # tbao = ToastNotifier()
    # tbao.show_toast("DOWNLOADED VIDEO", "ĐÃ TẢI XONG VIDEO. \n Kích thước ước lượng: " + str(size)+"MB! \n Hãy kiểm tra nó đi nào!!!!\n APP BY TXA VLOG:))")
    if save_tttb == "1":
        messagebox.showinfo("Thông báo", "Tải xuống thành công. \nVui lòng kiểm tra thư mục " + fl + "\n Với tên: " + safe_filename(ul.title) + file_extension + "\n Kích thước: " + str(size) + "MB" + "\n Thời gian: "+ duration_str + "\n Chất lượng " + str(chatluong))
        messagebox.showinfo("Thông tin trên YT về video từ link của bạn", "Số lượt xem video ở thời điểm htại: " + str(luot_Xem_htai) + " views! \n URL kênh: " + kenh + "\n Từ khóa video: " + str(key))
    elif save_tttb == "2": 
        pass
    # status = Label(txa, text="DOWNLOADED!", font=("Arial bold", 15), background='#ff0fff').place(x=50, y=160)
    else: 
        print("LỖI FILE CẤU HÌNH")
    status.config(text="Đã tải xong")
    txa.title("VideoDownloaded tại thư mục: " + fl + "!Chất lượng: "+ az)
    with open("Mô tả về video-with open notepad "+safe_filename(ul.title)+".data", "w") as file:
        file.write(str(mta))
        file.write("\n\n")
        file.write("TẠO VÀO LÚC: "+str(day)+'/'+str(month)+'/'+str(year)+' '+str(hour)+':'+str(minute)+':'+str(second)+'!\n')
        file.write("URL VIDEO: "+urls+'\n')
        file.write("Chất lượng: "+az+'\n')
        file.write("Nơi lưu file video này: " + fl + "/" + safe_filename(ul.title) + file_extension+"!\n")
        file.write("©FILE BY TXA VLOG!!IB FB ME: https://bom.so/FB_ADMIN")
        file.close()
    with open(fl+"HELLO.txt","w") as f:
        f.write("LOL")
        f.close()

    print(meta) 
    print(str(s))
    # + "Thời gian: " + str(thoigian) + "s"
    # END, "Tên video: " + ten_vd  + "\n" 
def info(event=None):
    messagebox.showinfo("INFO", "💖APP ĐƯỢC VIẾT BỞI TXA VLOG!💖")
    messagebox.showinfo("INFO", "✝Chức năng: TẢI XUỐNG VIDEO YOUTUBE")
    messagebox.showinfo("INFO", "✔VERSION 3.7\n Nếu có thắc mắc ib fb: https://bom.so/FB_ADMIN")

# def clif():
#     messagebox.showinfo("INFO", "✔VERSION 2.2\n Nếu có thắc mắc ib fb: https://bom.so/FB_ADMIN")

def check():
    ht ="3.7"
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
    getdl = f'{up["pban"]}'

    for i in range(3):
        with open('CHECKING UPDATE_'+ str(year)+str(month)+str(day)+'-'+str(hour)+str(minute)+str(second)+'.txa', "+w") as f:
            f.write('CHECK UPDATE....')
            f.write('\n')
            f.write('Phiên bản hiện tại của bạn là: '+str(ht)+'\n')
            f.write("Phiên bản trên trang web của chúng tôi: "+str(getdl)+'\n')
            f.write("DATE: "+ str(year)+'/'+str(month)+'/'+str(day)+'-'+str(hour)+':'+str(minute)+':'+str(second)+'('+str(fr)+')'+'\n')
            f.write("INDEX OF "+str(i)+'\n')
            f.write("DATE UPDATE: "+str(d1)+'/'+str(m1)+'/'+str(y1)+'\n')
            f.write("©️Copy by TXA VLOG!!®️\n")
            f.write("Đây là bản 🆓🆓🆓🆓!")
            f.close()
    # htai = f'{up["hta"]}'
    if getdl > str(ht):
        messagebox.showinfo("The update is available v" +getdl, "ĐÃ CÓ BẢN CẬP NHẬT MỚI VÀO NGÀY "+day+'/'+month+'/'+year+"!\n HÃY TRUY CẬP TRANG WEB https://bom.so/YouTube-Downloader để lấy phiên bản mới nhất!!🙌")
    elif getdl < str(ht):
        messagebox.showerror("There is no update", "CHX CÓ BẢN CẬP NHẬT KHẢ DỤNG😂("+ht+")")

    else:
        messagebox.showwarning("THIS IS A UPDATE LASTED VERSION!!" + str(ht), "BẠN ĐANG Ở PBẢN MS NHẤT R CÒN GÌ😒😒😒!")
    print("DONE!!")
        
# Create a label
title_window = Label(txa, text="YouTube Downloader", font=("Arial bold", 20), background='#f5f5f5').place(x=190, y=10)

#INSERT URL
url = StringVar()
url_label = Label(txa, text="URL:", font=("Arial bold", 15), background='#ff0f0f').place(x=70, y=70)
url_entry = Entry(txa, width=30,textvariable = url, font=("Arial bold", 15), background='#00cf0f').place(x=150, y=70)

#RIGHTMENU
txa_menu = Menu(txa, tearoff=False)
txa_menu.add_command(label="Copy url", command=di)
txa_menu.add_separator()
txa_menu.add_command(label="CONTACT ME", command=contact)

txa.bind("<Button-3>", txa_popup)

#INSERT PATH
path = StringVar()
path_label = Label(txa, text="PATH:", font=("Arial bold", 15), background='#ff0fce').place(x=70, y=100)
path_e = Entry(txa,text=save_path, width=30, font=("Arial bold", 15), background='#00cf0f', textvariable=path).place(x=150, y=100)
path_button = Button(txa,height=-50, text="Browse", font=("Arial bold", 15), background='#00cfff', command=get_path).place(x=500, y=100)

#INSERT COMBOBOX
combo_label = Label(txa, text="Quality:", font=("Arial bold", 15), background='#f00f0f').place(x=70, y=130)
qua = ["Cao(720p)", "360p", "144p", "MP3 Audio File"]
cbb = Combobox(txa, width=30, font=("Arial bold", 15),state='readonly', values=qua, background='#00c00f')
cbb.grid(column=0, row=0, sticky=(W, E))
cbb.place(x=150, y=130)


#PT_DOWNLOAD
pt_download = Progressbar(txa, orient='horizontal', length=300, mode='determinate')
pt_download.place(x=90, y=190)

#BUTTON
btn_download = Button(txa, text="Download", font=("Arial bold", 15), background='#00cfff', command=lambda:_thread.start_new_thread(download, ())).place(x=220, y=230)
# btn_info = Button(txa, text="Xem thông tin app", font=("Arial bold", 15), background='#00cfff', command=info).place(x=120, y=230)
# btn_clif = Button(txa, text="Xem phiên bản", font=("Arial bold", 15), background='#00cfff', command=clif).place(x=500, y=230)
# btn_check = Button(txa, text="Kiểm tra cập nhật", font=("Arial bold", 16), background='#00cfff', command=check).place(x=450, y=230)

#STATUS
status = Label(txa, font=("Arial bold", 15), background='#ff0fff')
status.place(x=90, y=160)

#TEXT_INFO
text_info = Label(txa, width=50, height=10, font=("Arial bold", 15), background='#00cfff')

#REMAIN FREE
remain = Label(txa, text='Tgian dùng thử ở đây', font=("Verdana italic", 16), background='#f0c0ff')
remain.place(x=10, y=290)

#OPTION LEFT
menubadr = Menu(txa, selectcolor='#fff0cc')
fme = Menu(menubadr,tearoff=0)
sub = Menu(fme, tearoff=0)


# fme.add_cascade(label='FUNCTION', menu=sub)
# fme.add_separator()
# sub.add_command(label="LOL", command=te)
fme.add_command(label='Exit', command=exi)
fme.add_separator()
fme.add_command(label='Các phím tắt trg app', command=shortcut)
fme.add_separator()
fme.add_command(label='Setting', command=lambda: setting(True), accelerator='Ctrl+Shift+I')

#HELP
hep = Menu(menubadr, tearoff=False, font=("Arial bold", 12))
hep_sup = Menu(hep, tearoff=0, font=("Arial bold", 11))

#OPTION HELP
hep.add_cascade(label='Thông tin', command=lambda: info(True), accelerator='Ctrl+K')
hep.add_separator()
hep.add_cascade(label='Check cập nhật', command=check, font=("Arial italic", 10))
hep.add_separator()
hep.add_cascade(label='Check cập nhật phiên bản 2(Online)', command= lambda:update(), font=("Verdana italic", 14))
hep.add_separator()
hep.add_command(label='Bản quyền', accelerator='Ctrl+W', command=lambda: about_window(True), compound='left', underline=0, font=("Arial", 10))
# hep.add_separator()

#MENU OPTION
opt = Menu(menubadr, tearoff=False)
opt_s = Menu(opt, tearoff=0)

opt.add_command(label='Đổi màu nền(background) app', accelerator='Ctrl+I', command=lambda: changebg(True), compound='left', font=("Verdana bold", 12))
opt.add_separator()
opt.add_command(label='Reset màu về mặc định', accelerator='Ctril+R', command=lambda: resetbg(True), compound='left',font=("Times New Roman italic", 11))

#txa.bind("<Button-3>", show)
def show_window(icon, item):
   icon.stop()
   txa.after(0,txa.deiconify())

def quit_window(icon, item):
   icon.stop()
   txa.destroy()

# Label để hiển thị số lần tải xuống còn lại
downloads_left_label = Label(txa, text="")
downloads_left_label.pack()

# Hide the window and show on the system taskbar
def hide_window():
   messagebox.showinfo("🥇🥇ĐÃ THU NHỎ","🙌🙌ỨNG DỤNG ĐÃ ĐC THU NHỎ XUỐNG KHAY HỆ THỐNG!!")
   messagebox.showinfo("👉👉👉👉THÔNG TIN🍀🍀", "🔽🔽🔽VUI LÒNG CLICK CHUỘT PHẢI VÀO ICON Ở KHAY HỆ THỐNG VÀ CHỌN CHỨC NĂNG CẦN THIẾT!!🔽🔽")
   #t.show_toast("🥇🥇ĐÃ THU NHỎ", "🙌🙌ỨNG DỤNG ĐÃ ĐC THU NHỎ XUỐNG KHAY HỆ THỐNG!!📍 📍", icon_path="logo.ico")
   #t.show_toast("👉👉👉👉THÔNG TIN🍀🍀", "🔽🔽🔽VUI LÒNG CLICK CHUỘT PHẢI VÀO ICON Ở KHAY HỆ THỐNG VÀ CHỌN CHỨC NĂNG CẦN THIẾT!!🔽🔽", icon_path="logo.ico")
   txa.withdraw()
   image=Image.open("logo.ico")
   menu=(item('Hiển thị app', show_window), item('Thoát', quit_window), item('Check cập nhật', check), item('Trang web', contact))
   icon=pystray.Icon("name", image, "YT DOWNLOADER TXA - Free", menu)
   icon.run()


menubadr.add_cascade(label='File', menu=fme, font=("Arial bold", 9))
menubadr.add_cascade(label='Help', menu=hep, font=("Arial bold", 9))
menubadr.add_cascade(label='Option', menu=opt, font=("Verdana italic", 9))

txa.config(menu=menubadr)
# def key_press(evt):
#     # if evt=='Alt-q':
#     #     exi()
#     # elif 'Alt 1' in evt:
#     #     info()
#     if evt == "state=0x20000 keysym=q keycode=81 char='q'":
#         exi()

# txa.bind("<Alt-q>", key_press)


# txa.bind("<Alt-1>", key_press)
# txa.bind_all("<Alt-q>", error)
txa.bind("<Control-W>", about_window)
txa.bind("<Control-w>", about_window)
txa.bind("<Control-r>", resetbg)
# txa.bind("<Alt-d>", error1)
txa.bind("<Control-K>", info)
txa.bind("<Control-k>", info)
txa.bind("<Control-i>", changebg)
txa.bind("<Control-I>", setting)
# nen_i()
update_time()

if check_ne == "True":
# Gắn sự kiện kiểm tra kết nối mạng khi ứng dụng được mở
    start_application()
# txa.protocol('WM_DELETE_WINDOW', hide_window)

# Bắt đầu chương trình
downloads_left = get_downloads_left()
downloads_left_label.config(text="Số lần tải xuống còn lại: {}".format(downloads_left))
if downloads_left == 0:
    messagebox.showinfo("Hết lượt tải xuống", "Bạn đã hết lượt tải xuống video vui lòng mua bản PRO 🅿️ để không bị giới hạn!")
    txa.destroy()
else:
    txa.after(1000, update_downloads_left_label)
    txa.mainloop()

# txa.mainloop()