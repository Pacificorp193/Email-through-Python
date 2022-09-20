Python 3.10.7 (v3.10.7:6cc6b13308, Sep  5 2022, 14:02:52) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import smtplib
conn = smtplib.SMTP('stmp.gmail.com', 587)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    conn = smtplib.SMTP('stmp.gmail.com', 587)
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/smtplib.py", line 255, in __init__
    (code, msg) = self.connect(host, port)
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/smtplib.py", line 341, in connect
    self.sock = self._get_socket(host, port, self.timeout)
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/smtplib.py", line 312, in _get_socket
    return socket.create_connection((host, port), timeout,
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/socket.py", line 824, in create_connection
    for res in getaddrinfo(host, port, 0, SOCK_STREAM):
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/socket.py", line 955, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 8] nodename nor servname provided, or not known
>>> conn = smtplib.SMTP('smtp.gmail.com', 587)
...                                     
>>> type(conn)
...                                     
<class 'smtplib.SMTP'>
>>> conn
...                                     
<smtplib.SMTP object at 0x106f6e8c0>
>>> conn.ehlo()
...                                     
(250, b'smtp.gmail.com at your service, [204.113.203.34]\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8')
>>> connstarttls()
...                                     
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    connstarttls()
NameError: name 'connstarttls' is not defined
>>> conn.starttls()
...                                     
(220, b'2.0.0 Ready to start TLS')
>>> conn.quit()
...                                     
(221, b'2.0.0 closing connection er23-20020a17090af6d700b0020061adf86asm424450pjb.56 - gsmtp')
