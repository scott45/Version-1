from urllib import request  # this library module establishes a request

# the http link which i saved as a variable
data = "http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=2&e=8&f=2015&g=d&a=2&b=27&c=2014&ignore=.csv"

# my function to both retrieve and save the data permanently from the provided url link
# csv stands for comma separated file
def get_data_via_http(andela):
    json = request.urlopen(andela)  # json applied to make a request and open the server
    csv = json.read()               # data is read
    csv_str = str(csv)
    lines = csv_str.split("\\n")    # on response, it's outputted on different lines
    retrieved = r'goog.csv'
    fx = open(retrieved, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()


get_data_via_http(data)            # returned data
