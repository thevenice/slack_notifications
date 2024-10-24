from dataclasses import dataclass
from typing import Optional, Literal, List, Tuple

#NotificationPayload class
@dataclass
class NotificationPayload:
    channel_muted: bool
    is_thread_message: bool
    user_subscribed: bool
    user_in_dnd: bool
    dnd_override: bool
    is_channel_everyone_here_message: bool
    channel_mentions_suppressed: bool
    channel_notification_pref: Literal["Nothing", "Everything", "Mentions", "Default"]
    global_notification_pref: Literal["All", "Mentions", "DMs", "Highlight Words", "Never"]
    is_dm: bool
    is_mention: bool
    is_file_comment_owned_by_user: bool
    user_presence_active: bool
    highlight_word: bool
    is_mobile: bool
    past_mobile_push_threshold: bool = False

def get_test_cases() -> List[Tuple[str, NotificationPayload, bool]]:
    """
    Returns a list of test cases covering all major paths in the notification decision tree.
    Each test case includes a description, payload, and expected result.
    """
    test_cases = [
        # 1. Muted Channel Cases
        (
            "Muted channel with thread message and subscribed user (should notify)",
            NotificationPayload(
                channel_muted=True,
                is_thread_message=True,
                user_subscribed=True,
                user_in_dnd=False,
                dnd_override=False,
                is_channel_everyone_here_message=False,
                channel_mentions_suppressed=False,
                channel_notification_pref="Default",
                global_notification_pref="All",
                is_dm=False,
                is_mention=False,
                is_file_comment_owned_by_user=False,
                user_presence_active=False,
                highlight_word=False,
                is_mobile=False
            ),
            True
        ),
        
        # 2. DND Cases
        (
            "User in DND with override (should notify)",
            NotificationPayload(
                channel_muted=False,
                is_thread_message=False,
                user_subscribed=False,
                user_in_dnd=True,
                dnd_override=True,
                is_channel_everyone_here_message=True,
                channel_mentions_suppressed=False,
                channel_notification_pref="Everything",
                global_notification_pref="All",
                is_dm=False,
                is_mention=False,
                is_file_comment_owned_by_user=False,
                user_presence_active=False,
                highlight_word=False,
                is_mobile=False
            ),
            True
        ),
        
        # 3. @channel/@everyone/@here message
        (
            "@everyone message without suppressed mentions (should notify)",
            NotificationPayload(
                channel_muted=False,
                is_thread_message=False,
                user_subscribed=False,
                user_in_dnd=False,
                dnd_override=False,
                is_channel_everyone_here_message=True,
                channel_mentions_suppressed=False,
                channel_notification_pref="Default",
                global_notification_pref="All",
                is_dm=False,
                is_mention=False,
                is_file_comment_owned_by_user=False,
                user_presence_active=False,
                highlight_word=False,
                is_mobile=False
            ),
            True
        ),
        
        # 4. Channel Preference "Everything"
        (
            "Channel pref Everything with thread message and subscribed (should notify)",
            NotificationPayload(
                channel_muted=False,
                is_thread_message=True,
                user_subscribed=True,
                user_in_dnd=False,
                dnd_override=False,
                is_channel_everyone_here_message=False,
                channel_mentions_suppressed=False,
                channel_notification_pref="Everything",
                global_notification_pref="All",
                is_dm=False,
                is_mention=False,
                is_file_comment_owned_by_user=False,
                user_presence_active=False,
                highlight_word=False,
                is_mobile=False
            ),
            True
        ),
        
        # 5. Channel Preference "Mentions" with DM
        (
            "Channel pref Mentions with DM (should notify)",
            NotificationPayload(
                channel_muted=False,
                is_thread_message=False,
                user_subscribed=False,
                user_in_dnd=False,
                dnd_override=False,
                is_channel_everyone_here_message=False,
                channel_mentions_suppressed=False,
                channel_notification_pref="Mentions",
                global_notification_pref="All",
                is_dm=True,
                is_mention=False,
                is_file_comment_owned_by_user=False,
                user_presence_active=False,
                highlight_word=False,
                is_mobile=False
            ),
            True
        ),
        
        # 6. Channel Preference "Default" with Global "All"
        (
            "Channel Default, Global All, inactive user (should notify)",
            NotificationPayload(
                channel_muted=False,
                is_thread_message=False,
                user_subscribed=False,
                user_in_dnd=False,
                dnd_override=False,
                is_channel_everyone_here_message=False,
                channel_mentions_suppressed=False,
                channel_notification_pref="Default",
                global_notification_pref="All",
                is_dm=False,
                is_mention=False,
                is_file_comment_owned_by_user=False,
                user_presence_active=False,
                highlight_word=False,
                is_mobile=False
            ),
            True
        ),
        
        # 7. Channel Preference "Default" with Global "Mentions"
        (
            "Channel Default, Global Mentions, with mention (should notify)",
            NotificationPayload(
                channel_muted=False,
                is_thread_message=False,
                user_subscribed=False,
                user_in_dnd=False,
                dnd_override=False,
                is_channel_everyone_here_message=False,
                channel_mentions_suppressed=False,
                channel_notification_pref="Default",
                global_notification_pref="Mentions",
                is_dm=False,
                is_mention=True,
                is_file_comment_owned_by_user=False,
                user_presence_active=True,
                highlight_word=False,
                is_mobile=False
            ),
            True
        ),
        
        # 8. Channel Preference "Default" with Global "DMs"
        (
            "Channel Default, Global DMs, with DM (should notify)",
            NotificationPayload(
                channel_muted=False,
                is_thread_message=False,
                user_subscribed=False,
                user_in_dnd=False,
                dnd_override=False,
                is_channel_everyone_here_message=False,
                channel_mentions_suppressed=False,
                channel_notification_pref="Default",
                global_notification_pref="DMs",
                is_dm=True,
                is_mention=False,
                is_file_comment_owned_by_user=False,
                user_presence_active=True,
                highlight_word=False,
                is_mobile=False
            ),
            True
        ),
        
        # 9. Channel Preference "Default" with Global "Highlight Words"
        (
            "Channel Default, Global Highlight Words, with highlight (should notify)",
            NotificationPayload(
                channel_muted=False,
                is_thread_message=False,
                user_subscribed=False,
                user_in_dnd=False,
                dnd_override=False,
                is_channel_everyone_here_message=False,
                channel_mentions_suppressed=False,
                channel_notification_pref="Default",
                global_notification_pref="Highlight Words",
                is_dm=False,
                is_mention=False,
                is_file_comment_owned_by_user=False,
                user_presence_active=True,
                highlight_word=True,
                is_mobile=False
            ),
            True
        ),
        
        # 10. Mobile threshold case
        (
            "Mobile user past threshold (should not notify)",
            NotificationPayload(
                channel_muted=False,
                is_thread_message=False,
                user_subscribed=True,
                user_in_dnd=False,
                dnd_override=False,
                is_channel_everyone_here_message=False,
                channel_mentions_suppressed=False,
                channel_notification_pref="Everything",
                global_notification_pref="All",
                is_dm=False,
                is_mention=False,
                is_file_comment_owned_by_user=False,
                user_presence_active=False,
                highlight_word=False,
                is_mobile=True,
                past_mobile_push_threshold=True
            ),
            False
        ),
    ]
    return test_cases

