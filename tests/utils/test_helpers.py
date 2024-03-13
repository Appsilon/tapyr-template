def log_contain_message(log_sink, message):
    return any(message in record for record in log_sink.messages)
