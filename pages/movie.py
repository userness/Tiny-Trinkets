import streamlit as st            
import json
import pandas as pd
import requests

def search(inn):
	inn = inn.replace(" ", "+")
	json_data = requests.get(f"https://api.imdbapi.dev/search/titles?query={inn}")
	json_data = json_data.text
	data = json.loads(json_data)
	for item in data["titles"]:
		id = item["id"]
		title = item["primaryTitle"]
		data2 = requests.get(f"https://api.imdbapi.dev/titles/{id}/images")
		data2 = data2.json()
		data2 = data2["images"][0]["url"]

		
		st.html(f"""
<img onclick="https://vidlink.pro/movie/{id}" src="{data2}" width=30>{title}</img>
  		(""")







st.title("Movie Finder")
with st.form("da-form"):
	movie = st.text_input("Movie Title","The hunger Games")
	
	submitted = st.form_submit_button("Search")	
	if submitted:
		search(movie)


