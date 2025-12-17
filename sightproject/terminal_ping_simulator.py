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
    os.environ['TZ'] = 'Asia/Kuala_Lumpur' # Replace with your timezone
    time.tzset()

    try:
        while True:
            # 1. Create and shuffle the set of 15 numbers
            numbers_pool = list(range(1, 16))
            random.shuffle(numbers_pool)
            
            print(f"\n--- Starting new burst at {time.strftime('%H:%M:%S')} ---")

            # 2. Loop 15 times (the burst phase)
            while numbers_pool:
                switch_id = 0
                terminal_id = numbers_pool.pop()
                display_time = time.strftime("%H:%M:%S")
                current_time = time.strftime("%Y-%m-%d %H:%M:%S")
                # ping_status = 1 if random.random() < 0.8 else 0   # 80% chance of success
                ping_status = 0 if random.random() < 0.7 else 1   # 70% chance of failure

                if 1 <= terminal_id <= 5:
                    switch_id = 1
                    # {do something}

                elif 6 <= terminal_id <= 10:
                    switch_id = 2
                    # {something}   
                    
                else:
                    switch_id = 3
                    # {more}

                formatted_terminal_label = f"S{switch_id}T{terminal_id}"
                # Broadcast to the WebSocket group
                async_to_sync(channel_layer.group_send)(
                    "live_ping_updates", 
                    {
                        "type": "send_ping_update", 
                        "data": {
                            "terminal_label": formatted_terminal_label,
                            "terminal_id": terminal_id,
                            "switch_id": switch_id,
                            "ping_time" : current_time,
                            "label": display_time, 
                            "value": ping_status
                        }
                    }
                )
                
                print(f"  [Burst] Sent: {current_time} -> {formatted_terminal_label} PING = {ping_status}")
                
                # Sleep 2 seconds between each of the 15 numbers
                if numbers_pool: # Don't sleep 2s after the very last number
                    time.sleep(1)

            # 3. The Cooldown phase
            print(f"💤 Burst complete. Sleeping for 5 seconds...")
            time.sleep(5)
            
    except KeyboardInterrupt:
        print("\n🛑 Simulation stopped.")

if __name__ == "__main__":
    run_burst_simulator()