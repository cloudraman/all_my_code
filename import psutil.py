import psutil

# Get the CPU usage
cpu_usage = psutil.cpu_percent()

# Get the memory usage
memory_usage = psutil.virtual_memory().percent

# Print the CPU and memory usage
print(f'CPU usage: {cpu_usage}%')
print(f'Memory usage: {memory_usage}%')
import googleapiclient.discovery

# Set up the YouTube API client
api_service_name = "youtube"
api_version = "v3"
client = googleapiclient.discovery.build(api_service_name, api_version, developerKey=YOUR_API_KEY)

# Make a request to the YouTube API to retrieve a list of trending videos
request = client.videos().list(
    chart="mostPopular",
    part="id,snippet",
    regionCode="US",
    maxResults=50
)
response = request.execute()

# Print the titles of the trending videos
for video in response["items"]:
    print(video["snippet"]["title"])
