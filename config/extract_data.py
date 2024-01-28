from config import default_db
import csv
from google.cloud import storage


def extract_csv(query, file_name):
    """
    Extracts data from a PostgreSQL database and saves it as a CSV file.

    Args:
        query (str): SQL query to execute.
        file_name (str): Name of the file to be saved.
        db (str): Name of the PostgreSQL database.

    Returns:
        str: Path of the created CSV file.
    """


    # Create a cursor object to interact with the database
    cursor = default_db.cursor()

    # Execute the query
    cursor.execute(query)

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Define the CSV file path
    csv_file_path = '../data/' + file_name + '.csv'

    # Open the CSV file in write mode
    with open(csv_file_path, 'w', newline='') as csvfile:
        # Create a CSV writer object
        csv_writer = csv.writer(csvfile)

        # Write the column headers to the CSV file
        csv_writer.writerow([desc[0] for desc in cursor.description])

        # Write each row to the CSV file
        csv_writer.writerows(rows)

    print(f"We have extracted the {file_name} table with {len(rows)} line")
    cursor.close()
    default_db.close()
    return csv_file_path


def create_gcs_bucket(name):
    """
    Creates a new Google Cloud Storage (GCS) bucket.

    Args:
        name (str): Name of the bucket to be created.
    """

    key_path = "serviceAccountKey.json"
    client = storage.Client.from_service_account_json(key_path)
    bucket = client.create_bucket(name)
    print(f"Cloud Storage bucket '{bucket.name}' created successfully.")


def upload_csv_to_bucket(name, local_file_path, remote_file_name):
    """
    Uploads a local CSV file to a specified Google Cloud Storage (GCS) bucket.

    Args:
        name (str): Name of the GCS bucket.
        local_file_path (str): Local file path of the CSV file.
        remote_file_name (str): Name of the file in the GCS bucket.
    """

    key_path = "serviceAccountKey.json"
    client = storage.Client.from_service_account_json(key_path)
    bucket = client.get_bucket(name)
    blob = bucket.blob(remote_file_name)
    blob.upload_from_filename(local_file_path)
    print(f"File uploaded to Cloud Storage bucket: gs://{name}/{remote_file_name}")