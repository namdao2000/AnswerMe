import socket
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = "https://www.chegg.com/homework-help/questions-and-answers/contribution-margin-willie-company-sells-27-000-units-3500-per-unit-variable-costs-2030-pe-q6383345"

socket.sendto(message.encode(), ("127.0.0.1", 5000))