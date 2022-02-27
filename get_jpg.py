import urllib.request

def fetch_test_picture(URL = 'https://vkceyugu.cdn.bspapp.com/VKCEYUGU-b6301653-fced-4bc5-b608-8df53696a565/f1577d68-1ba3-4971-b7b8-3ee0917a5271.jpg',
    FILE_NAME = './/test//test.jpg', OPEN_MODE = 'wb'):
    request = urllib.request.urlopen(URL)
    write_file = open(FILE_NAME, OPEN_MODE)
    buffer = request.read()
    write_file.write(buffer)
    write_file.close()

# if __name__ == '__main__':
#     fetch_test_picture()