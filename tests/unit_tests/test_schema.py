"""Test formatting functionality."""

import unittest

import langchain.schema as schema
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage,
    get_buffer_string,
    messages_from_dict,
    messages_to_dict,
)
from langchain.schema import __all__ as schema_all


class TestGetBufferString(unittest.TestCase):
    human_msg: HumanMessage = HumanMessage(content="human")
    ai_msg: AIMessage = AIMessage(content="ai")
    sys_msg: SystemMessage = SystemMessage(content="sys")

    def test_empty_input(self) -> None:
        self.assertEqual(get_buffer_string([]), "")

    def test_valid_single_message(self) -> None:
        expected_output = f"Human: {self.human_msg.content}"
        self.assertEqual(
            get_buffer_string([self.human_msg]),
            expected_output,
        )

    def test_custom_human_prefix(self) -> None:
        prefix = "H"
        expected_output = f"{prefix}: {self.human_msg.content}"
        self.assertEqual(
            get_buffer_string([self.human_msg], human_prefix="H"),
            expected_output,
        )

    def test_custom_ai_prefix(self) -> None:
        prefix = "A"
        expected_output = f"{prefix}: {self.ai_msg.content}"
        self.assertEqual(
            get_buffer_string([self.ai_msg], ai_prefix="A"),
            expected_output,
        )

    def test_multiple_msg(self) -> None:
        msgs = [self.human_msg, self.ai_msg, self.sys_msg]
        expected_output = "\n".join(
            [
                f"Human: {self.human_msg.content}",
                f"AI: {self.ai_msg.content}",
                f"System: {self.sys_msg.content}",
            ]
        )
        self.assertEqual(
            get_buffer_string(msgs),
            expected_output,
        )


class TestMessageDictConversion(unittest.TestCase):
    human_msg: HumanMessage = HumanMessage(
        content="human", additional_kwargs={"key": "value"}
    )
    ai_msg: AIMessage = AIMessage(content="ai")
    sys_msg: SystemMessage = SystemMessage(content="sys")

    def test_multiple_msg(self) -> None:
        msgs = [
            self.human_msg,
            self.ai_msg,
            self.sys_msg,
        ]
        self.assertEqual(
            messages_from_dict(messages_to_dict(msgs)),
            msgs,
        )


def test_public_api() -> None:
    """Test for changes in the public API."""
    expected_all = [
        "AIMessage",
        "AgentAction",
        "AgentFinish",
        "BaseChatMessageHistory",
        "BaseDocumentTransformer",
        "BaseMemory",
        "BaseMessage",
        "BaseOutputParser",
        "BaseRetriever",
        "ChatGeneration",
        "ChatMessage",
        "ChatResult",
        "Document",
        "Generation",
        "HumanMessage",
        "LLMResult",
        "Memory",
        "OutputParserException",
        "PromptValue",
        "RUN_KEY",
        "RunInfo",
        "SystemMessage",
        "T",
        "get_buffer_string",
        "message_from_dict",
        "message_to_dict",
        "messages_from_dict",
        "messages_to_dict",
    ]

    assert sorted(schema_all) == expected_all

    # Assert that the object is actually present in the schema module
    for module_name in expected_all:
        assert hasattr(schema, module_name) and getattr(schema, module_name) is not None
