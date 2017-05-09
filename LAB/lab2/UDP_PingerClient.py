# This skeleton is valid for both Python 2.7 and Python 3.
# You should be aware of your additional code for compatibility of the Python version of your choice.

import time
from socket import *

# Get the server hostname and port as command line arguments                    
host = "localhost"  # FILL IN START		# FILL IN END
port = 12000  # FILL IN START		# FILL IN END
timeout = 1  # in seconds

# Create UDP client socket
# FILL IN START		
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Note the second parameter is NOT SOCK_STREAM
# but the corresponding to UDP

# Set socket timeout as 1 second
clientSocket.settimeout(timeout)

# FILL IN END

# Sequence number of the ping message
ptime = 0
RTT = 0

# Ping for 10 times
while ptime < 10:
    ptime += 1
    # Format the message to be sent as in the Lab description	
    data = "Ping number: " + ptime.__str__() + " Time: " + RTT.__str__() # FILL IN START		# FILL IN END

    try:

        # Record the "sent time"
        st = time.clock()
        # Send the UDP packet with the ping message
        clientSocket.sendto(data.encode(), (host, port))
        # Receive the server response
        msg, serverAdr = clientSocket.recvfrom(2048)
        # Record the "received time"
        rt = time.clock()
        # Display the server response as an output
        print(msg)
        # Round trip time is the difference between sent and received time
        RTT = rt - st

    # FILL IN END
    except:
        # Server does not response
        # Assume the packet is lost
        print("Request timed out.")
        continue

# Close the client socket
clientSocket.close()
