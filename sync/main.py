import argparse
from client import SyncClient
from pprint import pprint


def main():
    parser = argparse.ArgumentParser(
        description="""CLI to interact with firefox sync""",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(dest='login',
                        help='Firefox Accounts login.')
    parser.add_argument(dest='password',
                        help='Firefox Accounts password.')
    parser.add_argument(dest='action', help='The action to be executed',
                        default='get_collections', nargs='?',
                        choices=[m for m in dir(SyncClient)
                                 if not m.startswith('_')])

    args, extra = parser.parse_known_args()

    # XXX find a way to easily get client_state + bid assertion
    # from the browser console maybe.

    client = SyncClient(args.login, args.password)
    pprint(getattr(client, args.action)(*extra))

if __name__ == '__main__':
    main()
