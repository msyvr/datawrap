import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# Database connection parameters from environment variables
DB_PARAMS = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "database": os.getenv("DB_DATABASE"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}

# Create connection string and engine
connection_string = f"postgresql://{DB_PARAMS['user']}:{DB_PARAMS['password']}@{DB_PARAMS['host']}:{DB_PARAMS['port']}/{DB_PARAMS['database']}"
engine = create_engine(connection_string)
Session = sessionmaker(bind=engine)


# Update records
def update_records():
    updates = [
        text(
            "UPDATE raw_customers SET first_name = 'updateMichael' WHERE customer_id = 1;"
        ),
        text(
            "UPDATE raw_customers SET first_name = 'updateShawn' WHERE customer_id = 2;"
        ),
        text(
            "UPDATE raw_customers SET first_name = 'updateKathleen' WHERE customer_id = 3;"
        ),
    ]

    try:
        with engine.begin() as connection:  # Start a transaction
            for update in updates:
                connection.execute(update)
        print("Records updated successfully.")
    except SQLAlchemyError as e:
        print(f"An error occurred while updating records: {e}")


if __name__ == "__main__":
    update_records()
