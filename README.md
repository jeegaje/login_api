# API Mongga

## Route API

### 1. Login ###
- "http://127.0.0.1:5000/api/login" POST<br>
Mendapat akses login<br>
parameter : email, password<br>
Authorization : -

### 2. Contact Us ###

- "http://127.0.0.1:5000/api/contact_us" POST<br>
Menambah data contact_us<br>
parameter : perihal, nama, email, subjek, pesan<br>
Authorization : -

- "http://127.0.0.1:5000/api/contact_us/view/all" GET <br>
Mendapat semua data contact_us<br>
parameter : -<br>
Authorization : Token admin

- "http://127.0.0.1:5000/api/contact_us/view/kritik" GET <br>
Mendapat semua data contact_us berdasarkan perihal **Kritik/Saran**<br>
parameter : -<br>
Authorization : Token admin

- "http://127.0.0.1:5000/api/contact_us/view/sponsorship" GET <br>
Mendapat semua data contact_us berdasarkan perihal *Sponsorship*<br>
parameter : -<br>
Authorization : Token admin

- "http://127.0.0.1:5000/api/contact_us/view/bisnis" GET <br>
Mendapat semua data contact_us berdasarkan perihal *Kerjasama Bisnis*<br>
parameter : -<br>
Authorization : Token admin

- "http://127.0.0.1:5000/api/contact_us/view/partnering" GET <br>
Mendapat semua data contact_us berdasarkan perihal *Media Partnering*<br>
parameter : -<br>
Authorization : Token admin

- "http://127.0.0.1:5000/api/contact_us/view/bantuan" GET <br>
Mendapat semua data contact_us berdasarkan perihal *Pertanyaan atau Bantuan*<br>
parameter : -<br>
Authorization : Token admin
