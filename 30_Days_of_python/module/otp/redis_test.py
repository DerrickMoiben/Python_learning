import redis

# Connect to Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

# Set and get a value
redis_client.set('test_key', 'Hello from Python!')
value = redis_client.get('test_key')

print(f"Value from Redis: {value}")  # Should print: Hello from Python!

