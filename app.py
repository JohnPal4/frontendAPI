import streamlit as st
from api import (
    get_all_items,
    get_item,
    create_item,
    replace_item,
    patch_item,
    delete_item
)

st.set_page_config(page_title="Inventory Manager", layout="wide")

st.title("Inventory Management System")

menu = ["View All", "Get One", "Create", "Update (PUT)", "Patch (Partial)", "Delete"]
choice = st.sidebar.selectbox("Menu", menu)

# ---------------- VIEW ALL ----------------
if choice == "View All":
    st.subheader("All Inventory Items")
    data = get_all_items()
    st.dataframe(data)

# ---------------- GET ONE ----------------
elif choice == "Get One":
    st.subheader("Get Item by ID")
    material_id = st.number_input("Material ID", step=1)

    if st.button("Fetch"):
        data = get_item(material_id)
        st.json(data)

# ---------------- CREATE ----------------
elif choice == "Create":
    st.subheader("Create New Item")

    material_id = st.number_input("Material ID", step=1)
    material_name = st.text_input("Material Name")
    purchase_date = st.date_input("Purchase Date")
    purchase_quantity = st.number_input("Purchase Quantity", step=1)
    storage_location = st.text_input("Storage Location")
    on_hand_quantity = st.number_input("On Hand Quantity", step=1)

    if st.button("Create"):
        payload = {
            "material_id": material_id,
            "material_name": material_name,
            "purchase_date": purchase_date.isoformat() if purchase_date else None,
            "purchase_quantity": purchase_quantity,
            "storage_location": storage_location,
            "on_hand_quantity": on_hand_quantity
        }

        res = create_item(payload)
        st.success("Item created!")
        st.json(res)

# ---------------- UPDATE (PUT) ----------------
elif choice == "Update (PUT)":
    st.subheader("Replace Item (Full Update)")

    material_id = st.number_input("Material ID", step=1)
    material_name = st.text_input("Material Name")
    purchase_date = st.date_input("Purchase Date")
    purchase_quantity = st.number_input("Purchase Quantity", step=1)
    storage_location = st.text_input("Storage Location")
    on_hand_quantity = st.number_input("On Hand Quantity", step=1)

    if st.button("Update"):
        payload = {
            "material_id": material_id,
            "material_name": material_name,
            "purchase_date": purchase_date.isoformat() if purchase_date else None,
            "purchase_quantity": purchase_quantity,
            "storage_location": storage_location,
            "on_hand_quantity": on_hand_quantity
        }

        res = replace_item(material_id, payload)
        st.success("Item updated!")
        st.json(res)

# ---------------- PATCH ----------------
elif choice == "Patch (Partial)":
    st.subheader("Partial Update")

    material_id = st.number_input("Material ID", step=1)

    st.write("Fill only fields you want to update:")

    material_name = st.text_input("Material Name")
    purchase_quantity = st.number_input("Purchase Quantity", step=1)
    storage_location = st.text_input("Storage Location")
    on_hand_quantity = st.number_input("On Hand Quantity", step=1)

    if st.button("Patch"):
        payload = {}

        if material_name:
            payload["material_name"] = material_name
        if purchase_quantity:
            payload["purchase_quantity"] = purchase_quantity
        if storage_location:
            payload["storage_location"] = storage_location
        if on_hand_quantity:
            payload["on_hand_quantity"] = on_hand_quantity

        res = patch_item(material_id, payload)
        st.success("Item patched!")
        st.json(res)

# ---------------- DELETE ----------------
elif choice == "Delete":
    st.subheader("Delete Item")

    material_id = st.number_input("Material ID", step=1)

    if st.button("Delete"):
        res = delete_item(material_id)
        st.warning("Item deleted")
        st.json(res)
