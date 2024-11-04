#vLong ne
den = '[1;90m'
luc = '[1;32m'
trang = '[1;37m'
red = '[1;31m'
vang = '[1;33m'
tim = '[1;35m'
lamd = '[1;34m'
lam = '[1;36m'
purple = '\e[35m'
hong = '[1;95m'
xnhac = '[1;95m'
xduong = '[1;95m'
do = '[1;33m'
thanh_xau = trang + '' + lam + '[' + vang + 'vL' + lam + '] ' + trang + ' ' + luc
thanh_dep = trang + '' + lam + '[' + luc + 'vL' + lam + '] ' + trang + ' ' + luc
#vlongshare donhe
import requests
import json
import os
from sys import platform
from datetime import datetime
from time import sleep, strftime
import hashlib
import hmac
import uuid

try:
    from pystyle import Colors, Colorate
except ImportError:
    os.system('pip install pystyle')
    from pystyle import Colors, Colorate

secret_key = 'vLongzZ'

def generate_signature(data, secret_key, nonce):
    message = f'{data}{nonce}'
    return hmac.new(secret_key.encode(), message.encode(), hashlib.sha256).hexdigest()

def is_connected():
    try:
        import socket
        socket.create_connection(('1.1.1.1', 53))
        return True
    except OSError:
        return False

headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 11; Live 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.28 Mobile Safari/537.36'}

banners = f"""        ________                    _____  _______      _____  
\______ \  __ __ ___.__.   /  |  | \   _  \    /  |  | 
 |    |  \|  |  <   |  |  /   |  |_/  /_\  \  /   |  |_
 |    `   \  |  /\___  | /    ^   /\  \_/   \/    ^   /
/_______  /____/ / ____| \____   |  \_____  /\____   | 
        \/       \/           |__|        \/      |__| 

thongtin = f"""
        Tải Tool + source tool tại : https://dichvukey.site
        Mua Key Tại : ZALO : 0789041631
        Giá Chỉ 1k / ngày
        MUA CODE - LÀM TOOL GỘP LIÊN HỆ
        Bot spam sms free : https://t.me/vlongbotsms
