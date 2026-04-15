import streamlit as st

st.title("Kalyan's Restaurant")
st.header("Your Order")

# Initialize session state for selected items
if "selected_items" not in st.session_state:
    st.session_state.selected_items = []

# Food items with images and prices
food_data = {
    "Chicken Biryani": {
        "image": "https://th.bing.com/th/id/OIP.0csI89pXHQSxumqiZz_tIwHaE8?w=279&h=186&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
        "price": 350
    },
    "Paneer Tikka": {
        "image": "https://th.bing.com/th/id/OIP.zB9-oXacOrpqdWGJwJsSvQHaE8?w=280&h=187&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
        "price": 280
    },
    "Veg Spring Rolls": {
        "image": "https://th.bing.com/th/id/OIP.6K6KHt4e0YssTiJ18MYEFAHaH3?w=228&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
        "price": 200
    },
    "Chicken Wings": {
        "image": "https://th.bing.com/th/id/OIP.LpYdN3ZrxRvIsaLJuGO_sQHaHa?w=208&h=208&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
        "price": 320
    },
    "Mutton Biryani": {
        "image": "https://th.bing.com/th/id/OIP.EqRZjBzlk_oO8w64up3JAgHaE8?w=235&h=150&c=6&o=7&dpr=1.3&pid=1.7&rm=3",
        "price": 499
    },
    "Full Meals Combo": {
        "image": "https://th.bing.com/th/id/OIP.GjIwCh89aXCNSbCMbriWkwHaE7?w=285&h=190&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3",
        "price": 400
    }
}

# Get customer name
user1 = st.sidebar.text_input("Enter your name")

# Display food items as clickable images in sidebar
st.sidebar.subheader("Select Your Food Items")
cols = st.sidebar.columns(2)

for idx, (food_name, food_info) in enumerate(food_data.items()):
    with cols[idx % 2]:
        st.image(food_info["image"], use_container_width=True)
        st.caption(f"**{food_name}**")
        st.caption(f"₹{food_info['price']}")
        if st.button(f"Add {food_name}", key=food_name):
            if food_name not in st.session_state.selected_items:
                st.session_state.selected_items.append(food_name)
            st.rerun()

# Display selected items in main section as grid
if st.session_state.selected_items:
    st.subheader("Your Selected Orders")
    
    # Display items in a grid layout (4 items per row)
    cols = st.columns(4)
    for idx, food_item in enumerate(st.session_state.selected_items):
        with cols[idx % 4]:
            st.image(food_data[food_item]["image"], use_container_width=True)
            st.caption(f"**{food_item}**")
            st.caption(f"₹{food_data[food_item]['price']}")
            if st.button("Remove ✕", key=f"remove_{food_item}_{idx}"):
                st.session_state.selected_items.remove(food_item)
                st.rerun()
    
    # Calculate total price
    total_price = sum(food_data[item]["price"] for item in st.session_state.selected_items)
    st.markdown("---")
    st.write(f"**Total Price: ₹{total_price}**")
    
    # Success message
    st.success(f"Hello {user1}, your selected orders have been placed successfully! Thank you for choosing Kalyan's Restaurant.")
else:
    st.info("Please select food items from the sidebar to place your order.")    