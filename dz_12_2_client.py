import asyncio

async def main():
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
    operation = input('Enter operation (add, subtract, multiply): ')
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    message = f'{operation} {num1} {num2}\n'.encode()
    writer.write(message)
    await writer.drain()
    data = await reader.read(100)
    result = int(data.decode())
    print(f'Result: {result}')
    writer.close()

asyncio.run(main())