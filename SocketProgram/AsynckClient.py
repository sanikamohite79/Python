import asyncio

HOST = "127.0.0.1"
PORT = 5000


async def main():

    reader, writer = await asyncio.open_connection(
        HOST,
        PORT
    )

    print("Connected to server")

    try:
        while True:

            message = await asyncio.to_thread(
                input,
                "You: "
            )

            if message.lower() == "exit":
                break

            # Send message to server
            writer.write(
                (message + "\n").encode("utf-8")
            )

            await writer.drain()

            # Receive response from server
            data = await reader.readline()

            if not data:
                print("Server disconnected")
                break

            response = data.decode("utf-8").rstrip("\n")

            print("Server:", response)

    finally:
        writer.close()
        await writer.wait_closed()
        print("Disconnected from server")


try:
    asyncio.run(main())

except KeyboardInterrupt:
    print("\nClient stopped")