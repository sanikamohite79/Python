import asyncio

HOST = "127.0.0.1"
PORT = 5000


async def handle_client(reader, writer):
    address = writer.get_extra_info("peername")
    print("Connected:", address)

    try:
        while True:
            data = await reader.readline()

            if not data:
                break

            message = data.decode("utf-8").rstrip("\n")

            print("Received:", message)

            response = f"Server received: {message}\n"

            writer.write(response.encode("utf-8"))
            await writer.drain()

    finally:
        writer.close()
        await writer.wait_closed()
        print("Disconnected:", address)


async def main():
    server = await asyncio.start_server(
        handle_client,
        HOST,
        PORT
    )

    print(f"Async server listening on {HOST}:{PORT}")

    async with server:
        await server.serve_forever()


try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("\nServer stopped")