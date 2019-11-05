# SQS CLI

## Overview

SQS is cool

## Tasks

```
aws sqs list-queues

aws sqs list-queues --output text --query "QueueUrls"

queue_url=$(aws sqs list-queues --output text --query "QueueUrls")

aws sqs send-message --queue-url $queue_url --message-body "I'm an SQS message from the CLI"

aws sqs receive-message --queue-url $queue_url
```

Take note of the ReceiptHandle value in the response object. You will use it later.

You should notice that even though you've requested and successfully received your message using the CLI, the message continues to display in the SQS dashboard. This is because Amazon SQS doesn't automatically delete a message after it has been received, in case you don't successfully receive or process the message (for example, if your application fails or you lose connectivity). To delete a message you would send a separate delete request which acknowledges that you no longer need the message because you've successfully received and processed it.

```
aws sqs delete-message --queue-url $queue_url --receipt-handle YOUR_RECEIPT_HANDLE
```







