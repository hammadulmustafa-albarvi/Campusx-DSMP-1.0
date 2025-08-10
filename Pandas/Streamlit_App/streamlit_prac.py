# import streamlit as st
# import pandas as pd
# import time


# st.title('Startup Dashboard')

# st.header("I am learning Streamlit")

# st.subheader('And i am loving it')

# st.write('This is a normal text')

# st.markdown("""
#             ### My favorite movies
#             - Race 3
#             - Humshakal
#             - 3Idiots
#             """)


# st.code("""
#         def foo(input):
#             return f00**2
#         x=foo(2)
#         """)

# st.latex('x^2 + y^2 + z^2')

# df = pd.DataFrame({
#     'name':['hammad','ayan'],
#     'marks' : [50,34],
#     'package':[3,12]
# })

# st.dataframe(df)


# st.metric('Revenue','Rs 3 Lakh','-3%')

# st.json({
#     'name':['hammad','ayan'],
#     'marks' : [50,34],
#     'package':[3,12]
# })


# st.image("a.png")

# st.video('b.mp4')

# # st.audio(any audio file)


# st.sidebar.title('Side bar ka title')

# col1,col2=st.columns(2)

# with col1:
#     st.image('a.png')
    
# with col2:
#     st.image('a.png')
    
# st.error("Login failed")

# st.success("Login successful")

# st.info("some info")



# # bar = st.progress(0)

# # for i in range(1,101):
# #     time.sleep(0.1)
# #     bar.progress(i)
    
    
# st.text_input('Enter Email')

# st.number_input('Enter age')

# st.date_input('Enter Registration Date')


# gender = st.selectbox('Select Gender',['male','female'])

# email = st.text_input('Enter Email')
# password = st.text_input('Enter Password')

# btn = st.button('Login')

# if btn:
#     if email == 'hammad@gmail.com' and password == '1234':
#         st.success('Login successful')
#         st.write(gender)
#     else:
#         st.error('Login Failed')
        
# file = st.file_uploader('Upload a Csv File')

# if file is not None:
#     df = pd.read_csv(file)
#     st.dataframe(df.describe())