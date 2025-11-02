import sqlite3

# -------------------------------------------------------------------
# 1️⃣  Create the PNR table
# -------------------------------------------------------------------
def create_pnr_table(conn: sqlite3.Connection):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pnr_details (
            pnr_number TEXT PRIMARY KEY,
            passenger_name TEXT,
            train_number TEXT,
            train_name TEXT,
            source TEXT,
            destination TEXT,
            date_of_journey TEXT,
            coach TEXT,
            seat_number TEXT,
            status TEXT
        )
    """)
    conn.commit()

    # Insert sample data if empty
    cursor.execute("SELECT COUNT(*) FROM pnr_details")
    if cursor.fetchone()[0] == 0:
        sample_data = [
            ("1234567890", "Rahul Sharma", "12627", "Karnataka Express", "Delhi", "Bangalore", "2025-11-05", "S2", "34", "Confirmed"),
            ("2345678901", "Priya Singh", "12841", "Coromandel Express", "Kolkata", "Chennai", "2025-11-06", "A1", "14", "RAC"),
            ("3456789012", "Amit Kumar", "12951", "Mumbai Rajdhani", "Mumbai", "Delhi", "2025-11-07", "B1", "21", "Confirmed"),
            ("4567890123", "Neha Patel", "12723", "Andhra Express", "Vijayawada", "Delhi", "2025-11-08", "S4", "10", "Waiting"),
            ("5678901234", "Ravi Verma", "12659", "Chennai Mail", "Chennai", "Delhi", "2025-11-09", "S3", "17", "Confirmed"),
            ("6789012345", "Sneha Reddy", "12760", "Charminar Express", "Hyderabad", "Chennai", "2025-11-10", "A2", "06", "Confirmed"),
            ("7890123456", "Vikram Das", "12009", "Shatabdi Express", "Bhopal", "Delhi", "2025-11-11", "C1", "02", "Confirmed"),
            ("8901234567", "Kiran Nair", "16382", "Kanniyakumari Express", "Trivandrum", "Mumbai", "2025-11-12", "S6", "59", "RAC"),
            ("9012345678", "Deepika Rao", "12533", "Pushpak Express", "Lucknow", "Mumbai", "2025-11-13", "B2", "28", "Confirmed"),
            ("1122334455", "Arjun Mehta", "12615", "Grand Trunk Express", "Delhi", "Chennai", "2025-11-14", "S1", "49", "Waiting"),
            ("2233445566", "Meena Iyer", "12709", "Simhapuri Express", "Tirupati", "Secunderabad", "2025-11-15", "S2", "12", "Confirmed"),
            ("3344556677", "Sameer Khan", "12953", "August Kranti Rajdhani", "Mumbai", "Delhi", "2025-11-16", "A1", "05", "Confirmed"),
            ("4455667788", "Lakshmi Menon", "12625", "Kerala Express", "Trivandrum", "Delhi", "2025-11-17", "S5", "27", "RAC"),
            ("5566778899", "Manish Gupta", "12138", "Punjab Mail", "Delhi", "Mumbai", "2025-11-18", "B3", "30", "Confirmed"),
            ("6677889900", "Pooja Sharma", "12687", "Dehradun Express", "Chennai", "Dehradun", "2025-11-19", "A2", "11", "Waiting"),
            ("7788990011", "Harish Pandey", "12711", "Pinakini Express", "Vijayawada", "Chennai", "2025-11-20", "S2", "23", "Confirmed"),
            ("8899001122", "Nisha Bhat", "12029", "Shatabdi Express", "Pune", "Mumbai", "2025-11-21", "C1", "09", "Confirmed"),
            ("9900112233", "Gaurav Sinha", "12863", "Howrah Express", "Howrah", "Bangalore", "2025-11-22", "S6", "15", "RAC"),
            ("1010101010", "Rohit Joshi", "12673", "Cheran Express", "Coimbatore", "Chennai", "2025-11-23", "B1", "19", "Confirmed"),
            ("2020202020", "Ananya Das", "12785", "Bangalore Express", "Hyderabad", "Bangalore", "2025-11-24", "S3", "45", "Confirmed"),
        ]

        cursor.executemany("""
            INSERT INTO pnr_details (
                pnr_number, passenger_name, train_number, train_name,
                source, destination, date_of_journey, coach, seat_number, status
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, sample_data)
        conn.commit()
        print("✅ PNR table created with 20 sample records.")
    else:
        print("ℹ️ PNR table already exists, skipping sample data insertion.")


# -------------------------------------------------------------------
# 2️⃣  Fetch a passenger’s PNR details
# -------------------------------------------------------------------
def get_pnr_details(conn: sqlite3.Connection, pnr_number: str):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pnr_details WHERE pnr_number = ?", (pnr_number,))
    result = cursor.fetchone()
    if result:
        keys = [
            "pnr_number", "passenger_name", "train_number", "train_name",
            "source", "destination", "date_of_journey",
            "coach", "seat_number", "status"
        ]
        return dict(zip(keys, result))
    else:
        return None
