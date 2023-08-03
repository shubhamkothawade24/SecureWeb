import sqlite3
conn = sqlite3.connect('password.sqlite')
cur = conn.cursor()
try:
    cur.execute('CREATE TABLE pass (user VARCHAR, pass VARCHAR, web VARCHAR)')
except:
    print("")

# cur.execute('INSERT INTO pass (user, pass, web) VALUES ("yuvraj", "abc", "facebook")')
we = "twitter"
cur.execute("SELECT * FROM pass WHERE web=?", [we])
ans = cur.fetchall()
print(ans)

conn.commit()
conn.close()