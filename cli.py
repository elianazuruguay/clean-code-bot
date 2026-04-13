import click

from security.file_validator import FileValidationError
from ui.console import print_error, print_success
from llm.openai_client import OpenAIClient
from core.processor import CodeProcessor


@click.command()
@click.argument("file")
@click.option("--output", "-o", default=None, help="Optional output override path")
def main(file, output):

    try:
        llm = OpenAIClient()
        processor = CodeProcessor(llm)

        result_path = processor.process_file(file, output_path=output)

        print_success(f"Saved output to {result_path}")

    except FileValidationError as e:
        print_error("File Validation Error", str(e))

    except Exception as e:
        print_error("Unexpected Error", str(e))


if __name__ == "__main__":
    main()