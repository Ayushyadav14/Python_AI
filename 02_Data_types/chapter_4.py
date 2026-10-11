is_boiling = True
stri_count = 5
total_actions = stri_count + is_boiling  # upcasting
print(f"Total actions: {total_actions}")

milk_present = 0 # no milk
print(f"Is there milk? {bool(milk_present)}")

server_status = True
database_status = True

can_process_request = server_status and database_status
print(f"Can server process the request? {can_process_request}")