import streamlit as st
from neo4j import GraphDatabase

# Function to create a Neo4j driver instance
def create_driver(uri, user, password):
    return GraphDatabase.driver(uri, auth=(user, password))

# Function to execute a Neo4j query and return the results
def run_query(driver, query):
    with driver.session() as session:
        result = session.run(query)
        return [record for record in result]

# Streamlit app
def main():
    st.title("Neo4j Querying with Streamlit")

    # User input for Neo4j connection
    uri = st.text_input("Neo4j URI", "bolt://localhost:7687")
    user = st.text_input("Username", "neo4j")
    password = st.text_input("Password", type="password")

    # User input for Neo4j query
    query = st.text_area("Cypher Query", "MATCH (n) RETURN n LIMIT 10")

    if st.button("Run Query"):
        try:
            # Create a Neo4j driver instance
            driver = create_driver(uri, user, password)
            
            # Run the query and get the results
            results = run_query(driver, query)
            
            # Display the results
            for record in results:
                st.write(record)
                
            # Close the driver
            driver.close()
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
