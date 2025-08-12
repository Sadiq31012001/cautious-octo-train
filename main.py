from pyrogram import Client, filters
import os

# Your API credentials (replace with actual values)
api_id = 18747100
api_hash = "8c9c1a587505f4e5f0afccdae87e4b48"
source_channel = -1002233859472  # Your source channel
destination_channel = -1001664008087  # Destination channel

# Clear existing session (if any)
session_file = "my_session.session"
if os.path.exists(session_file):
    os.remove(session_file)
    print("⚠ Old session removed. Please re-login.")

app = Client(
    "my_session",  # Session name
    api_id=api_id,
    api_hash=api_hash
)

@app.on_message(filters.channel & filters.chat(source_channel))
def forward_message(client, message):
    try:
        print(f"📩 Forwarding message ID: {message.id}")
        message.forward(destination_channel)
        print("✅ Forwarded successfully!")
    except Exception as e:
        print(f"❌ Error: {e}")

print("🔌 Starting Telegram forwarder bot...")
print("ℹ You'll be asked to login with your phone number")
app.run()