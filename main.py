import sys
from src import scraper
from src import server

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("python3 main.py <twitter-handle> <server-address> <port>")
        print("-- Note: provide twitter handle without leading @")
        sys.exit()

    handle = sys.argv[1]
    address = sys.argv[2]
    port = int(sys.argv[3])

    scrape = scraper.Scraper(handle)
    serve = server.Server(address, port)

    scrape.start()
    serve.start()