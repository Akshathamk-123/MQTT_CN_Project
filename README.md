# MQTT_CN_Project

This is a part of My CN project in 4th semester
Name:Akshatha.M.K
SRN:PES1UG21CS062

# SimpleMQTT

## Overview

This project demonstrates a simple implementation of MQTT (Message Queuing Telemetry Transport) using Python sockets. It includes components for a publisher, a subscriber, and utility functions to handle network communication.

## What is MQTT?

MQTT is a lightweight messaging protocol designed for small sensors and mobile devices with low bandwidth. It works on the publish/subscribe model, where devices (publishers) send messages on specific topics and other devices (subscribers) receive messages on those topics. A central broker manages the communication between publishers and subscribers.

### How MQTT Works

1. **Publishers**: Devices that send messages on specific topics.
2. **Subscribers**: Devices that receive messages from specific topics they are interested in.
3. **Broker**: A server that receives messages from publishers and forwards them to the appropriate subscribers.

## Project Structure

- `utils.py`: Contains utility functions for handling forced exits and parsing integers.
- `template.py`: Provides a base `Template` class with default configurations and methods for logging, executing, and closing connections.
- `client.py`: Defines a `Client` class inheriting from `Template`, handling the connection setup and the main run loop.
- `subscriber.py`: Implements a `Subscriber` class that subscribes to topics and receives messages.
- `publisher.py`: Implements a `Publisher` class that publishes messages to topics.

## How the Code Works

### Publisher

1. Connects to the server.
2. Prompts the user for a topic and data to publish.
3. Sends the data to the server and waits for an acknowledgment.

### Subscriber

1. Connects to the server.
2. Prompts the user for a topic to subscribe to.
3. Receives and prints messages from the server on the subscribed topic.

## How to Run

### Prerequisites

- Python 3.x

### Installation

1. **Clone the repository**:

   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Install required packages**:

   This project uses the standard library, so no additional packages are required.

### Running the Project

1. **Start the Subscriber**:

   Open a terminal and run:

   ```bash
   python subscriber.py
   ```

2. **Start the Publisher**:

   Open another terminal and run:

   ```bash
   python publisher.py
   ```

### Usage

1. **In the Subscriber terminal**:

   - Enter a topic to subscribe to or type `exit_` to terminate the connection.

2. **In the Publisher terminal**:

   - Enter a topic to publish to or type `exit_` to terminate the connection.
   - Enter the data to publish.

### Example

1. **Subscriber**:

   ```plaintext
   Enter topic to subscribe or exit_ to terminate : news
   ```

2. **Publisher**:

   ```plaintext
   Enter topic to publish or exit_ to terminate : news
   Enter data to publish : Hello, World!
   ```

   The message "Hello, World!" will be received by the subscriber subscribed to the `news` topic.

## Notes

- Ensure that both the publisher and subscriber are connected to the same network.
- Adjust the IP address and port in `template.py` if necessary.
- This implementation is for educational purposes and does not include all features of a full MQTT broker.

## Conclusion

This project provides a basic understanding of how MQTT can be implemented using Python sockets. It demonstrates the core concepts of the publish/subscribe model and can be extended for more complex use cases.

