# Slack Notifications Logic – README

## Overview

This project implements the logic for determining when Slack should send a notification to a user. Based on a detailed flowchart provided by Slack Engineering, the system takes into account multiple factors such as user preferences, channel settings, Do Not Disturb (DND) status, mentions, and device-specific conditions. 

The complexity of Slack's notification logic lies in balancing various notification preferences and contexts, ensuring that users receive only the most relevant notifications. Despite the intricate decision-making process, the end goal is to create an experience where notifications "just work as intended."

This repository contains a single file that implements the decision tree from the Slack notification flowchart.

## Slack Notification Flowchart

The flowchart below illustrates how Slack decides to send a notification, based on various conditions such as user preferences, Do Not Disturb (DND) status, and channel settings.

![Slack Notification Flowchart](https://slack.engineering/wp-content/uploads/sites/7/2023/03/2017-notifications-summary.png?w=512)


## Project Structure

- **File:** `main.py`  
  This file includes the entire logic needed to determine when a notification should be sent, as well as test cases to validate different notification scenarios.

### Main Components:
1. **`NotificationPayload` class**  
   This `dataclass` represents the payload of a notification. It contains several attributes, each corresponding to a key decision factor from the Slack notification flowchart:
   - **Channel settings**: Muted, thread messages, mentions, etc.
   - **User preferences**: Do Not Disturb (DND) status, notification overrides, etc.
   - **Global and Channel notification preferences**: Specific notification types such as "All," "Mentions," "Nothing," etc.
   - **Mobile-specific settings**: Whether the user is on a mobile device and past the notification threshold.

2. **`should_send_notification` function**  
   This function encapsulates the logic for deciding if a notification should be sent. It evaluates the payload and applies the conditions from the Slack flowchart. Key checks include:
   - Whether the channel is muted
   - DND status and overrides
   - Presence of @mentions, @everyone, or @here messages
   - Specific notification preferences set by the user (both global and channel-based)
   - Device-based rules (e.g., mobile push thresholds)

3. **`get_test_cases` function**  
   This function provides a variety of test cases that represent different paths through the notification decision tree. Each test case includes:
   - A description
   - A `NotificationPayload` object with values reflecting a specific scenario
   - The expected outcome (whether a notification should be sent)

4. **`run_test_cases` function**  
   This function runs all the provided test cases, compares the actual results against the expected outcomes, and prints the results.

## Slack Notification Logic: The Design Philosophy

According to Slack Engineering, the logic for sending notifications may seem simple at first glance, but it involves a lot of behind-the-scenes complexity. Slack's design aims to strike a balance between notifying users of important events while avoiding unnecessary interruptions. Here’s a quote from Slack Engineering that highlights this complexity:

> "Flowchart of how Slack decides to send a notification  
> It is a great example of why a simple feature may take much longer to develop than many people think.  
> When we have a great design, users may not notice the complexity because it feels like the feature just working as intended."  
> – Slack Engineering Blog

## Running the Code

### Requirements
- Python 3.8 or higher

### Running Tests

To validate the notification logic, you can run the test cases provided:

1. Clone the repository:
   ```bash
   git clone https://github.com/thevenice/slack_notifications.git
   cd slack_notifications.git
   ```

2. Run the tests:
   ```bash
   python main.py
   ```

The script will execute a set of predefined test cases, each designed to simulate different Slack notification scenarios. For each test case, the output will indicate whether the result matches the expected outcome.

## Extending the Logic

The logic in this repository covers the most common notification paths. However, it can be extended or adapted to other platforms or features that have similar notification decision trees.

If you wish to add new test cases, simply modify the `get_test_cases` function with additional scenarios, making sure to specify the `NotificationPayload` and expected result.

## Conclusion

This project demonstrates how complex a seemingly simple feature like notifications can be. The Slack flowchart for notifications encapsulates numerous conditions that need to be handled carefully to provide users with a seamless experience. The provided code mirrors this logic and ensures that the notification system behaves as expected across a wide range of scenarios.

Feel free to explore, adapt, and extend this logic for your own projects!