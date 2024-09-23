"""Defines the module's public interface."""

from .gpt.query import clearConversationHistory, queryGPT, uploadFile

__all__ = ['uploadFile', 'queryGPT', 'clearConversationHistory']