import os
import django
import time
import random
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sightproject.settings')
django.setup()

def run_burst_simulator():
    channel_layer = get_channel_layer()
    print("📡 Starting Burst Simulation...")
    print("🚀 15 updates (2s delay) followed by a 90s cooldown.")

    try:
        while True:
            # 1. Create and shuffle the set of 15 numbers
            numbers_pool = list(range(1, 16))
            random.shuffle(numbers_pool)
            
            print(f"\n--- Starting new burst at {time.strftime('%H:%M:%S')} ---")

            # 2. Loop 15 times (the burst phase)
            while numbers_pool:
                random_value = numbers_pool.pop()
                current_time = time.strftime("%H:%M:%S")

                # Broadcast to the WebSocket group
                async_to_sync(channel_layer.group_send)(
                    "live_chart_updates", 
                    {
                        "type": "send_chart_update", 
                        "data": {
                            "label": current_time, 
                            "value": random_value
                        }
                    }
                )

                print(f"  [Burst] Sent: {current_time} -> {random_value}")
                
                # Sleep 2 seconds between each of the 15 numbers
                if numbers_pool: # Don't sleep 2s after the very last number
                    time.sleep(2)

            # 3. The Cooldown phase
            print(f"💤 Burst complete. Sleeping for 90 seconds...")
            time.sleep(90)
            
    except KeyboardInterrupt:
        print("\n🛑 Simulation stopped.")

if __name__ == "__main__":
    run_burst_simulator()