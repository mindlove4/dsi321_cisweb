deploy application บน heroku server
* จำเป็นต้องมี heroku command line interface 
หากไม่มีให้ download และ ติดตั้งจาก website นี้ https://devcenter.heroku.com/articles/heroku-cli#install-the-heroku-cli
* จำเป็นต้องมี heroku account
หากไม่มีให้สมัครได้ที่ https://signup.heroku.com/
ขั้นตอนการ deploy บน heroku server
1. สร้าง folder ที่ต้องการที่จะใช้เก็บ file ของ project 
2. เช็คให้มั่นใจว่า directory ที่ต้องการจะเก็บ file ตรงกับ directory บน command line
จากนั้นให้ใช้คำสั่งดังต่อไปนี้ตามลำดับ
1. git clone https://github.com/mindlove4/dsi321_cisweb.git
2. cd dsi321_cisweb
3. heroku login
ให้ login เข้า account heroku ให้เรียบร้อย
4. heroku create
ในขั้นตอนนี้จะได้ website และ application name มา
5. git add .
6. git commit -m "<text>"
7. heroku config:set DISABLE_COLLECTSTATIC = 1
8. git push heroku main
หากไม่สามารถทำข้อ 8 ได้ให้เปลี่ยนเป็น git push heroku master
เมื่อใช้คำสั่งทั้ง 8 ขั้นตอนครบแล้วจะทำให้ web application ของเราอยู่บน heroku server แล้ว
9. heroku open -a <app name>
คำสั่งข้อ 9 ใช้เพื่อเปิด website แต่สามารถเปิดได้โดยตรงจาก website ที่ได้ในข้อที่ 4 ได้เลย เช่นกัน
** หากมีปัญหาเช่น database ไม่โหลดให้ใช้คำสั่ง heroku run python manage.py migrate

หากต้องการเปลี่ยนแปลง database ให้ไปที่ https://dashboard.heroku.com/apps
แล้วเลือก application ที่คุณได้ deploy ไป จากนั้นให้ทำตามขั้นตอนดังนี้
1. ไปที่ Configure Add-ons
2. เลือก Heroku Postgres
3. เลือก settings 
4. กด view credentials จะพบกับ ข้อมูลของ database
5. กลับไปที่ setting.py ใน file project บนเครื่อง
6. แก้ไขข้อมูล DATABASES ให้ตรงกับข้อมูลในข้อที่ 4
7. จากนั้นให้ deploy application ใหม่อีกครั้งโดยเริ่มจาก git add . ไปจนถึง git push heroku main
** หากมีปัญหาเช่น database ไม่โหลดให้ใช้คำสั่ง heroku run python manage.py migrate

เมื่อทำครบทุกขั้นตอนแล้วหากไม่ต้องการใช้ google authenticate ก็สามารถเสร็จสิ้นกระบวนการได้เลย
แต่หากต้องการใช้ให้คุณทำ google API&service 
โดยเข้าไปที่ https://console.cloud.google.com/apis จากนั้นทำตามขั้นตอนด้านล่าง
1. สร้าง project ใหม่ของคุณขึ้นมาโดยกด create new project
2. เลือก project ที่คุณสร้างแล้วกด OAuth consent screen
3. เลือก external แล้วกด create 
4. กรอกข้อมูลในส่วน app name , email และ developer contact information
5. กด create จากนั้นกด save and continue
6. กลับไปที่ credential ทางมุมซ้าย
7. กด create credential แล้วเลือก create OAuth client ID
8. เลือก application type เป็น web application แล้ว กรอก app name
9. กด add url ตรง autorize java script origin
10. ใส่ link ของ web server ที่ได้จากการ deploy ลงไป
11. กด add url ตรง autorize redirect urls
12. ใส่ link ดังนี้ <web server>/accounts/google/login/callback/
13. กด create
เมื่อ create แล้วจะได้ client id และ client secret มาใช้งาน

เมื่อได้ client id และ client secret แล้ว
ใช้คำสั่ง heroku run python manage.py createsuperuser เพื่อสร้าง super user มาใช้งาน
ให้ไปที่ browser แล้วเข้า <web server>/admin
จากนั้นให้ทำตามขั้นตอนด้านล่าง
1. ไปที่ table site
2. กด add site
3. กรอก domain name ให้ถูกต้อง แล้วกรอก display name เป็นอะไรก็ได้แล้วกด save
4. ไปที่ตาราง Social applications กด add 
5. เลือก provider เป็น google
6. กรอก name เป็นอะไรก็ได้ตามที่สะดวก แล้วกรอก client id และ client secret ตามที่ได้มา
7. เลือก site ตามที่ได้ส้รางในขั้นตอนที่ 2 
8. กลับไปที่ setting.py ใน file project บนเครื่อง
9. เปลี่ยน SITE_ID เป็น id ของ site ที่เพิ่งสร้างในขั้นตอนที่ 3
10. deployment ขึ้นใหม่ ตามขั้นตอน deploy โดยเริ่มต้นแต่ git add . ไปจนถึง git push heroku main
เมื่อ deployment ขึ้นใหม่ก็จะสามารถใช้งาน google authenticate ได้แล้ว
