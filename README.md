# API Mongga

## Route API

### 1. Login ###
- "http://127.0.0.1:5000/api/login" POST<br>
Mendapat akses login<br>
parameter : email, password<br>
Authorization : -

### 2. Register ###
- "http://127.0.0.1:5000/api/register/user" POST<br>
Mendaftarkan user<br>
parameter : email, sandi, nama_depan, nama_akhir<br>
Authorization : -

- "http://127.0.0.1:5000/api/register/mentor" POST<br>
Mendaftarkan mentor<br>
parameter : email, sandi, nama_depan, nama_akhir<br>
Authorization : Token admin

### 3. Admin ###
- "http://127.0.0.1:5000/api/register/users/user" GET<br>
Mendapatkan semua data user<br>
parameter : -<br>
Authorization : Token admin

- "http://127.0.0.1:5000/api/register/users/mentor" GET<br>
Mendapatkan semua data mentor<br>
parameter : -<br>
Authorization : Token admin

- "http://127.0.0.1:5000/api/delete/<akun_id>" DELETE<br>
Menghapus data akun<br>
*akun_id diisi id akun yang ingin dihapus*<br>
parameter : -<br>
Authorization : Token admin

### 4. Contact Us ###

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
