import urllib.request
import webbrowser

webbrowser.open("https://github.com/")
get_url = urllib.request.urlopen('https://github.com/')
print("Response Status: " + str(get_url.getcode()))
