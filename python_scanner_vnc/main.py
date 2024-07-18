import asyncio, asyncvnc


async def run_client(host, port, password):
    try:
        async with asyncvnc.connect(host, port, None, password, None) as client:
            if client:
                print(client)
    except ConnectionRefusedError as ex:
        print('Timeot: ', ex)
    except PermissionError as ex:
        print('Password: ', ex)


if __name__ == '__main__':
    asyncio.run(run_client('', '', ''))
