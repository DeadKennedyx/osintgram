from instagrapi import Client
import yaml
import artwork
import printcolors as pc

pc.printout(artwork.ascii_art, pc.YELLOW)
pc.printout("\nVersion 1 - Developed by DeadKennedyx\n\n", pc.YELLOW)

with open("credentials.yaml", "r") as yamlfile:
    data = yaml.load(yamlfile, Loader=yaml.FullLoader)
    pc.printout("\nCredentials Read Succesfully\n\n", pc.YELLOW)

pc.printout("\nLogging in..\n\n", pc.YELLOW)
cl = Client()
        
try:
    cl.login(data[0]['Credentials']['username'], data[0]['Credentials']['password'])
except Exception as err:
    print(err)
    quit()

target_username = input("Enter Target Username:")
target_user_id = cl.user_id_from_username(target_username)
pc.printout("\nTarget Id: "+target_user_id+"\n", pc.GREEN)

while True:
    pc.printout("\nEnter a command:\n", pc.YELLOW)
    user_input = input("1) Get User Id\n2) Get User Media\n3) Get User Information\n4) Search Followers\n5) Search Following\n6) Search Most Recent Media/Posts By Location\n7) Get Media Information\n0) Exit\n")

    # Check the user input and execute the corresponding command
    if user_input == '1':
        print(target_user_id)
    elif user_input == '2':
        limit = input("Enter Number of Posts you want to retrieve:\n")
        pc.printout("Retrieving Posts..\n", pc.MAGENTA)
        print(cl.user_medias(target_user_id, limit))
    elif user_input == '3':
        pc.printout("Retrieving User Information..\n", pc.MAGENTA)
        print(cl.user_info(target_user_id))
    elif user_input == '4':
        query = input("Enter Follower Username:\n")
        pc.printout("Retrieving Follower..\n", pc.MAGENTA)
        print(cl.search_followers(target_user_id, query))
    elif user_input == '5':
        query = input("Enter Following Username:\n")
        pc.printout("Retrieving Following..\n", pc.MAGENTA)
        print(cl.search_following(target_user_id, query))
    elif user_input == '6':
        lat = input("Enter Location Latitude:\n")
        lng = input("Enter Location Longitude:\n")
        location = cl.location_search(lat, lng)[0]
        location.dict()
        location = cl.location_complete(location)
        limit = input("Enter Number of Posts you want to retrieve:\n")
        pc.printout("Retrieving Recent Medias In Location..\n", pc.MAGENTA)
        print(cl.location_medias_recent(location.pk, limit))
    elif user_input == '7':
        media_pk = input("Enter Media Pk:\n")
        pc.printout("Retrieving Media Information..\n", pc.MAGENTA)
        print(cl.media_info(media_pk).dict())
    elif user_input == '0':
        pc.printout("Exiting the program. Goodbye!", pc.CYAN)
        break  # Exit the loop
    else:
        print("Please enter a valid command.")
