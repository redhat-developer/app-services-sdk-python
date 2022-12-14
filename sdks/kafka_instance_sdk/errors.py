from enum import Enum 

#   kafkainstance error codes

class APIErrorCodes(Enum):
  # Invalid or missing credentials 
  ERROR_1 = "401" 

  # Client is not authorized to perform the requested operation 
  ERROR_2 = "403" 

  # No such topic 
  ERROR_3 = "404" 

  # No such consumer group 
  ERROR_4 = "404" 

  # Topic/Partition in request is invalid 
  ERROR_5 = "400" 

  # Topic/Partition in request does not exist 
  ERROR_6 = "400" 

  # Request body is malformed or invalid 
  ERROR_7 = "400" 

  # Request violates topic configuration policy 
  ERROR_8 = "400" 

  # Request contains invalid configuration 
  ERROR_9 = "400" 

  # Requested topic already exists 
  ERROR_10 = "409" 

  # Consumer group has connected clients 
  ERROR_11 = "423" 

  # Cluster not available 
  ERROR_12 = "503" 

  # Invalid ACL binding resourceType or operation 
  ERROR_13 = "400" 

  # No such error 
  ERROR_14 = "404" 

  # Unknown consumer group member 
  ERROR_15 = "400" 

  # Request body or parameters invalid 
  ERROR_16 = "400" 

  # Server has encountered an unexpected error 
  ERROR_99 = "500" 

