from __future__ import annotations

import json
import yaml
from fastmcp import FastMCP


def register_tools(mcp: FastMCP) -> None:
    """Register JSON/YAML tools with the MCP server."""

    @mcp.tool()
    def validate_json(json_string: str) -> str:
        """validating if a string is a valid JSON."""
        try:
            json.loads(json_string)
            return "Valid JSON"
        except Exception as e:
            return f"Invalid JSON: {str(e)}"

    @mcp.tool()
    def validate_yaml(yaml_string: str) -> str:
        """validating if a string is a valid YAML."""
        try:
            yaml.safe_load(yaml_string)
            return "Valid YAML"
        except Exception as e:
            return f"Invalid YAML: {str(e)}"

    @mcp.tool()
    def json_to_yaml(json_string: str) -> str:
        """Convert JSON string to YAML."""
        try:
            data = json.loads(json_string)
            return yaml.dump(data)
        except Exception as e:
            return f"Conversion failed: {str(e)}"

    @mcp.tool()
    def yaml_to_json(yaml_string: str) -> str:
        """Convert YAML string to JSON."""
        try:
            data = yaml.safe_load(yaml_string)
            return json.dumps(data, indent=2)
        except Exception as e:
            return f"Conversion failed: {str(e)}"
