import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="E-Commerce Recommendation System",
    page_icon="🛍️",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #2563eb;
        margin-bottom: 1rem;
    }
    .model-card {
        padding: 1.5rem;
        border-radius: 10px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        margin-bottom: 1rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .model-card h3 {
        color: white;
        margin-top: 0;
    }
</style>
""", unsafe_allow_html=True)

# Title and description
st.markdown('<h1 class="main-header">🛍️ E-Commerce Recommendation Engine</h1>', unsafe_allow_html=True)
st.markdown("### Smart product recommendations using multiple ML models")

# Create tabs for different recommendation types
tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "🔥 Trending", "👥 Personalized", "🔍 Similar Products"])

# Sample data (replace with your actual data)
sample_products = pd.DataFrame({
    'product_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'name': ['iPhone 15 Pro', 'Samsung Galaxy S23', 'MacBook Air M2', 'Sony Headphones', 
             'Nike Air Max', 'Levi\'s Jeans', 'Kindle Paperwhite', 'PlayStation 5', 
             'Dyson Vacuum', 'Nespresso Machine'],
    'category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 
                 'Fashion', 'Fashion', 'Electronics', 'Gaming', 'Home', 'Home'],
    'price': [999, 799, 1099, 299, 120, 80, 139, 499, 399, 199],
    'rating': [4.8, 4.6, 4.7, 4.4, 4.5, 4.3, 4.6, 4.8, 4.5, 4.4],
    'sales_count': [1500, 1200, 800, 2500, 3000, 2800, 1800, 900, 700, 850]
})

# TAB 1: Overview
with tab1:
    st.markdown("## 📋 Recommendation Models Overview")
    
    # Create columns for model cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="model-card">
            <h3>1. Popularity-Based Model</h3>
            <p><strong>For:</strong> New customers with no purchase history</p>
            <p><strong>Method:</strong> Shows trending and best-selling products</p>
            <p><strong>Best for:</strong> Cold start and initial engagement</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="model-card">
            <h3>2. Collaborative Filtering</h3>
            <p><strong>For:</strong> Returning customers with purchase history</p>
            <p><strong>Method:</strong> Personalizes based on similar users' behavior</p>
            <p><strong>Best for:</strong> Increasing customer retention</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="model-card">
            <h3>3. Content-Based Model</h3>
            <p><strong>For:</strong> Product discovery and cross-selling</p>
            <p><strong>Method:</strong> Finds similar products based on descriptions</p>
            <p><strong>Best for:</strong> Improving product discovery</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Statistics
    st.markdown("---")
    st.markdown("### 📈 System Statistics")
    
    stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)
    with stat_col1:
        st.metric("Total Products", len(sample_products), "10 items")
    with stat_col2:
        st.metric("Avg Rating", f"{sample_products['rating'].mean():.1f}★", "4.6★")
    with stat_col3:
        st.metric("Total Sales", f"{sample_products['sales_count'].sum():,}", "15,850")
    with stat_col4:
        st.metric("Categories", len(sample_products['category'].unique()), "4")

# TAB 2: Popularity-Based Recommendations (Trending)
with tab2:
    st.markdown("## 🔥 Trending & Best-Selling Products")
    
    # Sort by sales count for popularity
    trending_products = sample_products.sort_values('sales_count', ascending=False).head(5)
    
    # Display trending products
    for idx, row in trending_products.iterrows():
        with st.container():
            col1, col2, col3 = st.columns([1, 3, 1])
            with col1:
                st.markdown(f"**#{idx+1}**")
            with col2:
                st.markdown(f"**{row['name']}** - {row['category']}")
                st.progress(row['sales_count']/3000)
                st.caption(f"Sales: {row['sales_count']:,} units")
            with col3:
                st.markdown(f"**${row['price']}**")
            st.divider()
    
    # Sales visualization
    fig = px.bar(trending_products, x='name', y='sales_count',
                 title='Top Selling Products',
                 color='sales_count',
                 color_continuous_scale='viridis')
    st.plotly_chart(fig, use_container_width=True)

# TAB 3: Collaborative Filtering (Personalized)
with tab3:
    st.markdown("## 👥 Personalized Recommendations")
    
    # Simulate user selection
    st.markdown("### Select a customer profile:")
    user_type = st.selectbox(
        "Customer Type",
        ["New User (No History)", "Frequent Electronics Buyer", "Fashion Enthusiast", "Home & Living Shopper"]
    )
    
    # Simulate recommendations based on user type
    if user_type == "Frequent Electronics Buyer":
        recommendations = sample_products[sample_products['category'] == 'Electronics'].head(3)
    elif user_type == "Fashion Enthusiast":
        recommendations = sample_products[sample_products['category'] == 'Fashion'].head(3)
    elif user_type == "Home & Living Shopper":
        recommendations = sample_products[sample_products['category'] == 'Home'].head(3)
    else:
        # For new users, show trending products
        recommendations = sample_products.sort_values('sales_count', ascending=False).head(3)
    
    st.markdown(f"### Recommended for {user_type}:")
    for _, row in recommendations.iterrows():
        with st.expander(f"📱 {row['name']}"):
            st.write(f"**Category:** {row['category']}")
            st.write(f"**Price:** ${row['price']}")
            st.write(f"**Rating:** {row['rating']}★")
            st.write(f"**Sales:** {row['sales_count']:,} units")
            if st.button(f"Add to Cart", key=f"cart_{row['product_id']}"):
                st.success(f"Added {row['name']} to cart!")

# TAB 4: Content-Based Recommendations
with tab4:
    st.markdown("## 🔍 Find Similar Products")
    
    # Product selection
    selected_product = st.selectbox(
        "Select a product to find similar items:",
        sample_products['name'].tolist()
    )
    
    # Simple similarity calculation (based on category and price range)
    selected_row = sample_products[sample_products['name'] == selected_product].iloc[0]
    
    # Create similarity scores
    similarity_scores = []
    for _, product in sample_products.iterrows():
        if product['name'] != selected_product:
            # Simple similarity: same category = 1 point, price within 30% = 1 point
            score = 0
            if product['category'] == selected_row['category']:
                score += 1
            if abs(product['price'] - selected_row['price']) / selected_row['price'] < 0.3:
                score += 1
            if abs(product['rating'] - selected_row['rating']) < 0.5:
                score += 1
            
            similarity_scores.append({
                'name': product['name'],
                'category': product['category'],
                'price': product['price'],
                'rating': product['rating'],
                'similarity_score': score
            })
    
    # Show similar products
    if similarity_scores:
        similar_df = pd.DataFrame(similarity_scores)
        similar_df = similar_df.sort_values('similarity_score', ascending=False).head(3)
        
        st.markdown(f"### Products similar to **{selected_product}**:")
        
        cols = st.columns(3)
        for idx, (_, product) in enumerate(similar_df.iterrows()):
            with cols[idx]:
                st.info(f"**{product['name']}**")
                st.write(f"Category: {product['category']}")
                st.write(f"Price: ${product['price']}")
                st.write(f"Rating: {product['rating']}★")
                st.metric("Similarity", f"{product['similarity_score']}/3")
                if st.button("View Details", key=f"view_{idx}"):
                    st.session_state.selected_product = product['name']
    else:
        st.warning("No similar products found.")

# Sidebar for filters
with st.sidebar:
    st.markdown("## 🔧 Filters")
    
    price_range = st.slider(
        "Price Range ($)",
        min_value=int(sample_products['price'].min()),
        max_value=int(sample_products['price'].max()),
        value=(50, 1000)
    )
    
    categories = st.multiselect(
        "Categories",
        options=sample_products['category'].unique().tolist(),
        default=sample_products['category'].unique().tolist()
    )
    
    min_rating = st.slider("Minimum Rating", 1.0, 5.0, 4.0, 0.1)
    
    if st.button("Apply Filters"):
        filtered = sample_products[
            (sample_products['price'] >= price_range[0]) &
            (sample_products['price'] <= price_range[1]) &
            (sample_products['category'].isin(categories)) &
            (sample_products['rating'] >= min_rating)
        ]
        st.session_state.filtered_products = filtered
        st.success(f"Found {len(filtered)} products")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>🛍️ E-Commerce Recommendation System v1.0</p>
    <p>Using Streamlit, Pandas, and scikit-learn</p>
</div>
""", unsafe_allow_html=True)