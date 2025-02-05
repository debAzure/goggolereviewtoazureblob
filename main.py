# main.py
from fetch_reviews import fetch_google_reviews
from upload_reviews import upload_to_azure_blob

def main():
    # Step 1: Fetch Google reviews
    reviews = fetch_google_reviews()
    if reviews:
        print(f"Fetched {len(reviews)} reviews.")
        
        # Step 2: Upload the reviews to Azure Blob Storage
        upload_to_azure_blob(reviews)
    else:
        print("No reviews fetched.")

if __name__ == "__main__":
    main()