"""

def luu(key):
    try:
        with open("vLong_key.txt", 'w') as file_key:
            file_key.write(key)
    except Exception as e:
        print(f"Lỗi khi lưu key: {e}")

def checkkey(key):
    nonce = str(uuid.uuid4())
    signature = generate_signature(key, secret_key, nonce)
    try:
        response = requests.get(f'https://dichvukey.site/api/keyvip.php?key={key}&signature={signature}&nonce={nonce}')
        response.raise_for_status()
        check_keyphi = response.json()
        return check_keyphi
    except requests.RequestException as e:
        print(f"Lỗi khi check key: {e}")
        return {'status': 'error', 'msg': str(e)}

def vanlong(so):
    a = '────' * (so - 1) + '─'
    for i in range(len(a)):
        sleep(0.003)
    print(a)

def clear():
    if platform.startswith('linux'):
        os.system('clear')
    else:
        os.system('cls')

def banner():
    print('[0m', end='')
    clear()
    a = Colorate.Horizontal(Colors.blue_to_green, banners)
    print(a)
    print(thongtin)
    vanlong(17)

try:
    url = requests.post('https://dichvukey.site/key100.php', headers=headers, data={'pass': 'vLong'}).json()
    user_agent = url['user_agent']
    c = strftime('%d%m%Y')
    d = f'{c}toolvip{user_agent}'
    p = hashlib.md5(d.encode()).hexdigest()
    ma_key = p[:9]
    link = url['link']
except Exception as e:
    print(f'\033[91mKey Sai Hoặc Đã Hết Hạn\033[0m')
    exit(1)

banner()

def prompt_for_key():
    print(f'\033[91mVượt Link Hoặc Mua Key Tại : zalo 0789041631 \033[0m')
    print(f'\033[91mLink Lấy Key: {link}\033[0m')
    print(f'\033[99mKeyvip7day : vLongshare\033[3m')

    vanlong(17)
    key = input(f'\033[93mNhập Key Đã Mua Hoặc Key Free: \033[0m').strip()
    print('\033[91m', end='')
    vanlong(17)
    return key

def handle_key(key):
    check_keyphi = checkkey(key)
    if key == ma_key:
        print('\033[91mKey Chính Xác\033[0m')
        luu(key)
        return True
    elif check_keyphi.get('status') == 'error':
        print(f'\033[91mKey Sai Hoặc Đã Hết Hạn\033[0m')
        return False
    else:
        try:
            name = check_keyphi['name']
            remaining_days = check_keyphi['remaining_days']
            remaining_hours = check_keyphi['remaining_hours']
            remaining_minutes = check_keyphi['remaining_minutes']
            create = check_keyphi['create']

            print(f'\033[91mKey Chính Xác\033[0m')
            luu(key)
            return True
        except KeyError:
            print(f"\033[91m{check_keyphi.get('msg', 'Key không hợp lệ')}\033[0m")
            return False

while True:
    if not os.path.exists('vLong_key.txt'):
        key = prompt_for_key()
        if len(key) < 1:
            print('\033[91mKey không hợp lệ\033[0m')
            continue
        
        if handle_key(key):
            break
    else:
        with open('vLong_key.txt', 'r') as file_key:
            key_cu = file_key.read().strip()
        
        check_keyphi = checkkey(key_cu)
        if key_cu == ma_key:
            print('\033[91mKey Chính Xác\033[0m', end='\r')
            break
        elif check_keyphi.get('status') == 'error':
            print('\033[91mServer Key Phí Đang Lỗi Hãy Dùng Key Free\033[0m')
            os.remove('vLong_key.txt')
            continue
        else:
            try:
                name = check_keyphi['name']
                remaining_days = check_keyphi['remaining_days']
                remaining_hours = check_keyphi['remaining_hours']
                remaining_minutes = check_keyphi['remaining_minutes']
                create = check_keyphi['create']

                print(f'\033[91mKey Chính Xác\033[0m')
                break
            except KeyError:
                if check_keyphi.get('msg') == 'Key Không Tồn Tại!':
                    print(f'\033[91mKey {key_cu} Đã Được Thay Thế Vui Lòng Lấy Key Mới\033[0m')
                else:
                    print(f'\033[91m{check_keyphi.get("msg", "Lỗi không xác định")}\033[0m')
                os.remove('vLong_key.txt')
                continue

banner()
if 'check' in locals() and check:
    keycode = key_cu if len(key_cu) < 4 else '*' * len(key_cu)
    print(f'\033[91mNgười Mua: {name}\033[0m')
    print(f'\033[91mKey Code: {keycode}\033[0m')
    if len(key_cu) == 0:
        print(f'\033[91mHãy Mua KeyVip =)) \033[0m')
        print(f'\033[91mLink Lấy Key: {link}\033[0m')
        exit(0)

if 'check' in locals() and check:
    if len(keycode) == 0:
        print(f'\033[91mHãy Mua KeyVip =)) \033[0m')
        print(f'\033[91mLink Lấy Key: {link}\033[0m')
        exit(0)
    print(f'\033[91mSố Ngày Còn Lại: {remaining_days} Ngày, {remaining_hours} Giờ, {remaining_minutes} Phút\033[0m')
    print(f'\033[91mThời Gian Tạo key: {create}\033[0m')

print("\033[1;39m   ╔═════════════════════╗")
print("\033[1;39m   ║ \033[1;34mTOOL Trao Đổi Sub \033[1;39m  ║ ")
print("\033[1;39m   ╚═════════════════════╝")
print("\033[38;5;155m      Nhập Số \033[1;36m[1.1] \033[38;5;204mTOOL TDS TIKTOK + TIKTOK NOW")
print("\033[38;5;155m      Nhập Số \033[1;36m[1.2] \033[38;5;204mTOOL AUTO TDS FACEBOOK ")
print("\033[38;5;155m      Nhập Số \033[1;36m[1.3] \033[38;5;204mTOOL AUTO TDS PAGE PRO5 ")

print("\033[1;39m   ╔═════════════════════╗")
print("\033[1;39m   ║ \033[1;34mTOOL Tương Tác Chéo\033[1;39m ║ ")
print("\033[1;39m   ╚═════════════════════╝")
print("\033[38;5;155m      Nhập Số \033[1;36m[2.1] \033[38;5;204mTOOL TTC PAGE PRO5")
print("\033[1;39m   ╔══════════════╗")
print("\033[1;39m   ║ \033[1;34mTOOL GOLIKE\033[1;39m  ║ ")
print("\033[1;39m   ╚══════════════╝")
print("\033[38;5;155m      Nhập Số \033[1;36m[3.1] \033[38;5;204mTOOL GOLIKE TIKTOK \033[1;33m[AUTO]")
print("\033[38;5;155m      Nhập Số \033[1;36m[3.2] \033[38;5;204mTOOL GOLIKE TIKTOK \033[1;33m[BẤM TAY]")

print("\033[1;39m   ╔═══════════════╗")
print("\033[1;39m   ║ \033[1;34mTOOL KIẾM XU\033[1;39m  ║ ")
print("\033[1;39m   ╚═══════════════╝")
print("\033[38;5;155m      Nhập Số \033[1;36m[555] \033[38;5;204mTOOL HAMSTER ")
print("\033[38;5;155m      Nhập Số \033[1;36m[666] \033[38;5;204mTOOL BUFF LIKE MIỄN PHÍ\033[1;33m[ĐA COOKIE]")



print("\033[1;39m   ╔═════════════════════════════╗")
print("\033[1;39m   ║ \033[1;34mTOOL LIÊN QUAN VỀ FACEBOOK\033[1;39m  ║ ")
print("\033[1;39m   ╚═════════════════════════════╝")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.1] \033[38;5;204mTOOL CMT DẠO FB")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.2] \033[38;5;204mTOOL REG PAGE \033[1;33m[Chống Block]")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.3] \033[38;5;204mTOOL BUFF FOLLOW BẰNG PAGE PRO5")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.4] \033[38;5;204mTOOL CHUYỂN QUYỀN PAGE PRO5")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.5] \033[38;5;204mTOOL SPAM COMMENT FB")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.6] \033[38;5;204mTOOL SPAM BOX MESSENGER")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.7] \033[38;5;204mTOOL SPAM MESSENGER")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.9] \033[38;5;204mTOOL REG MAIL ẢO TẠO NICK FB")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.11] \033[38;5;204mTOOL GET COOKIE BẰNG TK MK")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.12] \033[38;5;204mTOOL NUÔI NICK FB \033[1;33m[VIP]")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.13] \033[38;5;204mTOOL GET TOKEN 16 LOẠI")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.14] \033[38;5;204mTOOL SPAM CMT PRO5")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.15] \033[38;5;204mTOOL LẤY ID BÀI VIẾT - ID NICK FB")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.16] \033[38;5;204mTOOL MẮNG NHAU Ở MESS VÀ BOX \033[1;33m[CÓ NGÔN SẴN]")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.17] \033[38;5;204mTOOL CHECK THÔNG TIN NICK FB")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.18] \033[38;5;204mTOOL GET COOKIE PAGE")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.19] \033[38;5;204mTOOL SHARE ẢO MAX SPEED \033[1;33m[COOKIE]")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.21] \033[38;5;204mTOOL SHARE ẢO ĐA LUỒNG")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.22] \033[38;5;204mTOOL SHARE ẢO MAX SPEED \033[1;33m[TOKEN]")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.23] \033[38;5;204mTOOL TỐ CÁO NICK FB")

print("\033[1;39m   ╔════════════════════════════════════╗")
print("\033[1;39m   ║ \033[1;34mTOOL SPAM SMS VÀ BUFF VIEW TIKTOK\033[1;39m  ║ ")
print("\033[1;39m   ╚════════════════════════════════════╝")
print("\033[38;5;155m      Nhập Số \033[1;36m[6.1] \033[38;5;204mTOOL SPAM SMS")
print("\033[38;5;155m      Nhập Số \033[1;36m[6.2] \033[38;5;204mTOOL BUFF VIEW TIKTOK PROXY")
print("\033[38;5;155m      Nhập Số \033[1;36m[6.3] \033[38;5;204mTOOL BUFF VIEW TIKTOK ZEFOY \033[1;33m[PC MỚI SÀI ĐƯỢC]")
print("\033[38;5;155m      Nhập Số \033[1;36m[6.4] \033[38;5;204mTOOL BUFF VIEW TIKTOK ZEFOY \033[1;33m[ALL THIẾT BỊ]")
print("\033[1;39m   ╔═════════════════════════╗")
print("\033[1;39m   ║ \033[1;34mTOOL VỀ MAIL VÀ PROXY \033[1;39m  ║ ")
print("\033[1;39m   ╚═════════════════════════╝")
print("\033[38;5;155m      Nhập Số \033[1;36m[7.1] \033[38;5;204mTOOL LỌC - CHECK MAIL")
print("\033[38;5;155m      Nhập Số \033[1;36m[7.2] \033[38;5;204mTOOL TÌM PROXY")
print("\033[38;5;155m      Nhập Số \033[1;36m[7.3] \033[38;5;204mTOOL LỌC PROXY")

print("\033[1;39m   ╔═══════════════════════════╗")
print("\033[1;39m   ║ \033[1;34mTOOL CÙI BẮP DỄ BỊ CRACK\033[1;39m  ║ ")
print("\033[1;39m   ╚═══════════════════════════╝")
print("\033[38;5;155m      Nhập Số \033[1;36m[8.1] \033[38;5;204mTOOL CỦA HDTTOOL \033[1;33m[BẢN NEW] ")


print("\033[1;39m   ╔══════════════╗")
print("\033[1;39m   ║ \033[1;34mTOOL DECODE\033[1;39m  ║ ")
print("\033[1;39m   ╚══════════════╝")
print("\033[38;5;155m      Nhập Số \033[1;36m[9.1] \033[38;5;204mTOOL DEC Kramer-Specter Deobf")
print("\033[38;5;155m      Nhập Số \033[1;36m[9.2] \033[38;5;204mTOOL DEC Marshal/PYC")



chon = float(input('\033[1;31m     Nhập Số \033[1;32m: \033[1;33m'))

import requests,os,sys, time
def check_internet_connection():
    try:
        response = requests.get("https://google.com/", timeout=5)
        return True
    except requests.ConnectionError:
        return False
if not check_internet_connection():
    print("\n\033[1;39mBạn bug 1 lần nữa sẽ bị dính botnet ngay nhé")
    sys.exit(1) 
if chon == 1.1 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/tdstiktok.py').text)

if chon == 1.2 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/tdsfb.py').text)
if chon == 1.3 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/tdspage.py').text)
if chon == 2.1 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/ttcpage.py').text)
if chon == 3.1 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/goliketiktokauto.py').text)
if chon == 3.2 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/obf-golike.py').text)
if chon == 5.1 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/cmtdaofb.py').text)
if chon == 5.2 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/regpage.py').text)
if chon == 5.3 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/buffpage.py').text)
if chon == 5.4 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/chuyenquyenqtv.py').text)
if chon == 5.5 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/cmtfb.py').text)
if chon == 5.6 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/spambox.py').text)
if chon == 5.7 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/spammess.py').text)

if chon == 5.9 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/mailfb.py').text)
if chon == 5.11 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/getcookie.py').text)
if chon == 5.12 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/nuoifb.py').text)
if chon == 5.13 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/gettoken.py').text)
if chon == 5.14 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/cmtpage.py').text)
if chon == 5.15 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/id.py').text)
if chon == 5.16 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/chuinhau.py').text)
if chon == 5.17 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/checkthongtinfb.py').text)
if chon == 5.18 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/cookiepro5.py').text)
if chon == 5.19 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/shareao.py').text)
if chon == 5.21 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/shareaodaluong.py').text)
if chon == 5.22 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/shareaotoken.py').text)
if chon == 5.23 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/tocao.py').text)
if chon == 6.1 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/sms.py').text)
if chon == 6.2 :
	exec(requests.get('https://raw.githubusercontent.com/vlong07/vlong07/main/viewprx.txt').text)
if chon == 6.3 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/zefoy.py').text)
if chon == 6.4 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/zefoylong.py').text)
if chon == 7.1 :
	exec(requests.get('https://raw.githubusercontent.com/vlong07/vlong07/main/mail.txt').text)
if chon == 7.2 :
	exec(requests.get('https://raw.githubusercontent.com/vlong07/vlong07/main/timproxy.txt').text)
if chon == 7.3 :
	exec(requests.get('https://raw.githubusercontent.com/vlong07/vlong07/main/locproxy.txt').text)
##van longg
if chon == 8.1 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/hdt.py').text)

	
#tool kiếm xu
if chon == 9.1 :
	exec(requests.get('https://raw.githubusercontent.com/KhanhNguyen9872/kramer-specter_deobf/main/kramer-specter-deobf.py').text)
if chon == 9.2 :
	exec(requests.get('https://raw.githubusercontent.com/vlong07/vlong07/main/pyc.txt').text)
if chon == 555 :
	exec(requests.get('https://raw.githubusercontent.com/vlong07/vlong07/main/ham.txt').text)
if chon == 666 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/666.py').text)
else :
	exit()
