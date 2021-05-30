from server import Server


def main():
    server = Server('localhost', 8000)
    print(f'Listening to port {server.port}')

if __name__ == "__main__":
    main()