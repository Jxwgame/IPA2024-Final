#######################################################################################
# Yourname:
# Your student ID:
# Your GitHub Repo: 

#######################################################################################
# 1. Import libraries for API requests, JSON formatting, time, and (restconf_final or netconf_final).

<!!!REPLACEME with code for libraries>

#######################################################################################
# 2. Assign the Webex hard-coded access token to the variable accessToken.

accessToken = "Bearer <!!!REPLACEME with hard-coded token!!!>"

#######################################################################################
# 3. Prepare parameters get the latest message for messages API.

# Defines a variable that will hold the roomId
roomIdToGetMessages = (
    "<!!!REPLACEME with roomID of the NPA2023 Webex Teams room!!!>"
)

while True:
    # always add 1 second of delay to the loop to not go over a rate limit of API calls
    time.sleep(1)

    # the Webex Teams GET parameters
    #  "roomId" is the ID of the selected room
    #  "max": 1  limits to get only the very last message in the room
    getParameters = {"roomId": roomIdToGetMessages, "max": 1}

    # the Webex Teams HTTP header, including the Authoriztion
    getHTTPHeader = {"Authorization": <!!!REPLACEME!!!>}

# 4. Provide the URL to the Webex Teams messages API, and extract location from the received message.
    
    # Send a GET request to the Webex Teams messages API.
    # - Use the GetParameters to get only the latest message.
    # - Store the message in the "r" variable.
    r = requests.get(
        "<!!!REPLACEME with URL of Webex Teams Messages API!!!>",
        params=<!!!REPLACEME with HTTP parameters!!!>,
        headers=<!!!REPLACEME with HTTP headers!!!>,
    )
    # verify if the retuned HTTP status code is 200/OK
    if not r.status_code == 200:
        raise Exception(
            "Incorrect reply from Webex Teams API. Status code: {}".format(r.status_code)
        )

    # get the JSON formatted returned data
    json_data = r.json()

    # check if there are any messages in the "items" array
    if len(json_data["items"]) == 0:
        raise Exception("There are no messages in the room.")

    # store the array of messages
    messages = json_data["items"]
    
    # store the text of the first message in the array
    message = messages[0]["text"]
    print("Received message: " + message)

    # check if the text of the message starts with the magic character "/" followed by your studentID and a space and followed by a command name
    #  e.g.  "/66070123 create"
    if message.find("<!!!REPLACEME!!!>") == 0:

        # extract the command
        command = <!!!REPLACEME!!!>
        print(command)

# 5. Complete the logic for each command

        if command == "create":
            <!!!REPLACEME with code for create command!!!>     
        elif command == "delete":
            <!!!REPLACEME with code for delete command!!!>
        elif command == "enable":
            <!!!REPLACEME with code for enable command!!!>
        elif command == "disable":
            <!!!REPLACEME with code for disable command!!!>
        elif command == "status":
            <!!!REPLACEME with code for status command!!!>
        else:
            responseMessage = "Error: No command or unknown command"
        
# 6. Complete the code to post the message to the Webex Teams room.
        
        # the Webex Teams HTTP headers, including the Authoriztion and Content-Type
        postHTTPHeaders = HTTPHeaders = {"Authorization": <!!!REPLACEME!!!>, "Content-Type": <!!!REPLACEME!!!>}

        # The Webex Teams POST JSON data
        # - "roomId" is is ID of the selected room
        # - "text": is the responseMessage assembled above
        postData = {"roomId": <!!!REPLACEME!!!>, "text": <!!!REPLACEME!!!>}

        # Post the call to the Webex Teams message API.
        r = requests.post(
            "<!!!REPLACEME with URL of Webex Teams Messages API!!!>",
            data=json.dumps(<!!!REPLACEME!!!>a),
            headers=<!!!REPLACEME!!!>,
        )
        if not r.status_code == 200:
            raise Exception(
                "Incorrect reply from Webex Teams API. Status code: {}".format(r.status_code)
            )
