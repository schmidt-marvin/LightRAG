"""
Centralized configuration constants for LightRAG.

This module defines default values for configuration constants used across
different parts of the LightRAG system. Centralizing these values ensures
consistency and makes maintenance easier.
"""

# Default values for environment variables
DEFAULT_MAX_GLEANING = 1
DEFAULT_FORCE_LLM_SUMMARY_ON_MERGE = 4
DEFAULT_WOKERS = 2
DEFAULT_TIMEOUT = 150

# Separator for graph fields
GRAPH_FIELD_SEP = "<SEP>"

# Logging configuration defaults
DEFAULT_LOG_MAX_BYTES = 10485760  # Default 10MB
DEFAULT_LOG_BACKUP_COUNT = 5  # Default 5 backups
DEFAULT_LOG_FILENAME = "lightrag.log"  # Default log filename
