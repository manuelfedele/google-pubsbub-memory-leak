import os
from google.cloud import pubsub_v1
from memory_profiler import profile

os.environ.setdefault('GOOGLE_APPLICATION_CREDENTIALS', 'path/to/key.json')
os.environ.setdefault('GOOGLE_CLOUD_PROJECT', 'project-id')
os.environ.setdefault('MY_TOPIC_NAME', 'test_memory_leak-sub')

topic_name = 'projects/{project_id}/topics/{topic}'.format(
    project_id=os.getenv('GOOGLE_CLOUD_PROJECT'),
    topic=os.getenv('MY_TOPIC_NAME'),  # Set this to something appropriate.
)

subscription_name = 'projects/{project_id}/subscriptions/{sub}'.format(
    project_id=os.getenv('GOOGLE_CLOUD_PROJECT'),
    sub=os.getenv('MY_TOPIC_NAME'),  # Set this to something appropriate.
)


@profile
def callback(message):
    # Memory intensive operation
    x = [n for n in range(int(1e5))]
    message.ack()
    print("ack")


with pubsub_v1.SubscriberClient() as subscriber:
    future = subscriber.subscribe(subscription_name, callback)
    print("Starting subscriber")
    try:
        print("Listening...")
        future.result(timeout=30)
    except KeyboardInterrupt:
        future.cancel()
