.PHONY: help run install test


# Default target
help:
	@echo "Available commands:"
	@echo ""
	@echo "Local Development:"
	@echo "  run          - Run server locally (no Docker)"
	@echo "  install      - Install dependencies locally"
	@echo "  test   - Run tests locally"


run:
	uvicorn main:app --host 0.0.0.0 --port 8100 --reload

test:
	python3 -m unittest test/test_common.py