import csv
import requests
import pandas as pd
import io

# https://www.football-data.co.uk/mmz4281/1920/E0.csv

class Main:

    def take_url_and_requests_csv(self, url):
        if ".csv" in url:
            try:
                request_content =requests.get(url).content
                pd.read_csv(
                io.StringIO(request_content.decode('utf-8')),
                usecols=['Div', 'Date', 'Time', 'HomeTeam', 'AwayTeam'])
                .to_json('my_file.json', orient='records', indent=1)
            except Exception as e:
                print(e)
            finally:
                with open('my_file.json', 'r+') as json_file:
                    print(json_file.read())
        else:
            print("the url must contain .csv extension")


if __name__ == "__main__":
    while True:
        print("Welcome! If you want to exit just tip 'exit'")
        main = Main()
        take_input_url = input("Provide the url please: ")
        main.take_url_and_requests_csv(take_input_url)
        if take_input_url == "exit":
            print("good bye")
            break
