import time
import random
import asyncio
from time import perf_counter


# Simulate downloading a single file
def sync_download_file(file_name):
    print(f"Starting download: {file_name}")
    duration = random.randint(1, 5)
    time.sleep(duration)  # Blocking sleep
    print(f"Finished downloading: {file_name} in {duration} seconds")

# Main function
def sync_main():
    """Run downloads synchronously (one-by-one) and print total time."""
    files = ['file1.zip', 'file2.mp4', 'file3.pdf', 'file4.jpg', 'file5.docx']

    print("\n[SYNC] Starting sequential downloads...\n")
    start = perf_counter()
    for file in files:
        sync_download_file(file)
    elapsed = perf_counter() - start
    print(f"\n[SYNC] All downloads finished in {elapsed:.2f}s\n")
        

# Simulate downloading a single file
async def async_download_file(file_name):
    print(f"Starting download: {file_name}")
    duration = random.randint(1, 5)  # pretend it takes 1–5 seconds
    await asyncio.sleep(duration)
    print(f"Finished downloading: {file_name} in {duration} seconds")

# The main function to handle all downloads
async def async_main():
    """Run downloads concurrently using asyncio and print total time."""
    files = ['file1.zip', 'file2.mp4', 'file3.pdf', 'file4.jpg', 'file5.docx']

    print("\n[ASYNC] Starting concurrent downloads...\n")
    start = perf_counter()
    # Create a list of download tasks
    tasks = [async_download_file(file) for file in files]

    # Run all downloads at the same time
    await asyncio.gather(*tasks)
    elapsed = perf_counter() - start
    print(f"\n[ASYNC] All downloads finished in {elapsed:.2f}s\n")

def run_sync_main():
    sync_main()

def run_async_main():
    asyncio.run(async_main())
    
def run_module():
    run_sync_main()
    run_async_main()