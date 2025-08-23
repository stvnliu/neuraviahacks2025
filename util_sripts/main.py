from api_interface.request_handler import DataHandler
from data_parsing.data_parser import FunnyClass

funny_class = FunnyClass()


def main():
    handler = DataHandler()
    print(handler.fetch_data())
    for i in range(100):
        print(i)


if __name__ == "__main__":
    main()
