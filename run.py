import os
import json
import time

# 1. Read the input filename passed from Cloud Function -> Cloud Build
input_file = os.environ.get('S3_KEY', 'unknown_file.mp4')
bucket_name = os.environ.get('GCS_BUCKET', 'unknown_bucket')

print(f"--- STARTING PROCESSING ---")
print(f"Processing file: {input_file}")
print(f"From bucket: {bucket_name}")

# 2. Simulate doing heavy video work
time.sleep(2) 

# 3. Generate a dummy result
result_data = {
    "file_processed": input_file,
    "status": "success",
    "predictions": ["cat", "dog", "person"]
}

# 4. Save result.json (This is what Cloud Build will pick up as an artifact)
with open('result.json', 'w') as f:
    json.dump(result_data, f)

print(f"--- FINISHED PROCESSING ---")
print(f"Saved result.json")