def run_test_cases(test_cases: List[Tuple[str, NotificationPayload, bool]]) -> None:
    """
    Runs all test cases and prints results.
    """

    def should_send_notification(payload: NotificationPayload) -> bool:
        """
        Determines whether a notification should be sent based on the given payload.
        Implements the decision tree from the flowchart.
        
        Args:
            payload: NotificationPayload object containing all relevant flags and preferences
        
        Returns:
            bool: True if notification should be sent, False otherwise
        """
        # First check if channel is muted
        if payload.channel_muted:
            # When channel is muted, only send if it's a thread message and user is subscribed
            return payload.is_thread_message and payload.user_subscribed
        
        # Check DND status
        if payload.user_in_dnd and not payload.dnd_override:
            return False
            
        # Check for @channel/@everyone/@here messages
        if payload.is_channel_everyone_here_message:
            if not payload.channel_mentions_suppressed:
                return True
                
        # Check channel notification preferences
        if payload.channel_notification_pref == "Nothing":
            return False
        elif payload.channel_notification_pref == "Everything":
            if payload.is_thread_message:
                return payload.user_subscribed
            return True
        elif payload.channel_notification_pref == "Mentions":
            if payload.is_dm:
                if payload.is_thread_message:
                    return payload.user_subscribed
                return True
            elif payload.is_mention:
                if payload.is_file_comment_owned_by_user:
                    return False
                return True
        elif payload.channel_notification_pref == "Default":
            # Check global notification preferences
            if payload.global_notification_pref == "All":
                if not payload.user_presence_active:
                    if payload.is_thread_message:
                        return payload.user_subscribed
                    return True
                elif payload.highlight_word:
                    if payload.is_thread_message:
                        return payload.user_subscribed
                    return True
            elif payload.global_notification_pref == "Mentions":
                return payload.is_mention
            elif payload.global_notification_pref == "DMs":
                return payload.is_dm
            elif payload.global_notification_pref == "Highlight Words":
                return payload.highlight_word
            elif payload.global_notification_pref == "Never":
                return False
                
        # Mobile-specific checks
        if payload.is_mobile and payload.past_mobile_push_threshold:
            return False
            
        return False    
    
    print("Running notification test cases:\n")
    for i, (description, payload, expected) in enumerate(test_cases, 1):
        result = should_send_notification(payload)
        status = "✓" if result == expected else "✗"
        print(f"Test {i}: {description}")
        print(f"Expected: {expected}, Got: {result} {status}\n")

if __name__ == "__main__":
    test_cases = get_test_cases()
    run_test_cases(test_cases)