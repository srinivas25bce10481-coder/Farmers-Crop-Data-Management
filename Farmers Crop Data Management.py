import streamlit as st
import sqlite3
import pandas as pd

class DatabaseManager:
    
    def __init__(self, db_file="farmers_crop_production.db"):
        self.db_file = db_file
        self.connection = sqlite3.connect(self.db_file, check_same_thread=False)
        self.create_tables_if_not_exist()

    def create_tables_if_not_exist(self):
        cursor = self.connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS farmers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                village TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS crops (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE 
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS production (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                farmer_id INTEGER,
                crop_id INTEGER,
                year INTEGER,
                quantity REAL,
                FOREIGN KEY(farmer_id) REFERENCES farmers(id),
                FOREIGN KEY(crop_id) REFERENCES crops(id)
            )
        ''')
        self.connection.commit()

    def add_farmer(self, name, village):
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO farmers (name, village) VALUES (?, ?)", (name, village))
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            st.error(f"Error adding farmer: {e}")
            return False

    def add_crop(self, name):
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO crops (name) VALUES (?)", (name,))
            self.connection.commit()
            return True
        except sqlite3.IntegrityError:
            st.warning(f"Crop '{name}' already exists in the database.")
            return False
        except sqlite3.Error as e:
            st.error(f"Error adding crop: {e}")
            return False

    def add_production_record(self, farmer_id, crop_id, year, quantity):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO production (farmer_id, crop_id, year, quantity) VALUES (?, ?, ?, ?)",
                (farmer_id, crop_id, year, quantity)
            )
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            st.error(f"Error recording production: {e}")
            return False

    def get_farmers(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, name, village FROM farmers ORDER BY name")
        return cursor.fetchall()

    def get_crops(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, name FROM crops ORDER BY name")
        return cursor.fetchall()

    def get_production_by_farmer(self, farmer_id):
        cursor = self.connection.cursor()
        cursor.execute('''
            SELECT crops.name, production.year, production.quantity
            FROM production
            JOIN crops ON production.crop_id = crops.id
            WHERE production.farmer_id = ?
            ORDER BY production.year DESC, crops.name
        ''', (farmer_id,))
        return cursor.fetchall()

def main():
    st.title("Farmers Crop Data Management")

    db = DatabaseManager()

    st.sidebar.title("Navigation")
    menu_options = ["Add Farmer", "Add Crop", "Record Production", "View Report"]
    choice = st.sidebar.radio("Go to", menu_options)

    if choice == "Add Farmer":
        st.header("Add a New Farmer")
        with st.form("add_farmer_form", clear_on_submit=True):
            name = st.text_input("Farmer Name")
            village = st.text_input("Village")
            submitted = st.form_submit_button("Add Farmer")
            
            if submitted:
                if not name or not village:
                    st.warning("Please enter both farmer name and village.")
                else:
                    if db.add_farmer(name, village):
                        st.success(f"Farmer '{name}' from '{village}' added successfully!")
                    else:
                        st.error("Failed to add farmer.")

    elif choice == "Add Crop":
        st.header("Add a New Crop")
        with st.form("add_crop_form", clear_on_submit=True):
            crop_name = st.text_input("Crop Name")
            submitted = st.form_submit_button("Add Crop")
            
            if submitted:
                if not crop_name:
                    st.warning("Please enter crop name.")
                else:
                    if db.add_crop(crop_name):
                        st.success(f"Crop '{crop_name}' added successfully!")

    elif choice == "Record Production":
        st.header("Record Crop Production")
        
        farmers = db.get_farmers()
        crops = db.get_crops()

        if not farmers or not crops:
            st.warning("Please add at least one farmer and one crop before recording production.")
            st.warning("Use the 'Add Farmer' and 'Add Crop' pages in the sidebar.")
            return

        farmer_options = {f"{f[1]} ({f[2]})": f[0] for f in farmers}
        crop_options = {c[1]: c[0] for c in crops}
        
        with st.form("record_production_form", clear_on_submit=True):
            selected_farmer_name = st.selectbox("Select Farmer", options=list(farmer_options.keys()))
            selected_crop_name = st.selectbox("Select Crop", options=list(crop_options.keys()))
            year = st.number_input("Year", min_value=1900, max_value=2100, value=2025)
            quantity = st.number_input("Quantity (in tons)", min_value=0.0, format="%.2f")
            
            submitted = st.form_submit_button("Record Production")
            
            if submitted:
                farmer_id = farmer_options[selected_farmer_name]
                crop_id = crop_options[selected_crop_name]
                
                if db.add_production_record(farmer_id, crop_id, year, quantity):
                    st.success("Production data recorded successfully!")
                else:
                    st.error("Failed to record production data.")

    elif choice == "View Report":
        st.header("View Farmer Production Report")
        
        farmers = db.get_farmers()
        if not farmers:
            st.warning("No farmers found. Please add farmers using the 'Add Farmer' page.")
            return

        farmer_options = {f"{f[1]} ({f[2]})": f[0] for f in farmers}
        selected_farmer_name = st.selectbox("Select Farmer to View Report", options=list(farmer_options.keys()))

        if st.button("Show Report"):
            farmer_id = farmer_options[selected_farmer_name]
            records = db.get_production_by_farmer(farmer_id)
            
            if records:
                st.subheader(f"Production Report for {selected_farmer_name}")
                
                df = pd.DataFrame(records, columns=["Crop", "Year", "Quantity (tons)"])
                df.insert(0, 'S.No.', range(1, 1 + len(df)))
                st.dataframe(df, use_container_width=True, hide_index=True)
            else:
                st.info("No production data found for this farmer.")

if __name__ == "__main__":
    main()