import streamlit as st

st.markdown(
    "<h1 style='color: red;'>Redbus Data Scraping Project</h1>", 
    unsafe_allow_html=True
)

st.markdown(
    "<h3 style='color: maroon;'>Check the buses availability here!</h3>", 
    unsafe_allow_html=True
)


import pandas as pd
import pymysql

mydb = pymysql.connect(
 host="localhost",
 user="root",
 password="PWsaga@31",
 database="guvi",
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM guvi.bus_routes")
data = mycursor.fetchall()  
columns = [desc[0] for desc in mycursor.description]  
table = pd.DataFrame(data, columns=columns)  

statelist=table["state"].unique().tolist()
statelist= ["Choose your state"] + statelist
#st.write(statelist)

selected_state=st.selectbox("states", statelist)

if selected_state != "Choose your state":
    routes = table[table["state"] == selected_state]["route_name"].unique().tolist()
    route_selected=st.selectbox("routes",["Choose your desired route"] + routes)

            
    st.sidebar.markdown("<h3 style='color: maroon;'>Filter star rating</h3>", unsafe_allow_html=True)
    rating = st.sidebar.radio(
        "Rating",
        options=[5, 4, 3, 2, 1],
        format_func=lambda x: "⭐" * x,
        horizontal=True
    )

    st.sidebar.markdown("<h3 style='color: maroon;'>Filter ticket fare</h3>", unsafe_allow_html=True)
    max_price = st.sidebar.slider("Price in INR", 100, 10000, 100, 1000)

    st.sidebar.markdown("<h3 style='color: maroon;'>Select tickets count</h3>", unsafe_allow_html=True)
    seats= st.sidebar.number_input("seats", min_value=1, max_value=57)

    if max_price > 100:
        buses = table[(table["route_name"]== route_selected) &
                    (table["star_rating"]>= rating) &
                    (table["price"]<= max_price) &
                    (table["seats_available"]>= seats) 
                    ]["busname"].tolist()
        #st.write(buses)

        bus_selected=st.radio("Available buses", buses)

        if bus_selected:
            if st.button(f"{bus_selected} bus details"):
                #st.write("success")                
                bus_details = table[
                                    (table["state"] == selected_state) & 
                                    (table["route_name"] == route_selected) & 
                                    (table["busname"] == bus_selected)  
                                    ][["bustype","departing_time","duration","star_rating","price"]]
                st.table(bus_details)

