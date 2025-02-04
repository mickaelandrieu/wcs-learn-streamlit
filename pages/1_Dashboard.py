import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Dashboard des Ventes",
    page_icon = ":bar_chart:",
    layout="wide",
)

sales = pd.read_csv('superstore.csv', parse_dates=['Ship Date', 'Order Date'])

st.markdown('# Suivi des ventes')

sales.rename(columns={"Order Date": "Order_Date"}, inplace = True)

orders = sales['Order ID'].nunique()
customers = sales['Customer Name'].nunique()
total_sales = sales['Sales'].sum()
benefits = sales['Profit'].sum()

# Créer une colonne 'is_discount' qui indique si la remise est supérieure à 0
sales['Discounted'] = sales['Discount'] > 0

# Utiliser apply pour convertir les valeurs booléennes en "OUI" ou "NON"
sales['Discounted'] = sales['Discounted'].apply(lambda x: "OUI" if x else "NON")

# Formatter le date en Français
sales['date_fr'] = sales['Order_Date'].dt.strftime("%d/%m/%Y")

st.markdown('### KPIs principaux 📈')

col1, col2, col3, col4 = st.columns(4)

col1.metric("Nombre de commandes", orders)
col2.metric("Nombre de clients", customers)
col3.metric("Chiffre d'affaires", str(round(total_sales))+ "$")
col4.metric("Bénéfices", str(round(benefits))+ "$")

with st.expander('### Formulaire de recherche 🔎'):
    categories = list(sales['Category'].unique())
    category_selector = st.multiselect(
        "Choisis ta catégorie de Produit",
        categories,
        ["Furniture"],
    )
    
    segments = list(sales['Segment'].unique())
    segment_selector = st.multiselect(
        "Choisis ton segment de clientèle",
        segments,
        ["Consumer"],
    )
    
    discount_selector = st.radio(
        "Sélectionnes les produits avec promo",
        ["OUI", "NON", "TOUS"],
        index = 2
    )
    
    first_sale_date = sales['Order_Date'].min() 
    last_sale_date =  sales['Order_Date'].max()
    
    sales_date_since_selector = st.date_input('Depuis', first_sale_date)
    sales_date_until_selector = st.date_input('Jusqu\'à', last_sale_date)

def query_builder(filters):
    query = ''
    i = 0
    for filter in filters:
        i = i + 1

        if filter['type'] == 'multi-select':
            if(i == 1):
                query = query + f"""{filter['column']} in {filter['value']}"""
            else:
                query = query + " " + f""" and {filter['column']} in {filter['value']}"""
        
        if filter['type'] == 'radio':
            if filter['value'] == "TOUS":
                continue
            if(i == 1):
                query = query + f"""{filter['column']} == '{filter['value']}'"""
            else:
                query = query + " " + f""" and {filter['column']} == '{filter['value']}'"""

        if filter['type'] == 'date-interval':
            if(i == 1):
                query = query + f"""'{filter['value'][0]}' <= {filter['column']} <= '{filter['value'][1]}'"""
            else:
                query = query + " " + f""" and '{filter['value'][0]}' <= {filter['column']} <= '{filter['value'][1]}'"""

    return query 

filters = [
    {"column": "Category", "value": category_selector, "type": "multi-select"},
    {"column": "Segment", "value": segment_selector, "type": "multi-select"},
    {"column": "Discounted", "value": discount_selector, "type": "radio"},
    {"column": "Order_Date", "value": [sales_date_since_selector, sales_date_until_selector], "type": "date-interval"}
]

columns = [filter_item["column"] for filter_item in filters] +  ["date_fr"]

pd_query = query_builder(filters)

daily_sales = sales[['Sales'] + columns].query(pd_query).groupby(by = ['Order_Date']).sum().sort_values(by='Order_Date').reset_index()
daily_profits = sales[['Profit'] + columns].query(pd_query).groupby(by = ['Order_Date']).sum().sort_values(by='Order_Date').reset_index()

st.markdown('### Suivi quotidien 📅')

st.markdown('#### Ventes 🛒')

daily_sales['date_fr'] = daily_sales['Order_Date'].dt.strftime("%d/%m/%Y")

graph1 = px.line(
    daily_sales,
    x = 'Order_Date',
    y = 'Sales',
    markers = True,
    labels= {
        'Order_Date': 'Date',
        'Sales': 'Ventes ($)'
    },
    color_discrete_sequence=["#e248db"]
)


graph1.update_traces(hovertemplate="<b>Date :</b> %{customdata} <br><b>Ventes :</b> %{y}$"
                                    "<br><b>Requête :</b> " + pd_query,
                                    customdata = daily_sales["date_fr"])

st.plotly_chart(graph1, use_container_width = False)

st.markdown('#### Profits 💰')

daily_profits['date_fr'] = daily_profits['Order_Date'].dt.strftime("%d/%m/%Y")

graph2 = px.line(
    daily_profits,
    x = 'Order_Date',
    y = 'Profit',
    markers = True,
    labels= {
        'Order_Date': 'Date',
        'Sales': 'Profits ($)'
    },
    color_discrete_sequence=["#39b2ca"]
)

graph2.update_traces(hovertemplate="<b>Date :</b> %{customdata} <br><b>Profits :</b> %{y}$"
                                    "<br><b>Requête :</b> " + pd_query,
                                    customdata = daily_profits["date_fr"])

st.plotly_chart(graph2, use_container_width = False)


st.markdown('#### Nombre de ventes par categorie de Produit 📚')



fig = px.pie(sales[['Sales']+columns].query(pd_query), values='Sales', names='Category')

st.plotly_chart(fig, use_container_width=True)

# --- Bouton d'export ---
try:
    filtered_sales = sales.query(pd_query)
except Exception as e:
    st.error(f"⚠️ Erreur dans la requête : {e}")
    filtered_sales = sales


st.download_button(
    label="📥 Exporter les données filtrées",
    data=filtered_sales.to_csv().encode("utf-8"),
    file_name="ventes_avec_filtres.csv",
    mime="text/csv"
)
