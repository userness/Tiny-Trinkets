import streamlit as st                                         #https://google.com/search?q=text
st.title("Digital Book Finder")
with st.form("da-form"):
	book = st.text_input("Book Title","The hunger Games 2")
	st.caption("Enter To Save")
	book = book.replace(" ", "+") # url encodinggggg i think
	
	submitted = st.form_submit_button("⬇️")	
	if submitted:  
		st.link_button('Continue', f'https://google.com/search?q={book}+filetype:pdf')
