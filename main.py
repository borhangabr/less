import streamlit as st
import pyodbc as odbc

server = '.'
database = 'videos'
tc = 'yes'

connection_string = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};Trusted_Connection={tc};'

con = odbc.connect(connection_string)

cur = con.cursor()

default_video_url = "D:\\MyVideo.mp4"

text = st.text_input('Enter The Video NAME')
Query = "exec get ?"
values = (text,)
cur.execute(Query, values)
results = cur.fetchall()

if results:
    st.title('Borhan')
    video_url = default_video_url if not results[0] else results[0][0]
    st.video(video_url)
else:
    st.title('Borhan')
    st.video(default_video_url)

cur.close()
con.close()
