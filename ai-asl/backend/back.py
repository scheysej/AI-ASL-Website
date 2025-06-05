import asyncio
import websockets
import json
import base64
import re
from pathlib import Path
from datetime import datetime
from inference_classifier import prediction

# def save_base64_image(data_url):
#     # Match data URL format
#     match = re.match(r'data:image/(png|jpeg);base64,(.*)', data_url)
#     if not match:
#         print("Invalid data URL")
#         return

#     image_data = base64.b64decode(match.group(2))

#     # Generate unique filename
#     timestamp = datetime.now().strftime('%Y%m%d-%H%M%S-%f')
#     Path("frames").mkdir(exist_ok=True)
#     filename = f"frames/frame-{timestamp}.jpg"

#     with open(filename, "wb") as f:
#         f.write(image_data)

#     print(f"Saved frame as {filename}")


async def handler(websocket):
    print("Client connected")
    async for message in websocket:
        print("Raw message received:")
        print(message[:100] + '...')  # Show only first 100 chars to avoid log spam

        try:
            data = json.loads(message)
            if data['type'] == 'frame':
                print("Received frame")
                predicted_letter = prediction(data['data'])

                await websocket.send(json.dumps({
                    "type": "prediction",
                    "value": predicted_letter,
                    "confidence": 0.97
                }))
        except Exception as e:
            print("Failed to process message:", e)

async def main():
    async with websockets.serve(handler, 'localhost', 8765):
        print("WebSocket server listening on ws://localhost:8765")
        await asyncio.Future()  # Run forever

if __name__ == '__main__':
    asyncio.run(main())
