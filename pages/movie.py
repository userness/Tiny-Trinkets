import streamlit as st                                         #https://google.com/search?q=text
st.title("Movie Finder")
with st.form("da-form"):
	movie = st.text_input("IMDb/TMDB id","The hunger Games")
	st.caption("Enter To Save")
	movie = movie.replace(" ", "+") # url encodinggggg i think
	
	submitted = st.form_submit_button("⬇️")	
	if submitted:  
		st.link_button('Continue', f'https://vidlink.pro/movie/{movie}')
