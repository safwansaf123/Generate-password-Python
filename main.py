import streamlit as st     # shortcut name for streamlit st or any other name may be used
import string              # specific letters are provided by this, example ascii letters, upper or lower case alphabet
import random              # random characters


def password_generator(length, use_digits, use_special):     # function created with name password generator with 3 specific parameters

    characters = string.ascii_letters

    if use_digits:                        # if user use digits (0-9) add them into characters
        characters += string.digits

    if use_special:                        # if user use special characters (@,#,$,&,*......) add them into characters
        characters += string.punctuation 

    # here digitd & special chararter joins in it 
# for loop is used 
    return ''.join(random.choice(characters) for _ in range(length))  # _ tells to python no specific length for password

# provide title on top of application
st.title("Password Generator")

# slider's function parameters i.e, min_value, max_value (arguments passed init) 
length = st.slider("select Password Length", min_value=6, max_value=32, value=12)


# user to check the box for what they want to use
use_digits = st.checkbox("Include Digits")
use_special = st.checkbox("Include Special characters")

# user click on button to generate password
if st.button("Generate Password"):
    password = password_generator(length, use_digits, use_special)
    st.write(f"Generated Password: '{password}'")   # system write the passowrd

st.write("-----------------")

st.write("learn in ramadan by asharib ali online lecture")

