import asyncio

async def handle_client(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    parts = message.split()
    operation = parts[0]
    num1 = int(parts[1])
    num2 = int(parts[2])
    result = 0
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    result = str(result).encode()
    writer.write(result)
    await writer.drain()
    writer.close()

async def main():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8888)
    await server.serve_forever()

asyncio.run(main())
