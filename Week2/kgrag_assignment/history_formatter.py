from chat_message import ChatMessage


class HistoryFormatter:

    @staticmethod
    def format(
        history: list[ChatMessage] | None,
    ) -> str:

        if not history:
            return ""

        lines = []

        for message in history:

            lines.append(
                f"{message.role.capitalize()}: {message.content}"
            )

        return "\n".join(lines)