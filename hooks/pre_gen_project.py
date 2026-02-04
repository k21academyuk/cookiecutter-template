#!/usr/bin/env python
"""
Pre-generation hook for cookiecutter template.
This runs BEFORE the project directory is created.
It sets up derived variables needed by the template.
"""
import sys

# Get user inputs
project_name = '{{ cookiecutter.project_name }}'

# Create a safe directory/slug name from project_name
# This converts spaces and hyphens to underscores and makes it lowercase
project_slug = project_name.lower().replace(' ', '_').replace('-', '_')

# Update the cookiecutter context with the new variable
# This makes project_slug available to all template files
"""{{ cookiecutter.update({'project_slug': '""" + project_slug + """'}) }}"""

print("=" * 60)
print(f"🚀 Initializing project: {project_name}")
print(f"📁 Directory name: {project_slug}")
print("=" * 60)

# Exit successfully
sys.exit(0)
