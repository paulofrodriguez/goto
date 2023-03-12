#! /usr/bin/python3
import webbrowser
import sys
import settings



# if len(sys.argv)>1:
#      input_url=sys.argv[1].lower()
#      if input_url.startswith("http"):
#           url=input_url
#      else:
#           url="http://"+input_url


#def config():
 #     webbrowser.open_new_tab(config_file_path)


def profile(profile):


    if (profile==None):
        return settings.default_profile
    else:

      new_profile = profile

      settings.config['SETTINGS']['DEFAULT_PROFILE'] = new_profile

      with open(settings.config_file_path, 'w') as configfile:
            settings.config.write(configfile)
      
      
      settings.default_profile=settings.config['SETTINGS']['DEFAULT_PROFILE']
      settings.config.read(settings.config_file_path)
      settings.url=''
      settings.url=settings.config[settings.default_profile]

def list():
    print(settings.urls)
    r=""
    for k,v in settings.urls.items():
        r=r+k + " "+v+"\n"
    print(r)
    return r
        


def add(key,url):
      if (profile==None):
            settings.config[settings.default_profile][key]=url
      else:
            settings.config[profile][key]=url







# if len(sys.argv)>1:
#       match sys.argv[1]:
#             case "add":
#                   print("adding...")
#             case "config":
#                   config()
#             case "profile":
#                   profile()
#             case "list":
#                   list()
#             case _:
#                   k=sys.argv[1].lower()
#                   url=settings.url[k]
#                   # Open URL in a new tab, if a browser window is already open.
#                   webbrowser.open_new_tab(url)



