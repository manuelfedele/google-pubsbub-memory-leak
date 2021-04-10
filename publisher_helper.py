import os
from google.cloud import pubsub_v1

os.environ.setdefault('GOOGLE_APPLICATION_CREDENTIALS', 'path/to/key.json')
os.environ.setdefault('GOOGLE_CLOUD_PROJECT', 'project-id')
os.environ.setdefault('MY_TOPIC_NAME', 'test_memory_leak')

publisher = pubsub_v1.PublisherClient()
topic_name = 'projects/{project_id}/topics/{topic}'.format(
    project_id=os.getenv('GOOGLE_CLOUD_PROJECT'),
    topic=os.getenv('MY_TOPIC_NAME'),  # Set this to something appropriate.
)

for i in range(4):
    future = publisher.publish(topic_name, b'My first message!', spam='eggs')
    future.result()
    print("Sent!")

