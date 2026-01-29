#!/usr/bin/env python3
"""Test script to verify imports work correctly"""

try:
    import streamlit as st
    print("✅ Streamlit imported successfully")
except ImportError as e:
    print(f"❌ Streamlit import failed: {e}")

try:
    import google.generativeai as genai
    print("✅ Google Generative AI imported successfully")
except ImportError as e:
    print(f"❌ Google Generative AI import failed: {e}")

try:
    import python_dotenv
    print("✅ Python-dotenv imported successfully")
except ImportError as e:
    print(f"❌ Python-dotenv import failed: {e}")

print("All import tests completed!")