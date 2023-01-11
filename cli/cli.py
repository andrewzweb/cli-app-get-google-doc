import argparse


class CLIArgs:

    def __init__(self):
        parser = argparse.ArgumentParser()

        parser.add_argument(
            '--fields',
            type=str,
            required=True,
            help="Field which can show you in result document"
        )

        parser.add_argument(
            'url',
            help="Link to docs.google what you want get")

        args = parser.parse_args()

        if "drive.google" not in args.url:
            raise Exception(f"Not correct URL, {args.url}")

        self.url = args.url
        self.fields = args.fields.split(",")

    def to_dict(self):
        return {
            "url": self.url,
            "fields": self.fields
        }
