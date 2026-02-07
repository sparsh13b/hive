# JSON YAML Tool

A utility tool for validating and converting JSON and YAML data using the FastMCP tool pattern.

## Description

This tool helps agents safely work with structured data by validating formats and converting between JSON and YAML.  
It is useful when handling API responses, configuration files, and structured outputs from LLMs.

## Arguments

### validate_json

| Argument | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| `json_string` | str | Yes | - | JSON string to validate |

---

### validate_yaml

| Argument | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| `yaml_string` | str | Yes | - | YAML string to validate |

---

### json_to_yaml

| Argument | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| `json_string` | str | Yes | - | JSON string to convert into YAML |

---

### yaml_to_json

| Argument | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| `yaml_string` | str | Yes | - | YAML string to convert into JSON |

## Environment Variables

This tool does not require any environment variables.

## Error Handling

Returns error strings for invalid inputs:

- `Invalid JSON: <error>` – When JSON parsing fails  
- `Invalid YAML: <error>` – When YAML parsing fails  
- `Conversion failed: <error>` – When conversion cannot be completed
